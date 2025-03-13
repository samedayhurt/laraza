# **Strong & Anonymous File Sync with End-to-End Encryption (E2EE)**

Syncthing does **not** provide end-to-end encryption (E2EE), so we must encrypt files **before syncing**. This guide sets up **gocryptfs** for encryption and runs **Syncthing or Magic Wormhole** over **Tor** for anonymity.

##Auto Setup
You can follow the steps below or use the simple [bash script](e2eesetup.sh) I've written that'll walk you through the setup.
---

## **1️⃣ Encrypt Files Before Syncing**
### **Best Encryption Options**
| Tool | Features | Best For |
|------|----------|----------|
| **gocryptfs** | AES-GCM-256, per-file encryption, fast, FUSE-based | General use |
| **age** | X25519, ChaCha20-Poly1305, simple CLI, great for scripts | Backup encryption |
| **Veracrypt** | Full-disk/volume encryption, plausible deniability | Large containers |

✅ **Recommended:** `gocryptfs` (best performance & usability)

### **Setup gocryptfs**
```bash
mkdir -p ~/encrypted ~/decrypted

gocryptfs -init ~/encrypted  # Initialize encrypted folder

gocryptfs ~/encrypted ~/decrypted  # Mount decrypted view
```
- **Sync only `~/encrypted`**, not `~/decrypted`.
- On another device, **decrypt synced data**:
```bash
gocryptfs ~/encrypted ~/decrypted
```

---

## **2️⃣ Sync Encrypted Data with Syncthing or Magic Wormhole**
### **Option 1: Syncthing**
- Add `~/encrypted` as a Syncthing folder.
- Disable **Global Discovery** and **Relays** for privacy.
- Sync encrypted data only.

### **Option 2: Magic Wormhole**
Magic Wormhole provides a **one-time, encrypted** file transfer method. Ideal for **ad-hoc** file sharing.

#### **Install Magic Wormhole**
```bash
sudo apt install magic-wormhole
```
#### **Send a file**
```bash
wormhole send myfile.txt
```
- A short code appears (e.g., `4-horse-battery`).
- Share this code securely.

#### **Receive a file**
```bash
wormhole receive 4-horse-battery
```

---

## **3️⃣ Run Over Tor for Anonymity**

### **Set Up a Tor Hidden Service for Syncthing**
```bash
echo -e "HiddenServiceDir /var/lib/tor/syncthing/\nHiddenServicePort 22000 127.0.0.1:22000" | sudo tee -a /etc/tor/torrc
sudo systemctl restart tor
```
- Find `.onion` address:
```bash
cat /var/lib/tor/syncthing/hostname
```
- **Add this address as a remote device in Syncthing.**

### **Use Tor for Magic Wormhole**
Run Magic Wormhole over Tor for extra privacy:
```bash
torsocks wormhole send myfile.txt
```

---

## **4️⃣ Harden Security & Privacy**
### **Disable Syncthing’s Global Discovery & Relays**
Edit `config.xml`:
```xml
<globalAnnounceEnabled>false</globalAnnounceEnabled>
<relaysEnabled>false</relaysEnabled>
```

### **Run in a Sandbox (Firejail)**
Firejail isolates Syncthing from the rest of the system, limiting access to files and network resources.

#### **Install Firejail**
```bash
sudo apt install firejail
```
#### **Run Syncthing inside Firejail with limited access:**
```bash
firejail --private --net=none syncthing --no-browser
```
- `--private`: Creates an isolated home directory (hides real files).  
- `--net=none`: Blocks network access until explicitly allowed.  

#### **Allow only specific network access (if using Tor):**
```bash
firejail --net=tor syncthing --no-browser
```

#### **Create a persistent Firejail profile for Syncthing:**
```bash
echo -e "whitelist ${HOME}/encrypted\nwhitelist ${HOME}/.config/syncthing\nnet none" | sudo tee /etc/firejail/syncthing.profile
```
Now you can run it safely with:
```bash
firejail syncthing
```

---

## **5️⃣ Use a VPN + Tor for Layered Privacy**
- VPN → Tor → Syncthing / Magic Wormhole

---

## **6️⃣ Automate Encryption & Syncing**
Create an auto-mount script:
```bash
#!/bin/bash
gocryptfs ~/encrypted ~/decrypted
syncthing --no-browser
```
Then, set up a **cron job** or **systemd service** to run it at startup.

---

## **Final Setup Summary**
✅ **gocryptfs for encryption**  
✅ **Sync only encrypted data**  
✅ **Syncthing or Magic Wormhole**  
✅ **Run over Tor Hidden Services**  
✅ **Disable discovery & relays**  
✅ **Run in a sandbox (Firejail)**  
✅ **VPN + Tor for extra anonymity**  
✅ **Automate with scripts**  
