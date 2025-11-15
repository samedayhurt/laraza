# Surveillance and Policing Risks

Pueblo’s Real-Time Crime Center (RTCC) centralizes high-risk surveillance technologies under a conservative municipal majority, while community complaints still bottleneck inside Internal Affairs. This brief summarizes the stack, highlights civil-liberties threats, and outlines immediate self-advocacy moves.

## Executive Summary
- **RTCC hub:** Daktronics and High Point Networks wired a 7’×12’ dvLED wall to ingest ShotSpotter, bodycams, drones, fixed cameras, and ALPR streams, giving PPD a fused view of protests and daily life.[^daktronics]
- **Community Connect pressure:** Residents and businesses are being nudged to register or live-feed their cameras via Genetec, without published retention limits or warrant requirements.[^cc]
- **Flock ALPR corridor:** Downtown Association-funded cameras scan every plate along Union Ave/Riverwalk, storing footage in Flock’s cloud for 30 days with hotlist matching.[^flock]
- **Complaint escalation gaps:** IA accepts submissions, but systemic issues require leaps to the DA, Colorado POST, and the Attorney General’s Pattern & Practice office—flows that most residents aren’t using yet.[^ia][^post]

## Technology Stack & Civil-Liberties Impact
### Real-Time Crime Center
- **Capabilities:** Multi-sensor fusion (ShotSpotter, bodycams, drones, CCTV, ALPR) displayed on dvLED wall with vendor-managed infrastructure.[^daktronics]
- **Risks:** False positives from acoustic sensors, opaque retention policies, and reliance on private vendors to process discovery requests.
- **Advocacy steps:** File CORA requests for RTCC vendor contracts and uptime logs; demand public retention schedules and audit summaries before new sensors go online.

### Community Connect (Genetec)
- **Program:** Voluntary camera registry/live-share encouraging residents to stream feeds directly to RTCC integrators (Arden, High Point, Linx).[^cc]
- **Risks:** De facto warrantless surveillance over private property; potential inequities as wealthier neighborhoods supply more feeds.
- **Advocacy steps:** Push for ordinance requiring judicial authorization or homeowner consent per request; publish a dashboard of registered zones so communities can opt out or scrutinize coverage.

### Flock Safety ALPR Corridors
- **Deployment:** Initial cameras purchased by the Downtown Association to cover Union Ave/Riverwalk intersections; Flock stores encrypted footage for 30 days and logs every query.[^flock]
- **Risks:** Expansion into residential 81008 without debate; shared databases across Colorado agencies increase dragnet scope.
- **Advocacy steps:** Request placement maps and usage audits quarterly; document opposition from civil-liberties advocates (e.g., Libertarian officials) to build cross-partisan pressure.

### Vendor data control
- **Vendors involved:** ShotSpotter/SoundThinking manage acoustic alerts, Genetec hosts Community Connect footage, and Flock Safety stores ALPR hits for 30 days in its cloud.
- **Risks:** Evidence lives on third-party servers with their own retention and subpoena policies, delaying disclosures and creating privatized gatekeepers.
- **Advocacy steps:** Demand MOUs that spell out retention, deletion, audit log access, and notification timelines; require the city to publish aggregate vendor queries and uptime reports quarterly.

## Complaint & Accountability Workflow
1. **Internal Affairs intake:** File in person/online/phone with badge numbers, timestamps, and hashed media; IA is obligated to investigate use-of-force and civil-rights complaints.[^ia]
2. **Escalate to prosecutors:** If IA stalls or misconduct appears criminal, send the same packet to the 10th Judicial District Attorney per Colorado POST guidance.[^post]
3. **Certification pressure:** File POST certification complaints for officers involved in violence; POST can revoke credentials after criminal adjudication.
4. **Pattern & Practice:** Submit systemic issues (retaliatory arrests, surveillance abuse) to the Colorado Attorney General’s Pattern & Practice intake (select “Governmental Authority”).
5. **Community tracking:** Log every complaint in the encrypted Obsidian vault with case IDs and hash lists so legal observers can testify to integrity.

## Action Checklist
- Map RTCC/ALPR coverage to protest routes using `data/pueblo_apparatus.geojson`; share static PNGs in Signal chats before events.
- Prepare two public-comment questions for each surveillance vote (privacy guardrails, audits, conflict disclosures).
- Maintain a “complaint go-bag” with blank IA forms, POST instructions, and instructions for hashing media on-site.
- Pair every complaint submission with a CORA request for IA logs to create external accountability.

## Source Notes
- [^daktronics]: “Eye On Crime Increases with Daktronics, High Point Networks Collaboration for Pueblo Police Department’s Real-Time Crime Center,” Daktronics press release, Sept 25 2025. https://www.daktronics.com/news/eye-on-crime-increases-with-daktronics-high-point-networks-collaboration-for-pueblo-police-department-s-real-time-crime-center
- [^cc]: City of Pueblo Community Connect Program, https://www.pueblo.us/2998/City-of-Pueblo-Community-Connect-Program (accessed 2025-01, logged 2025-11-15).
- [^flock]: Patrick Nelson, “License plate reading cameras coming to Pueblo,” KOAA News5, 2024. https://www.koaa.com/news/covering-colorado/license-plate-cameras-coming-to-pueblo
- [^ia]: “Internal Affairs Section,” Pueblo Police Department, https://www.pueblo.us/449/Internal-Affairs-Section (accessed 2025-11-15).
- [^post]: “Certification Inquiries & Officer Complaints,” Colorado POST, https://post.colorado.gov/certification-inquiries-officer-complaints (accessed 2025-11-15).
