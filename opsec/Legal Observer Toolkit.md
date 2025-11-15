# Pueblo Legal Observer & Documentation Toolkit

This guide focuses on rapid documentation workflows for Pueblo protests, mutual aid deployments, and courthouse actions. Use it to train new observers, standardize evidence handling, and feed credible complaints into the pipelines documented elsewhere in `opsec/`.

## 1. Pre-Deployment Checklist
1. **Assign roles:** At least two observers (primary recorder + runner) plus one comms lead tied into the [`GrapheneOS + Mudi`](../comms/GrapheneOS%20Mudi%20Field%20Kit.md) uplink.
2. **Gear each bag with:**
   - Notebooks with numbered pages, waterproof pens, and time-synced watches.
   - Faraday sleeves for confiscation-prone phones; spare microSD cards labeled with date/shift.
   - Printed quick references: Pueblo PD Internal Affairs contact, Colorado POST instructions, CORRN hotline, and local bail fund contacts.
3. **Create case IDs before you leave:** Format `YYYYMMDD-Event-ObserverInitials` so hashes, photos, and statements match from the start.

## 2. In-Field Evidence Capture
- **Video & audio:** Record short clips (<2 min) focused on badge numbers, signage, and crowd context. Immediately note the timestamp + clip filename in your log.
- **Still photos:** Take establishing shots of intersections (street signs, storefronts) whenever police form skirmish lines or deploy munitions—these help map incidents back to `data/pueblo_apparatus.geojson`.
- **Witness statements:** Collect 30-second voice memos (with consent) summarizing force used, names, and contact info. Tag them with the case ID; always capture a still of the witness if they consent so you can verify later.
- **Hashing on the curb:** After each clip, run `sha256sum clip.mp4 >> hashes.txt` on your Linux field laptop; text the hash over Signal to the legal channel so they know if footage is altered.

## 3. Immediate Escalation Paths
- **Police brutality/abuse:** Package your notes + hashes into a single encrypted archive and send to the IA contact (200 S. Main St.) the same night.[^1] If the case involves potential crimes, forward summaries to the 10th Judicial DA per POST guidance.[^2]
- **Pattern & practice:** Use the Attorney General’s Pattern & Practice form (select “Governmental Authority”) when you have multiple similar incidents from PPD or PCSO.[^2]
- **ICE sightings:** Call the Colorado Rapid Response Network hotline (844-864-8341, option 1) to dispatch docuteams if ICE agents appear alongside PPD/PCSO; leave a message on option 2 to log past interactions so advocates can track trends.[^3]

## 4. Post-Action Workflow
1. **Inventory media:** Compare your logbook to the file hashes; rename files to `CASEID_clip01.mp4`.
2. **Secure storage:** Drop footage into the encrypted Syncthing share described in `comms/e2eefilechange.md` so legal counsel can review without touching original devices.
3. **Map incidents:** Add coordinates + narrative summaries to `data/pueblo_apparatus.geojson` (temporary branch) for any new hot spots (e.g., unexpected ALPR trailers, ICE stings). This keeps the folium map actionable.
4. **Report back:** Update the protest Signal/Session channels with “What we documented” bullet points so volunteers know their testimony was captured.

## 5. Coordination Tips
- **Buddy system:** Observers move in pairs; if one is detained, the other mirrors the arrest, records badge numbers, and alerts comms.
- **Radio language:** Use consistent callouts (“Green DOT,” “Blue DOT”) for medics/legal to avoid broadcasting names over LoRa/APRS.
- **Interface with organizers:** Sit in on nightly debriefs to share trends (e.g., sheriffs escorting ICE) so tactics evolve quickly.

### If you only have 5 minutes
1. **Prep the case log:** Scrawl today’s date + location, snap a photo for backup, and set an alarm every 15 min to remind yourself to annotate.
2. **Hash & send:** After the first clip, run `sha256sum` and text the hash to the legal chat so everyone trusts the workflow.
3. **Escalate hot intel:** If you witness force or ICE collaboration, send a 3-line summary (who/what/where) plus the CORRN hotline number to the protest channel before officers leave the scene.

## References
[^1]: “Internal Affairs Section,” Pueblo Police Department, accessed Nov 15 2025. https://www.pueblo.us/449/Internal-Affairs-Section
[^2]: “Certification Inquiries & Officer Complaints,” Colorado POST, accessed Nov 15 2025. https://post.colorado.gov/certification-inquiries-officer-complaints
[^3]: “Home | CORRN,” Colorado Rapid Response Network, accessed Nov 15 2025. https://www.coloradorapidresponsenetwork.com/

