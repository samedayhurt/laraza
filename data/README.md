# Data

Raw notes, structured exports, and geospatial layers that power every report in this repo. Update these files first so downstream automation and compilers stay trustworthy.

## Table of Contents
| Resource | Format | Description |
| --- | --- | --- |
| [pueblo_context_raw_notes.md](pueblo_context_raw_notes.md) | Markdown | Chronological notebook capturing demographic, economic, and institutional context about Pueblo. |
| [pueblo_context_structured.json](pueblo_context_structured.json) | JSON | Agent-ready snapshot of Pueblo context fields (population, districts, institutions). |
| [pueblo_politics_raw_notes.md](pueblo_politics_raw_notes.md) | Markdown | Free-form research log on offices, power brokers, campaign moves, and notable votes. |
| [pueblo_politics_structured.json](pueblo_politics_structured.json) | JSON | Structured representation of offices, office holders, campaign finance, and controversies. |
| [surveillance_policing_raw.md](surveillance_policing_raw.md) | Markdown | Notes on RTCC tooling, procurement, policing controversies, and data-sharing findings. |
| [surveillance_policing_structured.json](surveillance_policing_structured.json) | JSON | Normalized `systems`, `policies`, and `cases` objects referenced by the surveillance report. |
| [immigration_ice_raw.md](immigration_ice_raw.md) | Markdown | Field notes covering ICE activity, jail cooperation chatter, and legal rapid-response leads. |
| [immigration_ice_structured.json](immigration_ice_structured.json) | JSON | Agreements, public statements, case summaries, and advocacy org records for immigration analysis. |
| [resources_directory_raw.md](resources_directory_raw.md) | Markdown | Scratchpad for resource leads, interviews, and intake notes before they are normalized. |
| [resources_directory_structured.json](resources_directory_structured.json) | JSON | Categorized directory of legal, housing, health, and activist resources for quick lookup. |
| [pueblo_apparatus.geojson](pueblo_apparatus.geojson) | GeoJSON | Map layer describing surveillance nodes and safe spaces used by `scripts/build_pueblo_map.py`. |
