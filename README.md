<p align="center" width="100%">
    <img width="25%" src="assets/asset1.png"> 
</p>

# La Raza VII.I.IX - A Field Guide on Open Source Intelligence (OSINT) and Technology Primers
This project equips community journalists, activists, and engaged citizens with the tools, techniques, and knowledge for effective open-source research and secure technology practices, fostering resilience and informed action. It also serves as a research log for secure communication methodologies, independent analysis of community issues, and the development of accessible tech solutions to empower all.

For all of our family.

## Table of Contents
- [Purpose](#purpose)
- [Disclaimer](#disclaimer)
- [How to Use This Repo](#how-to-use-this-repo)
- [Repository Structure](#repository-structure)
- [Pueblo 81008 Field Priorities](#pueblo-81008-field-priorities)
- [Data & Map Outputs](#data--map-outputs)
- [Field Use: Protest & Outreach Protection](#field-use-protest--outreach-protection)

---

## Purpose
In today’s digital landscape, privacy and operational security (OPSEC) are more important than ever. This guide will walk you through practical steps to secure your devices, communications, and data, ensuring that your online presence remains as private as possible. This is a field guide covering as much ground as we can, and attempting to distill it to the level anyone can use.

## Disclaimer
This project is worked on over time and space; while workflow guides may be shared, the world continues to evolve at light speed. Some information may be outdated by the time you see it, some techniques may be compromised by the time you use them, and some information may just be completely wrong. The goal here is to plant seeds for trees to grow from; learn, trust, but verify.

## How to Use This Repo
1. Clone this repo
```
git clone https://github.com/samedayhurt/laraza.git
```
2. Open as vault using [Obsidian](https://obsidian.md/)
3. Make edits and notes to make this guide your own

## Repository Structure
- **[Primers](primers/README.md):** Fast-start guides for Linux, direction finding, virtual machines, and other fundamentals.
- **[Secure Communication Techniques](comms/README.md):** Living playbooks for digital + RF channels, plus workflows like [Strong & Anonymous File Sync](comms/e2eefilechange.md) and the new [`GrapheneOS Mudi Field Kit`](comms/GrapheneOS%20Mudi%20Field%20Kit.md).
- **[Operational Security](opsec/README.md):** Threat-model worksheets, daily discipline checklists, Pueblo-specific legal observer workflows, and source vetting procedures aimed at civilians rather than military units.
- **[Non-Standard Communications](comms/nscomms.md)** & **[Direction Finding](primers/Direction%20Finding%20(Wi-Fi).md):** Specialized research threads that support Pueblo-focused investigations and counter-surveillance scouting.
- **[Pueblo 81008 Surveillance Memo](opsec/Pueblo%2081008%20Surveillance.md):** Political landscape notes, RTCC inventory, commercial telemetry analysis, police-abuse reporting routes, ICE collaboration research, and “5-minute” action blocks.
- **[Pueblo County Officials](opsec/Pueblo%20County%20Officials.md):** Quick reference on which party controls each county office plus the business ties and high-stakes decisions tied to those officials, paired with the new [`Legal Observer Toolkit`](opsec/Legal%20Observer%20Toolkit.md) for documentation escalations.
- **[Scripts](scripts/):** Automation such as `build_pueblo_map.py` to regenerate the folium overlay without external GIS tools.

## Pueblo 81008 Field Priorities
- **Political control:** Use `opsec/Pueblo County Officials.md` before outreach meetings to surface conflicts of interest (e.g., Republic Shooting Range co-ownership, sheriff lawsuits) and align campaigns with the right office.
- **Surveillance stack:** `opsec/Pueblo 81008 Surveillance.md` consolidates RTCC tooling, Community Connect tactics, ALPR corridors, and now Pueblo-specific police abuse + ICE reporting workflows.
- **Rapid protest comms:** `comms/GrapheneOS Mudi Field Kit.md` adapts DSOK’s GrapheneOS router workflow for medics, scouts, and legal observers who need hardened connectivity in 81008 without touching personal SIMs.
- **Accountability escalations:** The surveillance memo now points directly to Pueblo PD Internal Affairs forms, Colorado POST certification complaints, the Attorney General’s pattern-and-practice form, and Colorado Rapid Response Network (CORRN) hotline instructions so community members can escalate abuse or ICE sightings immediately.

## Data & Map Outputs
- **`data/pueblo_apparatus.geojson`** — working GeoJSON covering the 81008 boundary approximation, RTCC, downtown Flock ALPR zone, and Pueblo Mall security footprint.
- **`docs/maps/pueblo-surveillance-map.html`** — editable folium map (GitHub Pages friendly) driven by the GeoJSON to visualize sensors and political targets along march routes. A static preview (`docs/maps/pueblo-surveillance-map.png`) now lives alongside it for README embeds.
- **[`docs/pueblo-watchlist.md`](docs/pueblo-watchlist.md)** — rolling agenda/procurement tracker so you can match surveillance votes to the officials and business ties documented in `opsec/`.
- **`scripts/build_pueblo_map.py`** — regenerates the HTML overlay whenever the GeoJSON changes so everyone shares the same situational awareness.

<p align="center">
  <img src="docs/maps/pueblo-surveillance-map.png" alt="Pueblo surveillance apparatus map preview" width="70%">
</p>

## Field Use: Protest & Outreach Protection
- **Primers** help field researchers and volunteer medics spin up clean laptops/VMs before deployments so seized gear can’t reveal networks.
- **Secure Communication Techniques + Non-Standard Comms** pair encrypted drops (Tor + gocryptfs) with LoRa/APRS redundancies for marches where cell service or legal protections collapse.
- **GrapheneOS + Mudi kit** (documented under Comms & OPSEC) gives you a travel router + hardened phone chain so you can uplink livestreams or legal updates without exposing your home IP.
- **Operational Security** translates DSOK lessons to civilian teams: build threat models per action, enforce compartmentalized personas, and keep source notes in encrypted Obsidian vaults.
- **Pueblo 81008 memo/map** shows where surveillance infrastructure lives (RTCC feeds, Flock cameras) so organizers can plan ingress/egress routes that avoid persistent monitoring.
- **Pueblo County Officials guide** surfaces which electeds own businesses or make policy decisions affecting protest permits, jail funding, or public-records access—fuel for research requests and accountability campaigns.

When in doubt, start with the folder README to understand how each section is meant to be used in the field.
## Installing Virtual Machines
Setting up virtual machines (VMs) is a foundational step for security professionals. Here’s how to install and configure some of the most important VMs for privacy-focused operations.

### Kali Linux
Kali Linux is a powerful platform for penetration testing and ethical hacking.
1. **Download and install VirtualBox** or another hypervisor.
2. **Download Kali Linux ISO** from the [official site](https://www.kali.org/downloads/).
3. Create a new VM in VirtualBox and allocate resources.
4. Follow the installation prompts and configure the system.

More in depth
#### Setting Up Kali Linux VM
1. **Download VirtualBox** from [virtualbox.org](https://www.virtualbox.org/).
2. **Download the Kali Linux ISO** from [kali.org](https://www.kali.org/downloads/).
3. **Create a New VM in VirtualBox**:
   - Name: Kali Linux
   - Type: Linux, Version: Debian (64-bit)
4. **Configure Resources**:
   - RAM: Minimum 2GB (Recommended 4GB+)
   - Storage: 20GB or more
5. **Install Kali Linux**:
   - Boot the VM with the ISO and follow the installation prompts.
6. **Post-Installation**:
   - Update the system: `sudo apt update && sudo apt upgrade -y`
   - Install essential tools: `sudo apt install build-essential`

### TraceLabs VM
TraceLabs is used for OSINT and investigative work.
1. Head to the [TraceLabs GitHub page](https://github.com/tracelabs) to download the pre-configured VM.
2. Set it up in VirtualBox similarly to Kali.
3. Follow their installation and configuration steps to get started.
More in depth
#### Setting Up TraceLabs VM
1. **Download the TraceLabs OSINT VM** from their [GitHub repository](https://github.com/tracelabs).
2. **Install VirtualBox** if not already installed.
3. **Create a New VM**:
   - Import the TraceLabs VM file (usually a `.ova` or `.vdi` file).
   - Allocate sufficient resources (2GB+ RAM, 20GB+ storage).
4. **Configure Networking**:
   - Set network mode to "Bridged" or "NAT" depending on the requirement.
5. **Run the VM** and explore the pre-configured OSINT tools.

## Hardening Your Browser
Your web browser is often the first line of defense against attacks. Below are steps to make your browsing experience more secure, focusing on Firefox.

### Firefox Security
1. **Install Privacy-Focused Add-ons**:
   - uBlock Origin
   - HTTPS Everywhere
   - Privacy Badger
   - NoScript
2. **Configure Enhanced Tracking Protection**: 
   - Go to `about:preferences#privacy` and set to “Strict.”
3. **Disable Telemetry and Data Collection**:
   - Navigate to `about:config` and disable the following:
     - `datareporting.healthreport.uploadEnabled`
     - `toolkit.telemetry.enabled`
     - `browser.safebrowsing.malware.enabled`

More in depth
#### Hardening Firefox
1. **Install Security Add-ons**:
   - uBlock Origin: Blocks unwanted ads and trackers.
   - HTTPS Everywhere: Enforces HTTPS on supported websites.
   - Privacy Badger: Stops trackers that monitor your browsing.
   - NoScript: Blocks potentially harmful scripts.
   
   Install from the [Firefox Add-ons site](https://addons.mozilla.org/).

2. **Enable Strict Tracking Protection**:
   - Go to `Settings` > `Privacy & Security` > **Enhanced Tracking Protection** > Set to **Strict**.

3. **Disable Data Collection**:
   - Type `about:config` in the address bar.
   - Search for and disable:
     - `telemetry.enabled`
     - `datareporting.healthreport.uploadEnabled`
     - `browser.safebrowsing.malware.enabled`

4. **Disable WebRTC to Prevent IP Leaks**:
   - Search for `media.peerconnection.enabled` in `about:config` and set to `false`.

5. **Use a Secure Search Engine**:
   - Set your default search engine to [DuckDuckGo](https://duckduckgo.com/) or [Startpage](https://www.startpage.com/).

## Using Tor and a VPN
For an extra layer of anonymity, using Tor in combination with a VPN ensures that your online activity is harder to trace.

1. **Install a VPN**: Choose a no-logs VPN provider like Mullvad or ProtonVPN.
2. **Set up Tor Browser**: Download from the [official Tor Project site](https://www.torproject.org/).
3. **Configure VPN with Tor**: Start your VPN first, then launch Tor Browser to maximize privacy.

More in depth
#### Using Tor with a VPN
1. **Choose a No-Logs VPN**:
   - Examples: Mullvad, ProtonVPN, or NordVPN.
2. **Install the VPN Client**:
   - Connect to a VPN server. Ensure no-logs policy and leak protection are enabled.
3. **Download Tor Browser** from the [Tor Project](https://www.torproject.org/).
4. **Connect VPN, then Launch Tor**:
   - Start the VPN first, then open Tor Browser. This setup hides your IP from both the VPN provider and Tor entry nodes.
5. **Testing Your Connection**:
   - Use [check.torproject.org](https://check.torproject.org/) to ensure you are connected to the Tor network.

## Mudi Router and Blue Merle
These hardware devices provide an additional layer of network security and anonymity.

### Buying and Using the Mudi Router
1. Purchase a Mudi router from [GL.iNet](https://www.gl-inet.com/products/gl-e750-mudi/).
2. **Set up OpenVPN/WireGuard** on the Mudi to route all traffic through a secure tunnel.
3. **Configure Firewall and Adblock**: Enhance security by blocking unwanted traffic.

More in depth

#### Setting Up Mudi Router
1. **Purchase and Power On**:
   - Get the Mudi Router from [GL.iNet](https://www.gl-inet.com/products/gl-e750-mudi/).
2. **Log into the Web Interface**:
   - Default IP: `192.168.8.1`
   - Default Login: `admin/admin`
3. **Configure OpenVPN/WireGuard**:
   - Upload your VPN provider's configuration file.
   - Start the VPN connection from the dashboard.
4. **Enable Adblock**:
   - In the web interface, go to **Applications** > **Adblock** and turn it on.
5. **Firmware Updates**:
   - Check for and install the latest firmware updates for security improvements.
6. **Blue Merle**:
   - Consider installing the opkg for [srlabs blue-merle](https://github.com/srlabs/blue-merle)
   - SSH into Mudi router (root@192.168.8.1) with your admin login password
   - scp blue-merle to the Mudi device (follow instructions on the repo)
   - Utilize the toggle on devie, or LuCi web interface to roll IMEI and MAC address for your operational needs

## Generational Operational Security
OPSEC isn't just a one-time thing; it's something you need to maintain consistently, across different tools and platforms.

### Signal Messenger
1. Install Signal from [Signal.org](https://signal.org/).
2. **Use disappearing messages** and **secure backups** for all conversations.
3. **Vetting Members**: Make sure to vet group chat members for security, especially when working in sensitive environments.
More, in depth
#### Signal Setup and Best Practices
1. **Install Signal** on your mobile or desktop device from [signal.org](https://signal.org/).
2. **Use Disappearing Messages**:
   - In any conversation, go to `Settings` > `Disappearing Messages` and set a timer (e.g., 1 day).
3. **Secure Backups**:
   - Encrypt Signal backups and store them in a secure location.
4. **Vet Group Members**:
   - When creating Signal groups, ensure members are trusted and vetted to avoid leaks.

### Analyst Notebook
For intelligence gathering and visualization:
1. Use IBM Analyst Notebook to map out complex data and relationships.
2. Ensure that all sensitive information is stored securely using encrypted databases.

More in depth
#### Using IBM Analyst Notebook
1. **Install IBM Analyst Notebook**:
   - Obtain from IBM’s official site.
2. **Create a Secure Workspace**:
   - Use encrypted storage for data files.
3. **Map Relationships**:
   - Use visualizations to track connections between people, locations, and events.
4. **Export Securely**:
   - Export visualizations and data to encrypted formats for safe sharing.

### Obsidian for Secure Notes
1. Install [Obsidian](https://obsidian.md/).
2. **Enable local encryption** for vaults and use it to take private, organized notes.
3. Sync notes securely using encryption-friendly cloud services.
