# Pueblo Power & Procurement Watchlist

Use this tracker to monitor upcoming votes, contracts, and business interests that directly affect surveillance, policing budgets, and protest safety in Pueblo County.

## 1. Meeting Calendar Targets

> ⚠️ **Agenda automation was broken from Nov 2025 to Jul 2026.** `scripts/monitor_agendas.py` was scraping `pueblo.us/Archive.aspx?AMID=37`, a **defunct** Archive Center whose newest item is May 2022. The PDFs it collected are from **2012–2013** — `city_council-626.pdf`, logged on 2026-02-18 as "the latest agenda" with "no keyword matches," is the **January 14, 2013** agenda. **That all-clear was void.** No Feb–Jul 2026 agenda has been keyword-scanned. See `logs/search_log.md` (2026-07-29) and `scripts/README.md`.

| Body | Why it matters | Where to pull agendas |
| --- | --- | --- |
| **City Council** (1 City Hall Pl.) | Council leans conservative (5 of 7 seats) and approves surveillance expansions, protest permits, and curfews.[^1] The 5-2 majority survived the Nov 2025 seating of three new members — confirmed by the Feb 23, 2026 half-cent sales-tax ordinance passing 5-2. | Use the live source now wired into `scripts/monitor_agendas.py`; the [AgendaCenter page](https://www.pueblo.us/AgendaCenter/City-Council-1) renders via JavaScript and returns nothing to a plain scraper. **Verify the newest meeting date on every run** — a stale source is indistinguishable from a quiet month. |
| **Board of County Commissioners** (215 W. 10th) | Controls sheriff/jail budgets and signs RTCC/ALPR contracts; GOP holds 2 of 3 seats.[^2] **D3 is contested in Nov 2026** — Angela Giron (D) vs. Zach Swearingen (R) — for the seat controlling PCSO/jail/RTCC budgets. | `county.pueblo.org/board-county-commissioners/meeting-schedule` now returns **HTTP 404**, and the county domain returns 403 to scripted clients. Use the live source in the monitor script; fall back to Chieftain recaps. |
| **Public Safety Committee / RTCC briefings** | First public venue for Community Connect and Flock expansions; gather serial numbers for CORA requests. | Watch the agenda center for “Public Safety” keywords and attend virtually if possible. |

## 2. Procurement & Surveillance Pipeline
| Program | Current status | Watch items |
| --- | --- | --- |
| **RTCC build-out** | Daktronics & High Point Networks installed the dvLED wall + network backbone in 2024-25.[^3] | Track amendments for maintenance contracts, ShotSpotter renewals, Cloud storage add-ons; capture vendor invoices via CORA. |
| **Community Connect (Genetec)** | City advertising four integration “pillars,” pushing businesses/residents to register cameras.[^4] | Flag agenda items mentioning Genetec, Arden, High Point, or Linx; compare registries with neighborhoods lacking resources. |
| **Flock Safety ALPRs** | Began as Downtown Association–funded cameras on Union Ave & Riverwalk.[^5] **Pueblo PD is now expanding to 12 cameras (4 live as of the KOAA report), plus 4 mobile trailers and park cameras at Mitchell, Mineral Palace, City, and El Centro.**[^11] | ⚠️ **No council authorization vote for this expansion could be found anywhere in Feb–Jul 2026** — while the city was simultaneously lobbying against state ALPR regulation. **No disclosed cost, no funding source, no retention policy.** Deputy Chief Jim Martin has publicly asserted that a query audit log exists — **that statement makes the log CORA-able. Request it.** Ask specifically whether Pueblo data is exposed in Flock's nationwide lookup network, and whether Pueblo has any of the safeguards Denver negotiated (a $100k penalty for federal immigration sharing, federal task-force officers barred, data disabled in the national lookup). |

### 🔴 Live item — City Council, July 27 2026, Item N3 (verified in the agenda packet)

An ordinance accepting a **Colorado Division of Criminal Justice grant of $275,384** (CY2026, project **PS2509**, DCJ grant **#2024-SC-25-866**), ratifying the Mayor's execution. Verified directly in the July 27 2026 agenda packet. Three things in it matter:

1. **The grant's research component names the RTCC.** The packet states: *"The subject matter of research will be a comprehensive study of the **Real Time Crime Center**."* The work is assigned to PPD's **Crime Analyst and Threat Liaison Officer** with a research partner from the **Thomas V. Healy Center at CSU-Pueblo**. (Note the packet is internally ambiguous — the same paragraph also describes studying "effects of the CIT program" — so confirm the actual scope of work before characterizing it publicly.) **A city-funded RTCC study is the single best available lever for getting an independent coverage map and audit into the public record. Ask who owns the output and whether it will be published.**
2. **PPD was added as one of five new sites to the DOJ National Public Safety Partnership (PSP)** — a federal technical-assistance relationship that appears nowhere else in this repo. It brings DOJ/BJA consultants into PPD operations. Establish what data flows through it.
3. **Grant conditions create two enforceable hooks:** condition **#26 bars spending on unmanned aircraft systems (UAS/drones)** entirely, and condition **#27 permits Facial Recognition Technology only if the City already has policies protecting Fourth and First Amendment rights.** → **CORA target: does the City of Pueblo have an FRT policy?** If it does not, it cannot lawfully spend this grant on FRT. If it claims one, that document should be public. Colorado has **no** state FRT warrant requirement after SB26-071 died, so this grant condition may be the only binding FRT constraint on Pueblo.

Also on the same agenda: **item R8** (updated CIT Master Services Agreement with Health Solutions) and **item N6** (PCSO–PPD MOU on alternate/default **E911 call routing** between answering points).

**Notable negative — worth knowing:** a keyword scan of **29 city and 20 county agendas/packets (Jan–Jul 2026)** returned **zero** genuine hits for Flock, ALPR, license plate readers, ShotSpotter, SoundThinking, Genetec, or Fusus. No new ALPR or gunshot-detection procurement went through either body in 2026. Combined with the 12-camera Flock expansion reported by KOAA, that means **the ALPR build-out is not moving through council at all** — it is running on grants, the Downtown Association, vendor trials, or mayoral authority. Stop watching only for agenda items; start asking how it is being funded.

## 3. Business & Conflict Tracker
| Official | Business / Leverage | Decisions to watch |
| --- | --- | --- |
| **Zach Swearingen (R)** | Co-founded Republic Shooting Range and The Beach fitness club.[^2] | Push transparency when firearms contracts or shooting range subsidies appear. |
| **Miles Lucero (D)** | Ties to railroad technology firms + medical practice via spouse.[^2] | Watch infrastructure/jail procurement votes for potential overlaps. |
| **Sheriff David Lucero (D)** — **OUTGOING** | Runs jail/ICE interactions; issued public pledge to avoid ICE round-ups absent criminal nexus.[^6] | **Lucero LOST the June 30, 2026 Democratic primary to Allen Medina, 53.16%–46.84%.**[^8] No Republican filed, so Medina is effectively the next sheriff as of **January 2027**. Every ICE-protection assumption in this repo rests on a pledge belonging to an officeholder on the way out. |
| **Sheriff-elect Allen Medina (D)** | Takes office Jan 2027 over the jail, detainer practice, and PCSO's share of the RTCC/ALPR stack. | Has said he will not raid non-criminal residents and frames it in 4th/5th Amendment terms; centers transparency; will end the FOP litigation.[^9] **He has said nothing on the record about surveillance technology — ALPR, ShotSpotter, drones, or data sharing. Get him on record before January.** |

## 4. State Legislation Tracker (2026 session — CLOSED)

> ### ⚠️ OUTCOME: all three bills are DEAD. Colorado adjourned sine die May 13, 2026 with **no** ALPR statute, **no** law-enforcement surveillance statute, and **no** ban on government purchase of third-party data.
>
> Every constraint on Pueblo's RTCC stack is therefore **local and discretionary**. There is no state warrant requirement, no retention cap, no mandated audit, and no public device-count report. Advocacy has to run through council, the mayor, the sheriff, and CORA — not Denver.

The city passed resolutions *opposing* three bills at the **February 9, 2026** council meeting.[^7] All three then failed:

| Bill | Subject | City position | Final disposition | Why it mattered locally |
| --- | --- | --- | --- | --- |
| **[SB26-070](https://leg.colorado.gov/bills/SB26-070)** ("PEEPS Act") | Bans government access to databases revealing historical location information for individuals or vehicles. | **Opposed** | **LOST.** Cleared Senate Judiciary (2/23) and Appropriations (4/21), then **sponsors pulled it at Second Reading 4/29/26** — recorded as "Laid Over to 07/04/2026," a parking maneuver past sine die. Sen. Amabile: *"We didn't have the votes"*; she was told the Governor would veto. | Would have required a warrant for location data >72 hrs old, ~30-day retention cap, query logging, and a **public annual report of device count and locations**. |
| **[SB26-071](https://leg.colorado.gov/bills/SB26-071)** ("SAFE Act") | Limits law-enforcement surveillance tech to lawful public-safety purposes; imposes collection/storage/sharing/destruction rules. | **Opposed** | **LOST. Postponed indefinitely 6–1 in Senate Judiciary, 5/6/26.** Would have taken effect Jul 1, 2027. | Would have required a warrant for facial recognition, mandatory data destruction, a bar on data sales, and **biennial AG audits** — hitting ShotSpotter, BRINC drones, park cameras, BWC, Flock, and Community Connect at once. **Facial recognition in Colorado remains warrantless.** |
| **[HB26-1037](https://leg.colorado.gov/bills/HB26-1037)** | Bars government purchase of personal data from third parties. | **Opposed** — the city's resolution called it **"harmful to public safety."** | **LOST by one vote, twice, in one day.** House Judiciary 4/22/26: amendment adopted 6–5, refer-to-Appropriations **failed 5–6**, postpone-indefinitely **passed 6–5**. | Would have barred obtaining broker data "for anything of value" and added a **private cause of action** plus evidence exclusion. **This is the bill Pueblo called "harmful to public safety" and the one that came closest to passing — the highest-leverage 2027 target.** |

**Two 2026 laws that DID pass and do bind local agencies:**

| Law | Effective | What it creates that you can obtain |
| --- | --- | --- |
| **[HB26-1123](https://leg.colorado.gov/bills/hb26-1123)** (preventing sexual abuse in jails) | May 27, 2026 | Requires **body-worn-camera recording of jail strip searches**, restricted-access tagging, and an **annual report to the AG and jail standards advisory committee**. Applies to PCSO's new 672-bed facility — a brand-new document stream. |
| **[HB26-1276](https://leg.colorado.gov/bills/hb26-1276)** (safety of individuals who are immigrants) | Aug 12, 2026 | Quarterly unannounced detention inspections, POST immigration training, and an **AG-set policy on PII sharing** — the only surviving state lever on local data sharing. |

**Also note:** Gov. Polis **vetoed** HB26-1210 (surveillance pricing) and **vetoed SB26-005** on June 3, 2026 — so do **not** claim a state-court remedy against ICE agents exists. With the governor's office open in Nov 2026, sponsors have signalled a 2027 rewrite ("probably with a new governor" — Rep. Nguyen). The Nov 2026 governor's race is the upstream variable.

**Still unresolved in the public record:** vote counts and individual council-member statements on the Feb 9 resolutions, and the full WHEREAS clauses. Primary sources are the Feb 9 2026 agenda packet on the [City of Pueblo AgendaCenter](https://www.pueblo.us/AgendaCenter/City-Council-1) and the [meeting video](https://www.facebook.com/CityofPueblo/videos/pueblo-city-council/2145740586181846/). **Also unconfirmed:** whether the third resolution concerned HB26-1037 or HB26-1071 — one agenda summary lists a *support* position on HB26-**1071**, so verify the bill number against the signed resolution before citing.

**No Pueblo official is confirmed to have testified** at the Capitol on any of the three. Six news accounts name no Pueblo witness, and the SB26-070 attachment list contains no City of Pueblo, Pueblo PD, or CML filing — the only named municipal witness is a **Colorado Springs** deputy chief. Do not assert Pueblo testimony; the Senate Judiciary (2/23), Senate Appropriations (4/21), and House Judiciary (2/25) witness sign-in sheets are still outstanding.

The Colorado Municipal League's [position paper on SB26-070](https://www.cml.org/home/publications-news/resource-detail/position-paper-sb26-070-ban-government-access-to-historical-location-information) mirrors the likely Pueblo rationale (72-hour warrant impractical; 30-day deletion conflicts with court needs; public-records exposure; compliance burden).

## 5. Rapid Actions for Researchers
1. **Every Sunday:** Pull upcoming council/commission agendas, highlight items referencing surveillance tech or contracts over $250k, and post summaries in the protest Signal group.
2. **During meetings:** Livetweet/Thread about surveillance votes, tagging local reporters and linking to `opsec/Pueblo 81008 Surveillance.md` so the conversation stays grounded in prior findings.
3. **After votes:** File template CORA requests (scripts coming soon) for winning vendors’ scoring sheets, line-item costs, and data-sharing clauses; store responses in `/docs/procurement/`.

### If you only have 5 minutes
1. Skim the latest agenda PDF, search for “contract,” “purchase,” or “license plate,” and screenshot any hits for the team.
2. Post a reminder in the outreach chat about the next council meeting time/place so marshals can plan a presence.
3. Email the relevant clerk with a one-line records request (“Please provide the contract approved on [date] for [vendor]”) so the paper trail starts before implementation.

## References
[^1]: Dennis Maes, “Pueblo Democrats are now in disarray,” *Colorado Politics*, Mar 28 2025. https://www.coloradopolitics.com/2025/03/28/pueblo-democrats-are-now-in-disarray-maes-2ed3efb3-f7ee-474e-8597-316bf4c2d007/
[^2]: James Bartolo, “What to expect in 2025 with two new Pueblo County commissioners set to take office,” *Pueblo Chieftain*, Dec 9 2024. https://www.chieftain.com/story/news/2024/12/09/what-to-know-about-the-new-board-of-pueblo-county-commissioners/76621912007/
[^3]: “Eye On Crime Increases with Daktronics, High Point Networks Collaboration for Pueblo Police Department’s Real-Time Crime Center,” Daktronics press release, Sept 25 2025. https://www.daktronics.com/news/eye-on-crime-increases-with-daktronics-high-point-networks-collaboration-for-pueblo-police-department-s-real-time-crime-center
[^4]: “City of Pueblo Community Connect Program,” City of Pueblo website, accessed Nov 2025. https://www.pueblo.us/2998/City-of-Pueblo-Community-Connect-Program
[^5]: Patrick Nelson, “License plate reading cameras coming to Pueblo,” KOAA News5, 2024. https://www.koaa.com/news/covering-colorado/license-plate-cameras-coming-to-pueblo
[^6]: “Sheriff Lucero Issues Statement on Agency’s Cooperation with ICE,” Pueblo County Sheriff’s Office news release, Jan 23 2025. https://www.pueblosheriff.com/DocumentCenter/View/3323/Sheriff-Lucero-Statement

[^7]: Pueblo Chieftain, "Why Pueblo city council is against these 3 state bills," Feb 11 2026. https://www.chieftain.com/story/news/2026/02/11/why-pueblo-city-council-is-against-these-3-state-bills/88604786007/ — Resolutions adopted Feb 9 2026 opposing SB26-070, SB26-071, HB26-1037. Preview coverage: https://www.yahoo.com/news/articles/know-pueblo-city-council-meeting-143018079.html

[^8]: "Live results: Here's who's winning the race for Pueblo County sheriff," *Pueblo Chieftain* via Yahoo, Jun 30 2026. https://www.yahoo.com/news/politics/articles/live-results-heres-whos-winning-013239034.html — Medina 11,882 (53.16%) def. Lucero 10,470 (46.84%); 22,352 ballots cast; no Republican filed.

[^9]: "Sheriff candidate Allen Medina outlines vision for Pueblo County during Labor Council forum," *Pueblo Star Journal*, Jun 1 2026. https://pueblostarjournal.org/news/2026/06/01/sheriff-candidate-allen-medina-outlines-vision-for-pueblo-county-during-labor-council-forum/

[^10]: "'We didn't have the votes': Amabile pulls Colorado bill limiting Flock and other license plate readers," *Boulder Reporting Lab*, Apr 30 2026. https://boulderreportinglab.org/2026/04/30/amabile-pulls-colorado-bill-limiting-flock-and-other-license-plate-readers-we-didnt-have-the-votes/

[^11]: "Pueblo Police expand Crime Center technology to improve investigation ability," *KOAA News5*. https://www.koaa.com/news/local-news/in-your-community/pueblo/pueblo-police-expand-crime-center-technology-to-improve-investigation-ability — 12 Flock cameras (4 live), 4 mobile trailers, park cameras at Mitchell/Mineral Palace/City/El Centro; Deputy Chief Jim Martin asserts a documented query log.
