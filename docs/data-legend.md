# Data Legend & Provenance Guide

This note explains where each dataset/report in the repo comes from, how it is updated, and which sources to cite so collaborators can audit or extend the work.

---

## 0. Verification Tiers — read this before citing anything

*Added 2026-07-30 after a review found the repo had been publishing claims of wildly different evidentiary weight in the same flat, declarative voice.*

**Why this section exists.** This repo had published a data-flow diagram asserting a Flock→Palantir pipeline that had been publicly fact-checked as false, and it survived for months because nothing in the file distinguished it from the verified facts around it. In the same July 2026 pass, while *fixing* that error, the maintainer introduced a new one — asserting that a federal grant condition was "the only binding FRT constraint on Pueblo" when a 2022 state statute (SB22-113) was still in force and stronger. Two different people made the same class of mistake in the same file within an hour.

The problem is not carelessness. It is that a vendor's marketing page and a court docket **look identical** once they've been paraphrased into a bullet point. Tier your claims and that stops happening.

| Tier | Meaning | How to treat it |
| --- | --- | --- |
| **[A] Primary** | An official record read directly: statute text, court docket, agenda packet, agency report, contract. | Assert it. Cite the document, not coverage of it. |
| **[B] Corroborated** | Two or more independent outlets that don't share a byline or wire feed. | Assert it, name both. |
| **[C] Single-source** | One outlet, named, otherwise uncorroborated. | Attribute in-line: *"KOAA reported…"*. Never state as bare fact. |
| **[D] Vendor / self-reported** | The vendor or agency describing its own deployment or performance. | **Reliable on existence, unreliable on scale, timing, and effectiveness.** A vendor won't invent a customer, but it will omit dates, costs, retention, and failure rates. Never quote its effectiveness claims as findings. |
| **[E] Unverified / community** | Social posts, a photo of a pole, word of mouth. | Log it, act on it operationally if you like, **never publish it as established.** Mark do-not-map. |

**Rules that follow from this:**

1. **Absence of evidence is not evidence.** "No council vote was found" ≠ "no council vote occurred." Say which one you mean. The Feb 2026 false all-clear happened because a *tooling failure* was recorded as a *finding of fact*.
2. **A [D] source that omits a date does not establish recency.** If a vendor page says "70 cameras are installed" with no timeline, you have learned the count, not when it changed. Do not write "new" or "just installed."
3. **Never claim a legal protection does not exist** without checking statutes still in force. Overstating the absence of protection makes organizers forfeit hooks they actually have — it is not a safe direction to err in.
4. **Give the base rate.** "PCSO reported 0 of 12 months" is true and damning-sounding; "PCSO is one of 59 agencies out of 235 (25%) that reported nothing" is true and *usable*, because the first invites a one-line rebuttal that discredits everything next to it.
5. **When two numbers in this repo disagree, say so in the file.** Do not silently pick one. An unreconciled figure presented as settled is how a percentage gets quoted back at you by a reporter who then finds the other number.
6. **Retractions stay visible.** If a published claim is withdrawn, strike it through with a note rather than deleting it. Someone read the old version.

**Applying tiers:** put the tag inline where the claim lives — `**[A]** SB22-113 requires…`, `**[D]** Genetec states 70 cameras are installed…`. Tagging the highest-traffic claims (README, `reports/`, handouts) matters most; raw notes in `data/` can carry the tag in the source line.

---

## 0.1 Known limitations of this research method

Be honest about these when handing findings to anyone else:

- **Much of the primary record is not machine-readable.** `chieftain.com`, `coloradonewsline.com`, `cpr.org`, `9news.com`, `dcj.colorado.gov`, `post.colorado.gov`, `county.pueblo.org`, and `census.gov/quickfacts` all return 403 to scripted clients. The city's AgendaCenter and Genetec's customer pages are JavaScript-rendered and return nothing to a plain fetch. **A periodic manual browser session is a structural requirement of this project, not an optional extra.**
- **The Census API now requires a key.** Keyless requests return an HTML "Missing Key" page — including URLs that worked in Nov 2025. Figures currently come from a Census Reporter mirror, which serves ACS verbatim but has no subject tables, so poverty is computed from B17001 rather than S1701.
- **Sensor placement is generally not public.** Camera and sensor *counts* are obtainable; *locations* mostly are not. Coverage polygons in the GeoJSON are approximations and are labeled as such. Don't let a drawn polygon imply survey accuracy.
- **Automated research has a budget ceiling.** The July 2026 pass exhausted its web-search allowance mid-run, which is why some entries are marked provisional. That is a real limit on how much can be verified in one sitting — plan passes accordingly rather than assuming a sweep was exhaustive.

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
