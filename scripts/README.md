# Scripts

Utility helpers that keep the Pueblo artifacts reproducible.

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
