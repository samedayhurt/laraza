# Data Legend & Provenance Guide

This note explains where each dataset/report in the repo comes from, how it is updated, and which sources to cite so collaborators can audit or extend the work.

## 1. Context & Demographics
- **Files:** `data/pueblo_context_raw_notes.md`, `data/pueblo_context_structured.json`.
- **Sources:** U.S. Census Bureau QuickFacts (city/county), ACS 5-year subject tables for ZIPs 81008/07/06/05, city communication channels (`pueblo.us`, official Facebook).
- **Updates:** Add new census pulls (population, race, income, poverty) and note additional channels (e.g., Telegram, newsletters) as they are discovered. District-level stats will be derived once TIGER/Line boundaries are incorporated.

## 2. Politics & Power
- **Files:** `data/pueblo_politics_*`, `docs/pueblo-watchlist.md`, `reports/pueblo_power_map.md`.
- **Sources:** Local reporting (Pueblo Chieftain, Colorado Politics, Colorado Newsline), official statements (Sheriff ICE pledge), agenda trackers, and conflict-of-interest notes from `opsec/`.
- **Updates:** Weekly agenda audits via `docs/agendas/` PDFs (downloaded with `scripts/download_agendas.py`) plus manual additions from council/commission meetings. Cite every policy/official entry with public URLs (logged in `logs/source_index.md`).

## 3. Surveillance & Policing
- **Files:** `data/surveillance_policing_*`, `opsec/Pueblo 81008 Surveillance.md`, `reports/surveillance_and_policing_risks.md`.
- **Sources:** Vendor press releases (Daktronics, High Point Networks), city programs (Community Connect, Flock Safety), Pueblo PD IA site, Colorado POST, AG Pattern & Practice program.
- **Updates:** Append new vendor contracts, RTCC capabilities, complaint workflows, and CORA findings. Log each source in `logs/source_index.md` for traceability.

## 4. Immigration & ICE
- **Files:** `data/immigration_ice_*`, `reports/immigration_and_ice_risks.md`.
- **Sources:** CPR News rumor coverage, Sheriff Lucero statement, CORRN, RMIAN, Colorado Immigrant Rights Coalition.
- **Updates:** Record hotline escalations, courthouse observations, detention cases, and policy changes. Tie every incident to its source URL/date.

## 5. Resources & Mutual Aid
- **Files:** `data/resources_directory_*`, `reports/pueblo_resources_guide.md`.
- **Sources:** Organization websites (Colorado Legal Services, Posada, YWCA, Rape Crisis Services, Health Solutions, Catholic Charities, PCCLD TechConnect, Cooperative Care Center, etc.).
- **Updates:** Add new orgs as you verify services; include contact info, eligibility, and verification date. Keep the quick-reference table synced with the structured JSON.

## 6. Protection & Comms
- **Files:** `reports/journalist_activist_protestor_protection_guide.md`, `docs/digital-footprint-protection.md`, `comms/README.md`, `opsec/README.md`.
- **Sources:** Internal playbooks plus public best practices (e.g., DSOK workflows). When citing new guidance, point to the relevant report (`surveillance_and_policing_risks.md`, etc.) so users see the research backing the recommendation.

## 7. Automation & Logs
- **Automation:** `scripts/download_agendas.py` pulls the newest agenda PDFs into `docs/agendas/`. Requires the repo’s Python venv + Playwright (see `scripts/README.md`).
- **Logging:** Every research or automation run must update `logs/search_log.md` with date/agent/task/notes and add source entries to `logs/source_index.md`. Safety/ethics reviews are recorded in `logs/safety_ethics_review.md`.

## How to Use This Legend
1. When contributing data or reports, reference the section above to confirm you’re using the canonical files and logging sources correctly.
2. If a new type of data (e.g., union records, detention zoning maps) is added, extend this legend with a short paragraph so future teams understand the provenance.
3. Keep transparency front and center: every factual claim should trace back to a public URL or official document stored locally, and the relevant log entry should make it easy to audit the workflow.
