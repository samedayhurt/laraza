#!/usr/bin/env python3
"""Download the newest Pueblo agenda PDFs from the live CivicClerk portal API.

Primary source (verified 2026-07-29): the CivicClerk OData API. See
scripts/pueblo_sources.py for the full access pattern and the history of why the
old CivicPlus Archive Center scraper was silently returning 2013 documents.

The legacy Archive Center remains wired up ONLY as an explicitly-labeled
fallback, and any result it produces trips the staleness warning.
"""
import argparse
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

import pueblo_sources
from pueblo_sources import (
    CIVICCLERK_TENANTS,
    LEGACY_ARCHIVE_FALLBACK,
    USER_AGENT,
    fetch_meetings,
    staleness_warning,
)

# Kept for backwards compatibility with anything that imported this name.
# These are DEFUNCT archive URLs, not the live source.
ARCHIVES = dict(LEGACY_ARCHIVE_FALLBACK)

SOURCES = list(CIVICCLERK_TENANTS.keys())


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "document"


def fetch_archive_links(url: str) -> list[str]:
    """LEGACY FALLBACK: scrape the defunct CivicPlus Archive Center.

    Returns newest-first by ADID (higher ADID == newer upload). Do not rely on
    this: the archive's newest entry is 2022-05-23.
    """
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        html = resp.read().decode("utf-8", "ignore")
    ids = re.findall(r"Archive\.aspx\?ADID=(\d+)", html)
    seen = set()
    unique: list[int] = []
    for adid in ids:
        if adid in seen:
            continue
        seen.add(adid)
        unique.append(int(adid))
    # Newest first, so we stop walking backwards through 2012.
    unique.sort(reverse=True)
    return [
        urllib.parse.urljoin(url, f"/ArchiveCenter/ViewFile/Item/{adid}")
        for adid in unique
    ]


def download_file(url: str, dest: pathlib.Path) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        return False
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=90) as resp, open(dest, "wb") as fh:
        fh.write(resp.read())
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", choices=SOURCES, nargs="?", default="city_council")
    parser.add_argument("--limit", type=int, default=3, help="Number of newest meetings to download")
    parser.add_argument("--out", type=pathlib.Path, default=pathlib.Path("docs/agendas"))
    parser.add_argument(
        "--packets",
        action="store_true",
        help="Also download the full Agenda Packet, not just the Agenda",
    )
    parser.add_argument(
        "--legacy-archive",
        action="store_true",
        help="Force the DEFUNCT CivicPlus Archive Center fallback (debugging only)",
    )
    parser.add_argument(
        "--list-only",
        action="store_true",
        help="List discovered meetings and URLs without downloading",
    )
    args = parser.parse_args()

    label = CIVICCLERK_TENANTS[args.archive]["name"]
    file_types = ("Agenda", "Agenda Packet") if args.packets else ("Agenda",)

    meetings: list[dict] = []
    if not args.legacy_archive:
        try:
            meetings = fetch_meetings(args.archive, limit=args.limit, file_types=file_types)
        except (urllib.error.URLError, OSError, ValueError, KeyError) as exc:
            print(f"Live CivicClerk lookup failed for {label}: {exc}", file=sys.stderr)

    warning = staleness_warning(label, meetings)
    if warning:
        print(warning, file=sys.stderr)

    if meetings:
        print(f"{label}: {len(meetings)} meeting(s), newest first")
        downloaded = 0
        for meeting in meetings:
            print(f"  {meeting['date']}  {meeting['category']}  {meeting['portal_url']}")
            for doc in meeting["files"]:
                if args.list_only:
                    print(f"      [{doc['type']}] {doc['url']}")
                    continue
                # event_id disambiguates two meetings held on the same date
                # (the county routinely holds several).
                name = (
                    f"{args.archive}-{meeting['date']}-"
                    f"{meeting['event_id']}-{slugify(doc['type'])}.pdf"
                )
                dest = args.out / name
                try:
                    if download_file(doc["url"], dest):
                        print(f"      Saved {dest}")
                        downloaded += 1
                    else:
                        print(f"      Already have {dest}")
                except (urllib.error.URLError, OSError) as exc:
                    print(f"      FAILED {doc['url']}: {exc}", file=sys.stderr)
        if not args.list_only and downloaded == 0:
            print("No new files downloaded.")
        return 0

    # ---- Fallback: defunct Archive Center -------------------------------
    legacy_url = LEGACY_ARCHIVE_FALLBACK.get(args.archive)
    if not legacy_url:
        print(f"No live meetings and no legacy archive configured for {args.archive}.", file=sys.stderr)
        return 1

    print(
        f"FALLING BACK to the DEFUNCT legacy Archive Center for {label}: {legacy_url}\n"
        f"Anything retrieved here is almost certainly years out of date.",
        file=sys.stderr,
    )
    try:
        links = fetch_archive_links(legacy_url)
    except (urllib.error.URLError, OSError) as exc:
        print(f"Legacy archive fetch failed too: {exc}", file=sys.stderr)
        return 1
    if not links:
        print(f"No agenda links found for {args.archive}.", file=sys.stderr)
        return 1

    downloaded = 0
    for link in links[: args.limit]:
        adid = link.rstrip("/").split("/")[-1]
        dest = args.out / f"{args.archive}-{adid}.pdf"
        if args.list_only:
            print(f"  [legacy] {link}")
            continue
        try:
            if download_file(link, dest):
                print(f"Saved {dest}  (LEGACY ARCHIVE - likely stale)")
                downloaded += 1
            else:
                print(f"Already have {dest}")
        except (urllib.error.URLError, OSError) as exc:
            print(f"FAILED {link}: {exc}", file=sys.stderr)
    if not args.list_only and downloaded == 0:
        print("No new files downloaded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
