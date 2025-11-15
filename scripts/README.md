# Scripts

Utility helpers that keep the Pueblo artifacts reproducible.

## Directory Contents
| Resource | Type | Description |
| --- | --- | --- |
| [README.md](README.md) | Guide | Explains what each automation does and when to run it. |
| [build_pueblo_map.py](build_pueblo_map.py) | Python script | Generates the interactive/PNG surveillance maps from the GeoJSON dataset. |
| [download_agendas.py](download_agendas.py) | Python script | Uses Playwright to fetch and archive Pueblo City Council agendas. |

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

## `download_agendas.py`
- **Purpose:** Fetches the latest City Council agenda PDFs from the `pueblo.us` Archive Center so planners can review surveillance, ICE, and voter-rights votes without manual downloads.
- **Setup:** Uses the repo’s Python venv. Install Playwright once and download Chromium (already done in this repo):
  ```bash
  python3 -m venv .venv
  . .venv/bin/activate
  pip install playwright
  playwright install chromium
  ```
  (Future runs only need `. .venv/bin/activate`.)
- **Usage:**
  ```bash
  .venv/bin/python scripts/download_agendas.py --limit 2
  ```
  Downloads the newest two PDFs into `docs/agendas/` (e.g., `city_council-3943.pdf`). Additional archive IDs can be added inside the script (`ARCHIVES` dict) as they are discovered.
- **When to run:** Weekly, before meetings, so surveillance/ICE/union/voter-rights agenda items can be parsed and logged immediately.
