# Virtual Machines Primer

Virtual machines (VMs) let you compartmentalize risky workflows, rehearse complex tooling, and recover instantly from mistakes. Treat them as disposable labs that keep your host system, your data, and your sources safe.

## Why Virtualize?
- **Compartmentalization:** Keep OSINT, malware triage, and publishing work in isolated sandboxes.
- **Reproducibility:** Snapshots let you roll back to a known-good state before every mission.
- **Hardware flexibility:** You can run Linux tooling from a Windows laptop (or the opposite) without dual-booting.
- **Attribution control:** Network modes and Tor gateways keep investigative traffic separate from personal browsing.

## Picking a Hypervisor
| Tool | Works best for | Notes |
| --- | --- | --- |
| [VirtualBox](https://www.virtualbox.org/) | General-purpose labs | Free, cross-platform, easy USB passthrough. |
| [VMware Workstation Player/Fusion](https://www.vmware.com/) | Heavy workloads or GPU needs | Proprietary but polished hardware support. |
| [KVM + virt-manager/QEMU](https://virt-manager.org/) | Linux hosts that need performance | Uses kernel virtualization; scriptable with libvirt. |
| [UTM/Parallels](https://mac.getutm.app/) | Apple silicon | UTM wraps QEMU for arm64, Parallels for commercial support. |

Pick the hypervisor your hardware supports well—consistency matters more than brand.

## Prepare the Host First
1. **Enable virtualization** (Intel VT-x / AMD-V / Apple Hypervisor) in BIOS/UEFI.
2. **Update the host OS** and firmware; patching holes on the host protects every VM.
3. **Verify downloads** with vendor checksums:
   ```bash
   sha256sum kali-linux-2024.2-virtualbox-amd64.ova
   ```
4. **Allocate resources intentionally:** keep at least 4 GB RAM and 2 CPU cores free for the host to avoid thrash.
5. **Plan storage:** use separate disks/partitions for VM images when possible; encrypt them if the host travels.

## Building a Clean Baseline VM
1. Download the ISO/OVA from the project’s official site (Kali, TraceLabs, Ubuntu, etc.).
2. Create a new VM and set:
   - **Firmware:** UEFI for modern OSes, BIOS if required.
   - **CPU/RAM:** 2 cores / 4 GB minimum for Kali; more if running browsers or Docker.
   - **Storage:** 40 GB dynamically allocated VDI/VMDK keeps snapshots smaller.
3. Boot from the ISO and walk through installation. Disable third-party analytics if prompted.
4. Post-install tasks:
   - Update packages (`sudo apt update && sudo apt full-upgrade`).
   - Install guest additions for clipboard + display resizing.
   - Harden the image (firewall, minimal services, add baseline tooling).
5. **Snapshot immediately** and name it `00-clean-install`. This becomes the reset point.

## Networking Modes (Choose Per Use Case)
- **NAT:** Default setting, shares the host’s connection. Good for everyday browsing with moderate privacy.
- **Bridged:** VM appears as a device on the local network. Needed for scanning or RF gear that expects direct LAN access—watch your footprint.
- **Host-only:** VM talks only to the host. Pair with a proxy/VPN on the host for safe data staging.
- **Internal networks:** Create isolated mini-LANs (e.g., analyst VM + data diode). Ideal for replicating multi-host workflows.
- **Tor/VPN gateway VM:** Run a small Linux VM that forces traffic through Tor or Mullvad, then point analyst VMs at it via host-only networking.

Document which mode each VM uses so you can prove (or troubleshoot) routing later.

```mermaid
flowchart LR
    Host[(Host OS)]
    Gateway[[VPN/Tor Gateway VM]]
    Analyst1[[Analyst VM]]
    Analyst2[[Publish VM]]
    Internet(((Internet)))

    Host -->|Host-only| Gateway
    Gateway -->|NAT/Bridge| Internet
    Host -->|Internal Network| Analyst1
    Host -->|Internal Network| Analyst2
    Analyst1 <-->|Shared Folder (RO)| Host
    Analyst2 -.->|Snapshot/Clone| Analyst1
```

*Keep the gateway minimal and disposable; analyst VMs should never reach the internet directly.*

## Snapshots, Templates, and Clones
1. **Golden Image:** Keep one “pristine” VM with no personal data.
2. **Linked Clones:** Spin off short-lived workspaces from the golden image; delete when done.
3. **Snapshot cadence:** 
   - Before installing new tooling.
   - Before importing third-party data.
   - After configuring a workflow that you’ll need again.
4. **Exports:** Periodically `File → Export Appliance` so you can recreate the lab if the laptop is seized or fails.

## Operational Hygiene
- **Disable shared clipboards/drag-and-drop** unless absolutely needed; copy using text files or password managers instead.
- **Limit shared folders** to read-only dropboxes for moving sanitized data.
- **Use dedicated user accounts** within the VM for analysis vs. admin tasks.
- **Keep guest additions updated** to avoid privilege escalation bugs.
- **Log what you change** (packages, scripts, ports) in Obsidian so you can rebuild quickly.

### Pueblo protest scenario
- **Rapid intake:** During an East Side march, boot the “Witness Intake” VM, connect it through the GL.iNet Mudi (see Comms guide), and record statements using Obsidian. If deputies confiscate your hardware, the VM disk stays encrypted and you can restore it from the gocryptfs backup later.
- **Evidence triage:** Use a clean VM to open drone footage shared by Pueblo Rights Collective. Scrub metadata, drop the redacted clip into Syncthing, and export a PDF timeline for lawyers—without tainting the host OS or leaking identifiers.

## Quick Start Checklist
1. Confirm virtualization + RAM availability.
2. Download ISO/OVA + verify checksum.
3. Create VM, apply baseline resource settings.
4. Install OS, update, add tooling, snapshot.
5. Configure networking mode + proxy/VPN/Tor chain.
6. Export the golden image and store it offline.

### If you only have 5 minutes
1. **Snapshot safety:** Before leaving for a rally, take a quick snapshot named `pre-protest-<date>` so you can roll back if tear gas or power loss corrupts the VM.
2. **Log wipe:** Launch the VM, clear recent files, and power it down—confirm no decrypted data sits outside gocryptfs before you head downtown.
3. **USB triage:** Plug a witness USB into the VM, copy its content to an encrypted volume, and immediately eject the stick so you can hand it back without propagating malware.

With a hardened VM library, onboarding new teammates or rebuilding after compromise becomes a matter of minutes instead of days.
