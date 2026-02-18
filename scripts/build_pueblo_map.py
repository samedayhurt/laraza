#!/usr/bin/env python3
"""Generate the Pueblo surveillance folium overlay from GeoJSON data."""

from pathlib import Path
import json
import folium
from folium import plugins

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "pueblo_apparatus.geojson"
OUT_DIR = ROOT / "docs" / "maps"
OUT_PATH = OUT_DIR / "pueblo-surveillance-map.html"

STYLE_COLORS = {
    "boundary": {"color": "#ff6f00", "fillColor": "#ff6f00", "fillOpacity": 0.05},
    "default": {"color": "#0057b7", "fillColor": "#3388ff", "fillOpacity": 0.2},
}

TYPE_META = {
    "rtcc": {"color": "red", "icon": "bullseye"},
    "acoustic-surveillance": {"color": "darkred", "icon": "volume-up"},
    "drone-surveillance": {"color": "purple", "icon": "plane"},
    "fixed-surveillance": {"color": "orange", "icon": "video-camera"},
    "mobile-surveillance": {"color": "darkpurple", "icon": "truck"},
    "alpr": {"color": "green", "icon": "camera"},
    "alpr-corridor": {"color": "green", "icon": "road"},
    "park-surveillance": {"color": "cadetblue", "icon": "tree"},
    "community-support": {"color": "lightblue", "icon": "heart"},
    "law-enforcement": {"color": "blue", "icon": "shield"},
    "institution": {"color": "gray", "icon": "university"},
    "watch-site": {"color": "black", "icon": "flag"},
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
    m = folium.Map(location=[38.29, -104.61], zoom_start=12, tiles="CartoDB positron", control_scale=True)
    plugins.Fullscreen(position="topleft").add_to(m)

    # Build per-type layers for toggling.
    layers = {}
    for feature in data["features"]:
        ftype = feature["properties"].get("type", "default")
        layers.setdefault(ftype, folium.FeatureGroup(name=ftype, show=True))

    # Add polygons/lines first so markers sit on top.
    for feature in data["features"]:
        if feature["geometry"]["type"] == "Point":
            continue
        ftype = feature["properties"].get("type", "default")
        folium.GeoJson(
            feature,
            style_function=style_function,
            tooltip=folium.features.GeoJsonTooltip(fields=["name", "type"], aliases=["Name", "Category"]),
        ).add_to(layers[ftype])

    # Cluster points by type.
    clusters = {ftype: plugins.MarkerCluster(name=f"{ftype}-cluster") for ftype in layers}
    for feature in data["features"]:
        if feature["geometry"]["type"] != "Point":
            continue
        lon, lat = feature["geometry"]["coordinates"]
        props = feature["properties"]
        ftype = props.get("type", "default")
        meta = TYPE_META.get(ftype, {"color": "blue", "icon": "info-sign"})

        src_lines = []
        for src in props.get("sources", []):
            if isinstance(src, str) and src.startswith("http"):
                src_lines.append(f'<a href="{src}" target="_blank">{src}</a>')
            else:
                src_lines.append(src)
        sources_html = "<br/>".join(src_lines) if src_lines else "n/a"

        html = (
            f"<strong>{props.get('name','')}</strong><br/>{props.get('description','')}"
            f"<br/><em>Sources:</em><br/>{sources_html}"
        )
        icon = folium.Icon(color=meta["color"], icon=meta["icon"], prefix="fa")
        folium.Marker([lat, lon], popup=folium.Popup(html, max_width=360), icon=icon).add_to(
            clusters[ftype]
        )

    for ftype, layer in layers.items():
        cluster = clusters.get(ftype)
        if cluster:
            cluster.add_to(layer)
        layer.add_to(m)

    folium.LayerControl(collapsed=False).add_to(m)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    m.save(OUT_PATH)
    print(f"Map written to {OUT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
