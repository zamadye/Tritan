# TRITAN — Product Roadmap

Last updated: 2026-05-08

---

## Vision

Prediction market intelligence platform. Non-custodial, transparent, verifiable.
Bukan trading bot biasa — statistical edge system dengan AI verification dan full audit trail.

---

## Business Model

**Non-custodial SaaS** — user input L2 API credentials (bukan private key).
Fund tetap di wallet user. Platform hanya execute orders atas nama user.

### Subscription Tiers (Fase 2+)
| Tier | Price | Features |
|------|-------|----------|
| Free | $0 | Demo mode, signal crypto/geo only, 5 scan/hari |
| Starter | $29/mo | Auto-execute up to $50 exposure, basic categories |
| Pro | $79/mo | Full auto-execute up to $500, all categories, agentic tools |
| Fund | $299/mo | Unlimited exposure, multi-wallet, API access |

**Unit economics:** Cost per user ~$2-3/mo → margin 90-99%

---

## Security Architecture (Fase 1+)

```
User input API creds (L2 only, bukan private key)
    ↓
HTTPS POST → Backend encrypt dengan Fernet
key = PBKDF2(MASTER_KEY + user_id)
    ↓
Simpan ciphertext di DB (plain text tidak pernah tersimpan)
    ↓
Saat execute: decrypt in-memory → pakai → discard
    ↓
Full audit log setiap action
```

User bisa revoke kapanpun dari Polymarket → bot otomatis berhenti.

---

## FASE 0 — Private Stable (Sekarang → Bulan 3)

*Target: 300 trades, WR ≥52% konsisten 3 bulan. Tidak launch sebelum ini.*

| Priority | Task | Status |
|----------|------|--------|
| P0 | Fix semua bug logic (SL, analyzer, duplikat) | ✅ Done |
| P0 | Collect 300 trade data dengan strategi baru | 🔄 Running |
| P0 | Exit strategy: sports=resolved, crypto/geo max 24h, dynamic TP | ✅ Done |
| P0 | Config via dashboard (semua env vars + deskripsi) | ✅ Done |
| P1 | **AI Trade Monitor Assistant** (dashboard floating chat) | 🔄 In Progress |
| P2 | Tutorial/Guide page (EN/ID) | ⏳ |
| P2 | Login form (single user, token-based) | ⏳ |
| P3 | Credential input form (Polymarket keys) | ⏳ |

---

## FASE 1 — Beta Launch (Bulan 4-5)

*Trigger: 300 trades resolved, WR ≥52%, equity curve upward*

- [ ] Multi-user backend (PostgreSQL + encrypted credentials)
- [ ] Google OAuth login
- [ ] Per-user bot instance (Redis job queue)
- [ ] Waitlist system (50 slots free 1 bulan)
- [ ] Performance sharing (equity curve image generator)
- [ ] Hard limits per user (max bet, daily loss limit, auto-pause)

---

## FASE 2 — Paid Launch (Bulan 6)

*Trigger: 20+ beta users aktif, feedback diimplementasi*

- [ ] Subscription billing (Stripe)
- [ ] Signal-only mode (free tier — crypto/geo)
- [ ] Auto-execute mode (paid tier — all categories)
- [ ] Referral system (1 bulan gratis per referral)
- [ ] TOS + disclaimer + risk disclosure

---

## FASE 3 — Growth Modules (Bulan 7-12)

- [ ] Analytics dashboard per user (breakdown per category, comparison ke market)
- [ ] Leaderboard anonymous ("User #23 up 34% this month")
- [ ] "Share your month" — generate equity curve image untuk social media
- [ ] Knowledge base query ("Market ini mirip 47 kasus lain, historical WR X%")
- [ ] Hire freelancer pertama (frontend atau content, setelah MRR >$3,000)

---

## FASE 4 — Scale (Tahun 2)

- [ ] Mobile app atau Telegram bot
- [ ] API access untuk Pro/Fund tier
- [ ] Social layer (copy top performer allocation)
- [ ] Explore raise atau acquisition
- [ ] Target valuation: $500k-$1M (4-5x ARR)

---

## Viral Mechanisms

1. **Performance sharing** — "Share your month" button → equity curve image → Twitter/LinkedIn
2. **Leaderboard** — anonymous ranking → FOMO
3. **Referral** — 1 bulan gratis per referral
4. **Transparency marketing** — post performance publik setiap bulan, verifiable data

---

## Moat (Defensible Advantage)

1. **Proprietary dataset** — 19,624+ resolved markets dengan calibration model (kompetitor butuh 2-3 tahun replicate)
2. **Calibration model** — terus improve setiap hari berjalan
3. **User behavior data** — setelah ribuan trades, tau pattern per profil user
4. **Track record** — 3 tahun performance history yang verified dan auditable

---

## Revenue Projection (Realistis)

| Timeline | Users | MRR |
|----------|-------|-----|
| Bulan 6 | 20 paying | ~$1,000-1,500 |
| Bulan 9 | 80-100 users | ~$5,000-8,000 |
| Bulan 12 | 150-200 users | ~$10,000-15,000 |
| Tahun 2 | 300+ users | $15,000-20,000+ |

Valuation at 4x ARR (Tahun 2): **$720k - $960k**

---

## Rules

1. **Jangan launch sebelum 3 bulan proof** — satu bulan bad performance setelah launch = reputasi rusak
2. **Jangan pegang private key user** — hanya L2 API credentials
3. **Hire untuk weakness, bukan untuk tasks yang bisa di-automate**
4. **Urutan: Prove → Secure → Beta → Paid → Scale** — tidak bisa skip
