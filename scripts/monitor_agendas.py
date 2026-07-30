#!/usr/bin/env python3
"""
Monitor Pueblo City Council and County agendas for surveillance/immigration keywords.

This script:
1. Downloads the latest agenda PDFs from Pueblo government websites
2. Extracts text from PDFs (if pdftotext is available)
3. Searches for keywords related to surveillance, ICE, and civil liberties
4. Generates alerts when matches are found
5. Logs all activity for audit trail

Usage:
    python3 monitor_agendas.py                    # Check all sources
    python3 monitor_agendas.py --source city      # Check only city council
    python3 monitor_agendas.py --keywords-only    # Just show keyword matches from existing PDFs
    python3 monitor_agendas.py --output alerts.md # Write alerts to file
    python3 monitor_agendas.py --packets          # Also pull full agenda packets

Exit codes:
    0 = ran clean, no keyword matches
    2 = keyword matches found
    3 = a data source was stale or empty (result is NOT a verified all-clear)

Requirements:
    - Python 3.8+
    - pdftotext (optional, from poppler-utils) for PDF text extraction
    - Internet connection for downloading agendas

Cron example (check every Sunday at 6pm):
    0 18 * * 0 cd /path/to/laraza && python3 scripts/monitor_agendas.py >> logs/agenda_monitor.log 2>&1
"""

import argparse
import datetime
import hashlib
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Optional

import pueblo_sources
from pueblo_sources import (
    CIVICCLERK_TENANTS,
    LEGACY_ARCHIVE_FALLBACK,
    STALENESS_DAYS,
    USER_AGENT,
    fetch_meetings,
    staleness_warning,
)

# Configuration
AGENDA_DIR = pathlib.Path("docs/agendas")
LOG_FILE = pathlib.Path("logs/agenda_monitor.log")
ALERT_FILE = pathlib.Path("docs/agenda_alerts.md")
STATE_FILE = pathlib.Path("docs/agendas/.monitor_state.json")

# Sources to monitor.
#
# LIVE source (verified 2026-07-29) is the CivicClerk OData API -- see
# scripts/pueblo_sources.py for the full access pattern.
#
#   City of Pueblo  -> https://puebloco.api.civicclerk.com/v1
#   Pueblo County   -> https://pueblococo.api.civicclerk.com/v1
#
# The two `legacy_url` values below are DEAD and kept only for labeled fallback:
#   * https://www.pueblo.us/Archive.aspx?AMID=37 -- CivicPlus Archive Center,
#     newest entry 2022-05-23, most content 2013 and older. This is what caused
#     the 2026-02-18 false all-clear on the January 2013 agenda.
#   * https://county.pueblo.org/board-county-commissioners/meeting-schedule --
#     HTTP 404. The county's live agendas are on CivicClerk tenant `pueblococo`;
#     county.pueblo.org itself now returns HTTP 403 to scripted clients, so
#     there is no legacy HTML fallback for the county at all.
SOURCES = {
    "city_council": {
        "name": CIVICCLERK_TENANTS["city_council"]["name"],
        "api": CIVICCLERK_TENANTS["city_council"]["api"],
        "legacy_url": LEGACY_ARCHIVE_FALLBACK["city_council"],
    },
    "county_commissioners": {
        "name": CIVICCLERK_TENANTS["county_commissioners"]["name"],
        "api": CIVICCLERK_TENANTS["county_commissioners"]["api"],
        # No working legacy fallback -- see note above.
        "legacy_url": None,
    },
}

# Keywords to monitor - grouped by category
# Using word boundaries \b to reduce false positives
KEYWORDS = {
    "surveillance": [
        r"\breal[\-\s]?time\s+crime\b",
        r"\brtcc\b",
        r"\bshotspotter\b",
        r"\bsoundthinking\b",
        r"\bcommunity\s+connect\b",
        r"\bgenetec\b",
        r"\bflock\s+safety\b",
        r"\blicense\s+plate\s+reader",
        r"\balpr\b",
        r"\bsurveillance\s+(camera|system|program|equipment)",
        r"\bsecurity\s+camera",
        r"\bpark\s+camera",
        r"\btraffic\s+camera",
        r"\bspeed\s+camera",
        r"\bdrone\s+(program|unit|fleet|response|first\s+responder)",
        r"\bdaktronics\b",
        r"\bhigh\s+point\s+networks\b",
        r"\bfacial\s+recognition\b",
        # Vectors surfaced by the April 2026 editorial research
        r"\bbrinc\b",
        r"\bfusus\b",
        r"\baxon\b",
        r"\bfusion\s+center\b",
        r"\bcell[\-\s]?site\s+simulator\b",
        r"\bstingray\b",
        r"\bgunshot\s+detection\b",
        r"\bcamera\s+trailer\b",
    ],
    "immigration": [
        # "ICE" the agency, excluding Pueblo's Ice Arena, ice rinks, ice cream, etc.
        # The bare-word version false-positived on "ICE ARENA CONCESSION EQUIPMENT".
        r"\bice\b(?!\s*(cream|skating|skate|rink|arena|machine|storm|melt|hockey))",
        r"\bimmigration\s+(enforcement|detainer|hold|policy|resolution)",
        r"\bcustoms\s+and\s+border\b",
        r"\bcbp\b",
        r"\bdeportation\b",
        r"\bdetention\s+(center|facility|bed|contract)",
        r"\bsanctuary\s+(city|policy|resolution)",
        r"\b287\s*\(?g\)?\b",
        r"\bimmigrant\s+(rights|protection|community)",
    ],
    "policing": [
        # Bare "Police Department" appears in nearly every agenda (staff reports,
        # employee recognitions, routine CDOT agreements) and drowned out real hits.
        # Require an action/procurement word nearby instead.
        r"\bpolice\s+(contract|agreement|budget)",
        r"\bpolice\s+department\b.{0,120}?\b(contract|agreement|purchase|equipment|technology|software|grant|budget|camera|surveillance|drone)",
        r"\bbody[\-\s]?worn\s+camera",
        r"\bbody\s*cam\b",
        r"\buse\s+of\s+force\b",
        r"\binternal\s+affairs\b",
        r"\bcitizen\s+oversight\b",
        r"\bpublic\s+safety\s+(budget|committee|department)",
        r"\blaw\s+enforcement\s+(contract|agreement|budget)",
        r"\bsheriff\s+(budget|contract|department)",
    ],
    "civil_liberties": [
        r"\bfirst\s+amendment\b",
        r"\bprotest\s+(permit|ordinance|policy)",
        r"\bdemonstration\s+(permit|policy)",
        r"\bfree\s+speech\b",
        r"\bprivacy\s+(policy|concern|right|impact)",
        r"\bcivil\s+rights\b",
        r"\bcivil\s+liberties\b",
        r"\bfourth\s+amendment\b",
    ],
    "procurement": [
        r"\bsurveillance\s+contract",
        r"\bsecurity\s+(vendor|contract)",
        r"\bprocurement\s+(surveillance|camera|security)",
        r"\brfp\b.*\b(camera|security|surveillance)",
        r"\bbid\b.*\b(camera|security|surveillance)",
        r"\bsole\s+source\b",
        r"\barpa\s+fund",
        r"\bgrant\b.*\b(surveillance|camera|security|rtcc)",
        r"\b(daktronics|genetec|flock|soundthinking)\s+contract",
    ],
}


def log(message: str, level: str = "INFO") -> None:
    """Log a message with timestamp."""
    timestamp = datetime.datetime.now().isoformat()
    log_line = f"[{timestamp}] [{level}] {message}"
    print(log_line)

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(log_line + "\n")


def fetch_html(url: str) -> str:
    """Fetch HTML content from a URL."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; LaRazaMonitor/1.0)"}
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", "ignore")
    except Exception as e:
        log(f"Failed to fetch {url}: {e}", "ERROR")
        return ""


def download_file(url: str, dest: pathlib.Path) -> bool:
    """Download a file if it doesn't exist."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        return False

    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; LaRazaMonitor/1.0)"}
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            with open(dest, "wb") as f:
                f.write(resp.read())
        log(f"Downloaded: {dest.name}")
        return True
    except Exception as e:
        log(f"Failed to download {url}: {e}", "ERROR")
        return False


def extract_pdf_text(pdf_path: pathlib.Path) -> str:
    """Extract text from a PDF using pdftotext or PyPDF2 as fallback."""
    # Try pdftotext first (best quality)
    if shutil.which("pdftotext"):
        try:
            result = subprocess.run(
                ["pdftotext", "-layout", str(pdf_path), "-"],
                capture_output=True,
                text=True,
                timeout=60
            )
            if result.stdout.strip():
                return result.stdout
        except Exception as e:
            log(f"pdftotext failed for {pdf_path}: {e}", "WARN")

    # Fallback to PyPDF2 if available
    try:
        import PyPDF2
        text_parts = []
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
        if text_parts:
            return "\n".join(text_parts)
    except ImportError:
        pass  # PyPDF2 not installed
    except Exception as e:
        log(f"PyPDF2 failed for {pdf_path}: {e}", "WARN")

    # Fallback to pdfplumber if available
    try:
        import pdfplumber
        text_parts = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
        if text_parts:
            return "\n".join(text_parts)
    except ImportError:
        pass  # pdfplumber not installed
    except Exception as e:
        log(f"pdfplumber failed for {pdf_path}: {e}", "WARN")

    log(f"No PDF extraction method available for {pdf_path}. Install: poppler-utils, PyPDF2, or pdfplumber", "ERROR")
    return ""


def search_keywords(text: str, filename: str) -> list[dict]:
    """Search text for keywords and return matches."""
    matches = []
    text_lower = text.lower()

    for category, patterns in KEYWORDS.items():
        for pattern in patterns:
            for match in re.finditer(pattern, text_lower, re.IGNORECASE):
                # Get context around match
                start = max(0, match.start() - 100)
                end = min(len(text), match.end() + 100)
                context = text[start:end].replace("\n", " ").strip()

                matches.append({
                    "category": category,
                    "keyword": pattern,
                    "match": match.group(),
                    "context": f"...{context}...",
                    "file": filename,
                })

    return matches


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "document"


def discover_source(source: str, limit: int, packets: bool = False) -> tuple[list[tuple[str, str]], list[dict]]:
    """Discover newest-first agenda documents for a source via CivicClerk.

    Returns (links, meetings) where links is [(url, filename), ...] ordered
    NEWEST FIRST and meetings is the raw meeting metadata (for the staleness
    guard and for reporting real meeting dates).

    On failure, falls back to the explicitly-labeled DEFUNCT Archive Center if
    one is configured for this source.
    """
    conf = SOURCES[source]
    file_types = ("Agenda", "Agenda Packet") if packets else ("Agenda",)

    meetings: list[dict] = []
    try:
        meetings = fetch_meetings(source, limit=limit, file_types=file_types)
    except (urllib.error.URLError, OSError, ValueError, KeyError) as exc:
        log(f"Live CivicClerk lookup failed for {conf['name']}: {exc}", "ERROR")

    if meetings:
        links = []
        for meeting in meetings:
            for doc in meeting["files"]:
                # event_id disambiguates two meetings held on the same date
                # (the county routinely holds several).
                filename = (
                    f"{source}-{meeting['date']}-"
                    f"{meeting['event_id']}-{_slug(doc['type'])}.pdf"
                )
                links.append((doc["url"], filename))
        return links, meetings

    # ---- Fallback: DEFUNCT legacy Archive Center ------------------------
    legacy_url = conf.get("legacy_url")
    if not legacy_url:
        log(
            f"No live meetings for {conf['name']} and NO legacy fallback exists "
            f"for this source. Treat any scan result as unverified.",
            "ERROR",
        )
        return [], []

    log(
        f"FALLING BACK to DEFUNCT legacy Archive Center for {conf['name']}: "
        f"{legacy_url} -- results are almost certainly years out of date.",
        "WARN",
    )
    html = fetch_html(legacy_url)
    if not html:
        return [], []

    ids = {int(a) for a in re.findall(r"Archive\.aspx\?ADID=(\d+)", html)}
    links = []
    # Newest first (higher ADID == newer upload), so we stop walking
    # backwards through 2012.
    for adid in sorted(ids, reverse=True)[:limit]:
        url = urllib.parse.urljoin(legacy_url, f"/ArchiveCenter/ViewFile/Item/{adid}")
        links.append((url, f"{source}-{adid}.pdf"))
    return links, []


def load_state() -> dict:
    """Load monitoring state from file."""
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE) as f:
                state = json.load(f)
                # Validate state structure
                if not isinstance(state, dict):
                    raise ValueError("Invalid state format")
                if "processed" not in state:
                    state["processed"] = []
                return state
        except (json.JSONDecodeError, ValueError) as e:
            log(f"Corrupted state file, resetting: {e}", "WARN")
            return {"processed": [], "last_run": None}
    return {"processed": [], "last_run": None}


def save_state(state: dict) -> None:
    """Save monitoring state to file."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    state["last_run"] = datetime.datetime.now().isoformat()
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def generate_alert_report(
    all_matches: list[dict],
    new_files: list[str],
    source_status: Optional[list[dict]] = None,
    stale_warnings: Optional[list[str]] = None,
) -> str:
    """
    Generate a markdown alert report.

    `source_status` and `stale_warnings` are written into the report itself, not just
    the console. A reader coming back to this file weeks later must be able to tell
    whether "0 matches" meant "nothing happened" or "we scanned nothing." From
    Nov 2025 to Jul 2026 this file could not distinguish those, and a scan of the
    January 2013 agenda was recorded as a clean bill of health.
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    verified = bool(source_status) and not stale_warnings

    report = f"""# Agenda Monitoring Alert Report

**Generated:** {now}
**New files downloaded:** {len(new_files)}
**Keyword matches found:** {len(all_matches)}

"""

    if stale_warnings:
        report += (
            "> ## 🛑 NOT AN ALL-CLEAR — stale or empty source\n>\n"
            "> At least one source failed its freshness check, so the keyword results below\n"
            "> are **not** evidence that nothing is happening. Fix the source, then re-run.\n>\n"
        )
        for w in stale_warnings:
            for line in w.strip().splitlines():
                if line and not line.startswith("!"):
                    report += f"> {line}\n"
        report += ">\n> See `scripts/pueblo_sources.py`.\n\n"
    elif verified:
        report += "> ✅ **Source freshness verified** — an empty result below is meaningful.\n\n"
    else:
        report += (
            "> ℹ️ **Keyword-only run** (`--keywords-only`): existing PDFs were rescanned and\n"
            "> **no source freshness check was performed**. This tells you nothing about\n"
            "> whether new agendas have been published.\n\n"
        )

    if source_status:
        report += "## Source Status\n\n| Body | Newest meeting | Age | Verdict |\n| --- | --- | --- | --- |\n"
        for s in source_status:
            report += (
                f"| {s['name']} | {s.get('newest') or '—'} | "
                f"{s.get('age_days', '—')} d | {s['verdict']} |\n"
            )
        report += "\n"

    report += "---\n\n"

    if new_files:
        report += "## New Agendas Downloaded\n\n"
        for f in new_files:
            report += f"- {f}\n"
        report += "\n---\n\n"

    if all_matches:
        report += "## Keyword Alerts\n\n"

        # Group by category
        by_category = {}
        for match in all_matches:
            cat = match["category"]
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append(match)

        for category, matches in sorted(by_category.items()):
            report += f"### {category.replace('_', ' ').title()}\n\n"

            for m in matches[:10]:  # Limit to 10 per category
                report += f"**File:** `{m['file']}`\n"
                report += f"**Matched:** `{m['match']}`\n"
                report += f"**Context:** {m['context']}\n\n"

            if len(matches) > 10:
                report += f"*...and {len(matches) - 10} more matches in this category*\n\n"
    else:
        report += "## No Keyword Matches Found\n\n"
        report += "No surveillance, immigration, or civil liberties keywords detected in the scanned agendas.\n\n"

    report += """---

## Recommended Actions

If matches were found:
1. Review the full agenda PDF in `docs/agendas/`
2. Check the meeting date and add to calendar
3. Prepare public comment if needed
4. Update `docs/pueblo-watchlist.md` with relevant items
5. Share with community organizers via Signal

## Keywords Monitored

"""

    for category, patterns in KEYWORDS.items():
        report += f"**{category.replace('_', ' ').title()}:** "
        report += ", ".join(p.replace(r"\s+", " ").replace(r"\b", "") for p in patterns[:5])
        report += "...\n"

    report += "\n---\n\n*Generated by La Raza VII.I.IX monitoring system*\n"

    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        choices=["city", "county", "all"],
        default="all",
        help="Which sources to check"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="Number of newest agendas to download per source"
    )
    parser.add_argument(
        "--keywords-only",
        action="store_true",
        help="Only search existing PDFs, don't download new ones"
    )
    parser.add_argument(
        "--output",
        type=pathlib.Path,
        default=ALERT_FILE,
        help="Output file for alert report"
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress output except errors"
    )
    parser.add_argument(
        "--packets",
        action="store_true",
        help="Also download full Agenda Packets (large, but where contracts live)"
    )
    args = parser.parse_args()

    log("=" * 60)
    log("Starting agenda monitoring run")

    state = load_state()
    new_files = []
    all_matches = []
    stale_warnings = []
    source_status = []

    # Download new agendas from the LIVE CivicClerk API (newest first).
    if not args.keywords_only:
        wanted = []
        if args.source in ["city", "all"]:
            wanted.append("city_council")
        if args.source in ["county", "all"]:
            wanted.append("county_commissioners")

        for source in wanted:
            conf = SOURCES[source]
            log(f"Checking {conf['name']} agendas ({conf['api']})...")
            links, meetings = discover_source(source, args.limit, packets=args.packets)

            warning = staleness_warning(conf["name"], meetings)
            newest = meetings[0]["date"] if meetings else None
            age_days = None
            if newest:
                try:
                    age_days = (
                        datetime.date.today() - datetime.date.fromisoformat(newest)
                    ).days
                except ValueError:
                    age_days = None

            if warning:
                stale_warnings.append(warning)
                for line in warning.strip().splitlines():
                    log(line, "WARN")
                source_status.append({
                    "name": conf["name"], "newest": newest,
                    "age_days": age_days if age_days is not None else "—",
                    "verdict": "🛑 STALE / EMPTY — not an all-clear",
                })
            elif meetings:
                log(
                    f"{conf['name']}: newest meeting {newest} "
                    f"({meetings[0]['category']}) -- source is fresh"
                )
                source_status.append({
                    "name": conf["name"], "newest": newest, "age_days": age_days,
                    "verdict": "✅ fresh",
                })

            for url, filename in links:
                dest = AGENDA_DIR / filename
                if download_file(url, dest):
                    new_files.append(filename)

    # Search all PDFs for keywords
    log("Scanning agendas for keywords...")
    pdf_files = list(AGENDA_DIR.glob("*.pdf"))

    for pdf_path in pdf_files:
        text = extract_pdf_text(pdf_path)
        if text:
            matches = search_keywords(text, pdf_path.name)
            if matches:
                log(f"Found {len(matches)} keyword matches in {pdf_path.name}")
                all_matches.extend(matches)

    # Generate report
    report = generate_alert_report(all_matches, new_files, source_status, stale_warnings)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        f.write(report)
    log(f"Alert report written to {args.output}")

    # Save state
    state["processed"].extend(new_files)
    state["processed"] = list(set(state["processed"]))[-100:]  # Keep last 100
    save_state(state)

    # Summary
    log(f"Run complete: {len(new_files)} new files, {len(all_matches)} keyword matches")

    if all_matches and not args.quiet:
        print("\n" + "=" * 60)
        print("ALERT: Keywords detected in agendas!")
        print(f"See {args.output} for details")
        print("=" * 60)

    # Re-emit staleness warnings LAST so a dead source can never be mistaken for
    # a clean "no matches found" run (the 2026-02-18 false all-clear).
    if stale_warnings:
        for warning in stale_warnings:
            print(warning, file=sys.stderr)
        print(
            f"A source was stale/empty (threshold {STALENESS_DAYS} days). "
            f"The keyword result above is NOT a verified all-clear.",
            file=sys.stderr,
        )
        return 3  # Exit code 3 = source health problem

    return 0 if not all_matches else 2  # Exit code 2 = alerts found


if __name__ == "__main__":
    raise SystemExit(main())
