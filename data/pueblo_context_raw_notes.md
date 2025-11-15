# Pueblo Context Raw Notes

Collect demographic, economic, and governance context about Pueblo so downstream agents have consistent baselines.

## 2025-11-15 — Political realignment
- **Source:** `opsec/Pueblo 81008 Surveillance.md` + `docs/pueblo-watchlist.md` references (Colorado Politics, Pueblo Chieftain).
- **Notes:** Pueblo historically leaned Democratic, but as of 2025 Republicans control 5 of 7 city council seats and 2 of 3 county commission seats. Council races remain nonpartisan on paper, yet the conservative majority is driving surveillance approvals and curfew debates.
- **Follow-up:** Track whether November 2025 municipal results shift the balance back toward moderates; log each council vote tied to surveillance budgets.

## 2025-11-15 — Economic anchors
- **Source:** Existing repo narratives (README field priorities, watchlist) referencing RTCC vendors, railroad tech ties, and mall security footprint.
- **Notes:** Major local employers include rail technology firms (linked to Commissioner Miles Lucero), higher-ed institutions (Pueblo Community College, CSU-Pueblo), and downtown retail/tourism (Riverwalk, Union Ave) which fund ALPR corridors. Surveillance investments (Daktronics, High Point Networks, Flock Safety) represent new external vendors extracting public safety budgets.
- **Follow-up:** Pull Chamber of Commerce or state labor department data to quantify top employers and unemployment rate; correlate with surveillance/policing hotspots.

## 2025-11-15 — Geographic focus: ZIP 81008
- **Source:** `opsec/Pueblo 81008 Surveillance.md` + `data/pueblo_apparatus.geojson`.
- **Notes:** North-side ZIP 81008 includes the RTCC, mall, and major ingress/egress corridors targeted for ALPR and Community Connect recruitment. Mapping doorbell densities and commercial camera clusters remains a priority for march route planning.
- **Follow-up:** Update GeoJSON with new sensors/observations after each protest walk-through; capture socio-economic indicators for 81008 vs. rest of city.

## 2025-11-15 — Governance structure snapshot
- **Source:** `opsec/Pueblo 81008 Surveillance.md` (Political Power Snapshot section).
- **Notes:** Pueblo operates under a mayor-council model with nine districts, historically Democratic but now politically split; council races are nominally nonpartisan yet functionally align with partisan priorities. County commission shifts mirror this, giving GOP-aligned officials leverage even while city/county branding remains “purple.”
- **Follow-up:** Document mayoral authority vs. council authority (e.g., veto power, appointment approvals) and map how district boundaries overlap with surveillance deployments to assess representation gaps.

## 2025-11-15 — Census baseline (population, income, poverty)
- **Source:** U.S. Census Bureau, QuickFacts for Pueblo city and Pueblo County (https://www.census.gov/quickfacts/fact/table/pueblocitycolorado,pueblocountycolorado/PST045223), accessed 2025-11-15.
- **Notes:** 2023 population estimates — Pueblo city: 111,456; Pueblo County: 168,424. Median household income (2018-2022 dollars) — city: $54,137; county: $56,567. Persons in poverty — city: 22.8%; county: 18.1%.
- **Follow-up:** Incorporate these figures into public briefings and track changes annually; overlay poverty hotspots on surveillance map layers to highlight equity concerns.

## 2025-11-15 — ZIP-level median income & poverty
- **Source:** U.S. Census Bureau, ACS 2022 5-year subject tables via API (NAME, S1901_C01_012E, S1701_C02_001E for ZCTAs 81008, 81007, 81006, 81005).
- **Notes:** ZCTA 81008 (north-side RTCC zone) median household income $63,803; poverty ~13.62%. 81007 (West Pueblo/County) $89,530 income, 24.27% poverty. 81006 (east/southeast county) $67,077 income, 15.06% poverty. 81005 (southside city) $66,607 income, 40.08% poverty.
- **Follow-up:** Overlay these statistics on the folium map to show where surveillance budgets intersect with higher poverty (especially 81005) vs. higher-income areas (81007). Use the disparity when pushing for community investment vs. tech spend.

## 2025-11-15 — City communication channels to monitor
- **Source:** City of Pueblo official website (https://www.pueblo.us/) and Facebook page (https://www.facebook.com/CityofPueblo/), accessed 2025-11-15.
- **Notes:** City posts meeting updates, emergency alerts, and surveys on the website (Agenda Center, News releases) plus mirrored posts/videos on Facebook. Monitoring both ensures we catch last-minute agenda changes, proclamations, and public comment opportunities outside of PDF packets.
- **Follow-up:** Subscribe to site RSS/newsletters if available; add the Facebook page to the media monitoring list so quotes or livestreams can be archived for reports.

## TODO — District-level census + labor distribution
- **Planned:** Pull ACS 5-year estimates or local planning department shapefiles to map population, race, income, and unemployment by council district; collect top 10 employers with headcounts and union presence.
- **Status:** Pending—requires either API pulls or manual extraction from city economic development reports; note to revisit in next sprint.
- **Hint:** Once GIS boundaries are available, use Census API (state=08, place=62000) with TIGER/Line shapefiles to aggregate tracts per council district; for employers, pull Pueblo Chamber/Economic Development reports or state labor department dashboards.
