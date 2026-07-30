# Surveillance and Policing Risks

*Updated: **July 29, 2026***

Pueblo's Real-Time Crime Center (RTCC) continued expanding through 2026, widening acoustic coverage and adding mobile camera trailers while drone-first-responder flights remain active. This brief summarizes the current stack, highlights civil-liberties threats, and outlines immediate self-advocacy moves.

---

## ⚠️ July 2026 Update — What Changed, and Why It Changes Your Approach

### 1. The 2026 reform push failed entirely — but pre-2026 law still binds

All three 2026 Colorado bills that would have regulated this stack **died** (sine die May 13, 2026):

| Bill | Would have required | Outcome |
| --- | --- | --- |
| **SB26-070** ("PEEPS Act") | Warrant for location data >72 hrs old; ~30-day retention cap; query logging; **public annual report of device count and locations** | **LOST** — sponsors pulled it at Second Reading Apr 29 under a veto threat. Sen. Amabile: *"We didn't have the votes."* |
| **SB26-071** ("SAFE Act") | Warrant for facial recognition; mandatory data destruction; no data sales; **biennial AG audits** across ShotSpotter, drones, park cameras, BWC, Flock, and Community Connect | **LOST** — postponed indefinitely 6–1 in Senate Judiciary, May 6 |
| **HB26-1037** | Bar on obtaining broker data "for anything of value"; **private cause of action**; evidence exclusion | **LOST by one vote, twice, in one day** (House Judiciary, Apr 22) — the closest of the three, and the **highest-leverage 2027 target** |

Pueblo City Council formally **opposed all three** on Feb 9, 2026.

**What this means precisely:** there is now **no** state ALPR statute, **no** retention cap, **no** query-logging duty, **no** mandated audit, and **no** public device-inventory requirement covering ALPR, ShotSpotter, drones, or Community Connect. Those have to be won **locally** — council, mayor, sheriff — or extracted via CORA. **But facial recognition is the exception:** SB22-113 (2022) still imposes notice, accountability-report, human-review, and warrant duties (see §2). Don't tell people Colorado has no surveillance law at all — that's both wrong and forfeits your best existing hook. Sponsors have signalled a 2027 rewrite ("probably with a new governor" — Rep. Nguyen), which makes the **Nov 2026 governor's race** the upstream variable.

### 2. The single best lever available: the July 27, 2026 DCJ grant (item N3)

Verified directly in the agenda packet. A **$275,384 Colorado Division of Criminal Justice grant** (CY2026, project **PS2509**, grant **#2024-SC-25-866**), ratifying the Mayor's execution:

- **The grant's research component names the RTCC.** Packet text: *"The subject matter of research will be a comprehensive study of the **Real Time Crime Center**."* Assigned to PPD's **Crime Analyst and Threat Liaison Officer** with a research partner from the **Thomas V. Healy Center at CSU-Pueblo**. *(The same paragraph also references studying the CIT co-responder program, so the scope is genuinely ambiguous in the source — confirm before characterizing it publicly.)*
  → **Ask: who owns the study output, and will it be published?** A city-funded RTCC study is the most realistic path to an independent coverage map and audit entering the public record.
- **PPD was added as one of five new DOJ National Public Safety Partnership (PSP) sites** — a federal technical-assistance relationship, administered by BJA, that appears nowhere else in this repo. It puts DOJ consultants inside PPD operations. **Establish what data flows through it.**
- **Two enforceable grant conditions:**
  - **#26 bars grant funds from unmanned aircraft systems (UAS/drones)** or accessories entirely.
  - **#27 permits Facial Recognition Technology only if the City already has policies and procedures protecting Fourth and First Amendment rights, privacy, and civil liberties.**
  → 🔴 **CORA target: does the City of Pueblo have an FRT policy?** If not, it cannot lawfully spend this grant on FRT. If the City claims one, that document must be producible.
  → ⚠️ **This grant condition is not the only FRT constraint — and not the strongest.** **[SB22-113](https://leg.colorado.gov/bills/sb22-113)** (signed June 2022, effective Aug 2022, **still in force**) independently requires any agency, before developing/procuring/using facial recognition, to **file a public notice of intent with its reporting authority**, **produce an accountability report**, subject decisions to **meaningful human review**, **test in operational conditions**, and train operators — and it **bars warrantless real-time surveillance identification** and reliance on FRS alone for probable cause. **No Pueblo SB22-113 filing has been found.** A notice of intent is a public record, which makes it the cheapest early-warning tripwire on this entire stack. *(The oversight task force it created sunsets Sept 1, 2027 — the underlying duties do not.)* **SB25-143** additionally requires **local school board approval** for facial recognition in schools, making D60/D70 board agendas a free monitor.
- Same agenda: **item R8** (updated CIT Master Services Agreement with Health Solutions) and **item N6** (PCSO–PPD MOU on alternate/default **E911 call routing**).

### 3. 🔴 A SECOND ALPR SYSTEM: 70 Genetec Cloudrunner cameras, queried against federal NCIC

**This is the largest single change to Pueblo's surveillance footprint since the RTCC opened, and this repo did not know about it.**

- **Pueblo PD is running ~70 Genetec Cloudrunner ALPR cameras citywide** — an **order of magnitude** beyond the 22 fixed ALPRs previously documented here, and a **second, parallel ALPR vendor** alongside Flock.
- **Reads are queried against federal NCIC.** Combined with the EFF finding below, that is the mechanism of concern, not a hypothetical.
- **Retention, cost, camera placement, and use policy are all undisclosed.** → **CORA targets: the Cloudrunner contract, the placement map, the retention schedule, and the query audit log.**

> ### The ICE pathway is a toggle, not a leak
> EFF (June 25, 2026) documented that an **ICE-populated NCIC "Immigration Violator" hotlist can be switched on inside Flock**, generating real-time alerts against **ICE administrative warrants issued without judicial review**. **Pueblo has the mechanism on *both* Flock and Cloudrunner.** No Colorado agency appears to have been asked whether it is enabled. **Ask Pueblo PD, in writing, whether that hotlist is enabled on either system.** This is the single highest-priority records request in this brief.
>
> And note: **disabling the national lookup is not sufficient.** ATF searched Loveland's Flock data on ICE's behalf; SFPD's own audit found federal partners ran **299 improper searches** through a fusion center. The risk runs through *local* agencies querying for federal partners, which no vendor toggle prevents.

**The Flock side, and why it's bypassing council:**

- **Pueblo PD is expanding to 12 Flock cameras** (4 live), **4 mobile trailers**, and park cameras at **Mitchell, Mineral Palace, City, and El Centro** — with **no council authorization vote located anywhere in Feb–Jul 2026**, while the city lobbied against state ALPR regulation. No disclosed cost, funding source, or retention policy.
- ⚠️ **Scope-change flag:** **El Central Park** appears in the current camera list but was **not** in the December 2024 resolution that authorized $1M for cameras in five parks — and **Ray Aguilera Park and Lake Minnequa dropped off**. Verify before mapping or publishing; the authorized list and the deployed list do not match.
- **Notable negative:** a keyword scan of **29 city and 20 county agendas/packets (Jan–Jul 2026)** returned **zero** genuine hits for Flock, ALPR, license plate readers, ShotSpotter, SoundThinking, Genetec, or Fusus. No new ALPR or gunshot-detection procurement went through either body in 2026.
  → Together these mean the expansion is running on **grants, the Downtown Association, vendor trials, or mayoral authority**. Watch those channels — including the new **15% uncommitted-balance authority** on the half-cent sales tax, and the **Nov 2026 ballot question earmarked for "fire and city technology."**
- **Deputy Chief Jim Martin has publicly asserted that a query audit log exists.** That public statement makes it **CORA-able**. Request it.
- **Denver is the template to demand:** its Flock contract carries a **$100k penalty** for sharing with federal immigration enforcement, **bars federal task-force officers**, and **disables Denver data in Flock's nationwide lookup**. In Feb 2026 Denver's *auditor refused to sign* the contract after the mayor bypassed council. **Pueblo has no known equivalent to any of this.**

### 4. Laws that DID pass — new obtainable documents, and one setback

- **HB26-1123** (eff. **May 27, 2026**) — requires **body-worn-camera recording of jail strip searches**, restricted-access tagging, and an **annual report to the AG** and jail standards advisory committee. This applies to **PCSO's new 672-bed facility** (opened May 2026, fully occupied July 11). A brand-new document stream that did not exist before.
- **HB26-1276** (signed **June 4, 2026**) — increases penalties for local authorities sharing personal information with federal immigration agencies; **POST must set immigration-detainer training standards and officers must complete training by Dec 31, 2027**; the **AG must publish a personal-identifying-information protection policy**. Also expands CDPHE authority to inspect detention facilities.
  → 🔴 **The contested ground: the statute never mentions ALPR.** Ask each agency in writing: *"Do you treat ALPR reads and RTCC video as personal identifying information under HB26-1276?"* Their written answer is the whole ballgame.
- **SB26-152** (signed June 2, effective **Aug 12, 2026**) — automated-enforcement vendor compensation **must be flat fee or hourly, with no per-citation incentives.** → CORA target: the compensation schedule in any Pueblo automated-enforcement contract.
- ⚠️ **SETBACK — HB26-1312** (signed June 3, effective **Aug 12, 2026**) **reduces civilian seats on the POST Board** and increases line-officer representation. POST is the escalation venue this repo's complaint workflow points people toward, so that pathway is now weaker. Factor it into any advice about where to file.

### 5. ShotSpotter now auto-launches a drone — with no warrant in the loop

- **A ShotSpotter alert auto-triggers a BRINC drone launch**, gated only by an operator feasibility check. **No warrant, no independent review.** An acoustic sensor firing on an unverified signal now puts an aircraft over a neighborhood on its own.
- **83% of Pueblo's 3,383 ShotSpotter alerts had no corresponding 911 call** (608 calls against 3,383 alerts). So the overwhelming majority of drone-eligible triggers are events **no resident reported.**
- **Disclosure gap to use:** PPD's public UAV page still describes a **2018 three-drone unit** — it does not disclose the DFR program or the auto-launch integration at all. Put the vendor's own description side by side with the city's public page and ask council which one is accurate.
- Grant condition #26 on the July 27 DCJ award **bars that grant from funding drones**, so the drone program is funded elsewhere. → **Find out where.**

### 6. PCSO reported ZERO months of state-mandated use-of-force data

- Colorado's CY2024 Contacts & Use of Force report shows **PCSO reported 0 of 12 months** of legally required data. **PPD reported 10 of 12** (244.2 uses per 10k contacts, 3 deaths). **Neither agency reported race data.**
- This is a clean, documented, non-partisan compliance failure — the easiest accountability ask in this entire brief, and it needs no CORA request to establish.
- **Timing:** Sheriff Lucero, under whom the non-reporting happened, **lost the June 30 primary. Allen Medina runs unopposed, campaigned on transparency, and has taken no position on surveillance technology.** A commitment to full use-of-force reporting — and to a published ALPR/RTCC use policy — is a reasonable transition ask now, and much harder to obtain after January.
- Separately, the **10th Circuit cleared PCSO defendants' appeal**, sending a fatal-shooting lawsuit to jury trial.

### 7. Five Colorado cities cancelled Flock. Pueblo did nothing.

| Jurisdiction | What they did | Why it's usable here |
| --- | --- | --- |
| **Cañon City** (40 mi away) | Let the contract **expire**; chief cited "professional blind spots… concerning data security" | **Most transferable precedent** — a neighboring small city, and the *police chief* made the argument |
| **Fort Collins** | Council voted **6–1** to end the contract, remove cameras, stop collection; added a surveillance-tech moratorium | Strongest council-vote model |
| **Denver** | Mayoral non-renewal; **110 cameras removed** | Shows it doesn't require a council vote |
| **Douglas County** | Replaced Flock with a $22.8M Axon system over **data ownership** | Borrow the safeguards, not the swap |
| **Durango / Glenwood Springs / Thornton** | Removed **all 287(g) agencies** from sharing; monthly public reporting; revoked 2,100+ outside agencies | Ready-made sharing-restriction language |

Against that: **Colorado Springs is nearly tripling its readers** by police-chief administrative decision with no council vote — the same pattern visible in Pueblo.

**Vendor-risk facts worth citing in a council ask:** Flock **exposed live camera feeds to the open internet with no authentication** (Jan 2026), **leaked officers' plate-search reasons into DuckDuckGo and Bing**, faces a class action alleging **1.6M+ federal accesses** of SFPD data, and LAPD acknowledged **161 false stolen-vehicle hits** that led to stops of innocent people. Framing this as a **security and liability** problem reaches audiences the civil-liberties framing does not.

*One win worth naming:* after advocacy pressure, **Flock ended its rollout of audio detection of human voices** (EFF, July 2026). Gunshot detection remains, and still flags "community disruption."

### 8. Accountability context that changed

- **Sheriff Lucero lost the June 30, 2026 primary** to **Allen Medina**, who takes office **January 2027** unopposed. Medina centers transparency and has committed to not raiding non-criminal residents — but **he has said nothing on the record about surveillance technology.** Get him on record before January, while he still wants your support.
- **The county's new 672-bed jail** carries ~150 surplus beds plus sheriff-stated expansion room on 33 acres, arriving the same year ICE sought more Colorado capacity. **No federal bed contract is confirmed or denied** — logged as a risk to monitor, not a finding.
- **Automated speed enforcement arrived** in Pueblo via CDOT: $75 fines in the I-25/US 50B work zone from **July 30, 2026**. The separate 15-camera *city* proposal from July 2025 remains unresolved.
- **Budget austerity on both city and county** (city: 7 positions cut, 25 frozen, 15% operating reduction, $10M 2027 deficit; county: ~$10.2M deficit, 10 unpaid furlough days) — **expect slower CORA responses and plan deadlines accordingly.**

---

## Executive Summary
- **RTCC expansion:** $2M state grant (Jan 2025) funded video wall upgrades, drone program, and ShotSpotter now reported at 6 sq mi with city citing further build-out toward ~7 sq mi; mobile trailer fleet growing (likely 6 units).[^state]
- **Drone as First Responder:** July 2025 launch enables 60-90 second drone response to crime scenes, integrated with RTCC.[^drones]
- **73 mobile ALPRs:** Sheriff's Office equipped every patrol car with license plate readers (March 2025).[^alpr]
- **Community Connect Phase 2:** Live video feed integration from private cameras launched Spring 2025.[^cc]
- **Park surveillance:** $1.2M+ invested in cameras, ALPRs, and fiber at 5 parks.[^parks]
- **Flock ALPR concerns:** EFF report (Nov 2025) documents police using Flock network to surveil protesters nationwide.[^eff]

## Technology Stack & 2025 Expansions

### Real-Time Crime Center
- **Components:** ShotSpotter (6 sq mi reported; city indicates further expansion), body cams, drones, 22+ fixed cameras, 22 fixed ALPRs, four to six mobile trailers, Daktronics 7'×12' dvLED wall
- **Operations:** 10am-midnight daily; hiring for 24/7 coverage
- **Cost:** $2.2M initial (ARPA) + $410K/year recurring + $2M 2025 expansion
- **Performance claims:** 97% ShotSpotter accuracy, 40% violent crime reduction, 676 shooting incidents detected[^stats]
- **Risks:** No civilian oversight, opaque retention policies, private vendors control evidence
- **Advocacy:** File CORA requests for all vendor contracts; demand public retention schedules; request updated 2026 coverage maps and trailer deployment logs

### Drone as First Responder Program (NEW July 2025)
- **Capabilities:** 60-90 second response to crime scenes; footage integrated into RTCC
- **Operators:** Pueblo PD; Sheriff also operates S.O.A.R.R. UAV program
- **Risks:** Aerial surveillance of protests and gatherings without published policies
- **Advocacy:** Request drone deployment logs and footage retention policies via CORA

### Sheriff Mobile ALPR Fleet (NEW March 2025)
- **Deployment:** 73 systems in patrol cars; 3-lane view; 1-mile detection range
- **Operators:** Pueblo County Sheriff's Office
- **Risks:** County-wide dragnet of vehicle movements without warrant requirements
- **Advocacy:** Request placement data and query logs quarterly

### Community Connect (Genetec)
- **Phase 1 (Dec 2024):** Camera registry—residents register locations, provide footage on request
- **Phase 2 (Spring 2025):** Live video feeds streamed directly to RTCC
- **Participation options:** Registry only, Genetec Cloud SaaS, or on-premise integration
- **Risks:** De facto warrantless surveillance; wealthy neighborhoods over-represented
- **Advocacy:** Push for ordinance requiring judicial authorization; publish participation dashboard

### Flock Safety ALPR Corridors
- **Deployment:** 2 Downtown Association cameras (Union Ave/Riverwalk); part of 1,091-camera Colorado network
- **Retention:** 30 days cloud storage; motion-activated
- **NEW concern:** EFF November 2025 report documents police using Flock to surveil protesters and activists beyond criminal investigations[^eff]
- **Advocacy:** Request placement maps; document any protest-related queries

### Park Surveillance Infrastructure (NEW 2025)
- **Locations:** City Park, Mineral Palace Park, Ray Aguilera Park, Lake Minnequa, Mitchell Park
- **Components:** Cameras, license plate readers, Wi-Fi, fiber-optic connections to RTCC
- **Cost:** $1M (Dec 2024) + $228K fiber (July 2025)
- **Risks:** Surveillance of family gatherings, protests, community events in public spaces

### ShotSpotter / SoundThinking
- **Coverage:** Expanded from 3 to 6 square miles (2025 grant); city communications in early 2026 indicate continued expansion—request updated coverage map to verify
- **Performance:** 97% accuracy claimed; 73% of alerts NOT called in by citizens; 9 lives saved via rapid response
- **Cost:** $210,000/year
- **Risks:** False positives; acoustic data lives on vendor servers

## Civil Liberties Concerns (2025)

### No Civilian Oversight
- No independent review board monitors RTCC operations
- Limited public documentation of data retention and interagency sharing
- Private vendors (SoundThinking, Genetec, Flock, Daktronics) control primary evidence

### Flock ALPR Protest Surveillance
- EFF November 2025 report revealed police departments nationwide use Flock to track protesters
- No evidence of Pueblo-specific abuse, but same network infrastructure enables it
- Audit logs exist but policies on sharing unclear

### Community Connect Warrant Gaps
- Voluntary program lacks published warrant requirements for police access
- No published retention limits for private camera feeds shared with RTCC

## Complaint & Accountability Workflow
1. **Internal Affairs intake:** File in person/online/phone with badge numbers, timestamps, hashed media at pueblo.us/449/Internal-Affairs-Section
2. **Escalate to prosecutors:** Send packet to 10th Judicial District Attorney if IA stalls
3. **POST certification:** File complaints for officers involved in violence at post.colorado.gov
4. **Pattern & Practice:** Submit systemic issues to Colorado AG (select "Governmental Authority")
5. **Community tracking:** Log every complaint in encrypted vault with case IDs and hash lists

## Action Checklist
- [ ] Map RTCC/ALPR/drone coverage to protest routes using `data/pueblo_apparatus.geojson`
- [ ] Monitor City Council for speed camera proposal (15 cameras proposed July 2025)
- [ ] File CORA requests for drone deployment logs and ShotSpotter expansion zones
- [ ] Track when ARPA funds expire—$410K+/year ongoing costs shift to city budget
- [ ] Document any Flock ALPR queries related to protests for EFF/ACLU reporting
- [ ] Prepare public comment questions for surveillance votes (privacy guardrails, audits, conflicts)

## Source Notes
- [^state]: KOAA News5, "Pueblo's RTCC receiving $1 million from the state for upgrades," Jan 2025
- [^drones]: KKTV, "Pueblo Police Department introducing new technology: drones to Real Time Crime Center," July 12, 2025
- [^alpr]: KKTV, "Local deputies install automated license plate system in patrol cars," March 6, 2025
- [^cc]: City of Pueblo Community Connect Program, pueblo.us/2998 (accessed 2025-11)
- [^parks]: KRDO, "Pueblo City Council considers reallocation of ARPA funds for park surveillance," July 14, 2025
- [^eff]: EFF Deeplinks, "How Cops Are Using Flock Safety's ALPR Network to Surveil Protesters and Activists," Nov 2025
- [^stats]: SoundThinking press release, "Pueblo Chief of Police cites ShotSpotter success rates," 2025
