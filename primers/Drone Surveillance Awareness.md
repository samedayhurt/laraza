# Drone Surveillance Awareness

Understanding how law enforcement and private entities use drones helps you make informed decisions about privacy, public assembly, and civil liberties. This guide covers identification, capabilities, legal frameworks, and protective strategies.

---

## The Current Landscape (2025)

As of 2025, over **30,000 drones** are projected to be used by public safety agencies in the United States—a 300% increase from 2020. More than 1,000 police departments have adopted drone technology, with that number growing rapidly.

### Common Police Drone Models

| Model | Capabilities | Flight Time | Range | Identifying Features |
|-------|-------------|-------------|-------|---------------------|
| **DJI Matrice 30T** | Thermal + 48MP camera, 200x zoom | 41 min | 15 km | Large quadcopter, dual camera pods |
| **DJI Matrice 350 RTK** | Multi-sensor, centimeter positioning | 55 min | 15 km (9.3 mi) | Largest DJI enterprise drone |
| **DJI Matrice 4T** (2025) | 20MP wide + 56x hybrid zoom + thermal | 42 min | 20 km | Latest model, sleeker profile |
| **DJI Mavic 3 Enterprise** | Thermal, 56x zoom | 45 min | 15 km | Foldable, smaller footprint |
| **Skydio X2** | American-made, AI obstacle avoidance | 35 min | 6 km | Distinctive X-shaped arms |
| **Autel EVO II Dual** | 8K video + thermal | 42 min | 9 km | Orange accents, folding design |

> **Note:** Nearly 80% of drones used by American police are manufactured by DJI, designated a "Chinese military company" by the U.S. Department of Defense in 2022.

### What Police Drones Can See

```
┌─────────────────────────────────────────────────────────────────┐
│                    DRONE SENSOR CAPABILITIES                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  DAYLIGHT CAMERA          THERMAL (FLIR)        ZOOM CAPABILITY │
│  ┌─────────────┐          ┌─────────────┐       ┌─────────────┐ │
│  │ 48MP+       │          │ Heat sig    │       │ 200x hybrid │ │
│  │ 4K/8K video │          │ Through fog │       │ Read plates │ │
│  │ Face detail │          │ Night use   │       │ from 1+ mi  │ │
│  │ at 100m     │          │ Body detect │       │             │ │
│  └─────────────┘          └─────────────┘       └─────────────┘ │
│                                                                  │
│  ADDITIONAL SENSORS (Advanced Models):                           │
│  • LiDAR mapping          • Radio frequency detection            │
│  • Multispectral imaging  • Acoustic sensors                     │
│  • Gas detection          • Cellular IMSI collection (rare)      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Thermal Camera Reality

Modern thermal cameras on police drones can:
- Detect temperature variations as small as **50 millikelvins** (0.05°C)
- See through smoke, fog, and light foliage
- Identify body heat through thin walls (exterior heat signatures)
- Track individuals at night from 500+ meters
- **Cannot** see through glass, thick walls, or underground

---

## Identifying Drones in Your Area

### Visual Identification

```
COMMON DRONE SILHOUETTES
========================

Quadcopter (Most Common)           Hexacopter (Larger Payload)
        ▲                                   ▲
       /│\                                 /│\
      / │ \                               / │ \
     ●──┼──●                           ●──●─┼─●──●
        │                                   │
     ●──┼──●                           ●──●─┼─●──●
      \ │ /                               \ │ /
       \│/                                 \│/
        ▼                                   ▼

Fixed-Wing (Long Endurance)        Tethered (Persistent)
    ════╦════                            ○
        ║                                │
       ▄▀▀▀▀▀▀▄                          │ cable
        ═══════                          │
                                        ═╧═
```

### Audio Identification

| Drone Size | Sound Character | Audible Range |
|------------|-----------------|---------------|
| Small (Mavic) | High-pitched buzz | 50-100m |
| Medium (Matrice) | Deeper hum, multiple tones | 100-200m |
| Large (Matrice 350) | Loud, low drone | 200-400m |
| Fixed-wing | Airplane-like whine | 100-300m |

### FAA Remote ID (2024 Requirement)

Since March 2024, most drones must broadcast **Remote ID** information:
- Drone serial number or session ID
- Location and altitude of drone
- Location of control station or takeoff point
- Time mark
- Emergency status

**Apps to view Remote ID broadcasts:**
- OpenDroneID (Android/iOS)
- DroneScout (Android)
- Kittyhawk (requires account)

> **Limitation:** Remote ID tells you what's flying but won't stop surveillance. Some government drones may be exempt.

---

## Counter-Drone Detection Methods

### Passive Detection (Legal)

| Method | Equipment | Effectiveness | Cost |
|--------|-----------|---------------|------|
| **Visual observation** | Eyes, binoculars | Good for daytime | Free |
| **Audio detection** | Ears, parabolic mic | Works day/night | $0-200 |
| **Remote ID apps** | Smartphone | Limited to compliant drones | Free |
| **RF spectrum analyzer** | SDR + software | Detects control signals | $20-300 |
| **ADS-B receiver** | RTL-SDR dongle | Larger/commercial drones | $30 |

### RF Detection with SDR

```
DRONE RADIO FREQUENCIES
=======================

2.4 GHz Band          5.8 GHz Band          900 MHz (Some)
├────────────────┤   ├────────────────┤    ├──────────┤
│ WiFi overlap   │   │ Video downlink │    │ Long     │
│ Control signal │   │ Less congested │    │ range    │
│ Most consumer  │   │ Higher quality │    │ control  │
└────────────────┘   └────────────────┘    └──────────┘

Software: SDR# (Windows), GQRX (Linux), SDR++ (Cross-platform)
Hardware: RTL-SDR Blog V3 ($30), HackRF ($300), Airspy ($200)
```

### What NOT to Do (Illegal)

- **Do NOT jam drone signals** - Federal crime (47 U.S.C. § 333)
- **Do NOT shoot down drones** - Federal crime (18 U.S.C. § 32)
- **Do NOT interfere physically** - Even if over your property
- **Do NOT use counter-drone weapons** - Restricted to federal agencies

---

## Protective Strategies

### Physical Countermeasures (Legal)

```
THERMAL SIGNATURE REDUCTION
===========================

Standard Clothing          Emergency Blanket        Umbrella/Shade
    ┌─────┐                   ┌─────┐                ┌─────────┐
    │█████│ <- Visible        │░░░░░│ <- Reduced     │▀▀▀▀▀▀▀▀▀│
    │█████│    heat sig       │░░░░░│    signature   │  ┌───┐  │
    │█████│                   │░░░░░│                │  │   │  │
    └─────┘                   └─────┘                └──┴───┴──┘

• Mylar emergency blankets reflect IR (temporary use)
• Large umbrellas block both visual and thermal
• Dense tree canopy provides natural cover
• Indoor spaces are best protection
```

### Behavioral Countermeasures

1. **Awareness of drone presence**
   - Listen for buzzing sounds
   - Watch for movement against sky
   - Note repeated patterns (circling, hovering)

2. **Use of terrain and structures**
   - Move under covered areas (awnings, bridges, parking structures)
   - Stay near tall buildings that block line of sight
   - Use natural cover (trees, terrain features)

3. **Timing considerations**
   - Drones have limited flight time (20-55 minutes)
   - Battery swaps require landing
   - Night operations use thermal (different tactics needed)

4. **Group tactics**
   - Large groups make individual tracking difficult
   - Uniform appearance reduces distinguishability
   - Frequent movement patterns complicate tracking

### Digital Countermeasures

| Concern | Protection |
|---------|------------|
| Metadata in photos | Strip EXIF before sharing (see Digital Hygiene guide) |
| Drone footage analysis | Avoid distinctive clothing, accessories |
| Facial recognition | Hats, sunglasses, masks (where legal) |
| License plate capture | Drones can read plates from 1+ mile |
| Cell phone tracking | Airplane mode, Faraday bag during sensitive movements |

---

## Legal Framework

### Federal Regulations

- **FAA Part 107**: Commercial/government drone rules
- **Remote ID Rule**: Required since March 16, 2024
- **No-fly zones**: Airports, military bases, national parks, TFRs
- **Privacy**: No comprehensive federal drone privacy law

### Your Rights

1. **First Amendment**: Right to photograph/record drones in public spaces
2. **Fourth Amendment**: Warrant generally required for targeted surveillance of specific individuals
3. **State laws vary**: Some states restrict drone surveillance

### Colorado Specific

Colorado has **no specific drone privacy statute** as of 2025. General privacy and trespass laws apply. Pueblo PD's drone program operates under standard FAA Part 107 guidelines.

> **Pueblo Context**: The city allocated **$100,000** for drone expansion in 2024. Expect increased aerial surveillance at public events, protests, and high-crime areas.

---

## Detection Resources

### Apps and Software

| Tool | Platform | Purpose | Link |
|------|----------|---------|------|
| OpenDroneID | Android/iOS | Remote ID receiver | Play Store / App Store |
| DroneWatcher | Android | RF-based detection | dronesec.com |
| SDR++ | Win/Mac/Linux | Spectrum analysis | github.com/AlexandreRouworthe/SDRPlusPlus |
| ADS-B Exchange | Web | Aircraft tracking | adsbexchange.com |

### Hardware Options

| Device | Purpose | Price Range |
|--------|---------|-------------|
| RTL-SDR Blog V3 | RF spectrum monitoring | $30-40 |
| Airspy Mini | Higher quality SDR | $100 |
| Parabolic microphone | Audio detection | $50-200 |
| Night vision monocular | Visual ID at night | $100-500 |

---

## Pueblo-Specific Information

### Known Drone Operations

- **Pueblo Police Department**: Active drone program, DJI equipment
- **Pueblo County Sheriff**: Coordinates with PD on major events
- **Colorado State Patrol**: Helicopter support, possible drone use
- **CBP/ICE**: Predator drones operate from regional bases (larger scale)

### Areas of Likely Deployment

Based on past patterns and public records:
- Major protests and demonstrations
- Large public events (State Fair, Chile Festival)
- Crime scene documentation
- Traffic incident management
- Search and rescue operations

### Reporting and Documentation

If you observe drone surveillance at a public event:

1. **Document** - Note time, location, flight pattern, visible markings
2. **Photograph/Video** - If safe to do so
3. **File FOIA request** - Colorado Open Records Act (CORA) for drone logs
4. **Report to community** - Share with La Raza network via Signal

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│              DRONE AWARENESS QUICK REFERENCE                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  DETECT:  □ Listen for buzzing       □ Watch sky for movement│
│           □ Check Remote ID apps     □ Note flight patterns  │
│                                                             │
│  PROTECT: □ Use overhead cover       □ Avoid distinctive gear│
│           □ Move unpredictably       □ Phone in airplane mode│
│                                                             │
│  LEGAL:   ✓ Photograph drones        ✗ Do NOT jam signals   │
│           ✓ Document surveillance    ✗ Do NOT shoot down    │
│           ✓ File records requests    ✗ Do NOT interfere     │
│                                                             │
│  REPORT:  Document → Photograph → FOIA → Share via Signal   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Sources

- [San Francisco Police DJI Matrice 30T Deployment](https://dronexl.co/2025/01/05/san-francisco-police-dji-matrice-30t-drones-surveillance/) - DroneXL
- [Police Drones In-Depth Guide 2024](https://uavcoach.com/police-drones/) - UAV Coach
- [Security Drones Guide 2025](https://uavcoach.com/security-drones/) - UAV Coach
- [Best Police Drones 2024](https://www.dslrpros.com/blogs/drone-trends/best-12-police-drones-in-2024-full-reviews-and-features) - DSLRPros
- [Counter-Drone Vulnerabilities](https://www.police1.com/terrorism/op-ed-americas-drone-blind-spot-and-the-9-10-moment-were-ignoring) - Police1
- [FAA Remote ID Information](https://www.faa.gov/uas/getting_started/remote_id)
- [EFF Street Level Surveillance](https://sls.eff.org/) - Electronic Frontier Foundation

---

*Part of La Raza VII.I.IX - Community Field Guide for Pueblo, CO*
*github.com/samedayhurt/laraza*
