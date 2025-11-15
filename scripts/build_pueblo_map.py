#!/usr/bin/env python3
"""Generate the Pueblo surveillance folium overlay from GeoJSON data."""

from pathlib import Path
import json
import folium

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "pueblo_apparatus.geojson"
OUT_DIR = ROOT / "docs" / "maps"
OUT_PATH = OUT_DIR / "pueblo-surveillance-map.html"

STYLE_COLORS = {
    "boundary": {"color": "#ff6f00", "fillColor": "#ff6f00", "fillOpacity": 0.05},
    "default": {"color": "#0057b7", "fillColor": "#3388ff", "fillOpacity": 0.2},
}


def style_function(feature):
    base = STYLE_COLORS.get(feature["properties"].get("type"), STYLE_COLORS["default"])
    return {
        "color": base["color"],
        "fillColor": base["fillColor"],
        "fillOpacity": base["fillOpacity"],
        "weight": 2,
    }


def main():
    data = json.loads(DATA.read_text())
    m = folium.Map(location=[38.29, -104.61], zoom_start=12, tiles="CartoDB positron")

    folium.GeoJson(
        data,
        style_function=style_function,
        tooltip=folium.features.GeoJsonTooltip(fields=["name", "type"], aliases=["Name", "Category"]),
    ).add_to(m)

    for feature in data["features"]:
        if feature["geometry"]["type"] != "Point":
            continue
        lon, lat = feature["geometry"]["coordinates"]
        props = feature["properties"]
        html = (
            f"<strong>{props['name']}</strong><br/>{props['description']}<br/>"
            + "<em>Sources:</em> "
            + "<br/>".join(props.get("sources", []))
        )
        folium.Marker([lat, lon], popup=folium.Popup(html, max_width=360)).add_to(m)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    m.save(OUT_PATH)
    print(f"Map written to {OUT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
