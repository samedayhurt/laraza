# Signal Hardening Guide

Signal is the gold standard for secure messaging—end-to-end encrypted, open source, and metadata-minimized. This guide covers installation, hardening, and operational security practices.

---

## Why Signal?

| Feature | Signal | SMS/iMessage | WhatsApp | Telegram |
|---------|--------|--------------|----------|----------|
| End-to-end encryption | Always | Partial | Yes | Optional |
| Open source | Yes | No | No | Partial |
| Metadata minimization | Yes | No | No | No |
| No ads/tracking | Yes | No | No | No |
| Disappearing messages | Yes | Limited | Yes | Yes |
| Self-destructing media | Yes | No | Yes | Yes |

**Signal's advantages:**
- Encryption is always on, no way to disable it
- Open source—anyone can audit the code
- Minimal metadata collection (only phone number and last connection time)
- Non-profit organization, not ad-supported
- Recommended by EFF, ACLU, and security researchers worldwide

---

## Installation

### Download from Official Sources Only

**Never download Signal from third-party sites.** Fake Signal apps exist and can compromise your security.

| Platform | Official Source |
|----------|-----------------|
| Android | [signal.org/android](https://signal.org/android) or Google Play Store |
| iPhone | App Store (search "Signal Private Messenger") |
| Desktop | [signal.org/download](https://signal.org/download) |
| F-Droid | Not available (F-Droid build process incompatible with Signal's security model) |

**Android without Google Play:**
1. Go to [signal.org/android/apk](https://signal.org/android/apk)
2. Download the APK
3. Verify the checksum (listed on the page)
4. Install manually

### Initial Setup

1. **Install the app**
2. **Enter your phone number** — Signal requires a phone number for registration
3. **Verify via SMS or phone call**
4. **Create a PIN** — This is critical, don't skip it

---

## Registration Privacy

### Using a Secondary Number

Your Signal phone number is visible to anyone you message. For additional privacy, consider registering with a secondary number:

**Options for secondary numbers:**

| Service | Privacy Level | Cost | Notes |
|---------|---------------|------|-------|
| Google Voice | Low | Free | Tied to Google account |
| MySudo | Medium | $0.99-14.99/mo | Up to 9 numbers, designed for privacy |
| Hushed | Medium | $1.99-4.99/mo | Temporary or long-term numbers |
| JMP.chat | High | $2.99/mo | XMPP-based, accepts crypto |
| Prepaid SIM | High | $10-30 once | Cash-purchased, most private |

**Cash-purchased prepaid SIM (Most Private):**
1. Buy a prepaid SIM card with cash (Tracfone, Mint Mobile, etc.)
2. Activate using a VPN and minimal/fake info where possible
3. Use for Signal registration only
4. Can keep the SIM inactive after registration (Signal doesn't require ongoing cell service)

**Note:** Once registered, changing your Signal number notifies your contacts. Choose carefully.

---

## Security Settings

Open Signal → tap your profile picture → **Settings**

### Privacy Settings

**Settings → Privacy:**

| Setting | Recommendation | Why |
|---------|----------------|-----|
| Screen Lock | **Enable** | Requires phone unlock to open Signal |
| Screen Security | **Enable** | Blocks screenshots, hides in app switcher |
| Incognito Keyboard | **Enable** | Prevents keyboard from learning your typing |
| Read Receipts | **Disable** for sensitive contacts | Don't reveal when you've read messages |
| Typing Indicators | **Disable** | Don't reveal when you're typing |
| Link Previews | **Disable** | Previews can leak info to linked sites |
| Relay Calls | **Enable** | Routes calls through Signal servers, hiding your IP |

### Disappearing Messages

**Critical for operational security.** Messages auto-delete after a set time.

**To enable default disappearing messages:**
1. Settings → Privacy → Default timer for new chats
2. Choose a duration (1 day to 4 weeks)

**To enable for existing chat:**
1. Open the conversation
2. Tap the contact/group name at the top
3. Tap "Disappearing messages"
4. Choose duration

**Recommendations:**
- 24 hours for highly sensitive communications
- 1 week for general activist/organizer groups
- 4 weeks for less sensitive, ongoing discussions

### Registration Lock

**Prevents someone from re-registering your number on a different device.**

1. Settings → Account → Registration Lock
2. **Enable**

This protects against SIM-swap attacks where an attacker takes over your phone number.

### Signal PIN

Your PIN encrypts your Signal data (contacts, settings, profile) in Signal's cloud backup.

**Requirements:**
- Minimum 4 digits, but longer is better
- Can be alphanumeric (Settings → Account → Change your PIN → "Create alphanumeric PIN")

**If you forget your PIN:** You'll lose your Signal data after 7 days of failed attempts. Write it down and store securely.

---

## Group Security

### Creating Secure Groups

1. Tap the pencil icon → "New group"
2. Add trusted members only
3. Give it a clear, non-identifiable name
4. Set an appropriate disappearing message timer

### Group Admin Controls

**As admin, configure:**

1. Tap group name → "Group settings"
2. **Permissions:**
   - Who can edit group info → Admins only
   - Who can send messages → All members (or Admins only for announcements)
3. **Membership:**
   - Who can add members → Admins only (recommended)
   - Approve new members → Enable if available

### Invite Links

Group invite links can be shared, which is convenient but risky.

**Best practices:**
- Disable invite links for sensitive groups
- If using links, reset them periodically
- Share links only via secure channels (not email, not social media)

### Vetting New Members

Before adding someone to a sensitive group:
1. Verify their identity through another channel
2. Meet in person if possible
3. Start with less sensitive groups, build trust over time
4. Consider a vetting process agreed upon by existing members

---

## Desktop App Security

Signal Desktop syncs with your phone and stores messages locally.

### Risks

- Computer malware can access Signal messages
- Anyone with access to your unlocked computer can read messages
- Desktop likely has weaker full-disk encryption than phone

### Hardening

1. **Enable screen lock:** Settings → Privacy → Screen Lock
2. **Use on encrypted drive:** Ensure your computer has full-disk encryption enabled
3. **Lock when away:** Always lock your computer when stepping away
4. **Consider not using Desktop:** For highest security, use Signal only on a hardened phone (GrapheneOS)

### When to Use Desktop

- Long-form writing (easier on keyboard)
- Work that doesn't require mobility
- When phone is unavailable

### When to Avoid Desktop

- Public computers (never)
- Shared computers (never)
- Computers you don't fully control
- While traveling or in hostile environments

---

## If Your Device is Seized

### Preparation (Before It Happens)

1. **Enable device encryption** (see main README)
2. **Use a strong device password** (not just fingerprint/face)
3. **Enable auto-lock** (30 seconds or less)
4. **Enable Signal screen lock**
5. **Set short disappearing message timers**
6. **Don't keep sensitive messages** — delete manually if important
7. **Know your rights** — see [Legal Observer Toolkit](../opsec/Legal%20Observer%20Toolkit.md)

### During Seizure

**You generally do NOT have to:**
- Provide your password (5th Amendment in US)
- Unlock your phone
- Provide biometrics in most jurisdictions (less clear legally)

**You should:**
- State clearly: "I do not consent to a search of this device"
- Remain silent beyond identifying yourself
- Request a lawyer

**GrapheneOS users:** Enable duress PIN (wipes device when entered)

### After Seizure

1. **Assume the device is compromised** — even if returned
2. **De-authorize the device:** On another device, go to Settings → Linked Devices → Remove the seized device
3. **Change your Signal PIN**
4. **Warn your contacts** that messages to your old device may be compromised
5. **Don't use the returned device** for sensitive communication — it may have been tampered with

---

## Operational Discipline

Technical security means nothing without behavioral security.

### Do

- Verify new contacts through another channel before sensitive discussion
- Use disappearing messages consistently
- Delete sensitive messages manually if timer is too long
- Back up important information elsewhere before it disappears
- Keep Signal and your OS updated
- Use on a hardened device (GrapheneOS ideal)

### Don't

- Screenshot sensitive messages
- Forward messages without permission
- Discuss Signal groups on other platforms ("Did you see what X posted in the Signal?")
- Add unknown people to sensitive groups
- Use Signal for anything truly illegal (it's secure, not magic)
- Assume encryption means total anonymity (metadata exists)

### Code Words and Duress Signals

Establish with your trusted contacts:

- **Code word for "I'm compromised"** — If you send this word, they should assume your device is in hostile hands
- **Check-in protocols** — Regular check-ins; missed check-in triggers concern
- **Safe words** — Confirm identity if communication seems off

**Example:**
> Normal sign-off: "Talk soon"
> Duress sign-off: "Best regards" — signals something is wrong

---

## Metadata Awareness

Signal encrypts message content, but some metadata exists:

**What Signal knows:**
- Your phone number
- When you last connected
- That you sent a message (not to whom, thanks to sealed sender)

**What Signal doesn't know:**
- Message content
- Who you're messaging (with sealed sender)
- Your contacts
- Your groups

**What your phone knows:**
- All of the above
- Full message history (if not using disappearing messages)

**What network observers see:**
- That you're using Signal (can be identified by traffic patterns)
- Timing and size of messages (not content)

**Mitigation:**
- Use VPN or Tor to hide Signal usage from network observers
- Use disappearing messages to minimize what's stored on device
- Use relay calls to hide IP from call recipients

---

## Troubleshooting

### Messages not delivering

1. Check internet connection
2. Check if contact blocked you (you won't see their status updates)
3. Check if you blocked them (Settings → Privacy → Blocked)
4. Both parties should update Signal to latest version

### Verification failed

Safety numbers change when someone reinstalls Signal or gets a new phone. This is normal but should be verified.

1. Contact them through another channel
2. Compare safety numbers: tap contact name → "View safety number"
3. If numbers match, tap "Verified"

### Can't receive calls

1. Ensure Signal has microphone permission
2. Check "Relay calls" setting (may cause issues on some networks)
3. Check if battery saver is blocking Signal

---

## Quick Reference

### Recommended Settings

```
Privacy:
  Screen Lock: ON
  Screen Security: ON
  Incognito Keyboard: ON
  Read Receipts: OFF (for sensitive contacts)
  Typing Indicators: OFF
  Link Previews: OFF
  Relay Calls: ON

Account:
  Registration Lock: ON
  PIN: Alphanumeric, 8+ characters

Default disappearing messages: 7 days or less
```

### Emergency Checklist

If you suspect compromise:
1. [ ] De-authorize all linked devices
2. [ ] Change PIN
3. [ ] Enable registration lock (if not already)
4. [ ] Alert contacts via another channel
5. [ ] Consider creating new Signal account with new number

---

## Additional Resources

- [Signal Support](https://support.signal.org/)
- [Signal Blog](https://signal.org/blog/) — Security updates and announcements
- [EFF's Signal Guide](https://ssd.eff.org/module/how-use-signal-android)
- [Security in a Box - Signal](https://securityinabox.org/en/apps/signal/)

---

*Signal is a tool, not a guarantee. Combine technical security with operational discipline for meaningful protection.*
