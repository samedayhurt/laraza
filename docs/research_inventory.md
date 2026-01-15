# Repository Research Inventory

This inventory reclassifies all existing materials against the `AGENTS.md` workflow so contributors know what already exists, what’s missing, and which files to extend.

## 00 — Orchestrator & Global Setup
- `README.md`: Top-level mandate, roadmap, field priorities, and usage instructions.
- `AGENTS.md`: Operating manual for all agents plus ethics constraints.
- `logs/search_log.md`: Template for logging every task run.
- `logs/source_index.md`: Template for citing every source/URL.
- `logs/safety_ethics_review.md`: Template for the mandatory ethics checks before publishing.

## 01 — Pueblo Context Mapper
- **POPULATED** — `data/pueblo_context_raw_notes.md` contains demographics, economy, geographic focus (ZIP 81008), governance structure, census baselines, and city communication channels.
- `data/pueblo_context_structured.json` contains normalized demographic and economic data.
- **Pending:** District-level census/labor statistics (logged as TODO for future sprint).

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
- **POPULATED** — `data/immigration_ice_raw.md` contains:
  - Federal court ruling (*Ramirez Ovando v. Noem*, Nov 25, 2025)
  - Sheriff ICE cooperation policy and statements
  - CORRN hotline documentation and volunteer network (3,000+)
  - RMIAN detention hotline and services
  - Colorado Immigrant Rights Coalition workshops
  - ICE social media monitoring threat assessment
  - Statewide ICE enforcement surge data (arrests quadrupled 2025 vs 2024)
  - Courthouse monitoring template
- `data/immigration_ice_structured.json`: Contains normalized risks, policies, and advocacy resources.

## 05 — Resources Mapper
- `opsec/Legal Observer Toolkit.md`, `UTS for Civilians.md`, and primers list individual services.
- **POPULATED** — `data/resources_directory_raw.md` contains 11 dated entries for legal aid, housing, DV services, immigration support, mental health, and mutual aid.
- `data/resources_directory_structured.json` contains 21 verified resources with contact info, eligibility, and services including:
  - Colorado Legal Services, Posada, Mariposa Center (DV), Juniper Southern Colorado (sexual assault)
  - CORRN, RMIAN, Catholic Charities immigration services
  - Health Solutions, Pueblo Community Health Center (FQHC)
  - Care and Share, Salvation Army, Cooperative Care Center
  - NeighborWorks, United Way, 211 Colorado
- **Pending:** Mutual aid networks, bail funds, worker centers, LGBTQ+ affirming services.

## 06 — Rights & Risk Translator
- `README.md` (Field Use) and `comms/README.md` provide rights-forward framing.
- **COMPLETED** — `reports/journalist_activist_protestor_protection_guide.md` is fully populated with:
  - Top risks for November 2025 (RTCC, digital surveillance, ICE escalation, political landscape)
  - Field safety checklists (before/during/after actions)
  - Digital hygiene essentials (phone security, secure comms, VPN recommendations)
  - Rapid resource contact table
  - Emergency digital security help (Access Now, EFF Cape, Front Line Defenders)
- **Pending:** Spanish translation of protection guide.

## 07 — Report Compiler
- **COMPLETED** — All major reports in `reports/` are fully populated:
  - `pueblo_power_map.md`: Political power structure, decision-makers, conflicts of interest
  - `surveillance_and_policing_risks.md`: RTCC stack, civil liberties concerns, complaint workflows
  - `immigration_and_ice_risks.md`: ICE agreements, cooperation policies, defense resources
  - `pueblo_resources_guide.md`: Legal, financial, health, activist support services
  - `journalist_activist_protestor_protection_guide.md`: Actionable field safety guidance

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
