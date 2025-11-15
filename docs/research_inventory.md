# Repository Research Inventory

This inventory reclassifies all existing materials against the `AGENTS.md` workflow so contributors know what already exists, what’s missing, and which files to extend.

## 00 — Orchestrator & Global Setup
- `README.md`: Top-level mandate, roadmap, field priorities, and usage instructions.
- `AGENTS.md`: Operating manual for all agents plus ethics constraints.
- `logs/search_log.md`: Template for logging every task run.
- `logs/source_index.md`: Template for citing every source/URL.
- `logs/safety_ethics_review.md`: Template for the mandatory ethics checks before publishing.

## 01 — Pueblo Context Mapper
- (Not yet populated) — Need `data/pueblo_context_raw_notes.md` + structured JSON per AGENTS; current repo has contextual narrative inside `docs/pueblo-watchlist.md` and `opsec/Pueblo 81008 Surveillance.md` but no dedicated context file.

## 02 — Politics & Power Mapper
- `docs/pueblo-watchlist.md`: Rolling agenda & procurement tracker with actionable next steps.
- `opsec/Pueblo County Officials.md`: Party control, business ties, and notable actions for County offices.
- `opsec/Pueblo 81008 Surveillance.md`: Includes political linkage to surveillance programs.
- `data/pueblo_politics_raw_notes.md` & `data/pueblo_politics_structured.json`: Now seeded with council majority + commissioner business-tie entries; keep appending new agenda observations.

## 03 — Surveillance & Policing Researcher
- `opsec/Pueblo 81008 Surveillance.md`: Threat inventory, RTCC stack, reporting workflows.
- `docs/maps/pueblo-surveillance-map.html|.png` + `data/pueblo_apparatus.geojson`: Geospatial record of sensors and safe spaces.
- `data/surveillance_policing_raw.md` & `data/surveillance_policing_structured.json`: Populated with RTCC/Community Connect/ALPR notes and complaint escalation steps; ready for more incidents.

## 04 — Immigration & ICE Risk Mapper
- `opsec/Pueblo 81008 Surveillance.md` immigration section plus `opsec/Legal Observer Toolkit.md` references.
- `data/immigration_ice_raw.md` & `data/immigration_ice_structured.json`: Empty scaffolds awaiting hotline + courthouse logs.

## 05 — Resources Mapper
- `opsec/Legal Observer Toolkit.md`, `UTS for Civilians.md`, and primers list individual services but need consolidation.
- `data/resources_directory_raw.md` & `data/resources_directory_structured.json`: Standing by for intake.

## 06 — Rights & Risk Translator
- `README.md` (Field Use) and `comms/README.md` provide rights-forward framing.
- Target output: `reports/journalist_activist_protestor_protection_guide.md` (outline ready, awaiting upstream content).

## 07 — Report Compiler
- Placeholders for all major reports exist in `reports/` with outlines referencing self-advocacy hooks; they must be filled once structured data matures.

## 08 — Safety & Ethics Reviewer
- `logs/safety_ethics_review.md` prepared for sign-offs; begins once draft reports are ready.

## Supporting Tooling & Assets
- `comms/`, `primers/`, `opsec/`: Operational knowledge base for every agent.
- `docs/digital-footprint-protection.md`: Device + metadata hygiene checklist that links comms/opsec actions to the research workflow.
- `docs/data-legend.md`: Provenance guide describing how each dataset/report is derived (sources, automation, logging) for transparency.
- `scripts/build_pueblo_map.py`: Automation hook for refreshing the surveillance folium map.
- `.obsidian/`: Ensures local vault renders correctly for field teams.

**Next Actions**
1. Continue backfilling `data/` scaffolds with sourced notes + citations (next targets: district-level census/labor stats, upcoming council agendas, childcare/mutual-aid resources).
2. Promote structured data into the `reports/` outlines and start narrative drafting.
3. Keep this inventory updated whenever new files/gaps emerge so the orchestrator can assign work quickly, and log TODOs (e.g., census/labor pulls) in `data/pueblo_context_raw_notes.md`.
