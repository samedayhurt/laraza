# Phone Security Quickstart

**10 minutes to significantly reduce your exposure**

---

## 1. Location Permissions (3 minutes)

### iPhone
1. **Settings → Privacy & Security → Location Services**
2. Review each app. Set to:
   - **Never** → Social media, games, shopping, news, weather
   - **While Using** → Maps, navigation, ride-share
   - **Always** → Nothing (or only Find My)

### Android
1. **Settings → Location → App location permissions**
2. Same logic: **Don't allow** for most apps, **Allow only while using** for maps

---

## 2. Kill the Advertising ID (1 minute)

Your advertising ID links your activity across apps. Delete it.

### iPhone
- Settings → Privacy & Security → Tracking → **"Allow Apps to Request to Track" → OFF**
- Settings → Privacy & Security → Apple Advertising → **Personalized Ads → OFF**

### Android
- Settings → Privacy → Ads → **Delete advertising ID**
- (Or: Settings → Google → Ads → Opt out of personalization)

---

## 3. Disable Background App Refresh (1 minute)

Apps send data even when you're not using them.

### iPhone
- Settings → General → Background App Refresh → **OFF** (or selective)

### Android
- Settings → Apps → [each app] → Battery → **Restricted**

---

## 4. Review Cloud Backup (2 minutes)

Cloud backups are convenient. They're also subpoena targets.

### iPhone
- Settings → [Your Name] → iCloud
- Review what's syncing. Consider turning OFF:
  - **Messages** (if using Signal for sensitive conversations)
  - **Photos** (or use local backup only)

### Android
- Settings → Google → Backup
- Same consideration for Messages, Photos

**Alternative:** Local encrypted backup (iTunes/Finder with encryption checkbox, or Android local backup)

---

## 5. Strong PIN (1 minute)

### Change to 6+ Digits
- **iPhone:** Settings → Face ID & Passcode → Change Passcode → Passcode Options → Custom Numeric Code
- **Android:** Settings → Security → Screen lock → PIN

**Don't use:** Birthday, 123456, repeated digits, address numbers

---

## 6. Know the Biometrics Rule (30 seconds)

| | Police can force |
|--|------------------|
| **Face ID / Fingerprint** | Yes (courts have ruled) |
| **PIN / Password** | No (5th Amendment protection) |

**Before sensitive situations:** Disable biometrics

- **iPhone:** Settings → Face ID & Passcode → iPhone Unlock → OFF
- **Android:** Settings → Security → Fingerprint → Disable for unlock

**Emergency lockdown (iPhone):** Press side button 5 times → Forces PIN

---

## 7. Install Signal (2 minutes)

### Why Signal
- End-to-end encrypted (like WhatsApp)
- **Minimal metadata collection** (unlike WhatsApp)
- Non-profit, open source
- ICE can't get your conversation patterns from Signal

### Setup
1. Download from App Store / Play Store
2. Register with phone number
3. **Settings → Privacy:**
   - Screen Security → ON
   - Registration Lock → ON
   - Disappearing Messages → 1 week (recommended default)

### Move Conversations
Your Signal contacts who have Signal will appear automatically. Start moving sensitive conversations there.

---

## Quick Reference

```
┌─────────────────────────────────────────────────────────────┐
│                PHONE SECURITY PRIORITY                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  DO TODAY:                                                   │
│  □ Location permissions → Never (for most apps)             │
│  □ Delete advertising ID                                     │
│  □ Install Signal                                            │
│  □ 6+ digit PIN                                              │
│                                                              │
│  BEFORE SENSITIVE SITUATIONS:                                │
│  □ Disable Face ID / fingerprint                             │
│  □ Update phone to latest version                            │
│  □ Know where Emergency SOS is                               │
│  □ Consider: leave phone at home                             │
│                                                              │
│  IF PHONE IS SEIZED:                                         │
│  □ Do NOT unlock                                             │
│  □ "I do not consent to a search"                           │
│  □ Give PIN only if judge orders (with lawyer)               │
│                                                              │
│  CORRN (ICE emergencies): 844-864-8341                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## The Threat You're Reducing

**Location data flows like this:**

```
Your phone → App → Data aggregator → Data broker → ICE/Police (no warrant)
```

**Each step above cuts a link:**
- Denying location permission = App can't collect
- Deleting ad ID = Harder to correlate across apps
- Using Signal = Metadata not available to Meta → ICE

---

## Emergency Numbers

| Resource | Number |
|----------|--------|
| **CORRN** (ICE activity) | 844-864-8341 |
| **RMIAN Detention Hotline** | (303) 866-9308 |
| **Access Now** (digital security emergency) | accessnow.org/help |

---

*Part of Digital Hygiene: Let's Talk — January 2026*
*La Raza VII.I.IX — github.com/samedayhurt/laraza*
