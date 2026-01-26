# Secure Messengers Comparison

Not all "encrypted" messengers are equal. This guide compares the major options, explains their trade-offs, and helps you choose the right tool for your threat model.

---

## Quick Comparison

| Messenger | Phone # Required | Decentralized | E2EE Default | Metadata | Best For |
|-----------|------------------|---------------|--------------|----------|----------|
| **Signal** | Yes | No | Yes | Minimal | Most people, general secure comms |
| **Session** | No | Yes | Yes | Very minimal | Anonymity, no phone number |
| **Element/Matrix** | No | Yes (federated) | Optional | Server sees metadata | Groups, self-hosting |
| **SimpleX** | No | Yes | Yes | Near-zero | Maximum privacy |
| **Briar** | No | Yes (P2P) | Yes | None | Offline/mesh, protests |
| **Wire** | No (email) | No | Yes | Moderate | Business, European privacy |
| **Threema** | No | No | Yes | Minimal | Swiss privacy, one-time purchase |

---

## Detailed Analysis

### Signal

**Best for:** Most people, general secure communication, activism

**Strengths:**
- Industry-leading encryption protocol (used by WhatsApp, Facebook Messenger)
- Open source client and server
- Minimal metadata collection
- Strong track record (subpoenas reveal almost nothing)
- Easy to use, familiar interface
- Voice/video calls encrypted
- Disappearing messages

**Weaknesses:**
- Requires phone number (identity anchor)
- Centralized servers (single point of failure/blocking)
- Based in USA (subject to US law)
- Phone number visible to contacts

**Threat model:** Protects message content from everyone including Signal. Does not provide anonymity (phone number links to identity).

**Setup:** See [Signal Hardening Guide](Signal-Hardening-Guide.md)

---

### Session

**Best for:** Anonymous communication, users who can't share phone numbers

**Strengths:**
- No phone number or email required
- Decentralized network (Oxen Service Nodes)
- Onion routing (like Tor) for metadata protection
- Open source
- Multi-device without phone as primary

**Weaknesses:**
- Smaller network effect (fewer users)
- Slower message delivery (onion routing adds latency)
- Younger project, less battle-tested
- No voice/video calls (as of 2025)
- Group features less mature than Signal

**Threat model:** Designed for anonymity. No central server knows who talks to whom.

**Setup:**
1. Download from [getsession.org](https://getsession.org/)
2. Generate Session ID (no registration needed)
3. Back up your recovery phrase (critical—only way to recover account)
4. Share Session ID with contacts

**Session ID example:** `05abc123def456...` (66 characters)

---

### Element (Matrix Protocol)

**Best for:** Large groups, communities, self-hosters, bridging to other platforms

**Strengths:**
- Federated—anyone can run a server
- Can self-host for complete control
- Bridges to Slack, Discord, IRC, Signal, etc.
- End-to-end encryption (when enabled)
- Web, desktop, and mobile apps
- Good for large communities
- Open standard (not controlled by one company)

**Weaknesses:**
- E2EE not enabled by default (must enable per-room)
- Server operator sees metadata (who talks to whom, when)
- Complex setup for encrypted rooms
- Key verification UX can be confusing
- Some features break with encryption enabled

**Threat model:** With E2EE enabled, protects content from server operators. Metadata (who's in rooms, when messages sent) visible to server. Self-hosting mitigates server trust issues.

**Setup (using public server):**
1. Download Element from [element.io](https://element.io/)
2. Create account on matrix.org (default) or choose another server
3. For private conversations, create a DM and verify it shows "Encrypted"
4. For groups, create room → Settings → Security → Enable encryption

**Setup (self-hosted):** See [Self-Hosting Infrastructure](../primers/Self-Hosting-Infrastructure.md)

---

### SimpleX

**Best for:** Maximum metadata privacy, technical users

**Strengths:**
- No user identifiers at all (no phone, no username, no account)
- Each conversation uses different addresses
- Servers can't correlate who talks to whom
- Double-ratchet encryption (like Signal)
- Decentralized (anyone can run servers)
- Open source

**Weaknesses:**
- Newer project, smaller user base
- UX more complex than Signal
- No username means sharing contact info is manual
- Relays are less reliable than centralized services

**Threat model:** Even server operators can't determine who's communicating with whom. Near-zero metadata.

**Setup:**
1. Download from [simplex.chat](https://simplex.chat/)
2. App generates your first receiving address
3. Share your address link/QR code with contacts
4. Each contact gets a different link (one-time use recommended)

---

### Briar

**Best for:** Protests, offline communication, high-threat environments

**Strengths:**
- Works without internet (Bluetooth, Wi-Fi direct, mesh)
- Peer-to-peer (no servers at all)
- Messages stored only on devices
- Tor integration when internet available
- Designed for activists in hostile environments
- Open source

**Weaknesses:**
- Both users must be online to sync (no offline message delivery)
- Android only (no iOS, limited desktop)
- Battery-intensive (maintains P2P connections)
- Smaller user base
- Basic features only (text, images, forums)

**Threat model:** No servers means no central point to compromise. Even with network surveillance, Tor usage hides Briar traffic. Offline mesh mode leaves no network trace.

**Setup:**
1. Download from [briarproject.org](https://briarproject.org/) or F-Droid
2. Create account (stored only on your device)
3. Add contacts by scanning QR codes in person (most secure) or via links
4. Enable Tor for internet connectivity

**Field use:** At protests where cell networks are monitored or jammed, Briar can create local mesh networks using Bluetooth/Wi-Fi. Requires contacts to be physically nearby.

---

### Wire

**Best for:** Business use, European compliance, teams

**Strengths:**
- End-to-end encrypted by default
- No phone number required (email works)
- Good team/business features
- EU-based (Swiss jurisdiction)
- Open source
- Cross-platform with good desktop support

**Weaknesses:**
- Stores more metadata than Signal
- Business model depends on paid tiers
- Smaller user base
- Has had security issues in past (fixed)

**Threat model:** Encrypts content, but Wire servers see social graph (who talks to whom) and some metadata.

**Setup:**
1. Download from [wire.com](https://wire.com/)
2. Register with email (or phone)
3. Verify contacts through fingerprint comparison

---

### Threema

**Best for:** Users wanting European privacy, one-time purchase model

**Strengths:**
- Swiss-based, strong privacy laws
- One-time purchase (no subscription, no ads)
- No phone number or email required (Threema ID only)
- E2EE by default
- Minimal metadata
- NFC contact verification

**Weaknesses:**
- Paid app (~$5)
- Smaller user base outside Europe
- Closed source until recently (now open source)
- Server code not fully open source

**Threat model:** Similar to Signal for content protection. Threema ID provides some anonymity (not linked to phone/email unless you choose to link).

**Setup:**
1. Purchase from App Store/Play Store (~$5)
2. Generate Threema ID
3. Optionally link phone/email for discoverability
4. Add contacts via ID, QR code, or phone/email

---

## Choosing by Threat Model

### "I just want better privacy than WhatsApp/SMS"
**Use: Signal**

Easiest transition, most contacts will already have it or can easily install it.

### "I need anonymity—can't use my phone number"
**Use: Session or SimpleX**

Session is more mature; SimpleX has better metadata protection.

### "I'm organizing and need large group coordination"
**Use: Element (Matrix)**

Better group management, can self-host, bridges to other platforms.

### "I'm at a protest with unreliable cell service"
**Use: Briar**

Works over Bluetooth/Wi-Fi when internet is down or monitored.

### "I need secure business communication"
**Use: Wire or Element**

Wire for simplicity, Element for self-hosting and compliance control.

### "I want maximum security and can accept complexity"
**Use: SimpleX or Session over Tor**

Minimal to zero metadata, requires more setup and operational discipline.

---

## Multi-Messenger Strategy

Different contexts call for different tools. Consider using:

| Context | Messenger | Why |
|---------|-----------|-----|
| Family/friends | Signal | Easy, encrypted, they probably have it |
| Activism/organizing | Signal + Briar | Signal for planning, Briar for field backup |
| Anonymous sources | Session or SimpleX | No identity anchor |
| Large communities | Element | Scales better, more features |
| Maximum security contacts | SimpleX | Metadata-free |

**Operational security:** Don't discuss one secure messenger on another. Don't link your identities across messengers.

---

## Features Comparison

### Voice/Video Calls

| Messenger | Voice Calls | Video Calls | Group Calls |
|-----------|-------------|-------------|-------------|
| Signal | Yes (E2EE) | Yes (E2EE) | Yes (up to 40) |
| Session | No | No | No |
| Element | Yes (E2EE) | Yes (E2EE) | Yes |
| SimpleX | Yes (E2EE) | No | No |
| Briar | No | No | No |
| Wire | Yes (E2EE) | Yes (E2EE) | Yes |
| Threema | Yes (E2EE) | Yes (E2EE) | Yes |

### Group Size Limits

| Messenger | Max Group Size |
|-----------|----------------|
| Signal | 1,000 |
| Session | ~100 |
| Element | Unlimited |
| SimpleX | Small groups |
| Briar | Unlimited (forums) |
| Wire | 500 |
| Threema | 256 |

### Disappearing Messages

All listed messengers support disappearing/ephemeral messages except Briar (messages delete when app is uninstalled or manually deleted).

---

## Red Flags to Avoid

**Do not use these for sensitive communication:**

| Messenger | Why Not |
|-----------|---------|
| **Telegram** | E2EE off by default, only in "secret chats," server-side encryption questionable, metadata-heavy |
| **WhatsApp** | Owned by Meta, metadata collection, backups may not be encrypted, closed source |
| **iMessage** | Apple holds keys for iCloud backups, closed source, Apple ecosystem only |
| **Discord** | No E2EE, all messages readable by Discord, designed for gaming not security |
| **Slack** | No E2EE, employer can read all messages, designed for business not privacy |
| **Facebook Messenger** | Meta owns everything, E2EE optional and new, massive metadata collection |

---

## Setup Checklist

Regardless of which messenger you choose:

1. [ ] Download from official source only
2. [ ] Enable E2EE (if not default)
3. [ ] Enable disappearing messages
4. [ ] Disable read receipts if available
5. [ ] Disable link previews
6. [ ] Enable screen lock within the app
7. [ ] Enable registration lock / account protection if available
8. [ ] Verify contacts' identity through another channel
9. [ ] Back up recovery phrases/keys securely
10. [ ] Keep the app updated

---

## Additional Resources

- [EFF Surveillance Self-Defense](https://ssd.eff.org/)
- [Privacy Guides - Real-Time Communication](https://www.privacyguides.org/en/real-time-communication/)
- [Signal Hardening Guide](Signal-Hardening-Guide.md)
- [Emergency Communications Playbook](Emergency-Comms-Playbook.md)

---

*The best messenger is the one your contacts will actually use. Start with Signal for most people, add specialized tools as needed.*
