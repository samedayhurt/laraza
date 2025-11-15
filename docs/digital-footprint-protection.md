# Digital Footprint Protection Playbook

This playbook connects the Pueblo research pipeline to concrete device/metadata discipline so journalists, activists, and researchers can work without exposing personal networks. Use it alongside the comms/opsec primers referenced below.

## 1. Device & Account Compartmentalization
- **GrapheneOS + Mudi workflow:** Follow the [GrapheneOS + Mudi Field Kit](../comms/GrapheneOS%20Mudi%20Field%20Kit.md) to keep protest connectivity on hardened phones and travel routers. Treat each profile as its own identity (personal vs. field media) and wipe the “Field” profile after every deployment.
- **Virtual machines for intake:** Use the [Virtual Machines primer](../primers/Virtual%20Machines.md) to collect submissions and footage inside disposable VMs. Snapshot before each action so any malware or metadata artifacts die when you roll back.
- **Obsidian vault hygiene:** Case IDs (`YYYYMMDD-Event-Initials`) outlined in the [Legal Observer Toolkit](../opsec/Legal%20Observer%20Toolkit.md) keep notes, hashes, and media aligned without naming individuals.

## 2. Metadata Minimization
- **Hash everything:** Per the Legal Observer Toolkit, run `sha256sum file.ext >> CASEID_hashes.txt` on every clip before sharing. Copy hashes into the encrypted vault or `logs/source_index.md` so any alteration is obvious.
- **Strip EXIF/document properties:** Before uploading to `docs/maps/` or sharing with partners, run `exiftool -all= file.jpg` (or LibreOffice “Clear personal data”) and store sanitized copies in the vault.
- **Use role-specific accounts:** When filing CORA requests or emailing agendas, create role-based aliases (e.g., `councilwatch+pueblo@proton.me`). Store credentials in the encrypted vault instead of personal password managers.

## 3. Network & Comms Choices
- **Layered channels:** Combine Signal/Session (see [comms/README.md](../comms/README.md)) with LoRa/APRS fallbacks so RTCC tower dumps cannot map the entire network. Mudi routers tunnel traffic through WireGuard/Tor before touching local towers.
- **Community Connect awareness:** When discussing camera registries, cite the risks in [reports/surveillance_and_policing_risks.md](../reports/surveillance_and_policing_risks.md) and offer alternative workflows (encrypted dropboxes, on-site handoffs).
- **Location hygiene:** Rotate SIMs/MAC addresses when entering 81008; log device IDs and wipe routines in [Operational Security Techniques](../opsec/Operational%20Security%20Techniques.md) so seized hardware can be tied to specific missions.

## 4. Data Storage & Sharing
- **Structured data discipline:** All raw research goes into `data/*_raw` notebooks with sources tracked in `logs/source_index.md`. Structured JSON files should never include private identifiers—reference public titles and roles instead.
- **Encrypted sync:** Use the [Strong & Anonymous File Sync workflow](../comms/e2eefilechange.md) (gocryptfs + Tor Syncthing) for multi-person editing of sensitive docs (`reports/` drafts, witness statements). Never drop raw files into cloud storage without encryption.
- **Device audits:** After each sprint, run through the “Before/During/After” checklist in Operational Security Techniques to confirm devices, radios, and routers have been wiped or reset.

## 5. Field Checklist (5 minutes)
1. Power devices in airplane mode, confirm full-disk encryption, and only enable radios via the Mudi once onsite.
2. Open the VM or GrapheneOS field profile, sync the relevant `data/*` files via the encrypted share, and close the sync client when done.
3. After recording, hash media, drop it into the encrypted vault, and send only the minimum context (hash + short summary) over Signal/Session.

Tie every action back to the reports you’re producing: if a surveillance vote is pending, include metadata hygiene steps in testimony; when sharing the protection guide, remind recipients to run through this playbook before downloading or redistributing it.
