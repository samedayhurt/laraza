# Scripts

Utility helpers that keep the Pueblo artifacts reproducible.

## Directory Contents
| Resource | Type | Description |
| --- | --- | --- |
| [README.md](README.md) | Guide | Explains what each automation does and when to run it. |
| [build_pueblo_map.py](build_pueblo_map.py) | Python script | Generates the interactive/PNG surveillance maps from the GeoJSON dataset. |
| [pueblo_sources.py](pueblo_sources.py) | Python module | Shared source config + `fetch_meetings()` / `staleness_warning()`. **Start here** to understand where agendas come from. |
| [download_agendas.py](download_agendas.py) | Python script | Downloads City Council / County Commissioner agendas and packets. |
| [monitor_agendas.py](monitor_agendas.py) | Python script | Downloads agendas *and* keyword-scans them for surveillance/ICE/civil-liberties items. |
| [weekly_monitor.sh](weekly_monitor.sh) | Shell wrapper | Cron entry point; runs the monitor and reports alert status. |

> ## ⚠️ Read this before trusting any scan result
>
> From November 2025 to July 2026 these scripts scraped `pueblo.us/Archive.aspx?AMID=37`,
> a **defunct** CivicPlus Archive Center whose newest item is **May 2022**. The agendas they
> collected were from **2012–2013**. On 2026-02-18 the pipeline reported that "the latest
> City Council agenda" had **no surveillance/ICE/civil-liberties matches** — that agenda was
> `city_council-626.pdf`, the **January 14, 2013** agenda. **The all-clear was false**, and
> nothing from Feb–Jul 2026 had ever been scanned.
>
> Fixed 2026-07-29. Pueblo has migrated to **CivicClerk**, and both bodies expose an
> unauthenticated OData API:
>
> | Body | API base |
> | --- | --- |
> | City of Pueblo | `https://puebloco.api.civicclerk.com/v1` |
> | Pueblo County BOCC | `https://pueblococo.api.civicclerk.com/v1` |
>
> **`monitor_agendas.py` now exits `3` and prints a loud banner when the newest discovered
> meeting is more than 45 days old, or when a source returns nothing.** Exit `3` means
> *"this is not a verified all-clear."* Treat it as a failure, not a quiet week. Council meets
> roughly weekly, so anything approaching a 45-day gap is already suspicious.
>
> **An empty keyword scan is only meaningful if the source is proven fresh.** Every run logs
> the newest meeting date — read it.

## `build_pueblo_map.py`
- **Purpose:** Regenerates `docs/maps/pueblo-surveillance-map.html` from `data/pueblo_apparatus.geojson` using folium, including popups for every surveillance/safe-space point.
- **Setup:** Create a virtual environment once:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install folium
  ```
  Future runs only need `source .venv/bin/activate`.
- **Usage:**
  ```bash
  .venv/bin/python scripts/build_pueblo_map.py
  ```
  The script prints the relative path of the updated HTML map. Afterward, capture a static preview for the README with:
  ```bash
  google-chrome --headless --no-sandbox --disable-gpu \
    --window-size=1200,800 \
    --screenshot=docs/maps/pueblo-surveillance-map.png \
    file://$PWD/docs/maps/pueblo-surveillance-map.html
  ```
  (Any headless browser command works as long as it outputs the PNG into `docs/maps/`.)
- **When to rerun:** Anytime you edit `data/pueblo_apparatus.geojson` or add new surveillance/safe-space features.

Keep additional automation (CORA templates, watchlist scrapers, etc.) in this folder with short READMEs so future volunteers know how to execute them offline.

## `pueblo_sources.py`
- **Purpose:** Single source of truth for *where agendas come from*. Holds the CivicClerk tenant
  config, `fetch_meetings()` (returns newest-first and filters out CivicClerk's hidden
  year-2100 template rows), `file_url()`, and `staleness_warning()`.
- **No dependencies** beyond the standard library. A browser-style `User-Agent` is required —
  the API rejects default Python agents.
- **If agendas ever stop appearing, fix it here**, not in the two callers.

## `download_agendas.py`
- **Purpose:** Downloads agenda PDFs (and optionally full packets) for either body.
- **Setup:** None. Standard library only — no venv, no Playwright.
- **Usage:**
  ```bash
  python3 scripts/download_agendas.py --list-only              # show recent meetings, download nothing
  python3 scripts/download_agendas.py city_council --limit 5
  python3 scripts/download_agendas.py county_commissioners --limit 5
  python3 scripts/download_agendas.py --packets                # full packets — see size warning below
  python3 scripts/download_agendas.py --legacy-archive          # dead Archive Center, debugging only
  ```
- ⚠️ **Packets are enormous.** The 2026-07-27 city packet alone is **76 MB** (782 pages).
  `docs/agendas/*agenda-packet.pdf` is **gitignored** to protect clone size for the
  offline/phone workflow. Re-fetch packets on demand; don't commit them.

## `monitor_agendas.py`
- **Purpose:** The weekly job. Downloads new agendas, extracts text, keyword-scans for
  surveillance / immigration / policing / civil-liberties / procurement items, and writes
  `docs/agenda_alerts.md`.
- **Usage:**
  ```bash
  python3 scripts/monitor_agendas.py --source all --limit 8
  python3 scripts/monitor_agendas.py --keywords-only     # rescan existing PDFs, no downloads
  ```
- **Exit codes — check these in cron:**
  | Code | Meaning |
  | --- | --- |
  | `0` | Ran clean, no keyword matches, **source verified fresh** |
  | `2` | Keyword matches found — read `docs/agenda_alerts.md` |
  | `3` | **A source was stale or empty. The result is NOT an all-clear.** Investigate. |
- **`pdftotext`** (poppler-utils) gives the best text extraction. Note CivicClerk PDFs
  sometimes de-space words (`realproperty`), which can *break* `\b`-anchored patterns by
  fusing tokens — worth remembering when adding keywords.
- **Keyword tuning:** `ice` excludes arena/rink/skate/hockey/cream/machine/storm/melt, because
  Pueblo's **Ice Arena** appears in agendas constantly. `police department` requires a
  procurement/action word within 120 characters, because a bare match hits every
  Employee-of-the-Month notice and routine CDOT agreement.
- **When to run:** Weekly (see `weekly_monitor.sh`), and before any meeting you plan to attend.
