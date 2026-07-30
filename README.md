<p align="center" width="100%">
    <img width="25%" src="assets/asset1.png">
</p>

# La Raza VII.I.IX - A Field Guide on Open Source Intelligence (OSINT) and Technology Primers
This project equips community journalists, activists, and engaged citizens with the tools, techniques, and knowledge for effective open-source research and secure technology practices, fostering resilience and informed action. It also serves as a research log for secure communication methodologies, independent analysis of community issues, and the development of accessible tech solutions to empower all.

For all of our family.

---

## Pueblo Surveillance Apparatus Map

<p align="center">
  <a href="docs/maps/pueblo-map-public.html">
    <img src="docs/maps/pueblo-surveillance-map.png" alt="Pueblo, CO Surveillance Infrastructure Map - RTCC, ShotSpotter, ALPRs, ICE watch sites, and community resources" width="90%">
  </a>
</p>

<p align="center"><em>Click to open the dark-mode public map (search + layer toggles) served via GitHub Pages.</em></p>

**GitHub Pages landing (public):** https://samedayhurt.github.io/laraza/  
**Direct map URL:** https://samedayhurt.github.io/laraza/docs/maps/pueblo-map-public.html  
**Offline fallback (existing Folium build):** docs/maps/pueblo-surveillance-map.html

### How to use the map
- Open `docs/maps/pueblo-surveillance-map.html` in your browser (or via GitHub Pages if enabled).
- Toggle layers (e.g., RTCC, ALPR, drones, parks, community support) with the layer control; markers are clustered for dense areas.
- Click any pin to see description plus linked sources; polygons/lines show coverage areas like ShotSpotter or ALPR corridors.
- Regenerate after data changes with `.venv/bin/python scripts/build_pueblo_map.py` (folium already installed in `.venv`).

---

## Latest Updates (July 2026)

*Full research refresh 2026-07-29, **re-audited 2026-07-30**. Closes the Feb 18 → Jul 29 gap. Per-task log in `logs/search_log.md`; citations in `logs/source_index.md`; ethics sign-off in `logs/safety_ethics_review.md`.*

> ### 📐 New: claims in this repo are now tiered
>
> A July 30 re-audit found this project had been stating claims of very different evidentiary weight in the same flat, confident voice — which is how a **debunked** Flock→Palantir diagram survived here for months, and how the maintainer introduced a *fresh* overstatement while fixing it. **`docs/data-legend.md` §0 now defines verification tiers [A]–[E]** and the rules that follow from them: give the base rate, never sum unreconciled figures, absence of evidence is not evidence, and never claim a legal protection doesn't exist without checking statutes still in force.
>
> **Four claims published on July 29 were walked back on July 30** — the Cloudrunner recency implication, the DCJ "RTCC study" headline, the ShotSpotter 83% figure, and the PCSO framing. Details in each section below. **`reports/surveillance_and_policing_risks.md` §8 now lists every unreconciled number, and §9 lists what this research still does not know** — including the biggest gap of all: **nobody has ever asked how many private cameras are enrolled in Community Connect**, which is the entire consent question.

### 🛑 Read this first: two things in this repo were wrong in ways that mattered

**1. Agenda monitoring had never actually monitored anything.** `scripts/monitor_agendas.py` was scraping `pueblo.us/Archive.aspx?AMID=37` — a **defunct** archive whose newest item is **May 2022**. The PDFs it collected were from **2012–2013**. The Feb 18, 2026 note in this README saying "the latest City Council agenda contained no surveillance/ICE/civil-liberties items" described `city_council-626.pdf`, which is the **January 14, 2013** agenda. **That all-clear was false.** Nothing from Feb–Jul 2026 had ever been scanned.

Fixed: Pueblo has migrated to **CivicClerk**, which exposes an unauthenticated OData API for both bodies. Now wired in via `scripts/pueblo_sources.py`. The monitor **exits `3` and prints a banner** when a source is stale or empty, `weekly_monitor.sh` no longer prints "all clear" in that case, and `docs/agenda_alerts.md` now carries a **Source Status** table. An empty scan is only meaningful if the source is proven fresh.

**2. A hijacked domain sat in the domestic-violence referral path.** `ywcapueblo.org` — the stored website for Mariposa Center for Safety — has been released and now **301-redirects to a political campaign donation site**. It was rendering as a clickable link in the public map's popups. Purged everywhere; map GeoJSON re-embedded. The crisis line **719-545-8195** is unchanged and correct. Separately, the resources guide carried a **wrong DV crisis number** (719-545-4884), and Health Solutions' crisis address *and* phone were both wrong.

### State legislation: every guardrail failed

All three bills Pueblo City Council voted to oppose on Feb 9, 2026 are **dead**. Colorado adjourned sine die May 13, 2026 with **no ALPR statute, no law-enforcement surveillance statute, and no ban on government purchase of third-party data.**

| Bill | Outcome |
| --- | --- |
| **SB26-070** ("PEEPS Act") | Cleared two committees, then **sponsors pulled it at Second Reading Apr 29** under a veto threat. Sen. Amabile: *"We didn't have the votes."* |
| **SB26-071** ("SAFE Act") | **Postponed indefinitely 6–1**, Senate Judiciary, May 6. Would have required a warrant for facial recognition generally; **SB22-113 (2022) still requires one only for *real-time* identification**, so retrospective FR searches remain unwarranted. |
| **HB26-1037** (data brokers) | **Died by one vote, twice, in one day** (House Judiciary, Apr 22). The bill Pueblo called *"harmful to public safety"* — and the closest to passing. **Highest-leverage 2027 target.** |

Consequence: every constraint on Pueblo's RTCC stack is now **local and discretionary**. Two laws that *did* pass do bind local agencies and create new obtainable documents — **HB26-1123** (body-cam recording of jail strip searches + annual AG report, eff. May 27) and **HB26-1276** (AG-set PII-sharing policy, eff. Aug 12).

### Surveillance: the build-out is bypassing council

- **City Council, July 27, 2026, item N3** — a **$275,384 Colorado DCJ grant** (project PS2509), verified in the packet. Three findings, in descending order of how much weight they can bear:
  - **[A] Solid: PPD was added as one of five new DOJ National Public Safety Partnership (PSP) sites**, administered by BJA, which puts federal consultants inside PPD operations. This relationship appears nowhere else in the repo. **Establish what data flows through it.**
  - **[A] Solid: [SB22-113](https://leg.colorado.gov/bills/sb22-113)** (2022, still in force) requires a **public notice of intent, an accountability report, and a warrant for real-time identification** before any agency use of facial recognition. **No Pueblo filing has been found, and a notice of intent is a public record — the cheapest early-warning tripwire on this whole stack.**
  - ⚠️ **Weaker than I first reported: the "RTCC study" line.** The packet does say *"The subject matter of research will be a comprehensive study of the Real Time Crime Center"* — but **the immediately preceding sentence says the research partner is being sought "to study effects of the CIT program,"** and the entire surrounding grant is a **Crisis Intervention Team co-responder award** (Health Solutions MOU, HIPAA, 42 CFR Part 2, detox and crisis services). The RTCC sentence is most likely a **copy-paste artifact from a different application.** Still worth asking council about — it is in a signed city grant narrative — but **do not headline it as "the city is funding an RTCC study."**
  - ⚠️ **Also weaker than I first reported: grant conditions #26 (no drone spending) and #27 (facial recognition only with existing civil-liberties policies) are standard BJA award conditions, not Pueblo-specific.** Condition #27 is **not** evidence Pueblo plans to deploy facial recognition. It's still a usable hook — *if* the city ever spends this money on FRT it must already have a policy — but don't imply intent that isn't in the record.
- 🔴 **A SECOND ALPR SYSTEM the repo had no record of: ~70 Genetec Cloudrunner cameras, queried against CCIC and federal NCIC.** Running in parallel with Flock. **Retention, cost, placement, and written policy all undisclosed.**
  ⚠️ **Source is the vendor**, so scale is solid but **the deployment date is unknown** — these may have accumulated over years, which likely explains why zero Genetec ALPR procurement appears in 49 scanned 2026 agendas. **Don't say "they just installed 70 cameras."** Say: *roughly 70 ALPR cameras are operating that were never publicly accounted for, and the city hasn't disclosed when, at what cost, or with what retention.*
- ⚠️ **This repo cannot currently say how many ALPRs are in Pueblo.** Four unreconciled counts sit in these files — 22 fixed, ~70 Cloudrunner, 12 Flock, 73 PCSO mobile — and **they must not be added together.** Resolving that is now the single highest-value records request: ask the City and County separately for a full ALPR inventory by vendor, count, type, install date, and retention. See `reports/surveillance_and_policing_risks.md` §3.
- 🔴 **The ICE pathway is a toggle, not a leak.** EFF documented (June 2026) that an **ICE-populated NCIC "Immigration Violator" hotlist can be switched on inside Flock**, alerting in real time against ICE administrative warrants issued with **no judicial review**. **Pueblo has that mechanism on both Flock and Cloudrunner, and no one has asked whether it's on.** Note that disabling a vendor's national lookup is **not** sufficient — ATF searched Loveland's data for ICE, and an SFPD audit found 299 improper federal searches via a fusion center.
- **Pueblo PD is expanding to 12 Flock ALPR cameras** (4 live), 4 mobile trailers, and park cameras at Mitchell, Mineral Palace, City, and El Centro — with **no council authorization vote found anywhere in Feb–Jul 2026**, while the city lobbied against state ALPR regulation. Deputy Chief Jim Martin has publicly said a query audit log exists; **that makes it CORA-able.**
- **ShotSpotter now auto-launches a BRINC drone**, gated only by an operator feasibility check — no warrant, no independent review. ⚠️ **The alert-vs-911-call ratio is unreconciled** (7,715 detections/2,076 incidents for 2025 vs SoundThinking's 3,383 alerts/608 calls with no stated period) — **don't quote a percentage until the denominator is established.** The qualitative point holds: most drone-eligible triggers appear to be events no resident reported. PPD's public UAV page still describes a 2018 three-drone unit.
- **PCSO reported ZERO of 12 months of state-mandated use-of-force data for CY2024**; PPD reported 10/12 (9,244 contacts, 31 uses of force, 244.2 per 10k). Verified directly in the state PDF. **Give the base rate when using this — 59 of 235 agencies (25%) also reported nothing**, so PCSO isn't a unique outlier and framing it that way invites a one-line rebuttal. Still a documented compliance failure needing no CORA request, and the sheriff responsible just lost his primary.
- **Five Colorado cities cancelled Flock and seven restricted sharing; Pueblo did neither.** **Cañon City — 40 miles away — simply let its contract expire, with its own police chief citing "concerning data security."** That's the most transferable precedent available.
- **Correction to a claim this repo published:** the Palantir data-flow diagram in `opsec/Pueblo 81008 Surveillance.md` is **debunked** — there is no confirmed Flock–Palantir integration and the Thiel-owns-both claim is false (Colorado Sun fact-check, Feb 2026; Flock's trust page states it does not work with Palantir). Replaced with the documented NCIC→ICE-hotlist pipeline, which is better sourced and worse.
- **Notable negative:** a keyword scan of **49 real 2026 city and county agendas/packets** found **zero** genuine hits for Flock, ALPR, ShotSpotter, SoundThinking, Genetec, or Fusus. The ALPR build-out is not moving through either body — it runs on grants, the Downtown Association, vendor trials, or mayoral authority. **Stop watching only agendas.**
- Denver offers a template: its Flock contract carries a **$100k penalty** for federal immigration sharing, bars federal task-force officers, and disables Denver data in Flock's nationwide lookup. **Pueblo has no known equivalent.**

### ICE / immigration

- ***Ramirez Ovando v. Noem*** is **in force and has been enforced** — on **May 12, 2026** the court found ICE **"materially violated"** it and barred untrained officers from warrantless arrests. ⚠️ **It is on appeal** (10th Cir. 26-1027), undecided, no stay. **Cite it as in-effect-on-appeal, never as settled.**
- ***Noem v. Vasquez Perdomo*** (SCOTUS, Sept 2025) — a baseline gap the repo had missed entirely. Ethnicity, Spanish/accented English, location, and type of work may factor into reasonable suspicion for a **stop**. Both KYR handouts were rewritten; the old text implied protection that doesn't exist.
- **Sheriff Lucero lost the June 30, 2026 primary** to **Allen Medina**, who takes office **January 2027** unopposed. The ICE non-cooperation pledge this repo leans on belongs to an outgoing officeholder. **Medina has said nothing on the record about surveillance technology — get him on record before January.**
- **Walsenburg did NOT open** as ICE detention (JBC rejected the purchase Mar 31; zoning on the **Nov 3, 2026** ballot; capacity **752**, not 1,400). Capacity grew at **Hudson** instead — GEO won a **1,200-bed, five-year ICE contract on July 14, 2026**.
- **An unlisted ICE hold room serves the Pueblo area** (PUEHOLD): 315 people Jan–Oct 2025, stays of ~12/14/19 days, located **outside the city** near the Fremont County airport. **Absence from ICE's online locator is not evidence someone isn't detained.**

### Resources directory: verified, corrected, expanded 31 → 54

- **22 records corrected**, including the DV crisis number, Health Solutions' address *and* phone, the public defender's number, and Catholic Charities' Pueblo line.
- `data/resources_directory_structured.json` **had been invalid JSON since ~Jan/Feb 2026** (a `{` closed with `]`), so every downstream consumer had been silently failing to parse it for six months. Fixed.
- **23 new records.** The long-open **LGBTQ+ gap is closed** (Southern Colorado Equality Alliance + three recurring Pueblo-local groups). Added cooling refuge, bail, worker, food, utility, youth, veterans, and reentry entries.
- **13 entries could not be primary-verified** and are published under an explicit provisional warning rather than silently trusted. **ACOVA — a victim-services line in the emergency card whose domain no longer resolves — needs a human to call it.**
- Still structurally missing in Pueblo: no mutual aid network, no local bail fund, no worker center, no gender-affirming provider, no official cooling-center program, and **no under-18 emergency youth shelter**.

### Context

- **The $1.2B long rail mill opened July 16, 2026** under Atlas Holdings / Orion Steel (the EVRAZ era is over), ~1,000–1,300 jobs, on a 7-year Union Pacific contract.
- **Austerity on both sides:** city cut 7 positions, froze 25, and imposed a 15% operating cut against a **$10M 2027 deficit**; four 0.25% sales-tax questions go to the Nov 2026 ballot — **one is explicitly for "fire and city technology."** County faces ~$10.2M and imposed 10 unpaid furlough days. **Expect slower CORA responses.**
- ~**25% of Pueblo relies on SNAP** as federal work requirements land.
- **Two data corrections:** council is **7 seats (4 districts + 3 at-large)**, not "nine districts"; and the ACS-2022 ZIP poverty rates were mis-derived from a Census *count* column (`81005 = 40.08%` was impossible). Income deltas are reliable; those poverty deltas are not. Refreshed to **ACS 2024 5-year**.

**Stay safe. The times demand it.**

<details>
<summary><strong>Previous Updates (February 2026)</strong> — retained for provenance; see corrections above</summary>

**Surveillance Infrastructure Updates:**
- ShotSpotter coverage reported at ~6–7 sq mi (State of the City 2026); RTCC mobile camera trailers likely increased to 6 total; DFR drones remain active.
- Agenda monitoring refreshed (Feb 18, 2026): latest City Council agenda contained no surveillance/ICE/civil-liberties items; alerts logged in `docs/agenda_alerts.md`. — ⚠️ **FALSE.** The scanned file was the January 2013 agenda; the source had been dead since before this repo started monitoring.
- Surveillance data and risks report updated to reflect 2026 footprint and advocacy asks for coverage maps, trailer logs, and drone deployments.

**ICE / Immigration Updates:**
- Pueblo County Sheriff Lucero reaffirmed Jan 29, 2026: PCSO will not join ICE “roundups,” will only cooperate on criminal charges/officer safety; track jail-to-ICE detainers.
- Early 2026 reports show 104 ICE arrests statewide YTD; immigration risks report updated with context and the 2025 federal warrantless-arrest ruling.

**Resource Directory Updates:**
- SafeSide Recovery (Posada partner) added eight dorm-style units in Jan 2026, doubling 24/7 low-barrier shelter capacity in Pueblo.
- Resource guide and structured directory updated; keep intake details documented for follow-up.

**Data Flow & Tooling:**
- `monitor_agendas.py` + `download_agendas.py` remain the workflow for weekly agenda pulls; city agenda (Item 626) added to `docs/agendas/` for audit trail. — ⚠️ *Item 626 is the **January 14, 2013** agenda. This claim was void; see the July 2026 corrections above.*
- Safety/ethics review rerun (Feb 18, 2026): reports remain rights-focused, no private resident data exposed.

</details>

## Table of Contents
- [Pueblo Surveillance Apparatus Map](#pueblo-surveillance-apparatus-map)
- [Purpose](#purpose)
- [Disclaimer](#disclaimer)
- [How to Use This Repo](#how-to-use-this-repo)
- [Repository Structure](#repository-structure)
- [Pueblo 81008 Field Priorities](#pueblo-81008-field-priorities)
- [Data & Map Outputs](#data--map-outputs)
- [Roadmap: Guides & Self-Advocacy](#roadmap-guides--self-advocacy)
- [Field Use: Protest & Outreach Protection](#field-use-protest--outreach-protection)
- [Operational Security Layers](#operational-security-layers)

---

## Purpose
In today’s digital landscape, privacy and operational security (OPSEC) are more important than ever. This guide will walk you through practical steps to secure your devices, communications, and data, ensuring that your online presence remains as private as possible. This is a field guide covering as much ground as we can, and attempting to distill it to the level anyone can use.

## Disclaimer
This project is worked on over time and space; while workflow guides may be shared, the world continues to evolve at light speed. Some information may be outdated by the time you see it, some techniques may be compromised by the time you use them, and some information may just be completely wrong. The goal here is to plant seeds for trees to grow from; learn, trust, but verify.

## How to Use This Guide

This guide works **completely offline** once downloaded—no internet required. Choose the method that fits your comfort level:

---

### Option A: Read Online (Easiest)

Just browse this page. Click any link to read that section. No download needed.

**Limitations:** Requires internet, can't make personal notes, leaves browsing history.

---

### Option B: Download to Computer (Offline Use)

**What you'll get:** A folder with all guides, maps, and resources that works without internet.

#### Windows

1. Go to [github.com/samedayhurt/laraza](https://github.com/samedayhurt/laraza)
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. Find the downloaded file (usually in your Downloads folder), right-click it, select **"Extract All"**
5. Open the extracted `laraza-main` folder
6. Double-click any `.md` file to open it (they open in Notepad or any text editor)

**Tip:** For better reading, install a free Markdown viewer like [Typora](https://typora.io/) or [Mark Text](https://marktext.app/).

#### Mac

1. Go to [github.com/samedayhurt/laraza](https://github.com/samedayhurt/laraza)
2. Click the green **"Code"** button → **"Download ZIP"**
3. The ZIP will auto-extract in your Downloads folder (or double-click it)
4. Open the `laraza-main` folder
5. Double-click any `.md` file to read it in TextEdit

#### Linux

**Option 1 - Download ZIP:** Same as above, extract with your file manager.

**Option 2 - Command line:**
```bash
git clone https://github.com/samedayhurt/laraza.git
cd laraza
```

---

### Option C: Use with Obsidian (Best Experience)

[Obsidian](https://obsidian.md/) is a free note-taking app that makes this guide **interactive**—linked notes, searchable, and you can add your own research.

#### Step 1: Download the Guide

Follow Option B above to download and extract the files.

#### Step 2: Install Obsidian

1. Go to [obsidian.md](https://obsidian.md/)
2. Click **"Get Obsidian for free"**
3. Download for your system (Windows/Mac/Linux)
4. Install it like any other app

#### Step 3: Open as Vault

1. Open Obsidian
2. Click **"Open folder as vault"**
3. Navigate to the `laraza-main` folder you downloaded
4. Click **"Open"**
5. If prompted about "Trust author," click **"Trust"**

#### Step 4: Start Exploring

- Use the **left sidebar** to browse folders
- Click any note to read it
- Use `Ctrl+O` (or `Cmd+O` on Mac) to quickly search for any topic
- Try the **Graph View** (icon in left sidebar) to see how topics connect

**Making it yours:** Add your own notes, research, and observations. Your changes stay local—they won't affect anyone else's copy.

---

### Option D: Use on Phone (Offline)

#### Android

1. Install **Obsidian** from Google Play Store (free)
2. Download the guide:
   - In your phone's browser, go to [github.com/samedayhurt/laraza](https://github.com/samedayhurt/laraza)
   - Tap green **"Code"** button → **"Download ZIP"**
   - Extract the ZIP using your file manager (or install "ZArchiver" from Play Store)
3. Open Obsidian → **"Create new vault"** → **"Open folder as vault"**
4. Navigate to the extracted `laraza-main` folder → **"Use this folder"**

#### iPhone/iPad

1. Install **Obsidian** from App Store (free)
2. Download the guide:
   - In Safari, go to [github.com/samedayhurt/laraza](https://github.com/samedayhurt/laraza)
   - Tap green **"Code"** button → **"Download ZIP"**
   - When download completes, tap it to extract
   - Move the folder to "On My iPhone" in Files app
3. Open Obsidian → **"Open folder as vault"**
4. Navigate to the folder → **"Open"**

---

### Keeping Your Copy Updated

The guide is updated regularly. To get the latest version:

**If you downloaded the ZIP:** Download a fresh copy and replace your old folder (back up any personal notes first).

**If you used `git clone`:**
```bash
cd laraza
git pull
```

---

### Privacy Note

Downloading this guide leaves minimal trace—far less than reading online. For maximum privacy:
- Download over VPN or Tor
- Use the offline copy exclusively
- Store on an encrypted drive

See [Operational Security Layers](primers/Operational-Security-Layers.md) for complete privacy guidance.

---

### Encrypt Your Device (Recommended)

Full disk encryption ensures that if your device is lost, stolen, or seized, the data remains unreadable without your password.

#### Windows

**BitLocker (Windows Pro/Enterprise):**
1. Open **Control Panel** → **System and Security** → **BitLocker Drive Encryption**
2. Click **Turn on BitLocker** for your main drive
3. Choose how to unlock: **Password** recommended
4. Save your recovery key somewhere safe (NOT on the same device)
5. Choose **Encrypt entire drive** → **New encryption mode**
6. Click **Start encrypting**

**VeraCrypt (Windows Home or any version):**
1. Download from [veracrypt.fr](https://www.veracrypt.fr/en/Downloads.html)
2. Install and open VeraCrypt
3. Go to **System** → **Encrypt System Partition/Drive**
4. Choose **Normal** → **Encrypt the Windows system partition**
5. Choose **Single-boot** (unless you dual-boot)
6. Create a strong password and PIM (leave PIM blank for default)
7. Create the rescue disk when prompted (required)
8. Run the pre-test, then encrypt

#### Mac

**FileVault (Built-in):**
1. Open **System Preferences** → **Security & Privacy** → **FileVault**
2. Click the lock icon and enter your password
3. Click **Turn On FileVault**
4. Choose how to unlock: **iCloud account** or **recovery key** (recovery key is more private)
5. Save your recovery key somewhere safe
6. Encryption begins automatically (takes a few hours)

#### Linux

**During Installation (Easiest):**
Most Linux installers offer "Encrypt the new installation" during setup. Check this box and set a strong passphrase.

**After Installation (LUKS):**
Encrypting after install is complex and risky—reinstall with encryption enabled if possible. For existing systems, consider encrypting your home folder:
```bash
# Install ecryptfs
sudo apt install ecryptfs-utils
# Migrate your home directory (log in as different user first)
sudo ecryptfs-migrate-home -u yourusername
```

#### Android

Most modern Android phones are encrypted by default. To verify:
1. Go to **Settings** → **Security** → **Encryption & credentials**
2. Should say "Encrypted" under "Encrypt phone"

If not encrypted:
1. Charge to 80%+ and plug in
2. Go to **Settings** → **Security** → **Encrypt phone**
3. Set a strong PIN/password (pattern is weaker)
4. Wait for encryption to complete (1-2 hours)

**GrapheneOS:** Encrypted by default with stronger implementation than stock Android.

#### iPhone/iPad

iOS devices are encrypted by default when you set a passcode.

**Strengthen it:**
1. Go to **Settings** → **Face ID & Passcode** (or Touch ID & Passcode)
2. Tap **Change Passcode**
3. Tap **Passcode Options** → **Custom Alphanumeric Code**
4. Set a strong password (not just 6 digits)

**Why this matters:** A 6-digit PIN can be cracked in hours. An alphanumeric password with 10+ characters could take years.

---

### Self-Hosting Your Infrastructure

For maximum control over your data, consider self-hosting your own cloud services. This eliminates third-party access to your files, communications, and research.

**See the full guide:** [Self-Hosting Infrastructure](primers/Self-Hosting-Infrastructure.md)

Quick overview of what you can self-host:
- **File sync:** Nextcloud, Syncthing
- **Passwords:** Vaultwarden (Bitwarden compatible)
- **Communication:** Matrix/Element, XMPP, Jitsi
- **VPN:** WireGuard, Tailscale
- **Notes:** Obsidian + Syncthing, Joplin Server

---

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
- **[`docs/digital-footprint-protection.md`](docs/digital-footprint-protection.md)** — ties the research workflow to device hygiene, metadata minimization, and the comms/OPSEC primers so teams keep their digital footprint tight while executing the roadmap.
- **[`docs/data-legend.md`](docs/data-legend.md)** — summarizes where each dataset/report comes from (census, media, vendor releases, automation scripts) so readers can audit provenance and extend the pipeline transparently.

## Roadmap: Guides & Self-Advocacy
We follow the `AGENTS.md` workflow so research flows into actionable guides that teach Pueblo residents how to advocate for themselves.

1. **Research + Logging Layer**
   - Populate the raw/structured notebooks in `data/` (politics, surveillance/policing, immigration/ICE, community resources) and cite everything inside `logs/source_index.md`.
   - Record investigations, FOIA/CORA pulls, and desk research sessions in `logs/search_log.md` so anyone can audit how findings were produced; log TODOs (e.g., district-level census pulls, upcoming council agendas) in context notes so future sprints can pick them up quickly.
2. **Report & Guide Production**
   - Draft and continuously update the five Markdown reports inside `reports/`, prioritizing sections like “How to assert your right to record,” “How to push back on surveillance purchases,” and “Where to get immediate legal/financial help.”
   - Pair every risk description with a corresponding “self-advocacy move” (filing complaints, rallying allies, requesting hearings, redirecting budgets) before publishing.
3. **Community Activation & Review**
   - Convert report highlights into teach-ins, handouts, or Signal briefs for journalists, activists, organizers, and residents navigating arrests or ICE pressure.
   - Run a `logs/safety_ethics_review.md` check before release to ensure no private residents are exposed and that guidance stays rights-affirming rather than escalatory.

Update this roadmap as needs evolve—each bullet should map to issues/tasks so contributors understand how their work strengthens Pueblo’s self-advocacy muscle.

## Field Use: Protest & Outreach Protection
- **Primers** help field researchers and volunteer medics spin up clean laptops/VMs before deployments so seized gear can’t reveal networks.
- **Secure Communication Techniques + Non-Standard Comms** pair encrypted drops (Tor + gocryptfs) with LoRa/APRS redundancies for marches where cell service or legal protections collapse.
- **GrapheneOS + Mudi kit** (documented under Comms & OPSEC) gives you a travel router + hardened phone chain so you can uplink livestreams or legal updates without exposing your home IP.
- **Operational Security** translates lessons to civilian teams: build threat models per action, enforce compartmentalized personas, and keep source notes in encrypted Obsidian vaults.
- **Pueblo 81008 memo/map** shows where surveillance infrastructure lives (RTCC feeds, Flock cameras) so organizers can plan ingress/egress routes that avoid persistent monitoring.
- **Pueblo County Officials guide** surfaces which electeds own businesses or make policy decisions affecting protest permits, jail funding, or public-records access—fuel for research requests and accountability campaigns.

When in doubt, start with the folder README to understand how each section is meant to be used in the field.

## Operational Security Layers

Security is about layers—no single tool protects you completely, but combining the right tools for your threat level creates meaningful protection. We've organized our security guidance into a progressive system that scales with your needs.

| Layer | Tools | Use Case |
|-------|-------|----------|
| **1. Browser** | Hardened Firefox, uBlock Origin, containers | Daily research, reading agendas, general OSINT |
| **2. Network** | VPN (Mullvad/ProtonVPN), Tor Browser | Anonymized research, sensitive searches |
| **3. Isolation** | Virtual Machines (TraceLabs, Kali, Whonix) | Handling untrusted files, deep research |
| **4. Hardware** | Mudi router + Blue Merle, GrapheneOS | Field deployment, protests, documentation |
| **5. Communications** | Signal, encrypted Obsidian vaults | Coordination, sharing findings securely |

**Start with Layer 1, add layers as your threat model requires.**

For complete setup guides, threat model analysis, and practical workflows (researching city agendas, documenting protests, handling CORA requests), see:

**[Operational Security Layers (Full Guide)](primers/Operational-Security-Layers.md)**

The guide includes:
- Step-by-step setup for each layer
- Tool recommendations with security criteria
- VM configurations for OSINT research
- Mudi router + Blue Merle IMEI randomization
- Signal best practices for group security
- Practical workflows tied to Pueblo-specific threats
