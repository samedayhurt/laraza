# Surveillance Counter-Measures

A comprehensive guide to understanding and protecting yourself from modern surveillance technologies. This guide covers physical, digital, and commercial data surveillance with practical defensive strategies.

---

## The Surveillance Ecosystem (2025)

Modern surveillance operates on multiple layers simultaneously. Understanding this ecosystem is the first step to protecting yourself.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SURVEILLANCE ECOSYSTEM MAP                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  GOVERNMENT DIRECT              CORPORATE DATA BROKERS                   │
│  ┌──────────────────┐          ┌──────────────────────┐                 │
│  │ • Police cameras │◄────────►│ • Fog Data Science   │                 │
│  │ • Stingrays/IMSI │          │ • Babel Street       │                 │
│  │ • Drones         │          │ • Venntel/Gravy      │                 │
│  │ • Flock ALPR     │          │ • Mobilewalla        │                 │
│  └────────┬─────────┘          └──────────┬───────────┘                 │
│           │                               │                              │
│           ▼                               ▼                              │
│  ┌──────────────────────────────────────────────────────┐               │
│  │              YOUR LOCATION & IDENTITY                 │               │
│  └──────────────────────────────────────────────────────┘               │
│           ▲                               ▲                              │
│           │                               │                              │
│  ┌────────┴─────────┐          ┌──────────┴───────────┐                 │
│  │ • Cell towers    │          │ • App location data  │                 │
│  │ • WiFi networks  │          │ • Ad tracking IDs    │                 │
│  │ • Bluetooth      │          │ • Social media       │                 │
│  │ • License plates │          │ • Credit cards       │                 │
│  └──────────────────┘          └──────────────────────┘                 │
│  INFRASTRUCTURE                 COMMERCIAL APPS                          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## CRITICAL THREAT: Commercial Telemetry Data

### The Hidden Surveillance Market

**This is the most overlooked surveillance threat.** Government agencies increasingly bypass warrant requirements by purchasing your location data from commercial brokers.

### How Your Data Gets Sold

```
YOUR PHONE
    │
    ▼
┌─────────────────┐
│  Weather App    │ ──► Location every 5 min
│  Social Media   │ ──► Check-ins, tags, posts
│  Shopping Apps  │ ──► Purchase + location
│  Games          │ ──► Background location
│  News Apps      │ ──► Reading habits + location
└─────────────────┘
    │
    ▼
┌─────────────────┐
│  AD NETWORKS    │
│  (Google, Meta, │
│   data brokers) │
└─────────────────┘
    │
    ▼
┌─────────────────┐     ┌─────────────────┐
│ FOG DATA SCIENCE│     │  BABEL STREET   │
│ "Fog Reveal"    │     │  "Locate X"     │
│ 250M+ devices   │     │  CBP/ICE client │
│ Billions of pts │     │  No vetting     │
└─────────────────┘     └─────────────────┘
    │                           │
    ▼                           ▼
┌─────────────────────────────────────────┐
│         LOCAL POLICE / ICE / CBP         │
│   Point-and-click access to your life    │
│   No warrant required (they claim)       │
└─────────────────────────────────────────┘
```

### Real-World Examples

| Incident | What Happened | Source |
|----------|---------------|--------|
| **Protest Tracking** | 17,000 protesters tracked via cell data without knowledge | BuzzFeed News |
| **Mobilewalla** | Estimated demographics of BLM protesters from cell data | CNBC |
| **Fog Reveal** | Sold to 1,000+ agencies; no warrant needed | EFF/AP |
| **ICE Purchases** | CBP/ICE bought Babel Street subscriptions for immigrant tracking | EPIC FOIA |
| **Flock + Immigration** | 1,400+ immigration searches through Denver's ALPR network in 2024 | NBC News |

### What They Can See

With commercial telemetry data, law enforcement can:
- **See everywhere you've been** for months/years
- **Identify your home and work** addresses automatically
- **Map your social network** by who you meet with
- **Track protest attendance** by geofencing event locations
- **Identify patterns** (church, clinic, lawyer, activist meetings)
- **Follow you in real-time** with Locate X and similar tools

### Protection Strategies

| Risk | Mitigation |
|------|------------|
| **App location access** | Deny location permissions; use "While Using" only when necessary |
| **Advertising ID** | Reset regularly; opt out of personalized ads |
| **Background location** | Disable for all apps; check permissions monthly |
| **WiFi/Bluetooth scanning** | Disable when not actively using |
| **Cell location** | Airplane mode or Faraday bag for sensitive movements |

**How to reset your Advertising ID:**
- **iOS**: Settings → Privacy → Tracking → Toggle off "Allow Apps to Request to Track"
- **Android**: Settings → Privacy → Ads → Delete advertising ID

---

## Facial Recognition

### Current Capabilities (2025)

- **Error rates**: Up to 100x higher for Black and Asian faces vs white faces (NIST study)
- **UK Police**: 1,000+ arrests via facial recognition in 2024 alone
- **Clearview AI**: Scraped billions of social media photos; used by 600+ agencies
- **Real-time matching**: Can identify individuals in crowds within seconds

### Protection Strategies

```
FACIAL RECOGNITION DEFEAT SPECTRUM
==================================

LOW EFFORT                                              HIGH EFFORT
────────────────────────────────────────────────────────────────────►

Sunglasses   Hat + Mask   IR LEDs    CV Dazzle    Full Face    Stay
& Hat        (most        in glasses  Makeup      Covering     Indoors
             effective)                (limited
                                      effectiveness)

EFFECTIVENESS VS MODERN AI:
██████████   ████████░░   ██████░░░░  ████░░░░░░  ████████░░  ██████████
   70%          80%          60%         40%         80%        100%
```

### Practical Recommendations

1. **Most effective**: Wide-brimmed hat + sunglasses + COVID-style mask
2. **Avoid distinctive features**: Unique tattoos, piercings, hair colors
3. **Uniform appearance**: Blend with crowd in common clothing
4. **IR glasses/LEDs**: Can overwhelm some camera systems (check legality)
5. **Don't rely on makeup**: CV Dazzle was designed for 2010-era algorithms

### What Doesn't Work Well

| Technique | Problem |
|-----------|---------|
| **CV Dazzle makeup** | Designed for deprecated algorithms; makes you conspicuous to humans |
| **Partial face covering** | Modern AI can identify from partial features |
| **Only sunglasses** | Many systems work with just lower face |
| **Hoodies alone** | Profile, gait, and body shape still trackable |

---

## License Plate Readers (ALPR)

### The Network

```
FLOCK SAFETY ALPR NETWORK
=========================

5,000+ Law Enforcement Agencies
           │
           ▼
┌─────────────────────────────────┐
│     NATIONWIDE DATABASE          │
│  • Billions of scans/month       │
│  • 30-day+ retention             │
│  • Cross-jurisdictional search   │
│  • Real-time alerts              │
└─────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────┐
│     SEARCHABLE BY:               │
│  • Plate number                  │
│  • Vehicle make/model/color      │
│  • Time range                    │
│  • Geographic area               │
│  • "Hot list" matches            │
└─────────────────────────────────┘
```

### Pueblo Context

- **Flock ALPR cameras** deployed throughout city
- **73 mobile ALPRs** on patrol vehicles (2024)
- **Cross-jurisdictional access** with Denver and other CO cities
- **1,400+ immigration searches** through Denver's network alone (2024)

### Legal Avoidance Reality

> "The only way to avoid ALPR data collection would be to give up driving altogether or to keep a vehicle away from the range of a license plate reader — an impossible task in many places."
> — Brennan Center for Justice

### What You Can Do

| Action | Effectiveness | Legality |
|--------|---------------|----------|
| **Alternative transport** | High | Legal |
| **Plate covers/sprays** | Varies | **Often illegal** |
| **Awareness of camera locations** | Medium | Legal |
| **Route planning** | Medium | Legal |
| **Carpooling/ride-share** | Medium | Legal |

**Note**: Many "anti-ALPR" products are illegal and don't work against modern systems anyway. Focus on legal alternatives.

---

## Cell Phone Surveillance

### Stingray/IMSI Catchers

Cell-site simulators (CSS), also known as Stingrays, fake cell towers to intercept phone communications.

```
HOW STINGRAYS WORK
==================

Normal Connection:           Stingray Attack:

  📱 ────────► 🗼            📱 ────────► 📡 (Fake) ────► 🗼
  Phone      Real Tower      Phone      Stingray      Real Tower

                            Stingray captures:
                            • IMSI (SIM identity)
                            • IMEI (phone identity)
                            • Location
                            • Call/SMS metadata
                            • Can force 2G downgrade
```

### Detection: EFF's Rayhunter (2025)

The Electronic Frontier Foundation released **Rayhunter**, an open-source tool to detect Stingrays:
- Runs on mobile hotspots
- Monitors for suspicious cell behavior
- Alerts on 2G downgrade attempts
- Detects unusual IMSI requests

**Hardware needed**: Compatible mobile hotspot (~$50-100)
**Software**: github.com/EFForg/rayhunter

### Protection Strategies

| Method | Effectiveness | Notes |
|--------|---------------|-------|
| **Airplane mode** | Complete | No connectivity |
| **Faraday bag** | Complete | Blocks all signals |
| **Disable 2G** | Partial | Prevents downgrade attacks |
| **Use Signal** | Partial | Encrypts content, not metadata |
| **VPN** | Partial | Encrypts data, not call metadata |
| **Burner phone** | High | For sensitive situations |

**How to disable 2G:**
- **Android**: Settings → Network → Preferred network type → LTE/5G only
- **iPhone**: Not directly possible; use Lockdown Mode for some protection

---

## WiFi and Bluetooth Tracking

### How You're Tracked

Your devices constantly broadcast unique identifiers:

```
YOUR PHONE BROADCASTS
=====================

WiFi Probe Requests          Bluetooth
────────────────────         ─────────────
"Looking for: HomeWiFi"      Device name: "John's iPhone"
"Looking for: WorkWiFi"      MAC Address: AA:BB:CC:DD:EE:FF
"Looking for: CoffeeShop"
MAC Address: 11:22:33:44     Even with WiFi "off," many
                             phones still scan for networks
```

### Retail and Public Tracking

- **Shopping malls** track your path through stores
- **Airports** monitor passenger flow
- **Smart city infrastructure** logs device presence
- **Marketing firms** build movement profiles

### Protection

1. **Disable WiFi when not connected** (truly off, not just disconnected)
2. **Disable Bluetooth when not using**
3. **Use MAC randomization** (enabled by default on newer devices)
4. **Rename device** to something generic ("Phone" not "Sarah's iPhone")
5. **Disable "Ask to Join Networks"**

---

## Social Media Intelligence (SOCMINT)

### Government Monitoring

ICE and other agencies conduct **24/7 social media monitoring**:
- Public posts scanned automatically
- Location data from check-ins and tags
- Network analysis (who you're connected to)
- Sentiment analysis for "threat assessment"
- Historical posts archived even if deleted

### Protection Strategies

```
SOCIAL MEDIA OPSEC CHECKLIST
============================

□ Disable location tagging on all posts
□ Review tagged photos before they appear
□ Use pseudonymous accounts for activism
□ Don't post real-time during sensitive activities
□ Assume all posts are permanent (screenshots exist)
□ Review friend/follower lists regularly
□ Don't discuss immigration status online
□ Use Signal for organizing, not social media
□ Separate personal and activist identities
□ Review privacy settings monthly
```

### Platform-Specific Risks

| Platform | Main Risks |
|----------|------------|
| **Facebook/Instagram** | Real identity, location history, network mapping |
| **Twitter/X** | Real-time location, network analysis, public by default |
| **TikTok** | Facial recognition, behavioral data, foreign access concerns |
| **WhatsApp** | Metadata (who you talk to, when), backup vulnerabilities |
| **LinkedIn** | Employment/immigration status, professional network |

---

## Operational Security for Protests

### Before the Event

```
PRE-PROTEST CHECKLIST
=====================

PHONE:
□ Back up important data
□ Remove sensitive apps (immigration, banking)
□ Log out of social media
□ Disable biometric unlock (use strong PIN)
□ Enable airplane mode or leave phone home
□ If bringing: use burner or secondary device

PHYSICAL:
□ Remove identifying jewelry/accessories
□ Cover distinctive tattoos
□ Wear common, plain clothing
□ Bring hat, sunglasses, mask
□ Carry emergency contacts on paper
□ Know your legal observer's location
```

### During the Event

| Risk | Counter-Measure |
|------|-----------------|
| Facial recognition | Hat + sunglasses + mask |
| Drone surveillance | Stay under cover when possible |
| ALPR | Carpool, use transit, park away from venue |
| Cell tracking | Airplane mode or Faraday bag |
| Social media | Don't post location in real-time |
| Undercover officers | Assume you're being watched |

### After the Event

1. **Don't post identifying photos** of others without consent
2. **Blur faces** before any public sharing
3. **Strip metadata** from all photos (see Digital Hygiene guide)
4. **Wait to post** until well after event concludes
5. **Secure legal observer notes**
6. **Debrief** with trusted organizers only

---

## Quick Reference: Threat vs. Counter-Measure

| Threat | What It Captures | Counter-Measure |
|--------|------------------|-----------------|
| **Commercial telemetry** | Location via apps | Deny location permissions; reset Ad ID |
| **Facial recognition** | Identity from face | Hat, sunglasses, mask |
| **ALPR** | Vehicle movements | Alternative transport; route awareness |
| **Stingray** | Phone identity, location | Airplane mode; Faraday bag |
| **WiFi tracking** | Device presence | Disable WiFi when not connected |
| **Social media** | Network, location, content | Pseudonymous accounts; no real-time posts |
| **Drones** | Visual/thermal surveillance | Cover; unpredictable movement |
| **Flock cameras** | Vehicle + occupant | Awareness; FOIA camera locations |

---

## Resources

### Detection Tools
- **Rayhunter** (Stingray detection): [github.com/EFForg/rayhunter](https://github.com/EFForg/rayhunter)
- **OpenDroneID** (drone detection): App stores
- **SnoopSnitch** (cell anomalies): Android only

### Organizations
- [Electronic Frontier Foundation - Street Level Surveillance](https://sls.eff.org/)
- [ACLU - Stingray Tracking](https://www.aclu.org/issues/privacy-technology/surveillance-technologies/stingray-tracking-devices)
- [Brennan Center - ALPR](https://www.brennancenter.org/our-work/research-reports/automatic-license-plate-readers-legal-status-and-policy-recommendations)
- [Privacy International](https://privacyinternational.org/examples/tracking-protest-surveillance)

### Further Reading
- [EFF: Inside Fog Data Science](https://www.eff.org/deeplinks/2022/08/inside-fog-data-science-secretive-company-selling-mass-surveillance-local-police)
- [EFF: How Ad Tech Became Cop Spy Tech](https://www.eff.org/tl/deeplinks/2022/08/how-ad-tech-became-cop-spy-tech)
- [Marshall Project: Protest Surveillance Technologies](https://www.themarshallproject.org/2024/11/12/protest-surveillance-technologies)
- [EFF: Location Data Brokers](https://www.eff.org/issues/location-data-brokers)
- [Krebs: Global Surveillance Free-for-All](https://krebsonsecurity.com/2024/10/the-global-surveillance-free-for-all-in-mobile-ad-data/)

---

## Sources

- [The Marshall Project - Protest Surveillance Technologies](https://www.themarshallproject.org/2024/11/12/protest-surveillance-technologies)
- [BuzzFeed News - 17,000 Protesters Tracked](https://www.buzzfeednews.com/article/carolinehaskins1/protests-tech-company-spying)
- [NBC News - Flock Cameras and Immigration Searches](https://www.nbcnews.com/tech/tech-news/flock-police-cameras-scan-billions-month-sparking-protests-rcna230037)
- [EFF - Inside Fog Data Science](https://www.eff.org/deeplinks/2022/08/inside-fog-data-science-secretive-company-selling-mass-surveillance-local-police)
- [EFF - Babel Street Locate X](https://www.eff.org/deeplinks/2024/11/creators-police-location-tracking-tool-arent-vetting-buyers-heres-how-protect)
- [EFF - Rayhunter](https://www.eff.org/deeplinks/2025/03/meet-rayhunter-new-open-source-tool-eff-detect-cellular-spying)
- [EFF - Cell-Site Simulators](https://sls.eff.org/technologies/cell-site-simulators-imsi-catchers)
- [ACLU - Stingray Tracking Devices](https://www.aclu.org/issues/privacy-technology/surveillance-technologies/stingray-tracking-devices)
- [Brennan Center - ALPR Legal Status](https://www.brennancenter.org/our-work/research-reports/automatic-license-plate-readers-legal-status-and-policy-recommendations)
- [Cloudwards - How to Block Stingray](https://www.cloudwards.net/how-to-block-stingray-surveillance/)
- [Privacy International - Facial Recognition](https://privacyinternational.org/long-read/5682/toward-regulation-addressing-legal-void-facial-recognition-technology)
- [Adam Harvey - CV Dazzle](https://adam.harvey.studio/cvdazzle)

---

*Part of La Raza VII.I.IX - Community Field Guide for Pueblo, CO*
*github.com/samedayhurt/laraza*
