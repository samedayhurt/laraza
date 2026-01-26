# Operational Security Layers

A practical guide to protecting yourself while researching surveillance infrastructure, documenting police activity, organizing, or simply staying informed. Built for community journalists, activists, and engaged residents—not security professionals.

**Core principle:** Security is about layers. No single tool protects you completely, but combining the right tools for your threat level creates meaningful protection.

---

## Understanding Your Threat Model

Before choosing tools, understand what you're protecting against:

| Threat | Example | Protection Layer |
|--------|---------|------------------|
| **Passive surveillance** | ISP logging, Flock ALPR correlating your movements | VPN, Tor, browser hardening |
| **Targeted tracking** | Device fingerprinting, ad network profiling | Browser containers, VMs, hardened devices |
| **Physical device seizure** | Phone taken at protest, laptop seized | Encryption, burner devices, compartmentalization |
| **Network interception** | Public Wi-Fi monitoring, stingray/IMSI catchers | VPN, encrypted comms, Mudi router |
| **Social engineering** | Phishing, pretexting, informants | Vetting, compartmentalization, operational discipline |

**For Pueblo-specific threats:** The [Pueblo 81008 Surveillance Memo](../opsec/Pueblo%2081008%20Surveillance.md) documents the local apparatus—RTCC, ShotSpotter, Flock ALPRs, Community Connect, and ICE infrastructure. Your protection choices should account for these systems.

---

## Layer 1: Browser Hardening

**Protects against:** Tracking, fingerprinting, data collection, casual surveillance

**When to use:** Daily browsing, reading city agendas, general research, social media

### Firefox Hardening (Recommended)

Firefox offers the best balance of usability and privacy. Modern Firefox (91+) includes many protections by default.

**Step 1: Install Firefox**
- Download from [mozilla.org](https://www.mozilla.org/firefox/)
- Avoid Snap/Flatpak versions on Linux if possible (sandboxing can interfere with some privacy tools)

**Step 2: Configure Privacy Settings**
1. Open Settings → Privacy & Security
2. Set Enhanced Tracking Protection to **Strict**
3. Enable "Delete cookies and site data when Firefox is closed"
4. Disable "Ask to save passwords" (use a dedicated password manager instead)
5. Under Address Bar, disable all suggestions except Bookmarks

**Step 3: Install Essential Extensions**
| Extension | Purpose |
|-----------|---------|
| [uBlock Origin](https://addons.mozilla.org/firefox/addon/ublock-origin/) | Blocks ads, trackers, malware domains |
| [Multi-Account Containers](https://addons.mozilla.org/firefox/addon/multi-account-containers/) | Isolates browsing sessions (work, research, personal) |
| [LocalCDN](https://addons.mozilla.org/firefox/addon/localcdn/) | Serves common libraries locally, prevents CDN tracking |

**Note:** HTTPS Everywhere is no longer needed—Firefox enforces HTTPS by default since version 91.

**Step 4: Harden about:config (Optional)**
Type `about:config` in the address bar and modify:

```
privacy.resistFingerprinting = true          # Reduces fingerprinting surface
privacy.trackingprotection.enabled = true    # Force tracking protection
geo.enabled = false                          # Disable geolocation
media.peerconnection.enabled = false         # Disable WebRTC (prevents IP leaks)
dom.battery.enabled = false                  # Hide battery status
```

**Warning:** `privacy.resistFingerprinting` may break some websites. Disable it temporarily if needed.

### Alternative: Mullvad Browser

For higher-threat research, consider [Mullvad Browser](https://mullvad.net/browser)—a Firefox fork hardened by the Tor Project team, designed to make all users look identical.

- Pre-configured with anti-fingerprinting
- No account or Mullvad VPN subscription required
- Use for sensitive searches where you want maximum anonymity without Tor's speed penalty

---

## Layer 2: VPN + Tor

**Protects against:** ISP surveillance, network-level tracking, geographic correlation, some forms of censorship

**When to use:** Researching sensitive topics, accessing blocked resources, protecting your IP from websites you visit

### VPN Selection Criteria

Not all VPNs are trustworthy. Prioritize:

1. **No-logs policy** (audited, not just claimed)
2. **Anonymous payment** (cash, crypto)
3. **Jurisdiction** (outside Five Eyes preferred, but less important than audit history)
4. **Open-source clients** (auditable code)

**Recommended providers:**
| Provider | Notes |
|----------|-------|
| [Mullvad](https://mullvad.net) | Gold standard. Account numbers only, accepts cash. €5/month. |
| [ProtonVPN](https://protonvpn.com) | Swiss jurisdiction, free tier available, integrates with ProtonMail |
| [IVPN](https://ivpn.net) | Similar to Mullvad, smaller but reputable |

**Avoid:** Free VPNs (you're the product), VPNs with aggressive marketing, anything claiming "military-grade encryption."

### VPN Setup

1. Create account (use email alias or none if provider allows)
2. Download official client from provider's website (not app stores if possible)
3. Enable kill switch (blocks internet if VPN drops)
4. Enable DNS leak protection
5. Connect before starting sensitive work

### Tor Browser

Tor routes your traffic through three relays, making it extremely difficult to trace back to you.

**When to use Tor:**
- Researching topics that could flag you (ICE operations, police misconduct, surveillance vendors)
- Accessing .onion sites
- When you need stronger anonymity than a VPN provides

**Setup:**
1. Download ONLY from [torproject.org](https://www.torproject.org/)
2. Verify the signature (instructions on download page)
3. Don't install additional extensions (breaks anonymity)
4. Don't maximize the window (fingerprinting vector)
5. Don't torrent or use for large downloads (overloads the network)

### VPN + Tor: When and How

**VPN → Tor (You → VPN → Tor → Internet)**
- Your ISP sees VPN traffic, not Tor
- VPN provider sees you connecting to Tor
- Use when: Tor is blocked, or you don't want ISP to know you use Tor

**Tor → VPN (You → Tor → VPN → Internet)**
- More complex, requires VPN provider that accepts Tor connections
- Exit node sees VPN traffic
- Rarely needed for most users

**For most community research:** VPN alone is sufficient. Add Tor for sensitive searches.

---

## Layer 3: Virtual Machines

**Protects against:** Malware, forensic analysis, cross-contamination between activities, targeted exploits

**When to use:**
- Handling untrusted files (PDFs from CORA requests, documents from unknown sources)
- Deep OSINT research where you might encounter malicious content
- Creating isolated environments for different projects

### Understanding VMs

A virtual machine is a computer running inside your computer. If the VM gets compromised, your host system stays clean. If your laptop is seized, encrypted VMs add another layer of protection.

### VirtualBox Setup (Free, Cross-Platform)

**Step 1: Install VirtualBox**
- Download from [virtualbox.org](https://www.virtualbox.org/)
- Linux: Also available via package managers (`apt install virtualbox`)

**Step 2: Create a VM**
1. Click "New"
2. Name your VM (e.g., "Research-VM")
3. Select OS type (Linux/Debian for Kali, Linux/Ubuntu for general use)
4. Allocate resources:
   - RAM: 4GB minimum, 8GB recommended
   - Storage: 40GB+ (dynamically allocated saves space)
5. Create the VM

**Step 3: Install the OS**
1. Download your chosen ISO
2. In VM settings → Storage → Add optical drive → Select ISO
3. Start VM and follow installation prompts

### Recommended VMs by Use Case

| Use Case | Recommended VM | Why |
|----------|----------------|-----|
| **General research** | Ubuntu or Linux Mint | User-friendly, stable, familiar interface |
| **OSINT investigations** | [TraceLabs OSINT VM](https://github.com/tracelabs/tlosint-vm) | Pre-configured with 100+ OSINT tools |
| **Security testing** | [Kali Linux](https://www.kali.org/) | Industry standard for security research |
| **Maximum isolation** | [Whonix](https://www.whonix.org/) | Routes everything through Tor, two-VM architecture |
| **Disposable sessions** | [Tails](https://tails.net/) | Amnesic—leaves no trace (boot from USB, not VM) |

### TraceLabs OSINT VM Setup

TraceLabs is purpose-built for missing persons investigations and OSINT research.

1. Download the OVA file from [TraceLabs GitHub](https://github.com/tracelabs/tlosint-vm)
2. In VirtualBox: File → Import Appliance → Select the OVA
3. Adjust resources if needed (4GB+ RAM recommended)
4. Boot and explore the pre-installed tools

**Key tools included:**
- Maltego (relationship mapping)
- Recon-ng (reconnaissance framework)
- theHarvester (email/subdomain enumeration)
- Spiderfoot (automated OSINT)
- Social media analysis tools

### Kali Linux Setup

For security research and network analysis:

1. Download ISO from [kali.org](https://www.kali.org/get-kali/)
2. Create new VM (Debian 64-bit, 4GB+ RAM, 40GB+ storage)
3. Boot from ISO, select "Graphical Install"
4. Post-install:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install virtualbox-guest-x11  # Better VM integration
```

### VM Security Practices

- **Snapshot before risky operations** — Revert if something goes wrong
- **Don't share folders with host** unless necessary — Creates attack surface
- **Use NAT networking** for isolation, **Bridged** only when you need local network access
- **Encrypt the VM disk** — VirtualBox supports this in settings
- **Delete VMs when done** with sensitive projects — Don't let evidence accumulate

---

## Layer 4: Hardware Security (Mudi Router + GrapheneOS)

**Protects against:** Network-level attacks, IMSI catchers, device seizure, location tracking via home IP

**When to use:** Field deployment (protests, documentation), travel, when you need a clean network identity

### GL.iNet Mudi Router

The Mudi (GL-E750) is a portable 4G router that creates a secure network bubble around your devices.

**Why it matters:**
- All your devices connect through VPN automatically
- Your phone's real IMEI/IMSI never touches the cell network directly
- Portable—fits in a pocket, runs on battery
- Can run Tor as a transparent proxy

**Setup:**

1. **Purchase:** [GL.iNet store](https://www.gl-inet.com/products/gl-e750-mudi/) (~$200 with modem)

2. **Initial Configuration:**
   - Insert SIM card (prepaid, cash-purchased recommended)
   - Power on, connect to "GL-E750-xxx" Wi-Fi (default password on device)
   - Navigate to `192.168.8.1` in browser
   - Set admin password (NOT the default)

3. **Configure VPN:**
   - Go to VPN → WireGuard Client (or OpenVPN)
   - Upload your VPN provider's config file
   - Enable "VPN Policy" to force all traffic through VPN
   - Enable kill switch

4. **Firmware Updates:**
   - Check System → Upgrade for latest firmware
   - Consider flashing OpenWrt for advanced features

### Blue Merle: IMEI/MAC Randomization

[Blue Merle](https://github.com/srlabs/blue-merle) is an add-on package that randomizes your Mudi's cellular identifiers, making it harder to track.

**What it does:**
- Randomizes IMEI on each boot or on-demand
- Randomizes MAC address
- Helps prevent cell tower correlation attacks

**Installation:**

1. SSH into your Mudi:
```bash
ssh root@192.168.8.1
# Password is your admin password
```

2. Download and install:
```bash
cd /tmp
wget https://github.com/srlabs/blue-merle/releases/latest/download/blue-merle.ipk
opkg install blue-merle.ipk
```

3. Use the physical toggle switch on the Mudi, or access via LuCI web interface to randomize identifiers

**Note:** Changing IMEI may be illegal in some jurisdictions. Research your local laws.

### GrapheneOS (Hardened Android)

For a fully hardened mobile setup, pair the Mudi with a GrapheneOS phone.

**What it provides:**
- Hardened Android without Google services
- Per-app network permissions
- Sandboxed Google Play (if needed) without system-level access
- Verified boot, exploit mitigations

**Supported devices:** Pixel phones only (Pixel 6 and newer recommended)

**Installation:** Follow the [official web installer](https://grapheneos.org/install/web)

**Field kit combination:**
- GrapheneOS Pixel (no SIM, or prepaid SIM)
- Connected to Mudi router (VPN-tunneled 4G)
- Blue Merle randomizing cellular identifiers
- Result: Hardened device on anonymized network

See also: [GrapheneOS Mudi Field Kit](../comms/GrapheneOS%20Mudi%20Field%20Kit.md) for detailed deployment guide.

---

## Layer 5: Secure Communications

**Protects against:** Message interception, metadata analysis, account compromise

**When to use:** Coordinating with others, sharing sensitive findings, organizing

### Signal Messenger

Signal is the gold standard for secure messaging—end-to-end encrypted, open source, metadata-minimized.

**Setup:**

1. Install from [signal.org](https://signal.org/) (not third-party app stores)
2. Register with a phone number (consider a VoIP number for additional separation)
3. Set a PIN (Settings → Account → Signal PIN)
4. Enable registration lock (prevents SIM-swap attacks)

**Best Practices:**

| Setting | Recommendation |
|---------|----------------|
| Disappearing messages | Enable by default (1 week or less for sensitive groups) |
| Screen lock | Enable (Settings → Privacy → Screen Lock) |
| Relay calls | Enable to hide IP from callers |
| Link previews | Disable |
| Read receipts | Disable for sensitive contacts |

**Group Security:**
- Vet members before adding to sensitive groups
- Use invite links sparingly (disable after recruiting)
- Consider separate groups for different trust levels
- Admins should enable "Admin approval" for new members

**Operational Discipline:**
- Don't screenshot sensitive messages
- Don't forward messages without consent
- Don't discuss Signal groups on other platforms
- Have a code word for "I'm compromised, ignore future messages"

### Obsidian for Secure Notes

[Obsidian](https://obsidian.md/) is a local-first note-taking app perfect for research documentation.

**Why Obsidian:**
- Notes stored locally as plain Markdown files
- No account required
- Works offline
- Can be synced via encrypted methods

**Security Setup:**

1. Install from [obsidian.md](https://obsidian.md/)
2. Create vault in an encrypted location (Cryptomator, VeraCrypt, or encrypted home folder)
3. Don't use Obsidian Sync for sensitive vaults—use encrypted alternatives:
   - [Syncthing](https://syncthing.net/) (P2P, encrypted in transit)
   - [Cryptomator](https://cryptomator.org/) + any cloud provider
   - Local-only (no sync)

**This repository is an Obsidian vault.** Open the `laraza` folder in Obsidian to get linked notes, graph view, and full navigation.

---

## Practical Workflows

### Workflow: Researching a City Agenda Item

**Scenario:** You want to research a surveillance vendor mentioned in an upcoming city council agenda.

1. **Layer 1:** Use hardened Firefox with containers
   - Create a "Research" container for this session
   - Search for vendor name, contracts, news coverage

2. **Layer 2:** If researching sensitive vendors (Palantir, ICE contractors):
   - Enable VPN before searching
   - Consider Tor Browser for vendor websites that might log visitors

3. **Documentation:**
   - Save findings to Obsidian vault
   - Screenshot relevant pages (metadata-strip before sharing)
   - Log sources in your research notes

4. **Sharing:**
   - Share findings via Signal, not email
   - Use disappearing messages for draft discussions

### Workflow: Documenting a Protest

**Scenario:** You're doing legal observation at a protest.

1. **Hardware:**
   - GrapheneOS phone or dedicated burner
   - Connected via Mudi router (VPN active, Blue Merle randomized)
   - Leave personal phone at home or in Faraday bag

2. **During event:**
   - Document via camera (not social media apps)
   - Note badge numbers, timestamps, locations
   - Don't livestream directly—record, then upload later

3. **After event:**
   - Transfer footage to encrypted storage
   - Strip metadata before sharing
   - Upload from coffee shop or library (not home)
   - Coordinate via Signal about what to publish

4. **If device seized:**
   - GrapheneOS has duress PIN option (wipes device)
   - Mudi can be wiped by holding reset button
   - Know your rights: [Legal Observer Toolkit](../opsec/Legal%20Observer%20Toolkit.md)

### Workflow: CORA/FOIA Research

**Scenario:** You're requesting surveillance contracts via Colorado Open Records Act.

1. **Submitting request:**
   - Use Layer 1 (hardened browser) for the request form
   - Consider using a pseudonym + separate email if allowed
   - VPN recommended to avoid IP logging

2. **Receiving documents:**
   - Open in a VM—PDFs can contain malware or tracking
   - TraceLabs or Ubuntu VM recommended
   - Extract text, analyze in isolated environment

3. **Storing findings:**
   - Move sanitized data to main system
   - Document in Obsidian with source citations
   - Add to `logs/source_index.md` for this repository

4. **Sharing:**
   - Redact any private individual information
   - Run through `logs/safety_ethics_review.md` checklist
   - Publish or share via secure channels

---

## Quick Reference

| Need | Solution |
|------|----------|
| Basic privacy for daily browsing | Hardened Firefox + uBlock Origin |
| Hide IP from websites | VPN (Mullvad, ProtonVPN) |
| Maximum anonymity | Tor Browser |
| Handle untrusted files | Virtual Machine (Ubuntu, TraceLabs) |
| Field deployment | Mudi router + GrapheneOS |
| Secure messaging | Signal with disappearing messages |
| Research documentation | Obsidian in encrypted vault |
| Protest documentation | Full stack: GrapheneOS → Mudi → VPN → encrypted storage |

---

## Additional Resources

**In this repository:**
- [Pueblo 81008 Surveillance Memo](../opsec/Pueblo%2081008%20Surveillance.md) — Local threat landscape
- [GrapheneOS Mudi Field Kit](../comms/GrapheneOS%20Mudi%20Field%20Kit.md) — Detailed hardware setup
- [Digital Hygiene for Everyday People](Digital%20Hygiene%20for%20Everyday%20People.md) — Beginner-friendly overview
- [Surveillance Counter-Measures](Surveillance%20Counter-Measures.md) — Advanced techniques
- [Data Broker Opt-Out Guide](Data%20Broker%20Opt-Out%20Guide.md) — Reduce your exposure

**External:**
- [EFF Surveillance Self-Defense](https://ssd.eff.org/) — Comprehensive guides
- [Privacy Guides](https://www.privacyguides.org/) — Tool recommendations
- [PRISM Break](https://prism-break.org/) — Alternative software suggestions

---

*Security is a practice, not a product. Start with Layer 1, add layers as needed, and maintain discipline across all of them.*
