# Self-Hosting Infrastructure

A guide to running your own cloud services—file sync, passwords, communication, and more—without relying on third-party providers who can be subpoenaed, hacked, or shut down.

**Why self-host:**
- Your data stays on hardware you control
- No third-party access (Google, Microsoft, Dropbox can't hand over what they don't have)
- Resilience against service shutdowns or policy changes
- Learn how the systems work (knowledge is power)

**Trade-offs:**
- You're responsible for security and maintenance
- Requires some technical knowledge (this guide helps)
- Hardware and electricity costs
- No support team to call

---

## Hardware Options

### Raspberry Pi (Budget: $50-150)

Best for: Small deployments, 1-5 users, low power consumption

**Recommended:** Raspberry Pi 4 (4GB or 8GB RAM) or Raspberry Pi 5

**Setup:**
1. Buy a Raspberry Pi 4/5 with power supply
2. Get a quality microSD card (32GB+) or USB SSD (faster, more reliable)
3. Flash [Raspberry Pi OS Lite](https://www.raspberrypi.com/software/) (64-bit)
4. Enable SSH during setup
5. Connect to your network (Ethernet preferred for servers)

**Cost breakdown:**
- Raspberry Pi 4 (4GB): ~$55
- Power supply: ~$15
- 128GB SSD + USB adapter: ~$25
- Case: ~$10
- **Total: ~$105**

### Old Laptop/Desktop (Budget: Free-$100)

Best for: More power, better redundancy, repurposing old hardware

Any x86_64 computer from the last 10 years works. 8GB+ RAM recommended.

**Setup:**
1. Install [Ubuntu Server](https://ubuntu.com/download/server) or [Debian](https://www.debian.org/)
2. During install, enable OpenSSH server
3. Connect via Ethernet for best reliability

### VPS (Budget: $5-20/month)

Best for: Remote access without opening home network, better uptime

**Privacy-focused providers:**
- [Njalla](https://njal.la/) - Anonymous registration, accepts crypto
- [1984 Hosting](https://1984hosting.com/) - Iceland, strong privacy laws
- [OrangeWebsite](https://www.orangewebsite.com/) - Iceland
- [Bahnhof](https://www.bahnhof.net/) - Sweden, fought for WikiLeaks

**Trade-off:** You trust the VPS provider with physical access. For highest security, self-host at home with encrypted drives.

### Mini PC (Budget: $150-400)

Best for: Quiet, low-power, more capable than Pi

**Options:**
- Intel NUC (used/refurbished)
- Beelink Mini PCs
- Minisforum devices

---

## Networking Fundamentals

### Accessing Your Server Remotely

**Option 1: Tailscale (Easiest)**

Tailscale creates a private network between your devices without opening ports.

```bash
# Install on your server (Ubuntu/Debian)
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up

# Install on your phone/laptop
# Download from tailscale.com or app stores
```

Now access your server via its Tailscale IP (100.x.x.x) from anywhere.

**Option 2: WireGuard VPN (More Control)**

Self-hosted VPN for accessing your home network.

```bash
# Install WireGuard
sudo apt install wireguard

# Generate keys
wg genkey | tee privatekey | wg pubkey > publickey

# Configure /etc/wireguard/wg0.conf
[Interface]
PrivateKey = <your-private-key>
Address = 10.0.0.1/24
ListenPort = 51820

[Peer]
PublicKey = <client-public-key>
AllowedIPs = 10.0.0.2/32
```

Requires port forwarding on your router (UDP 51820).

**Option 3: Tor Hidden Service (Maximum Privacy)**

Access your services over Tor without revealing your IP.

```bash
# Install Tor
sudo apt install tor

# Edit /etc/tor/torrc, add:
HiddenServiceDir /var/lib/tor/myservice/
HiddenServicePort 80 127.0.0.1:80

# Restart Tor
sudo systemctl restart tor

# Get your .onion address
sudo cat /var/lib/tor/myservice/hostname
```

---

## File Sync & Storage

### Nextcloud (Full Cloud Suite)

Replacement for: Google Drive, Dropbox, Google Calendar, Google Contacts

**Features:** File sync, calendar, contacts, notes, collaborative editing, mobile apps

**Installation (Docker - Recommended):**

```bash
# Install Docker
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER

# Create docker-compose.yml
mkdir ~/nextcloud && cd ~/nextcloud
```

Create `docker-compose.yml`:
```yaml
version: '3'
services:
  nextcloud:
    image: nextcloud:latest
    container_name: nextcloud
    restart: unless-stopped
    ports:
      - "8080:80"
    volumes:
      - ./data:/var/www/html
    environment:
      - SQLITE_DATABASE=nextcloud
```

```bash
# Start Nextcloud
docker compose up -d

# Access at http://your-server-ip:8080
# Create admin account on first visit
```

**Mobile apps:** Available on F-Droid, Google Play, and App Store.

**Hardening:**
- Put behind HTTPS (use Caddy or nginx with Let's Encrypt)
- Enable 2FA in settings
- Disable public sharing if not needed
- Regular backups of the `data` folder

### Syncthing (Peer-to-Peer Sync)

Replacement for: Dropbox, Google Drive (sync only, no web interface)

No central server—devices sync directly with each other.

**Installation:**

```bash
# Ubuntu/Debian
sudo apt install syncthing

# Start and enable
sudo systemctl enable --now syncthing@$USER

# Access web UI at http://localhost:8384
```

**Setup:**
1. Install Syncthing on all devices you want to sync
2. Add devices by sharing Device IDs (in Actions → Show ID)
3. Create a folder to share, add the other device(s) to it
4. Folders sync automatically when devices are online together

**Hardening:**
- Set GUI password (Actions → Settings → GUI)
- Disable global discovery and relays for maximum privacy:
  - Actions → Settings → Connections
  - Uncheck "Global Discovery" and "Enable Relaying"
  - Use only "Local Discovery" or direct device IPs

**Mobile:** Available on F-Droid (Syncthing-Fork recommended) and Play Store.

---

## Password Management

### Vaultwarden (Bitwarden Compatible)

Self-hosted password manager compatible with all Bitwarden apps.

**Installation (Docker):**

```bash
mkdir ~/vaultwarden && cd ~/vaultwarden
```

Create `docker-compose.yml`:
```yaml
version: '3'
services:
  vaultwarden:
    image: vaultwarden/server:latest
    container_name: vaultwarden
    restart: unless-stopped
    ports:
      - "8081:80"
    volumes:
      - ./data:/data
    environment:
      - SIGNUPS_ALLOWED=false  # Disable after creating your account
      - ADMIN_TOKEN=your-secure-admin-token
```

```bash
docker compose up -d
# Access at http://your-server-ip:8081
```

**Setup:**
1. Create your account at the web interface
2. Edit `docker-compose.yml`, set `SIGNUPS_ALLOWED=false`
3. Restart: `docker compose down && docker compose up -d`
4. Use official Bitwarden apps, point them to your server URL

**Critical:** Put behind HTTPS before using in production. Passwords over HTTP can be intercepted.

---

## Communication

### Matrix/Element (Encrypted Chat)

Self-hosted replacement for: Slack, Discord, WhatsApp groups

**Features:** Federated (can talk to other Matrix servers), E2EE, bridges to other platforms

**Installation (Docker with Synapse):**

```bash
mkdir ~/matrix && cd ~/matrix
```

Create `docker-compose.yml`:
```yaml
version: '3'
services:
  synapse:
    image: matrixdotorg/synapse:latest
    container_name: synapse
    restart: unless-stopped
    ports:
      - "8008:8008"
    volumes:
      - ./data:/data
    environment:
      - SYNAPSE_SERVER_NAME=your-domain.com
      - SYNAPSE_REPORT_STATS=no
```

```bash
# Generate config
docker run -it --rm \
  -v $(pwd)/data:/data \
  -e SYNAPSE_SERVER_NAME=your-domain.com \
  -e SYNAPSE_REPORT_STATS=no \
  matrixdotorg/synapse:latest generate

# Start server
docker compose up -d
```

**Clients:** Element (web, desktop, mobile) - point to your server during login.

### XMPP with Prosody (Lightweight Chat)

Older but battle-tested protocol. Very lightweight.

```bash
# Install Prosody
sudo apt install prosody

# Configure /etc/prosody/prosody.cfg.lua
# Set your domain, enable OMEMO for encryption

# Create user
sudo prosodyctl adduser you@your-domain.com
```

**Clients:** Conversations (Android), Monal (iOS), Gajim (Desktop)

### Jitsi Meet (Video Calls)

Self-hosted replacement for: Zoom, Google Meet

```bash
# Quick install script (Debian/Ubuntu)
wget https://github.com/jitsi/jitsi-meet/raw/master/doc/quick-install/quick-install.sh
chmod +x quick-install.sh
sudo ./quick-install.sh
```

Requires a domain name with ports 80, 443, and 10000/UDP open.

### Mumble (Voice Chat)

Low-latency voice chat, great for real-time coordination.

```bash
# Install server
sudo apt install mumble-server

# Configure
sudo dpkg-reconfigure mumble-server
# Set password, enable autostart
```

**Client:** Mumble (desktop), Plumble (Android)

---

## VPN Server

### WireGuard (Recommended)

Fast, modern VPN protocol.

```bash
# Install
sudo apt install wireguard

# Generate server keys
cd /etc/wireguard
wg genkey | sudo tee server_private.key | wg pubkey | sudo tee server_public.key
sudo chmod 600 server_private.key
```

Create `/etc/wireguard/wg0.conf`:
```ini
[Interface]
PrivateKey = <server-private-key>
Address = 10.0.0.1/24
ListenPort = 51820
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

[Peer]
# Client 1
PublicKey = <client-public-key>
AllowedIPs = 10.0.0.2/32
```

```bash
# Enable IP forwarding
echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

# Start WireGuard
sudo wg-quick up wg0
sudo systemctl enable wg-quick@wg0
```

**Router config:** Forward UDP port 51820 to your server.

**Client config:**
```ini
[Interface]
PrivateKey = <client-private-key>
Address = 10.0.0.2/32
DNS = 1.1.1.1

[Peer]
PublicKey = <server-public-key>
Endpoint = your-public-ip:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
```

### Tailscale (Zero-Config Alternative)

If WireGuard is too complex, Tailscale handles everything automatically.

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up --advertise-exit-node  # Make this device a VPN exit
```

On clients, enable "Use exit node" and select your server.

---

## Notes & Documentation

### Obsidian + Syncthing

This repository is already set up for Obsidian. Sync between devices with Syncthing:

1. Install Syncthing on all devices
2. Share your Obsidian vault folder
3. Notes sync automatically

**Conflict handling:** Syncthing creates `.sync-conflict` files if two devices edit the same file simultaneously. Resolve manually.

### Joplin Server (Alternative)

Open-source Evernote alternative with self-hosted sync.

```bash
# Docker installation
mkdir ~/joplin && cd ~/joplin
```

Create `docker-compose.yml`:
```yaml
version: '3'
services:
  joplin:
    image: joplin/server:latest
    container_name: joplin
    restart: unless-stopped
    ports:
      - "22300:22300"
    environment:
      - APP_BASE_URL=http://your-server-ip:22300
      - DB_CLIENT=sqlite3
```

```bash
docker compose up -d
```

---

## Security Hardening

### Firewall

```bash
# Install UFW
sudo apt install ufw

# Default deny incoming, allow outgoing
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow SSH (important - don't lock yourself out!)
sudo ufw allow ssh

# Allow specific services
sudo ufw allow 8080/tcp  # Nextcloud
sudo ufw allow 51820/udp # WireGuard

# Enable firewall
sudo ufw enable
```

### Automatic Updates

```bash
# Install unattended-upgrades
sudo apt install unattended-upgrades

# Enable automatic security updates
sudo dpkg-reconfigure -plow unattended-upgrades
```

### Fail2ban (Brute Force Protection)

```bash
# Install
sudo apt install fail2ban

# Enable for SSH
sudo systemctl enable --now fail2ban
```

### Backups

**The 3-2-1 Rule:**
- **3** copies of your data
- **2** different storage types
- **1** offsite backup

**Simple backup script:**
```bash
#!/bin/bash
# backup.sh - Run weekly via cron

BACKUP_DIR="/path/to/backups"
DATE=$(date +%Y-%m-%d)

# Stop services
docker compose -f ~/nextcloud/docker-compose.yml down
docker compose -f ~/vaultwarden/docker-compose.yml down

# Create backup
tar -czf "$BACKUP_DIR/server-backup-$DATE.tar.gz" \
  ~/nextcloud/data \
  ~/vaultwarden/data \
  /etc/wireguard

# Restart services
docker compose -f ~/nextcloud/docker-compose.yml up -d
docker compose -f ~/vaultwarden/docker-compose.yml up -d

# Keep only last 4 backups
ls -t "$BACKUP_DIR"/server-backup-*.tar.gz | tail -n +5 | xargs -r rm
```

**Offsite:** Encrypt backups with `age` or `gpg` before uploading to any cloud storage.

---

## Quick Start: Minimal Privacy Setup

If you want to get started quickly, here's the minimal self-hosted stack:

| Service | Solution | Time to Setup |
|---------|----------|---------------|
| File sync | Syncthing | 15 minutes |
| Passwords | Vaultwarden | 30 minutes |
| VPN access | Tailscale | 10 minutes |
| Notes | Obsidian + Syncthing | Already done |

**Total time:** About 1 hour to have a fully self-hosted privacy stack.

---

## Troubleshooting

**Can't access server remotely:**
- Check firewall: `sudo ufw status`
- Check service is running: `docker ps` or `systemctl status <service>`
- Check Tailscale connection: `tailscale status`

**Docker container won't start:**
- Check logs: `docker logs <container-name>`
- Check disk space: `df -h`
- Check permissions on mounted volumes

**Services slow on Raspberry Pi:**
- Use USB SSD instead of SD card
- Check temperature: `vcgencmd measure_temp`
- Consider upgrading to Pi 5 or mini PC

---

## Resources

- [r/selfhosted](https://reddit.com/r/selfhosted) - Community for self-hosting
- [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - Comprehensive list of self-hosted software
- [LinuxServer.io](https://linuxserver.io/) - Well-maintained Docker images
- [Proxmox](https://proxmox.com/) - Virtualization platform for running multiple servers

---

*Self-hosting is a journey. Start small, learn as you go, and gradually take control of your digital infrastructure.*
