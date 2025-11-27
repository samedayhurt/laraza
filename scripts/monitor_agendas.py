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
import urllib.parse
import urllib.request
from typing import Optional

# Configuration
AGENDA_DIR = pathlib.Path("docs/agendas")
LOG_FILE = pathlib.Path("logs/agenda_monitor.log")
ALERT_FILE = pathlib.Path("docs/agenda_alerts.md")
STATE_FILE = pathlib.Path("docs/agendas/.monitor_state.json")

# Sources to monitor
SOURCES = {
    "city_council": {
        "name": "Pueblo City Council",
        "url": "https://www.pueblo.us/Archive.aspx?AMID=37",
        "pattern": r"Archive\.aspx\?ADID=(\d+)",
    },
    "county_commissioners": {
        "name": "Pueblo County Board of Commissioners",
        "url": "https://county.pueblo.org/board-county-commissioners/meeting-schedule",
        "pattern": r"href=[\"']([^\"']*\.pdf)[\"']",
        "base_url": "https://county.pueblo.org",
    },
}

# Keywords to monitor - grouped by category
KEYWORDS = {
    "surveillance": [
        r"real[\-\s]?time\s+crime",
        r"rtcc",
        r"shotspotter",
        r"soundthinking",
        r"community\s+connect",
        r"genetec",
        r"flock\s+safety",
        r"license\s+plate\s+reader",
        r"alpr",
        r"surveillance",
        r"camera",
        r"drone",
        r"daktronics",
        r"high\s+point\s+networks",
    ],
    "immigration": [
        r"\bice\b",
        r"immigration",
        r"customs\s+and\s+border",
        r"cbp",
        r"deportation",
        r"detention",
        r"sanctuary",
        r"287\s*\(?g\)?",
        r"detainer",
    ],
    "policing": [
        r"police\s+contract",
        r"body[\-\s]?worn\s+camera",
        r"body\s*cam",
        r"use\s+of\s+force",
        r"internal\s+affairs",
        r"citizen\s+oversight",
        r"police\s+budget",
        r"public\s+safety\s+budget",
    ],
    "civil_liberties": [
        r"first\s+amendment",
        r"protest",
        r"demonstration",
        r"assembly",
        r"free\s+speech",
        r"privacy",
        r"civil\s+rights",
        r"civil\s+liberties",
    ],
    "procurement": [
        r"contract",
        r"vendor",
        r"procurement",
        r"rfp",
        r"bid",
        r"sole\s+source",
        r"arpa\s+fund",
        r"grant",
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
    """Extract text from a PDF using pdftotext if available."""
    if not shutil.which("pdftotext"):
        log("pdftotext not found - install poppler-utils for PDF text extraction", "WARN")
        return ""

    try:
        result = subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), "-"],
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.stdout
    except Exception as e:
        log(f"Failed to extract text from {pdf_path}: {e}", "ERROR")
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


def get_city_council_links(html: str, base_url: str) -> list[tuple[str, str]]:
    """Extract agenda PDF links from city council archive page."""
    links = []
    ids = re.findall(r"Archive\.aspx\?ADID=(\d+)", html)
    seen = set()

    for adid in ids:
        if adid in seen:
            continue
        seen.add(adid)
        url = urllib.parse.urljoin(base_url, f"/ArchiveCenter/ViewFile/Item/{adid}")
        filename = f"city_council-{adid}.pdf"
        links.append((url, filename))

    return links


def load_state() -> dict:
    """Load monitoring state from file."""
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"processed": [], "last_run": None}


def save_state(state: dict) -> None:
    """Save monitoring state to file."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    state["last_run"] = datetime.datetime.now().isoformat()
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def generate_alert_report(all_matches: list[dict], new_files: list[str]) -> str:
    """Generate a markdown alert report."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    report = f"""# Agenda Monitoring Alert Report

**Generated:** {now}
**New files downloaded:** {len(new_files)}
**Keyword matches found:** {len(all_matches)}

---

"""

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
    args = parser.parse_args()

    log("=" * 60)
    log("Starting agenda monitoring run")

    state = load_state()
    new_files = []
    all_matches = []

    # Download new agendas
    if not args.keywords_only:
        if args.source in ["city", "all"]:
            log("Checking Pueblo City Council agendas...")
            html = fetch_html(SOURCES["city_council"]["url"])
            if html:
                links = get_city_council_links(html, "https://www.pueblo.us")
                for url, filename in links[:args.limit]:
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
    report = generate_alert_report(all_matches, new_files)

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

    return 0 if not all_matches else 2  # Exit code 2 = alerts found


if __name__ == "__main__":
    raise SystemExit(main())
