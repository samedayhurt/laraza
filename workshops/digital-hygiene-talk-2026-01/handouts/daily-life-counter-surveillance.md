# Daily Life Counter-Surveillance

**Protecting yourself from ubiquitous technical surveillance in Pueblo and Colorado**

This isn't about protests. This is about Tuesday.

---

## The Five Exhaust Streams

Everything you do generates trackable data. Understanding these streams is the first step to controlling them.

```
┌─────────────────────────────────────────────────────────────────┐
│                    YOUR DAILY DATA EXHAUST                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. FINANCIAL         Where + when + what you buy               │
│  2. PHYSICAL          Cameras, sensors, license plate readers   │
│  3. MOBILITY          Transit, tolls, rideshare, telematics     │
│  4. DEVICE            Phone location, WiFi, Bluetooth, apps     │
│  5. SOCIAL/COMMERCIAL Data brokers, voter files, subscriptions  │
│                                                                  │
│  All five streams feed into:                                     │
│  • Pueblo RTCC (Real-Time Crime Center)                          │
│  • CIAC (Colorado Information Analysis Center)                   │
│  • Federal databases (via purchases and fusion centers)          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1. Financial Exhaust

**What tracks you:**
- Credit/debit cards → Bank sells to data brokers
- Loyalty cards → Paired with ALPR in parking lots
- Payment apps (Venmo, CashApp) → Build social graphs from contacts
- Gas pumps → Often paired with license plate cameras

**What they learn:**
- Where you shop, eat, get gas
- When you're at specific locations
- Your routine (same Starbucks every morning)
- Your associations (split payments with whom)

**Counter-measures:**
| Action | Impact |
|--------|--------|
| **Cash for sensitive purchases** | No digital trail |
| **Prepaid cards** (cash-funded) | Breaks link to identity |
| **Avoid loyalty programs** | Or use purpose-built alias |
| **Separate accounts** for organizing work | Compartmentalization |

---

## 2. Physical Sensors in Pueblo

### What's Watching You

**RTCC (Real-Time Crime Center)** — Live since July 2024
- 7' x 12' video wall tiling live feeds
- Integrates: ShotSpotter, body cams, drones, fixed cameras, ALPR, Community Connect

**Flock Safety ALPR**
- Downtown intersections (Pueblo Downtown Association purchase, 2024)
- Captures: Plate, make, model, color, bumper stickers, damage
- Retention: 30 days (vendor cloud)
- Cross-agency sharing: ~30 Colorado agencies

**ShotSpotter**
- ~6 sq mi coverage in designated "high-crime" areas
- Alerts RTCC within 60 seconds
- Note: 89% false positive rate (MacArthur Justice Center study, Chicago data)

**Community Connect**
- Private doorbell/security cameras registered with police
- Police request footage without warrant
- No public retention policy

**Drones**
- 60-90 second response capability
- Feeds route to RTCC

### Camera Density Map Practice

**Exercise:** Walk your regular routes. Note:
- Doorbell cameras (Ring, Nest, Arlo) — often federated to police
- Business cameras — especially banks, gas stations, convenience stores
- Traffic cameras — not all are ALPR but many are
- Schools and public buildings

**Ingress/egress planning:** For sensitive meetings or events, identify routes with lower camera density. Enter one way, leave another.

---

## 3. Mobility Data

### How Your Movement Is Tracked

| Source | What It Captures | Retention |
|--------|------------------|-----------|
| **ALPR (Flock, Vigilant)** | Plate + timestamp + GPS | 30+ days (often years) |
| **Telematics** (Progressive, State Farm) | GPS every few seconds + driving behavior | Indefinite |
| **Rideshare** (Uber, Lyft) | Pickup/dropoff + payment + device scans | Years |
| **Transit cards** (RTD) | Tap location + time | Months (subpoenable) |
| **Toll systems** (E-470) | Plate + time + location | Years |
| **Parking apps** | Location + payment + duration | Years |

### Colorado Context

- **RTD Denver** responds quickly to law enforcement requests for smart-card data
- **E-470 toll records** are subpoenaed in criminal and civil cases
- **Denver ALPR network:** 1,400+ immigration searches in 2024 alone (NBC News)
- **Cross-jurisdictional ALPR sharing** — Pueblo plates scanned in Denver are searchable from Pueblo

### Counter-measures

| Action | Impact |
|--------|--------|
| **Disable telematics** (insurance dongles) | No real-time GPS broadcast |
| **Cash for gas/parking** when possible | Breaks location-payment link |
| **Rotate transit cards** or use paper tickets | Harder to build travel history |
| **Carpool with cash fuel** for sensitive travel | Plate isn't yours |
| **Park away from ALPR corridors** | Walk the last blocks |
| **Know camera locations** | Route planning |

**Reality check:** You cannot fully avoid ALPR if you drive. The goal is reducing unnecessary exposure, not invisibility.

---

## 4. Device Tracking

### Your Phone Constantly Broadcasts

**Even with GPS "off":**
- Cell tower triangulation (always, if cellular is on)
- WiFi scanning (looking for known networks)
- Bluetooth beaconing (device name + MAC)

**Apps sell location:**
- Weather apps, games, shopping apps, news apps
- Data flows: App → Ad network → Data broker → Police (no warrant)

### The Advertising ID Problem

Your phone has a unique advertising ID that links your activity across apps. This is the primary way commercial surveillance tracks you.

**Reset it regularly:**
- **iPhone:** Settings → Privacy → Tracking → OFF
- **Android:** Settings → Privacy → Ads → Delete advertising ID

This doesn't stop collection, but breaks the linking.

### Location Permissions Audit

Most apps don't need your location. Set everything to "Never" except:
- Maps/navigation → "While Using"
- Weather → "Never" (just search your city manually)
- Social media → "Never"
- Games → "Never"
- Shopping → "Never"

### WiFi/Bluetooth Discipline

- **Turn off WiFi when not connected** (truly off, not just disconnected)
- **Turn off Bluetooth when not using**
- Your device name should be generic ("iPhone" not "Maria's iPhone")

---

## 5. Social & Commercial Data Brokers

### What They Have on You

Data brokers aggregate:
- Voter registration (public in Colorado)
- Property records
- Vehicle registration
- Court filings
- Social media
- App location data
- Purchase history
- Subscription databases
- Breached credentials

### Colorado-Specific

- **Voter rolls + appended cell numbers** sold to political consultants
- Same lists leak to other buyers
- **Family locator apps** share geofenced visits (church, clinic, union hall) with marketing partners

### Counter-measures

| Action | Impact |
|--------|--------|
| **Data broker opt-outs** | Removes from people-search sites |
| **Alias emails** (SimpleLogin, Firefox Relay) | For petitions, newsletters |
| **Review social media** | What's public? What's tagged? |
| **Redact before posting** | Faces, plates, addresses in photos |

See: **Data Broker Starter Kit** handout for the first 5 opt-outs.

---

## What Colorado Sees

### CIAC (Colorado Information Analysis Center)

The state fusion center in Centennial. Aggregates data from local agencies and shares with federal partners.

**Data flows:**
```
Local (Pueblo RTCC) → State (CIAC) → Federal (FBI, DHS, ICE)
```

**What they have access to:**
- ALPR data from participating agencies
- Suspicious activity reports (SARs)
- Social media monitoring
- Commercial data purchases

### ICE Access

ICE doesn't need to run their own surveillance. They:
- **Purchase location data** from Venntel, Babel Street, Fog Data Science
- **Query ALPR databases** through state/local partnerships
- **Subpoena social media** metadata from platforms
- **Receive tips** from local law enforcement

**Sheriff Lucero's position (Jan 2025):** Will not participate in "roundups" but will assist ICE when "criminal charges exist or officer safety demands it."

---

## What Pueblo Does With This Data

### RTCC Workflow

1. Sensors (cameras, ALPR, ShotSpotter, body cams) generate data
2. Data streams to RTCC video wall
3. Analysts can query, correlate, alert in real-time
4. Data retained per policy (varies by source)
5. Can be shared with state (CIAC) and federal partners

### Documented Use Cases

- **Drug transaction observed** on video wall in real-time during Community Connect demo (Daktronics press release)
- **Vehicle tracking** via Flock cross-agency queries
- **ShotSpotter alerts** trigger drone and patrol response

### What We Don't Know (CORA Request Territory)

- Does RTCC data flow automatically to CIAC?
- What retention policies govern each data source?
- Who has access to query the systems?
- Are there audit logs of queries?
- What federal agencies have MOU access?

---

## Quick Checklist: Before Field Work

```
┌─────────────────────────────────────────────────────────────────┐
│              BEFORE SENSITIVE ACTIVITIES                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  FINANCIAL:                                                      │
│  □ Cash on hand for transit, food, fuel                          │
│  □ No linked payment apps used                                   │
│                                                                  │
│  PHYSICAL:                                                       │
│  □ Know camera clusters along route                              │
│  □ Plan ingress/egress via different corridors                   │
│  □ Wardrobe: layers, not disguises                               │
│                                                                  │
│  MOBILITY:                                                       │
│  □ Telematics disabled                                           │
│  □ If driving: park away from venue, walk in                     │
│  □ Consider: carpool, transit, alternative transport             │
│                                                                  │
│  DEVICE:                                                         │
│  □ Phone in airplane mode or left home                           │
│  □ If bringing: burner or secondary device                       │
│  □ No biometrics (PIN only)                                      │
│                                                                  │
│  FALLBACK:                                                       │
│  □ Emergency contact on paper                                    │
│  □ Legal observer identified                                     │
│  □ CORRN: 844-864-8341                                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## The Mindset

**Civilian resilience is about consistency, not gadgets.**

- Pick a small set of practices
- Build habits
- Teach the next person

You cannot achieve perfect invisibility. The goal is:
- Reduce unnecessary exposure
- Break easy correlations
- Make bulk surveillance less useful
- Protect your network, not just yourself

---

## Research Sources

- **UTS for Civilians** — opsec/UTS for Civilians.md
- **Surveillance Counter-Measures** — primers/Surveillance Counter-Measures.md
- **Pueblo 81008 Surveillance Memo** — opsec/Pueblo 81008 Surveillance.md
- **EFF - Fog Data Science** — eff.org/deeplinks/2022/08/inside-fog-data-science
- **NBC News - Flock + Immigration** — 1,400+ immigration searches through Denver ALPR
- **Brennan Center - ALPR** — brennancenter.org
- **FTC Enforcement (2024)** — Venntel, X-Mode, Mobilewalla location data sales

---

*Part of Digital Hygiene: Let's Talk — January 2026*
*La Raza VII.I.IX — github.com/samedayhurt/laraza*
