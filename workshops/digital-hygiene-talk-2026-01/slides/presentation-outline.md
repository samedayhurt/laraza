# DIGITAL HYGIENE: LET'S TALK

**A practical security conversation for journalists, activists, and community organizers**

*What you post. What you carry. What they can see.*

---

## Talk Structure

| Section | Time | Focus |
|---------|------|-------|
| **Opening** | 5 min | Frame the conversation |
| **Part 1: Ubiquitous Technical Surveillance** | 30 min | The landscape you're operating in |
| **Part 2: The Threat Surface in Pueblo** | 25 min | What's actually here |
| *Break* | 10 min | — |
| **Part 3: Security Check-Up** | 40 min | What you can do today |
| **Discussion + Q&A** | 10 min | Open floor |

---

# OPENING (5 minutes)

## Slide 1: Title

**DIGITAL HYGIENE: LET'S TALK**

What you post. What you carry. What they can see.

> **Notes:** This is a conversation, not a lecture. Jump in. Ask questions. Disagree with me. The goal is understanding, not fear.

---

## Slide 2: Why This Conversation

We live in an environment of constant technical surveillance — much of it invisible, normalized, and unregulated.

**This session is about:**
- Understanding what the surveillance landscape actually looks like
- Knowing what's specifically happening in Pueblo
- Reducing unnecessary exposure without paranoia or tech overload
- Leaving with things you can do *today*

**This session is not about:**
- Perfect security (doesn't exist)
- Fear (counterproductive)
- Technical expertise (not required)

---

## Slide 3: Who's In The Room

This conversation is designed for:
- Journalists
- Activists
- Mutual aid organizers
- Union organizers
- Community leaders
- Anyone doing public-facing or sensitive work

**You share a common exposure:** Your work puts you in contact with systems that collect, retain, and share information — often without your knowledge or consent.

---

# PART 1: UBIQUITOUS TECHNICAL SURVEILLANCE (30 minutes)

## Slide 4: The Surveillance You Already Know

**What most people think of:**
- NSA programs (post-Snowden awareness)
- Social media tracking
- "Big tech" data collection

**The reality:** The most consequential surveillance for local organizers isn't the NSA. It's the mundane infrastructure you drive past every day.

---

## Slide 5: License Plate Readers (ALPR)

**What they are:** Cameras that photograph every passing vehicle, extract the plate number via OCR, and log it with timestamp and GPS.

**Scale:**
- Vigilant Solutions (now Motorola) alone: **9+ billion plate scans** in their database
- Average: 14+ hits per person per month in urban areas with ALPR coverage
- Retention: Varies — some jurisdictions keep data for years

**What they reveal:**
- Where you go (church, clinic, lawyer's office, protest)
- When you go there
- How often
- Who else was there at the same time

> **Research:** Georgetown Law Center on Privacy & Technology found ALPR data used to track individuals' movements over extended periods, including to abortion clinics and immigration lawyers' offices.

---

## Slide 6: Flock Safety — The New Player

**Flock is different from legacy ALPR:**
- Marketed to HOAs, business districts, small towns
- Cloud-based with 30-day default retention
- Captures more than plates: vehicle make/model/color, bumper stickers, roof racks, damage
- "Vehicle fingerprinting" can track you even if you swap plates

**The network effect:**
- ~5,000 law enforcement agencies use Flock
- 30+ agencies in Colorado alone
- Data sharing between agencies is one click
- Private cameras (HOA, business) feed the same system

> **What this means:** A camera on a private business parking lot can feed the same database that ICE queries.

---

## Slide 7: Commercial Data Brokers

**The industry you didn't know existed:**
- **750+ registered data brokers** in the US (Privacy Rights Clearinghouse count)
- Combined revenue: **$250+ billion/year**

**What they collect:**
- Name, address, phone, email (the basics)
- Location data from apps (often real-time)
- Purchase history
- Social media activity
- Property records, vehicle registrations
- Political affiliation and donation history
- Relatives and associates

**The product:** A complete dossier on you, available to anyone who pays.

---

## Slide 8: Location Data — The Most Valuable Feed

**How your phone becomes a tracking beacon:**

1. You install an app (weather, games, shopping, coupons)
2. App requests location permission ("to improve your experience")
3. App sells location to data aggregator (buried in ToS)
4. Aggregator sells to data broker
5. Data broker sells to... anyone

**Who buys location data:**
- ICE and CBP (confirmed via FOIA, FTC enforcement)
- FBI, Secret Service, IRS (confirmed via contracts)
- Local police departments (Fog Data Science has 1,000+ clients)
- Private investigators
- Stalkers (yes, really — the price is low enough)

> **Research:** FTC enforcement actions in 2024 against Venntel/Gravy Analytics, X-Mode, and Mobilewalla confirmed these companies sold precise location data to federal agencies including ICE without warrants.

---

## Slide 9: How Private Surveillance Feeds Government Systems

```
┌─────────────────────────────────────────────────────────────────┐
│                    THE DATA PIPELINE                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   YOUR PHONE              PRIVATE SECTOR          GOVERNMENT    │
│   ──────────              ──────────────          ──────────    │
│                                                                  │
│   Apps you use ─────────► Data aggregators                      │
│                           (SDK providers)                        │
│                                 │                                │
│                                 ▼                                │
│                           Data brokers ──────────► ICE/CBP      │
│                           (Venntel, etc.)          (no warrant) │
│                                 │                                │
│                                 ▼                                │
│                           Local police ◄───────── Fusion        │
│                           (buys access)            Centers      │
│                                                                  │
│   Business cameras ─────► Flock Safety ──────────► 30+ CO       │
│   HOA cameras                                      agencies     │
│                                                                  │
│   Smart devices ────────► Device vendors                        │
│   (Ring, Nest)            (Amazon, Google)                      │
│                                 │                                │
│                                 ▼                                │
│                           Law enforcement                        │
│                           request portals                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**The warrant workaround:** When the 4th Amendment blocks direct collection, the government buys the data instead. This is legal (for now) and standard practice.

---

## Slide 10: "I Have Nothing to Hide"

**Why this phrase is dangerous:**

**1. It assumes you control what's "wrong":**
- What's legal today may not be tomorrow
- What's acceptable here may not be in another jurisdiction
- Immigration status. Union organizing. Protest attendance. Abortion access.

**2. It ignores relational exposure:**
- Your data reveals your network
- Your location shows who you visit
- Your contacts include people who *do* have something to hide

**3. It misunderstands the function of surveillance:**
- Surveillance isn't about catching criminals
- It's about power — who has information about whom
- The chilling effect is the point: self-censorship before any action

**The question isn't "what do you have to hide?"**
**The question is "who gets to decide what matters?"**

---

## Slide 11: The Five Exhaust Streams (UTS)

**Everything you do generates trackable data.** This isn't about protests. This is about Tuesday.

```
┌─────────────────────────────────────────────────────────────────┐
│                    YOUR DAILY DATA EXHAUST                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. FINANCIAL         Credit cards, loyalty programs, payment   │
│                       apps — paired with location                │
│                                                                  │
│  2. PHYSICAL          Cameras, ALPR, doorbells, drones,         │
│                       retail analytics                           │
│                                                                  │
│  3. MOBILITY          Transit cards, tolls, rideshare,          │
│                       insurance telematics                       │
│                                                                  │
│  4. DEVICE            Phone location, WiFi probes, Bluetooth,   │
│                       app telemetry, advertising ID              │
│                                                                  │
│  5. SOCIAL/COMMERCIAL Data brokers, voter files, subscriptions, │
│                       social media, breached credentials         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**All five streams feed the same databases.**

---

## Slide 12: Financial Exhaust — Your Purchases Track You

**What happens when you swipe:**
- Bank/card data resold to data brokers
- Loyalty cards paired with ALPR in parking lots
- Payment apps (Venmo, CashApp) build social graphs
- Gas pumps increasingly have plate readers

**What they learn:**
- Your routine (same coffee shop every morning)
- Where you worship, seek medical care, meet people
- Who you split payments with (associations)

**Counter-measures:**
| Action | Impact |
|--------|--------|
| Cash for sensitive purchases | No digital trail |
| Prepaid cards (cash-funded) | Breaks identity link |
| Skip loyalty programs | Or use purpose-built alias |
| Separate accounts for organizing | Compartmentalization |

---

## Slide 13: Mobility Data — Your Movement Is Logged

**Every trip generates records:**

| Source | What It Captures |
|--------|------------------|
| **ALPR (Flock, Vigilant)** | Plate + time + GPS (30+ days, often years) |
| **Insurance telematics** | GPS every few seconds + driving behavior |
| **Rideshare** | Pickup/dropoff + payment + device scans |
| **Transit cards** | Tap location + time (months of history) |
| **Toll systems** | Plate + time + location |

**Colorado context:**
- RTD Denver responds quickly to law enforcement data requests
- E-470 toll records subpoenaed in criminal and civil cases
- **Denver ALPR: 1,400+ immigration searches in 2024** (NBC News)

**The hard truth:** You cannot fully avoid ALPR if you drive. The goal is reducing unnecessary exposure.

---

## Slide 14: Discussion Break

**Questions to consider:**
- Have you ever seen an ALPR camera in Pueblo? Where?
- Does your car insurance have a telematics device?
- Do you know which apps on your phone have location permission?

> **Notes:** Open this up. Get people talking. The goal is to surface what people already know and don't know.

---

# PART 2: THE THREAT SURFACE IN PUEBLO (25 minutes)

## Slide 12: What's Actually Here

**Pueblo is not a surveillance backwater.** The infrastructure is real, operational, and expanding.

| System | Status | Details |
|--------|--------|---------|
| **Real-Time Crime Center (RTCC)** | Live since July 2024 | Central nerve center for all feeds |
| **Flock Safety ALPR** | Operational | Downtown, key corridors |
| **ShotSpotter** | Operational | ~6 sq mi in "high-crime areas" |
| **Community Connect** | Active recruitment | Private cameras → police access |
| **Police drones** | Operational | 60-90 second response capability |
| **Body-worn cameras** | Standard | All feeds route to RTCC |

---

## Slide 13: The Real-Time Crime Center (RTCC)

**What it is:** A central hub where all surveillance feeds converge.

**Launched:** July 2024

**What it integrates:**
- ShotSpotter gunshot alerts
- Body-worn camera feeds (live)
- Drone footage
- Fixed surveillance cameras
- License plate readers
- Community Connect private cameras

**The display:** 7' x 12' Daktronics video wall, 1.2mm pixel pitch — technicians can tile multiple live sources simultaneously.

**Documented use case:** During a Community Connect open house, Deputy Chief James Martin stated the RTCC "observed a hand-to-hand drug transaction through the Daktronics screen," allowing staff to identify suspects in real time.

> **Source:** Daktronics press release, September 25, 2025

---

## Slide 14: Flock ALPR in Pueblo

**Deployment:** 2024, purchased by Pueblo Downtown Association in coordination with City and CDOT

**Location:** Major downtown intersections

**Capabilities:**
- Captures every passing plate
- Queries state and national hotlists
- Alerts on: stolen vehicles, Amber Alerts, hit-and-runs, insurance/license flags
- Vehicle fingerprinting: make, model, color, distinguishing features

**Retention:** 30 days (vendor cloud, encrypted)

**Data sharing:** ~30 Colorado agencies on Flock platform can pool queries

**The Columbus Day context:** You mentioned "pods" at Columbus Day — these are likely mobile Flock units or similar deployable ALPR. Temporary surveillance for specific events, but the data still enters the system.

> **Source:** KOAA News5, 2024

---

## Slide 15: ShotSpotter (SoundThinking)

**What it is:** Acoustic sensors that detect gunshots and triangulate location.

**Coverage:** ~6 square miles in designated "high-crime areas"

**Response time:** Alerts RTCC within 60 seconds of detected gunshot

**The problems:**

| Issue | Evidence |
|-------|----------|
| **False positives** | MacArthur Justice Center study: 89% of ShotSpotter alerts in Chicago resulted in no gun crime report |
| **Racial deployment** | Sensors concentrated in Black and brown neighborhoods |
| **Evidentiary concerns** | Company has altered audio evidence at police request (AP investigation) |
| **Cost** | $90,000-$100,000/year per square mile |

> **Research:** AP investigation (2021) documented ShotSpotter analysts modifying evidence. MacArthur Justice Center analysis of Chicago data (2021).

---

## Slide 16: Community Connect

**The pitch:** "Partner with police to keep your neighborhood safe by registering your cameras."

**The reality:** Voluntary surveillance network that normalizes police access to private footage without judicial oversight.

**How it works:**
1. Residents/businesses register cameras with police
2. Police can request footage directly (no warrant)
3. Some participants stream live to RTCC
4. System runs on Genetec platform

**What's missing:**
- No public retention schedules
- No warrant requirements
- No published data governance policy
- No audit logs of who accessed what

**The pressure:** Marketed as civic duty. Creates social pressure to participate. Refusal can be framed as "not caring about safety."

> **Source:** City of Pueblo Community Connect website

---

## Slide 17: What Colorado Sees — State-Level Aggregation

**CIAC (Colorado Information Analysis Center)** — State fusion center in Centennial

**What flows to CIAC:**
- ALPR data from participating agencies (including Pueblo)
- Suspicious Activity Reports (SARs) from local police
- Social media monitoring outputs
- Commercial data purchases

**What CIAC does:**
- Aggregates data from 200+ local/state agencies
- Shares with federal partners (FBI, DHS, ICE)
- Produces intelligence products for law enforcement
- Operates 24/7 watch desk

**Colorado-specific data:**
- **Voter rolls + cell numbers** sold to political consultants, leak elsewhere
- **1,400+ immigration searches** through Denver ALPR in 2024 (NBC News)
- **~30 Colorado agencies** on Flock cross-agency sharing platform

---

## Slide 18: Data Flow — Local to Federal

```
┌─────────────────────────────────────────────────────────────────┐
│                    YOUR DATA'S JOURNEY                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   PUEBLO (LOCAL)                                                │
│   ──────────────                                                │
│   RTCC: cameras, ALPR, ShotSpotter, drones, body cams          │
│   Community Connect: private cameras fed to police              │
│                         │                                        │
│                         ▼                                        │
│   COLORADO (STATE)                                              │
│   ────────────────                                              │
│   CIAC: aggregates from 200+ agencies                          │
│   Cross-agency ALPR sharing (Flock network)                    │
│                         │                                        │
│                         ▼                                        │
│   FEDERAL                                                       │
│   ───────                                                       │
│   FBI JTTFs ◄──► DHS Fusion Network ◄──► ICE/CBP               │
│   (+ commercial purchases: Venntel, Babel Street, Fog Data)    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**What we don't know (CORA request territory):**
- Does RTCC auto-feed to CIAC?
- What retention policies govern each data source?
- Which federal agencies have MOU access?
- Are there audit logs of who queries what?

---

## Slide 18: ICE and Local Partnerships

**Sheriff Lucero's statement (January 23, 2025):**
> "The Pueblo County Sheriff's Office WILL NOT support or participate in any round-up operations."

**The caveat:** Will assist ICE when "criminal charges exist or officer safety demands it."

**What this means:**
- Not a sanctuary policy
- Discretion remains with individual officers
- "Criminal charges" is a broad category
- Traffic stops can become federal encounters

**January 2025 context:** Statewide rumors of ICE "roundups" traced to agents assisting local police with narcotics arrest in Pueblo. Not a roundup, but demonstrates ICE presence and local collaboration.

**CORRN Hotline:** 844-864-8341 (option 1 for live, option 2 to document)

> **Sources:** Sheriff's Office statement, CPR reporting

---

## Slide 19: Why Journalists & Activists Are Disproportionately Affected

**Your work product is public:**
- Bylines, social media presence, event attendance
- Easy to identify and track

**Your sources need protection:**
- Your exposure = their exposure
- Metadata reveals your network even if content is encrypted

**You're already in databases:**
- Attended a protest? Possibly photographed, plate logged
- Published critical coverage? Possibly flagged in fusion center reports
- Organized a union drive? Possibly on a corporate intelligence list

**The chill is the point:**
- You don't need to be arrested to be affected
- Self-censorship, source reluctance, operational friction
- Surveillance succeeds when you change behavior

---

## Slide 20: Practical Daily Counter-Surveillance

**This isn't about protests. This is about Tuesday.**

| Stream | Exposure | Mitigation |
|--------|----------|------------|
| **Financial** | Card payments paired with location | Cash for sensitive purchases; prepaid cards |
| **Physical** | Cameras, ALPR everywhere | Map camera density; vary routes |
| **Mobility** | Telematics, tolls, transit cards | Disable telematics; rotate transit cards; cash for gas |
| **Device** | Phone location always on | Deny permissions; reset ad ID; airplane mode when needed |
| **Social/Commercial** | Data brokers have everything | Opt out regularly; alias emails; redact before posting |

**Handout:** "Daily Life Counter-Surveillance" — detailed guidance for each stream.

**The mindset:** Consistency beats gadgets. Pick a few practices. Build habits. Teach the next person.

---

## Slide 21: Discussion Break

**Questions for the room:**
- Has anyone here filed a CORA request with Pueblo PD?
- Has anyone had a source express concern about surveillance?
- Has anyone noticed the ALPR cameras downtown?

---

# BREAK (10 minutes)

---

# PART 3: SECURITY CHECK-UP (40 minutes)

## Slide 21: The Mindset

**Security is not about being perfect. It's about:**
- Understanding your threat model (who wants your data, what they can access)
- Reducing unnecessary exposure
- Making targeted choices about what to protect
- Building habits, not paranoia

**Today we'll cover:**
1. Social media privacy & metadata leakage
2. Phones: permissions, location, cloud backups
3. Computers: disk encryption, browser hygiene, backups

---

## Slide 22: Social Media — The Metadata Problem

**What you post** is obvious. **What you leak** is not.

**Metadata in photos:**
- EXIF data: GPS coordinates, device info, timestamp
- Even if you don't tag location, the image may contain it

**Engagement patterns:**
- Who you follow/friend reveals your network
- What you like reveals your interests
- When you're active reveals your schedule

**Platform-side collection:**
- IP addresses (even with VPN, if you're logged in)
- Browser fingerprinting
- Cross-site tracking

**The WhatsApp problem:** End-to-end encryption protects content. Meta still sees: who you message, when, how often, group memberships, last seen. ICE subpoenas this metadata.

---

## Slide 23: Social Media — What Actually Matters

**HIGH IMPACT (do these):**

| Action | Why |
|--------|-----|
| **Turn off location on posts** | Prevents geotagging |
| **Review tagged photos** | Others leak your location |
| **Audit friend/follow lists** | Your network is visible |
| **Use Signal for sensitive coordination** | Metadata minimized |
| **Separate accounts for organizing** | Compartmentalization |

**LOW IMPACT (don't obsess):**

- Deleting old posts (already scraped)
- Perfect privacy settings (platform can change them)
- Using a fake name (easily correlated if you have mutual connections)

---

## Slide 24: HANDS-ON — Social Media Audit

**Facebook (3 minutes):**
1. Settings → Privacy → "Who can see your future posts?" → Friends
2. Settings → Privacy → "Limit past posts" → Click Limit
3. Settings → Location → Turn OFF location history
4. Settings → Apps and Websites → Remove what you don't use

**Instagram (2 minutes):**
1. Settings → Privacy → Private Account → ON
2. Settings → Privacy → Activity Status → OFF
3. Settings → Privacy → Tags → Manually Approve

**For organizers:** Consider a separate account. Different email. Don't follow your real account. Don't use your real phone number.

---

## Slide 25: Phones — The Core Problem

**Your phone is designed to share data.** The defaults favor convenience and data collection.

**What your phone knows:**
- Your location (constantly, even with GPS "off" — via cell towers, WiFi, Bluetooth)
- Your contacts (synced to cloud)
- Your messages (if not encrypted)
- Your photos (with location metadata, synced to cloud)
- Your browsing (if using default browser logged into account)
- Your voice (if using voice assistant)
- Your face and fingerprint (if using biometrics)

**What leaks by default:**
- Location to apps (unless you deny)
- Photos to cloud (unless you disable)
- Contacts to cloud (unless you disable)
- Advertising ID (until you reset/delete)

---

## Slide 26: Phones — Permissions Audit

**Location permissions (most important):**
1. Settings → Privacy → Location Services (iPhone) or Settings → Location (Android)
2. Review each app
3. Set to "Never" for apps that don't need it
4. Set to "While Using" for maps/navigation
5. Set to "Never" for: social media, games, shopping, news

**The advertising ID:**
- iPhone: Settings → Privacy → Tracking → "Allow Apps to Request to Track" → OFF
- iPhone: Settings → Privacy → Apple Advertising → Personalized Ads → OFF
- Android: Settings → Privacy → Ads → Delete advertising ID

**Background app refresh:**
- Apps update in background, sending data even when not in use
- iPhone: Settings → General → Background App Refresh → OFF (or selective)
- Android: Settings → Apps → [App] → Battery → Restricted

---

## Slide 27: Phones — Cloud Backup Considerations

**The convenience trap:**
- iCloud/Google backup is convenient
- It's also a subpoena target
- Apple/Google will produce data in response to legal process

**What gets backed up (by default):**
- Messages (iCloud Messages, Google Messages backup)
- Photos (with location data)
- Contacts
- App data
- Device settings

**Options:**

| Choice | Trade-off |
|--------|-----------|
| **Keep cloud backup ON** | Convenient, but accessible via subpoena |
| **Disable cloud backup** | More secure, but you must manually backup |
| **Selective backup** | Disable for sensitive apps, keep for others |
| **Local encrypted backup** | iTunes/Finder backup with encryption, Android local backup |

**For sensitive work:** Consider disabling cloud backup for Messages, Photos. Use Signal (no cloud backup by default).

---

## Slide 28: Phones — Biometrics vs. PIN

**Legal reality:**

```
┌────────────────────────────────────────────────────────────────┐
│                                                                 │
│   BIOMETRICS                         PIN/PASSWORD              │
│   (Face ID, fingerprint)             (6+ digits)               │
│   ──────────────────────             ──────────────            │
│                                                                 │
│   Can be compelled                   Cannot be compelled       │
│   (treated as physical key)          (testimonial act)         │
│                                                                 │
│   Courts have ruled:                 5th Amendment protects    │
│   police can force you to            the contents of your      │
│   look at phone / press finger       mind                      │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

**Recommendation:**
- Daily use: Biometrics are fine for convenience
- Before sensitive situations: Disable biometrics, use PIN only
- iPhone: Settings → Face ID → iPhone Unlock → OFF
- Android: Settings → Security → Fingerprint/Face → Disable for unlock

**Emergency lockdown:**
- iPhone: Press side button 5 times → Emergency SOS screen → requires PIN to unlock
- Android: Power button → Lockdown (some models)

---

## Slide 29: Phones — Signal Setup

**Why Signal over WhatsApp/Telegram:**

| | Signal | WhatsApp | Telegram |
|--|--------|----------|----------|
| End-to-end encryption | Yes (always) | Yes | Only in "secret chats" |
| Metadata collection | Minimal | Extensive | Extensive |
| Open source | Yes | No | Partial |
| Owner | Non-profit | Meta | For-profit (UAE ties) |
| Government requests | Almost nothing to give | Metadata available | Has complied with requests |

**Signal settings to configure:**
1. Settings → Privacy → Screen Security → ON
2. Settings → Privacy → Registration Lock → ON
3. Settings → Privacy → Disappearing Messages → Set default (1 week recommended)
4. Settings → Privacy → Typing Indicators → OFF (optional)
5. Settings → Privacy → Read Receipts → OFF (optional)

---

## Slide 30: Computers — Disk Encryption

**Why it matters:**
- If your laptop is seized (or stolen), the drive can be read
- Disk encryption makes the data unreadable without your password
- This is the single most important computer security measure

**Status check:**

**macOS (FileVault):**
- System Preferences → Security & Privacy → FileVault
- Should say "FileVault is turned on"
- If not: Turn On FileVault (will take time, don't interrupt)

**Windows (BitLocker):**
- Settings → Update & Security → Device encryption
- Or: Control Panel → BitLocker Drive Encryption
- Note: BitLocker requires Windows Pro; Home edition has "Device Encryption" (less robust)

**Linux:**
- Usually set up at install time (LUKS)
- If not encrypted at install, more complex to add later

**The password matters:** Disk encryption is only as strong as your password. Use a strong passphrase.

---

## Slide 31: Computers — Browser Hygiene

**The problem:** Your browser is the primary vector for tracking.

**Quick wins:**

| Action | Impact |
|--------|--------|
| **Use Firefox or Brave** | Better privacy defaults than Chrome |
| **Block third-party cookies** | Prevents cross-site tracking |
| **Use uBlock Origin** | Blocks ads and trackers |
| **Use DuckDuckGo for search** | Doesn't profile you |
| **Clear cookies regularly** | Breaks tracking continuity |

**Firefox setup:**
1. Settings → Privacy & Security → Enhanced Tracking Protection → Strict
2. Install uBlock Origin extension
3. Settings → Privacy & Security → Cookies → Delete when Firefox closes (optional)

**For sensitive research:** Use Tor Browser. Slower, but routes traffic through multiple nodes.

---

## Slide 32: Computers — Browser Compartmentalization

**The concept:** Different browsers/profiles for different purposes.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                  │
│   DAILY BROWSING              LOGGED-IN ACCOUNTS                │
│   (Firefox + uBlock)          (Separate Firefox profile)        │
│   ──────────────────          ──────────────────────            │
│   • General research          • Email                           │
│   • News reading              • Social media                    │
│   • Not logged in             • Banking                         │
│                                                                  │
│                                                                  │
│   SENSITIVE RESEARCH          MAXIMUM PRIVACY                   │
│   (Brave private window)      (Tor Browser)                     │
│   ──────────────────────      ──────────────────                │
│   • Source research           • Whistleblower contact           │
│   • Investigating subjects    • Highly sensitive research       │
│   • Court records             • When you need anonymity         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Slide 33: Computers — Backups

**The 3-2-1 rule:**
- **3** copies of important data
- **2** different storage types
- **1** copy offsite

**Practical implementation:**

| Copy | Location | Purpose |
|------|----------|---------|
| **1** | Your computer | Working copy |
| **2** | External drive (encrypted) | Local backup |
| **3** | Cloud (encrypted) or second location | Disaster recovery |

**For journalists/activists:**
- Encrypt external drive (VeraCrypt, built-in disk utility)
- Consider what you put in cloud (subpoena target)
- Proton Drive, Tresorit for encrypted cloud (end-to-end, no provider access)

**Frequency:** Automate if possible. At minimum: weekly for working files.

---

## Slide 34: What Actually Matters — Priority List

**If you do nothing else:**

```
TIER 1: DO TODAY
================
□ Phone: Audit location permissions (set to Never/While Using)
□ Phone: Delete advertising ID
□ Computer: Verify disk encryption is ON
□ Install Signal, configure disappearing messages
□ Save CORRN number: 844-864-8341

TIER 2: DO THIS WEEK
====================
□ Social media: Turn off location, set to private
□ Browser: Switch to Firefox + uBlock Origin
□ Phone: Review cloud backup settings
□ Computer: Set up encrypted local backup
□ Search yourself on data broker sites (Spokeo, WhitePages)

TIER 3: ONGOING
===============
□ Monthly: Reset advertising ID
□ Quarterly: Re-run data broker opt-outs
□ Before sensitive situations: Disable biometrics
□ Regular: Delete apps you don't use
```

---

## Slide 35: Resources

**For continued learning:**
- **EFF Surveillance Self-Defense:** ssd.eff.org
- **Security in a Box:** securityinabox.org
- **Access Now Helpline:** accessnow.org/help (24/7 for urgent issues)

**For this project:**
- **Full documentation:** github.com/samedayhurt/laraza
- **Pueblo surveillance map:** docs/maps/pueblo-surveillance-map.html
- **Data broker opt-out guide:** primers/Data Broker Opt-Out Guide.md

**For emergencies:**
- **CORRN:** 844-864-8341 (ICE activity, detention)
- **RMIAN Detention Hotline:** (303) 866-9308

---

## Slide 36: Discussion

**Open floor:**
- What wasn't covered that you want to discuss?
- What's unclear?
- What's your biggest concern after today?

**For 1-on-1 help:** Stay after — we can walk through device settings together.

---

# APPENDIX: Research Citations

## License Plate Readers / ALPR
1. **Georgetown Law Center on Privacy & Technology** — "You Are Being Tracked: How License Plate Readers Are Being Used to Record Americans' Movements" (2013, updated)
2. **ACLU** — "You Are Being Tracked" report series
3. **EFF** — "Street-Level Surveillance: License Plate Readers"

## Data Brokers
4. **Privacy Rights Clearinghouse** — Data Broker Database (750+ registered)
   - privacyrights.org/data-brokers
5. **FTC Enforcement Actions (2024)** — Orders against Venntel/Gravy Analytics, X-Mode, InMarket, Mobilewalla
   - ftc.gov/enforcement
6. **Brennan Center for Justice** — "Data Brokers and the Government"

## ShotSpotter
7. **AP Investigation (2021)** — "ShotSpotter evidence altered in Chicago cases"
8. **MacArthur Justice Center (2021)** — Chicago ShotSpotter data analysis: 89% false positive rate

## Pueblo-Specific
9. **Daktronics Press Release (Sept 25, 2025)** — RTCC launch, system integration details
10. **KOAA News5 (2024)** — Flock ALPR deployment in Pueblo
11. **City of Pueblo** — Community Connect program documentation
12. **Pueblo County Sheriff (Jan 23, 2025)** — Statement on ICE cooperation
13. **CPR (Jan 24, 2025)** — Reporting on ICE activity rumors

## Legal / 5th Amendment
14. **State v. Diamond (MN 2017)** — Biometrics can be compelled
15. **Commonwealth v. Baust (VA 2014)** — Fingerprint compelled, passcode protected
16. **In re Search Warrant Application (N.D. Ill. 2017)** — Touch ID compulsion

## School Surveillance
17. **RAND Corporation (2023)** — "scant evidence" of AI surveillance effectiveness
18. **EFF (2024)** — "School Monitoring Software Sacrifices Student Privacy"

---

*Last updated: January 2026*
*La Raza VII.I.IX — Community Field Guide for Pueblo, CO*
