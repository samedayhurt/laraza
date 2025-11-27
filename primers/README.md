# Primers

This folder collects lightweight primers that provide just enough background to start experimenting with a new topic without wading through an entire textbook. Each document focuses on actionable context, trusted tooling, and links out to deeper dives once you are comfortable.

## Directory Contents

| Resource                                                      | Why it matters                                                                                        | Jump-start actions                                                                                          |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [README.md](README.md)                                       | Orientation for how primers support the Pueblo research workflow and how to contribute new ones.     | Scan this page first to choose the right primer and mirror the contribution guidelines.                     |
| [Linux Primer](Linux%20Primer.md)                             | Build a working knowledge of the operating system that powers most security tooling.                  | Install a beginner-friendly distribution (Ubuntu, Pop!\_OS) in a VM and follow the file system walkthrough. |
| [Direction Finding (Wi-Fi)](Direction%20Finding%20(Wi-Fi).md) | Understand how wireless devices are detected and tracked so you can both audit and defend against it. | Install Kismet or airodump-ng, practice gathering RSSI readings, then review mitigation tactics.            |
| [Virtual Machines](Virtual%20Machines.md)                     | Safely compartmentalize research workflows and rehearse complex setups before field use.              | Enable hardware virtualization, create a clean baseline VM, and capture a snapshot before customizing.      |
| [Drone Surveillance Awareness](Drone%20Surveillance%20Awareness.md) | Understand police drone capabilities, identification, and legal protective strategies. | Learn to identify common police drones, check Remote ID apps, understand thermal/zoom capabilities. |
| [Surveillance Counter-Measures](Surveillance%20Counter-Measures.md) | Comprehensive guide to modern surveillance ecosystem and defensive strategies. | Review commercial telemetry threats, protect against facial recognition, understand ALPR/Stingray risks. |
| [Digital Hygiene for Everyday People](Digital%20Hygiene%20for%20Everyday%20People.md) | Simplified privacy guide for non-technical community members. | Enable 2FA, use Signal, review app permissions, protect social media presence. |
| [Higiene Digital para la Comunidad](Higiene%20Digital%20para%20la%20Comunidad.md) | Spanish version of Digital Hygiene guide for Spanish-speaking community. | Same as above, in Spanish. |

> **Tip:** Primers are intentionally brief. Pair them with hands-on reps and notes in your Obsidian vault to solidify the material.

### Pueblo field examples
- **Linux Primer:** Flash a spare laptop with Pop!\_OS before canvassing Bessemer residents so you can safely ingest footage from borrowed SD cards without risking your daily driver.
- **Direction Finding:** Run a weekend scan around Union Avenue during marches to map where doorbell cameras and hotel APs overlap, then update the 81008 map with those hotspots so teams can reroute.
- **Virtual Machines:** Keep a "Protest Intake" VM with Obsidian + witness statement templates; boot it inside a coffee shop, sync via Tor, and shut it down after exporting redacted PDFs for public defenders.
- **Drone Awareness:** Before the Chile Festival protest, review police drone models so you can identify the Matrice 30T overhead; use Remote ID apps to confirm it's PPD and document for FOIA requests.
- **Surveillance Counter-Measures:** Reset your advertising ID and deny app location permissions before attending a city council meeting on surveillance—commercial telemetry data has been used to identify attendees.
- **Digital Hygiene:** Print copies of the Spanish version for the Bessemer community center so families know how to protect themselves from social media surveillance without needing technical backgrounds.

## How to Use These Notes

1. **Start with your use case.** Focus on the primer that unblocks today’s task (e.g., bootstrapping Kali before a research sprint).
2. **Replicate the workflow.** Work through the exercises end-to-end so that the commands and tooling become muscle memory.
3. **Record adaptations.** Copy the file into your vault, annotate with screenshots/configs that match your hardware, and link to related investigations.
4. **Revisit often.** Refreshing the basics before missions keeps errors (and surprises) to a minimum.

## Contributing a Primer

1. Keep it scoped—solve one problem well.
2. Lead with procedures and decisions, move references to the end.
3. Link to any scripts or assets in this repo so everything stays reproducible and offline-friendly.
4. Drop a short changelog entry in the pull request so others know what’s new.

Small, incremental additions compound quickly; send them even if they feel obvious.

### If you only have 5 minutes
1. **Linux:** Plug in your encrypted thumb drive, run `rsync` to pull today's photos, and confirm hashes before handing the drive to legal observers.
2. **Direction Finding:** Fire up the Kismet Android companion, log a five-minute walk around the protest perimeter, and screenshot any surprise MAC clusters to warn the crowd.
3. **Virtual Machines:** Launch your "Media Intake" VM, drop new evidence into the gocryptfs mount, and power it off—so even if police seize your laptop, the VM reveals nothing without the key.
4. **Drone Awareness:** Open OpenDroneID app and scan for any Remote ID broadcasts; if you see police drones, note the serial and file a CORA request later.
5. **Surveillance Counter-Measures:** Turn on airplane mode, put phone in Faraday bag, and wear hat + sunglasses + mask before entering a protest area.
6. **Digital Hygiene:** Share the Spanish PDF with a neighbor who's worried about ICE—the basics (Signal, 2FA, location permissions) take 10 minutes to set up.
