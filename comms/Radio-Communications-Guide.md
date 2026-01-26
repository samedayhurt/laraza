# Radio Communications Guide

When the internet is down, monitored, or unreliable, radio-based communications provide an independent channel that doesn't rely on cell towers, ISPs, or centralized infrastructure. This guide covers LoRa mesh networks, Reticulum, and amateur radio options.

---

## When Radio Beats Internet

| Scenario | Internet Problem | Radio Solution |
|----------|------------------|----------------|
| Cell network congestion | Overwhelmed at large events | LoRa mesh works independently |
| Cell jamming | Intentional interference | RF harder to blanket-jam |
| ISP/carrier surveillance | Traffic monitored | Point-to-point, no central logs |
| Infrastructure failure | Tower down, power outage | Battery-powered, decentralized |
| Remote areas | No cell coverage | Long-range RF propagation |

**Trade-offs:**
- Lower bandwidth (text, not video)
- Requires hardware beyond smartphones
- Some options require licensing
- Learning curve for setup

---

## Option 1: Meshtastic (LoRa Mesh)

**Best for:** Group coordination, text messaging, GPS sharing, no license required

Meshtastic creates a mesh network using inexpensive LoRa radios. Messages hop through the mesh until they reach the recipient.

### How It Works

```
[Phone A] ←Bluetooth→ [LoRa Node A] ~~~radio~~~ [LoRa Node B] ~~~radio~~~ [LoRa Node C] ←Bluetooth→ [Phone C]
```

- Each node relays messages for others
- Range: 1-10+ km per hop (line of sight)
- No internet, no cell service required
- Encrypted by default (AES256)

### Hardware Options

| Device | Price | Notes |
|--------|-------|-------|
| Heltec LoRa 32 V3 | ~$20 | Budget option, good starter |
| LILYGO T-Beam | ~$35 | Built-in GPS, longer battery |
| LILYGO T-Echo | ~$50 | E-ink display, very low power |
| RAK WisBlock | ~$40 | Modular, industrial quality |
| Heltec Wireless Tracker | ~$25 | GPS + display combo |

**Recommended starter:** LILYGO T-Beam Supreme (GPS + good battery + case options)

### Setup Guide

**Step 1: Flash Meshtastic Firmware**

1. Go to [flasher.meshtastic.org](https://flasher.meshtastic.org/)
2. Connect your device via USB
3. Select your device type
4. Click "Flash" and wait

**Step 2: Install Meshtastic App**

| Platform | Source |
|----------|--------|
| Android | F-Droid or Google Play |
| iOS | App Store |
| Desktop | [meshtastic.org](https://meshtastic.org/) |

**Step 3: Pair Device**

1. Open Meshtastic app
2. Enable Bluetooth on your phone
3. Tap "+" to add device
4. Select your Meshtastic device from list
5. Device pairs automatically

**Step 4: Configure**

In the app, go to Settings:

1. **Region:** Set to your location (affects legal frequencies)
   - US: `US` (915 MHz)
   - EU: `EU_868` (868 MHz)

2. **Channel:** Create or join a channel
   - Default channel is unencrypted public mesh
   - Create private channel with a name + PSK (pre-shared key)
   - Share channel settings with your group via QR code

3. **Device Role:**
   - `Client` - Normal use
   - `Router` - Fixed location, relays messages
   - `Tracker` - Primarily shares GPS location

### Operational Use

**For protests/events:**

1. **Pre-event:**
   - Distribute configured devices to team leads
   - Create private channel with strong PSK
   - Test range in the area

2. **During:**
   - Text-based coordination
   - Share GPS locations of key points
   - Mesh extends as people spread out

3. **Limitations:**
   - ~200 characters per message
   - Latency of several seconds
   - Battery life: 8-24 hours depending on device

### Legal Status

LoRa in ISM bands (915 MHz US, 868 MHz EU) is **license-free** for low-power use. Meshtastic complies with power limits by default.

---

## Option 2: Reticulum Network Stack

**Best for:** Data transfer over any medium, file sharing, more bandwidth than Meshtastic

Reticulum is a networking stack designed for high-latency, low-bandwidth networks. It can run over LoRa, packet radio, serial links, or the internet as a fallback.

### How It Works

- Creates encrypted, private network over unreliable links
- Works over LoRa, serial, TCP/IP, or any combination
- Applications built on top: LXMF (messaging), NomadNet (file sharing)
- No central servers—fully distributed

### Why Reticulum + LoRa?

| Feature | Meshtastic | Reticulum |
|---------|------------|-----------|
| Primary use | Simple messaging | Data networks |
| File sharing | No | Yes (NomadNet) |
| Bandwidth | ~200 chars/msg | Higher efficiency |
| Complexity | Easy | Moderate |
| Internet fallback | No | Yes (hybrid) |

**Reticulum is ideal when you need to move files or build more complex communications.**

### Hardware

Reticulum can use:
- **LoRa devices:** Same as Meshtastic (Heltec, T-Beam, etc.)
- **Packet radio TNCs:** For amateur radio bands
- **Serial links:** Direct cable connections
- **Internet:** As transport or fallback

### Setup Guide

**Step 1: Install Reticulum**

```bash
# Linux/Mac
pip install rns

# Verify installation
rnsd --version
```

**Step 2: Install LXMF (Messaging)**

```bash
pip install lxmf
```

**Step 3: Install NomadNet (Interface + File Sharing)**

```bash
pip install nomadnet
```

**Step 4: Configure LoRa Interface**

Create `~/.reticulum/config`:

```ini
[reticulum]
enable_transport = True
share_instance = Yes

[interfaces]
  [[RNode LoRa Interface]]
    type = RNodeInterface
    interface_enabled = True
    port = /dev/ttyUSB0
    frequency = 915000000
    bandwidth = 125000
    txpower = 17
    spreadingfactor = 8
    codingrate = 5
```

**Step 5: Flash RNode Firmware (for LoRa hardware)**

Reticulum uses RNode firmware for LoRa:

```bash
pip install rnode
rnodeconf --autoinstall
```

Follow prompts to flash your LoRa device.

**Step 6: Start Network**

```bash
# Start Reticulum daemon
rnsd

# In another terminal, start NomadNet
nomadnet
```

### Using NomadNet

NomadNet provides:
- Text messaging (LXMF)
- File sharing (pages and files)
- Network browser (like simple web pages)

**Interface:** Terminal-based (ncurses)

```
┌─ NomadNet ──────────────────────────────────────────────┐
│ Network │ Conversations │ Directory │ Files │ Config  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Conversations                                          │
│  ─────────────                                          │
│  > Alice [2 new]                                        │
│    Bob                                                  │
│    Field Team                                           │
│                                                         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### File Transfer over LoRa

With Reticulum, you can share files over LoRa (slowly but reliably):

1. In NomadNet, go to Files
2. Add files to your share directory (`~/.nomadnet/storage/`)
3. Others can browse and download

**Speed:** ~500 bytes/sec over LoRa (a 1MB file takes ~30 minutes)

**Use case:** Share documents, small images, text files when internet is unavailable.

### Hybrid Mode: LoRa + Internet

Reticulum can use multiple transports simultaneously:

```ini
[interfaces]
  [[RNode LoRa Interface]]
    # ... LoRa config ...

  [[TCP Server Interface]]
    type = TCPServerInterface
    interface_enabled = True
    listen_ip = 0.0.0.0
    listen_port = 4965

  [[TCP Client Interface]]
    type = TCPClientInterface
    interface_enabled = True
    target_host = trusted-friend.com
    target_port = 4965
```

Messages route over whatever path is available. If internet fails, LoRa takes over.

### Sideband (Mobile Client)

For Android/iOS, use **Sideband**:

1. Install from F-Droid (Android) or build from source
2. Connect to LoRa device via Bluetooth or serial
3. Send messages via LXMF protocol

---

## Option 3: Amateur Radio (APRS)

**Best for:** Longer range, established infrastructure, requires license

APRS (Automatic Packet Reporting System) is a ham radio protocol for sending GPS positions and short messages over VHF/UHF.

### Legal Requirements

**Amateur radio requires a license:**

| Country | License | Exam |
|---------|---------|------|
| USA | FCC Technician | 35 questions, no Morse code |
| Canada | Basic with Honours | 100 questions |
| UK | Foundation Licence | Online exam available |

**Study resources:**
- [hamstudy.org](https://hamstudy.org/) - Free practice exams
- [ARRL](https://arrl.org/) - Official US amateur radio organization

**Cost:** ~$35 exam fee, license is free for 10 years

### Why Get Licensed?

- Legal access to more power (50W vs 1W)
- Better range (50+ km with repeaters)
- Established infrastructure (repeaters, digipeaters)
- Community of experienced operators

### Hardware

**Budget setup (~$50):**
- Baofeng UV-5R (~$25)
- Programming cable (~$10)
- Better antenna (~$15)

**Better setup (~$200):**
- Yaesu FT-60R or similar
- Mobilinkd TNC (~$100) for APRS

### APRS Setup

**Method 1: Hardware TNC**

1. Get a Mobilinkd TNC3 or similar
2. Connect to your radio's audio/PTT
3. Install APRSDroid (Android) or similar
4. Configure callsign and APRS settings

**Method 2: Software TNC (Dire Wolf)**

```bash
# Install Dire Wolf
sudo apt install direwolf

# Configure /etc/direwolf.conf
ADEVICE plughw:1,0
ACHANNELS 1
MYCALL YOURCALL-9
MODEM 1200
```

Connect radio to computer sound card.

### APRS for Activists

**Position reporting:**
- Track team locations
- Visible to other hams (consider privacy)
- Use tactical callsigns (YOURCALL-9 for mobile)

**Messaging:**
- 67 characters max
- Store-and-forward via digipeaters
- Not encrypted (ham radio requires ID)

**Privacy concern:** APRS positions are public. Use only when coordination value outweighs privacy cost.

---

## Comparison Matrix

| Feature | Meshtastic | Reticulum | APRS |
|---------|------------|-----------|------|
| License required | No | No | Yes |
| Range (per hop) | 1-10 km | 1-10 km | 10-50+ km |
| Encryption | Yes (AES256) | Yes (Curve25519) | No (illegal) |
| File transfer | No | Yes | No |
| Infrastructure | None needed | None needed | Digipeaters |
| Complexity | Easy | Moderate | Moderate |
| Cost | $20-50 | $20-50 | $50-200 |
| Legal in US | Yes | Yes | Yes (licensed) |

### Recommendations by Use Case

| Use Case | Recommended |
|----------|-------------|
| Protest coordination | Meshtastic |
| File sharing without internet | Reticulum + LoRa |
| Long-range emergency comms | APRS (licensed) |
| Quick setup, minimal training | Meshtastic |
| Building resilient networks | Reticulum |
| Integration with ham community | APRS |

---

## Building Your Radio Kit

### Minimal Kit (~$50)

- 2x Heltec LoRa 32 V3 ($40)
- USB cables and chargers ($10)
- Meshtastic firmware
- Pairs of nodes for basic communication

### Standard Kit (~$150)

- 2x LILYGO T-Beam Supreme ($80)
- External antennas ($20)
- Battery packs ($20)
- Cases/weatherproofing ($30)
- Can support a small team

### Advanced Kit (~$400)

- Multiple T-Beams for mesh coverage
- Fixed router node with solar power
- Reticulum-capable nodes
- Baofeng + TNC for APRS fallback
- Laptop for NomadNet/network management

---

## Operational Security

### What Radio Reveals

- **RF emissions:** Your location can be triangulated
- **Traffic analysis:** Who's talking when, message sizes
- **APRS:** Callsign required, positions public

### Mitigations

1. **Keep transmissions brief** — Harder to triangulate
2. **Move after transmitting** — Don't stay in one place
3. **Use encryption** (Meshtastic/Reticulum) — Content protected
4. **Avoid APRS for sensitive ops** — Public and tied to license

### Field Protocol

1. **Test equipment before events** — Don't debug in the field
2. **Establish channels in advance** — Share PSKs securely beforehand
3. **Assign radio to specific roles** — Media, scouts, legal, command
4. **Have internet fallback** — Radio supplements, doesn't replace
5. **Know when to go silent** — If being actively monitored, radio silence

---

## Troubleshooting

### Meshtastic Issues

**Devices not connecting:**
- Check they're on same channel with same PSK
- Verify region settings match
- Try closer range first

**Short range:**
- Check antenna connection
- Move to higher ground
- Increase spreading factor (trades speed for range)

**Battery draining fast:**
- Enable power saving mode
- Reduce GPS update frequency
- Use `Client` role, not `Router`

### Reticulum Issues

**Daemon won't start:**
- Check config file syntax
- Verify serial port permissions
- Check LoRa device is properly flashed

**No connectivity:**
- Verify both ends have compatible configs
- Check frequency/bandwidth settings match
- Try direct cable connection first

### APRS Issues

**Not decoding packets:**
- Check audio levels (not too loud or quiet)
- Verify TNC configuration
- Make sure squelch isn't too tight

---

## Resources

### Meshtastic
- [meshtastic.org](https://meshtastic.org/) - Official site
- [Meshtastic Discord](https://discord.gg/meshtastic) - Community support

### Reticulum
- [reticulum.network](https://reticulum.network/) - Official documentation
- [GitHub: markqvist/Reticulum](https://github.com/markqvist/Reticulum)
- [NomadNet Manual](https://github.com/markqvist/NomadNet)

### Amateur Radio
- [ARRL](https://arrl.org/) - US ham radio organization
- [hamstudy.org](https://hamstudy.org/) - License exam prep
- [APRS.fi](https://aprs.fi/) - Live APRS map

### Hardware
- [Heltec Store](https://heltec.org/)
- [LILYGO Store](https://www.lilygo.cc/)
- [Mobilinkd](https://store.mobilinkd.com/) - APRS TNCs

---

*Radio communications require practice. Set up your equipment now, learn to use it, so it's ready when you need it.*
