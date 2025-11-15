#!/usr/bin/env python3
"""Download the latest agenda PDFs from configured Pueblo Agenda Center archives."""
import argparse
import pathlib
import re
import sys
import urllib.parse
import urllib.request

ARCHIVES = {
    "city_council": "https://www.pueblo.us/Archive.aspx?AMID=37",
    # Add other archives (e.g., planning commission) here when IDs are known.
}

def fetch_archive_links(url: str) -> list[str]:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8", "ignore")
    ids = re.findall(r"Archive\.aspx\?ADID=(\d+)", html)
    links = []
    seen = set()
    for adid in ids:
        if adid in seen:
            continue
        seen.add(adid)
        links.append(urllib.parse.urljoin(url, f"/ArchiveCenter/ViewFile/Item/{adid}"))
    return links

def download_file(url: str, dest: pathlib.Path) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        return False
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp, open(dest, "wb") as fh:
        fh.write(resp.read())
    return True

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", choices=ARCHIVES.keys(), nargs="?", default="city_council")
    parser.add_argument("--limit", type=int, default=3, help="Number of newest files to download")
    parser.add_argument("--out", type=pathlib.Path, default=pathlib.Path("docs/agendas"))
    args = parser.parse_args()

    archive_url = ARCHIVES[args.archive]
    links = fetch_archive_links(archive_url)
    if not links:
        print(f"No agenda links found for {args.archive}.", file=sys.stderr)
        return 1
    downloaded = 0
    for link in links[: args.limit]:
        adid = link.rstrip("/").split("/")[-1]
        dest = args.out / f"{args.archive}-{adid}.pdf"
        if download_file(link, dest):
            print(f"Saved {dest}")
            downloaded += 1
        else:
            print(f"Already have {dest}")
    if downloaded == 0:
        print("No new files downloaded.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
