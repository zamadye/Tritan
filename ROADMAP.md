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

---

# Technical Upgrade Roadmap

Berdasarkan riset 10+ GitHub repos (Mei 2026). Sumber: oracle3, HarrierOnChain, Polymarket py-sdk, PolyClaw, Kalshi AI Bot, dr-manhattan, daily_stock_analysis, valory-xyz/trader.

## Phase 0: Infrastructure Fix (CRITICAL)

### 0.1 Network/ISP Blocking
**Status:** BLOCKED
**Masalah:** Telkomsel block `gamma-api.polymarket.com` (internetbaik redirect)
**Solusi:**
- Pindah server ke Singapore/US (VPS $5/bulan) ← recommended
- Atau setup WireGuard VPN / proxy SOCKS5

### 0.2 SDK Migration: py-clob-client → py-sdk
**Status:** NOT STARTED | **Priority:** HIGH | **Effort:** 2-3 hari
**Source:** https://github.com/Polymarket/py-sdk (py-clob-client sudah archived)
**Impact:** Mencegah breakage saat old SDK deprecated

- [ ] Install `pip install polymarket`
- [ ] Refactor `_build_clob_client()` di `core.py`
- [ ] Update `execute_trade()` di `executor.py`
- [ ] Update `_execute_sell_order()` di `monitor.py`
- [ ] Update `sync_live_trades()` di `sync_live.py`
- [ ] Test demo → live

---

## Phase 1: Pricing Engine Upgrade

### 1.1 Wang Transform Fair-Value Model
**Source:** https://github.com/YichengYang-Ethan/oracle3 (240 stars)
**Priority:** HIGH | **Effort:** 1-2 minggu

Model pricing ilmiah trained di 291K+ resolved contracts. Exploit favorite-longshot bias (market 50/50 biasanya trade di ~0.57). Jadi second opinion ke MiMo LLM.

- [ ] Clone oracle3, pelajari Wang Transform engine
- [ ] Implement `agent/wang_transform.py`
- [ ] Integrate ke `analyzer.py` sebagai p_base alternatif
- [ ] Decision: kalau Wang + MiMo agree → high confidence

### 1.2 Favorite-Longshot Bias Correction
**Priority:** MEDIUM | **Effort:** 3-5 hari

- [ ] Tambah bias correction di `analyzer.py`
- [ ] p_market < 0.20 → koreksi ke atas (longshot overpriced)
- [ ] p_market > 0.80 → koreksi ke bawah (favorite underpriced)

---

## Phase 2: Multi-Model Ensemble

### 2.1 Multi-LLM Architecture
**Source:** https://github.com/0mnjb/Kalshi-AI-Trading-Bot (83 stars)
**Priority:** HIGH | **Effort:** 1-2 minggu

```
MiMo (forecaster) + Claude (bull) + GPT-4o (bear) + Gemini (risk)
→ Trade hanya saat weighted consensus (3/4 atau 4/4 agree)
```

- [ ] Tambah `agent/llm_ensemble.py`
- [ ] MiMo = forecaster, Claude = bull case, GPT-4o = bear case, Gemini = risk manager
- [ ] Update `analyzer.py` untuk query semua LLMs
- [ ] Implement weighted consensus logic
- [ ] Budget: max $5/hari API cost

### 2.2 Category Scoring System
**Source:** Kalshi AI Bot | **Priority:** MEDIUM | **Effort:** 3-5 hari

- [ ] Tambah `agent/category_scorer.py`
- [ ] Score per category 0-100 berdasarkan WR historis
- [ ] Block category dengan score < 30

---

## Phase 3: Arbitrage & Hedging

### 3.1 Cross-Market Arbitrage (8 strategies)
**Source:** oracle3 | **Priority:** MEDIUM | **Effort:** 2-3 minggu

1. Exclusivity: Market A + B mutual exclusive, harga A + B < 1.0
2. Implication: A implies B, tapi harga A > B
3. Cross-venue: Harga beda di Polymarket vs Kalshi
4. Event sum: Market yang harus sum to 1.0 tapi tidak

- [ ] Tambah `agent/arbitrage.py`
- [ ] Scan related markets (sama event/topic)
- [ ] Execute both sides simultaneously

### 3.2 Hedge Discovery
**Source:** https://github.com/chainstacklabs/polyclaw (345 stars)
**Priority:** MEDIUM | **Effort:** 1-2 minggu

- [ ] Tambah `agent/hedger.py`
- [ ] Contrapositive logic: scan market lain untuk hedge logis
- [ ] Tier: T1 (95%+), T2 (90%+), T3 (85%+), T4 (<85%)
- [ ] Auto-execute T1 hedges

---

## Phase 4: Signal Enhancement

### 4.1 On-Chain Whale Signal
**Source:** HarrierOnChain (242 stars) | **Priority:** MEDIUM | **Effort:** 1-2 minggu

- [ ] Tambah `agent/whale_monitor.py`
- [ ] Track top 10 Polymarket wallets via Polygon RPC
- [ ] Decode CTF transfer + order calldata
- [ ] Signal: whale buy → boost confidence (3-30s lead time)

### 4.2 Resolution Sniper
**Source:** HarrierOnChain | **Priority:** LOW | **Effort:** 3-5 hari

- [ ] Tambah `agent/sniper.py`
- [ ] Beli outcome >= 95% atau <= 5% untuk guaranteed payout
- [ ] Expected: 1-5% per trade, very high WR

---

## Phase 5: Dashboard Upgrade

### 5.1 Real-Time WebSocket (replace polling)
**Source:** dr-manhattan | **Priority:** LOW | **Effort:** 1 minggu

### 5.2 Strategy Chat Interface
**Source:** daily_stock_analysis (39.3K stars) | **Priority:** LOW | **Effort:** 1 minggu

---

## Timeline

| Phase | Duration | Dependencies |
|-------|----------|-------------|
| Phase 0: Infrastructure | 3-5 hari | Network fix |
| Phase 1: Pricing Engine | 2-3 minggu | Phase 0 |
| Phase 2: Multi-Model | 2-3 minggu | Phase 0 |
| Phase 3: Arbitrage | 3-4 minggu | Phase 1 |
| Phase 4: Signals | 2-3 minggu | Phase 0 |
| Phase 5: Dashboard | 2-3 minggu | Phase 1-2 |

## Budget

| Item | Cost |
|------|------|
| VPS (Singapore/US) | $5-10/bulan |
| LLM API (multi-model) | $5/hari = $150/bulan |
| Polygon RPC | $0 (public) |
| **Total** | **~$160-170/bulan** |
