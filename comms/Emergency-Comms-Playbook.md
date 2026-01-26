# Emergency Communications Playbook

When primary communications fail—whether from infrastructure outages, jamming, or seizure—this playbook provides fallback procedures to maintain coordination with your team.

**Print this document and keep a physical copy.** When your phone is seized or networks are down, you can't look this up.

---

## Communication Tiers

Establish multiple communication channels before you need them. If one fails, fall back to the next.

```
TIER 1: Primary (Internet-dependent)
├── Signal groups
├── Element/Matrix rooms
└── Secure email

TIER 2: Secondary (Cell-dependent)
├── SMS (unencrypted, last resort)
├── Phone calls
└── Signal over cellular only

TIER 3: Local/Mesh (Internet-independent)
├── Briar (Bluetooth/Wi-Fi mesh)
├── Meshtastic (LoRa radio)
├── Reticulum + NomadNet
└── Bridgefy / similar apps

TIER 4: Voice Radio
├── FRS/GMRS (license-free, short range)
├── Meshtastic voice (planned feature)
└── Ham radio APRS (licensed)

TIER 5: Physical
├── Runners with written messages
├── Pre-arranged meeting points
└── Visual signals
└── Dead drops
```

---

## Pre-Event Setup

### 1. Establish Communication Tree

Don't rely on one leader communicating with everyone. Use a tree structure:

```
           [Command]
          /    |    \
    [Team A] [Team B] [Team C]
    /  |  \
[A1] [A2] [A3]
```

**Each person should know:**
- Their direct contact (one level up)
- Their direct reports (one level down)
- One alternate contact (in case primary is unavailable)

### 2. Exchange Contact Info BEFORE the Event

For each trusted contact, collect:
- Signal-registered phone number
- Session ID (if using Session)
- Meshtastic/Briar contact info
- FRS/GMRS radio channel + CTCSS tone

**Store this information:**
- Encrypted notes app (Obsidian, Standard Notes)
- Physical paper backup (secure location)
- NOT in regular contacts app

### 3. Establish Code Words

Agree on code words/phrases beforehand. Simple is better—complex codes get forgotten under stress.

| Situation | Code Phrase |
|-----------|-------------|
| I'm OK, continuing | "Green light" |
| Need assistance, not urgent | "Yellow" |
| Emergency, need immediate help | "Red" |
| I've been detained/arrested | "I'm taking a break" |
| My device is compromised | "Let's switch to email" |
| Abort, disperse now | "Weather's turning" |
| All clear, resume | "Sun's out" |
| Meeting at backup location | "Coffee sounds good" |

**Customize these for your group.** Generic codes could be recognized.

### 4. Designate Backup Meeting Points

If all communications fail, where do you physically regroup?

| Situation | Location | Time Window |
|-----------|----------|-------------|
| Event dispersal | [Primary location] | Within 30 min |
| Cannot reach primary | [Secondary location] | Within 1 hour |
| Extended separation | [Tertiary location] | Every 4 hours, on the hour |
| Emergency extraction | [Safe house/friendly space] | ASAP |

**Requirements for backup locations:**
- Known to all team members
- Easy to find without GPS
- Multiple approach routes
- Not obvious (not the main protest site)
- Has cover/concealment

### 5. Test Everything

**Before any action:**
- [ ] All devices charged (100%)
- [ ] Signal groups tested
- [ ] Briar connections synced
- [ ] Meshtastic nodes paired and tested
- [ ] Radio channels programmed and tested
- [ ] Code words reviewed
- [ ] Backup locations confirmed
- [ ] Emergency contacts verified

---

## During an Event

### Communication Discipline

**DO:**
- Keep messages brief and factual
- Use code words for sensitive info
- Confirm receipt of critical messages ("Copy that")
- Maintain regular check-ins (every 15-30 minutes)
- Report position changes to your direct contact

**DON'T:**
- Discuss tactics, names, or plans in detail
- Send location data unless necessary
- Broadcast to entire group when not needed
- Use personal names—use roles or call signs
- Assume messages are private (even on Signal)

### Check-In Protocol

Establish a regular check-in schedule:

```
:00 - Team leads check in with command
:15 - Team members check in with leads
:30 - Team leads check in with command
:45 - Team members check in with leads
```

**If someone misses two consecutive check-ins:**
1. Try alternate contact method
2. Send runner to last known location
3. Alert their emergency contact
4. Assume compromise if no contact after 1 hour

### Escalation Protocol

```
SITUATION NORMAL
│ Regular check-ins, all systems go
│
├─── SITUATION YELLOW
│    │ Increased tension, potential threat
│    │ → Increase check-in frequency
│    │ → Prepare to switch to Tier 2/3
│    │
│    └─── SITUATION RED
│         │ Active threat, communications at risk
│         │ → Switch to Tier 3 (mesh/radio)
│         │ → Minimize non-essential traffic
│         │ → Prepare for dispersal
│         │
│         └─── COMMUNICATION BLACKOUT
│              │ No electronic comms safe
│              │ → Tier 5 only (physical)
│              │ → Runners, pre-set meeting points
│              │ → Abort if necessary
```

---

## Network Down Procedures

### Symptom: Cell Network Congested

**Signs:**
- Messages not sending
- Calls failing
- Very slow data
- Signal shows "connecting..."

**Response:**
1. Don't panic—this is common at large events
2. Switch to Wi-Fi if available (may also be congested)
3. Activate Tier 3: Briar, Meshtastic
4. Send runner to relay critical info
5. Wait it out—networks often recover

### Symptom: Cell Network Jammed

**Signs:**
- Complete loss of signal on all carriers
- Other people nearby also have no signal
- Signal returns when you move away from area

**Response:**
1. Assume hostile interference
2. Immediately switch to Tier 3/4
3. Alert team via mesh network
4. Consider relocating away from jamming source
5. Document the jamming (location, time, duration)

### Symptom: Internet Blocked (Still Have Cell Signal)

**Signs:**
- Can make calls but no data
- VPN won't connect
- Apps time out

**Response:**
1. Try different VPN servers/protocols
2. Use SMS as temporary fallback (unencrypted!)
3. Tor might bypass some blocks (try Orbot)
4. Switch to Tier 3/4 for sensitive info
5. Reserve SMS for non-sensitive coordination only

---

## Device Seizure Protocol

### Before Seizure (Preparation)

1. **Enable auto-lock** (30 seconds or less)
2. **Use strong password** (not just fingerprint)
3. **Enable device encryption** (default on modern phones)
4. **Enable Signal screen lock**
5. **Set disappearing messages** (24 hours or less)
6. **Know your unlock code** for duress PIN if using GrapheneOS
7. **Back up critical info** to secure location

### During Seizure

1. **Lock device immediately** if possible
   - GrapheneOS: Press power 5 times
   - iPhone: Press power 5 times or hold power + volume
   - Android: Press power button

2. **State clearly:** "I do not consent to a search of this device"

3. **Invoke your rights:**
   - "I am exercising my right to remain silent"
   - "I want a lawyer"

4. **Remember:** You generally do NOT have to:
   - Provide your password (5th Amendment)
   - Unlock with biometrics (less settled law—lock with password)
   - Explain what's on the device

5. **DO NOT:**
   - Try to delete data in front of them (obstruction)
   - Lie about having devices
   - Consent to anything

### After Seizure

**Immediately (if able):**
1. Contact legal support
2. Document everything (time, location, officers, badge numbers)
3. Alert your team via alternate channel

**From another device:**
1. De-authorize the seized device:
   - Signal: Settings → Linked Devices → Remove
   - Element: Settings → Sessions → Sign out
   - Bitwarden: Web vault → Settings → Deauthorize
2. Change passwords for accounts on that device
3. Warn contacts that messages to old device may be compromised
4. Enable additional security on accounts (2FA if not already)

**Do NOT use a returned device:**
- It may have been tampered with
- Assume it has spyware installed
- Factory reset is not sufficient
- Either don't use it or completely reinstall OS

### Notifying Team of Seizure

Use your duress code word. Example:

```
NORMAL:    "I'm heading home, talk soon"
COMPROMISED: "I'm heading home, take care" ← pre-agreed duress signal
```

If you can't communicate:
- Your missed check-ins should trigger concern
- Emergency contact should be notified
- Assume your device contents are visible to adversary

---

## Rapid Response Scenarios

### Scenario: Mass Arrest Situation

1. **If you're being arrested:**
   - Lock device
   - State "I do not consent to searches"
   - Stay silent except for: name, address, invoking rights
   - Remember badge numbers if possible

2. **If you witness arrests:**
   - Document from safe distance
   - Note badge numbers, time, location
   - Do NOT interfere physically
   - Report to legal support immediately

3. **Team response:**
   - Account for all team members
   - Relay info to legal observers
   - Activate jail support if pre-arranged
   - Document everything

### Scenario: Team Member Missing

```
0 min:   Miss first check-in
         → Try alternate contact method

15 min:  Miss second check-in
         → Send runner to last known location
         → Alert direct supervisor

30 min:  No contact
         → Alert emergency contact
         → Check local hospitals, jails
         → Consider filing missing person report

60 min:  Still no contact
         → Assume possible detention
         → Activate legal support
         → Prepare public statement if appropriate
```

### Scenario: Need to Evacuate Area Quickly

1. **Send abort code** to all channels simultaneously
2. **Disperse** in pre-planned directions (not all together)
3. **Go silent** on electronic comms for set period
4. **Regroup** at backup location at pre-arranged time
5. **Account** for all team members
6. **Debrief** only after confirming safety

### Scenario: Suspected Infiltrator/Compromise

**If you suspect someone is compromised:**
1. Do NOT confront them directly
2. Do NOT discuss suspicion on any channel they can access
3. Inform leadership via separate secure channel
4. Gradually reduce their access to sensitive info
5. Create new channels/groups without them for sensitive ops
6. Document concerning behavior

**If you suspect YOUR device is compromised:**
1. Stop using it for sensitive communication immediately
2. Use duress code to alert contacts
3. Switch to backup device/account
4. Do NOT try to "clean" the device—assume it's burned
5. Get a new device, start fresh

---

## Communication Equipment Checklist

### Basic Kit (Everyone)

```
[ ] Primary phone (Signal, Briar installed)
[ ] Backup battery pack (10,000+ mAh)
[ ] USB charging cable
[ ] Physical copy of this playbook
[ ] Emergency contact card (waterproof)
[ ] Cash (for emergencies)
```

### Enhanced Kit (Team Leads)

```
[ ] Everything in Basic Kit
[ ] Secondary phone or tablet
[ ] Meshtastic LoRa radio
[ ] FRS/GMRS radio
[ ] Portable phone charger (enough for multiple devices)
[ ] Small notebook + pencil (waterproof paper if possible)
```

### Advanced Kit (Communications Officer)

```
[ ] Everything in Enhanced Kit
[ ] Multiple Meshtastic nodes
[ ] Laptop with Reticulum/NomadNet
[ ] Backup SIM cards
[ ] Mudi router with VPN configured
[ ] Faraday bags
[ ] Signal boosting equipment (legal)
```

---

## Quick Reference Card

**Print this on a small card to carry:**

```
EMERGENCY COMMS QUICK REFERENCE
================================

CODES:
Green = OK          Yellow = Need help
Red = Emergency     "Taking a break" = Detained
"Switch to email" = Compromised

TIERS:
1. Signal/Element   (internet)
2. SMS/Calls        (cell)
3. Briar/Meshtastic (mesh)
4. Radio            (voice)
5. Runners/Meet     (physical)

IF SEIZED:
1. Lock device NOW
2. "I don't consent to searches"
3. "I want a lawyer"
4. Stay SILENT

BACKUP LOCATIONS:
Primary: ________________
Secondary: ______________
Time: Every __ hours, on the hour

EMERGENCY CONTACTS:
Legal: _________________
Medical: _______________
Team Lead: _____________
```

---

## After Action

### Debrief Checklist

After every event, review:

1. [ ] Did communication channels work as expected?
2. [ ] Were there any failures? What caused them?
3. [ ] Did everyone know the protocols?
4. [ ] Were code words used correctly?
5. [ ] Any security concerns or incidents?
6. [ ] What should we change for next time?

### Update Procedures

- Rotate code words regularly
- Update backup locations if compromised
- Replace any seized equipment
- Refresh contact info for any number changes
- Share lessons learned with broader community (sanitized)

---

## Legal Resources

**National:**
- National Lawyers Guild: (212) 679-5100
- ACLU Know Your Rights: aclu.org/know-your-rights
- EFF: eff.org

**Local (Colorado):**
- Colorado ACLU: (303) 777-5482
- CIRC Colorado: circcolorado.org

**Hotlines to memorize:**
- NLG Mass Defense: (212) 679-5100
- Local jail support: ________________

---

*Plan for the worst, hope for the best. When communications fail, preparation is the difference between chaos and coordinated response.*
