# Privacy and OPSEC Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Installing Virtual Machines](#installing-virtual-machines)
   - [Kali Linux](#kali-linux)
   - [TraceLabs VM](#tracelabs-vm)
3. [Hardening Your Browser](#hardening-your-browser)
   - [Firefox Security](#firefox-security)
4. [Using Tor and a VPN](#using-tor-and-a-vpn)
5. [Mudi Router and Blue Merle](#mudi-router-and-blue-merle)
   - [Buying and Using the Mudi Router](#buying-and-using-the-mudi-router)
   - [Setting Up Blue Merle](#setting-up-blue-merle)
6. [Generational Operational Security](#generational-operational-security)
   - [Signal Messenger](#signal-messenger)
   - [Analyst Notebook](#analyst-notebook)
   - [Obsidian for Secure Notes](#obsidian-for-secure-notes)
7. [Conclusion](#conclusion)

---

## Introduction
In today’s digital landscape, privacy and operational security (OPSEC) are more important than ever. This guide will walk you through practical steps to secure your devices, communications, and data, ensuring that your online presence remains as private as possible.

## Installing Virtual Machines
Setting up virtual machines (VMs) is a foundational step for security professionals. Here’s how to install and configure some of the most important VMs for privacy-focused operations.

### Kali Linux
Kali Linux is a powerful platform for penetration testing and ethical hacking.
1. **Download and install VirtualBox** or another hypervisor.
2. **Download Kali Linux ISO** from the [official site](https://www.kali.org/downloads/).
3. Create a new VM in VirtualBox and allocate resources.
4. Follow the installation prompts and configure the system.

### TraceLabs VM
TraceLabs is used for OSINT and investigative work.
1. Head to the [TraceLabs GitHub page](https://github.com/tracelabs) to download the pre-configured VM.
2. Set it up in VirtualBox similarly to Kali.
3. Follow their installation and configuration steps to get started.

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

## Using Tor and a VPN
For an extra layer of anonymity, using Tor in combination with a VPN ensures that your online activity is harder to trace.

1. **Install a VPN**: Choose a no-logs VPN provider like Mullvad or ProtonVPN.
2. **Set up Tor Browser**: Download from the [official Tor Project site](https://www.torproject.org/).
3. **Configure VPN with Tor**: Start your VPN first, then launch Tor Browser to maximize privacy.

## Mudi Router and Blue Merle
These hardware devices provide an additional layer of network security and anonymity.

### Buying and Using the Mudi Router
1. Purchase a Mudi router from [GL.iNet](https://www.gl-inet.com/products/gl-e750-mudi/).
2. **Set up OpenVPN/WireGuard** on the Mudi to route all traffic through a secure tunnel.
3. **Configure Firewall and Adblock**: Enhance security by blocking unwanted traffic.

### Setting Up Blue Merle
Blue Merle is a privacy-focused router designed for anonymity.
1. Set up your Blue Merle device.
2. Ensure VPN and Tor routing are active for all connections.

## Generational Operational Security
OPSEC isn't just a one-time thing; it's something you need to maintain consistently, across different tools and platforms.

### Signal Messenger
1. Install Signal from [Signal.org](https://signal.org/).
2. **Use disappearing messages** and **secure backups** for all conversations.
3. **Vetting Members**: Make sure to vet group chat members for security, especially when working in sensitive environments.

### Analyst Notebook
For intelligence gathering and visualization:
1. Use IBM Analyst Notebook to map out complex data and relationships.
2. Ensure that all sensitive information is stored securely using encrypted databases.

### Obsidian for Secure Notes
1. Install [Obsidian](https://obsidian.md/).
2. **Enable local encryption** for vaults and use it to take private, organized notes.
3. Sync notes securely using encryption-friendly cloud services.

## Conclusion
Maintaining privacy and OPSEC is an ongoing process, requiring constant vigilance and the use of the right tools. With these steps, you’ll be well on your way to ensuring that your data, identity, and communications remain protected.
