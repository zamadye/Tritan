# TRITAN — Progress Report & Platform Summary
**Last Updated:** 2026-05-08

---

## Apa Itu TRITAN?

TRITAN adalah sistem trading otomatis untuk **Polymarket** — platform prediction market terbesar di dunia. Sistem ini tidak menebak outcome (siapa yang menang, apakah event terjadi), melainkan **memprediksi pergerakan harga** kontrak YES/NO dalam 4-24 jam ke depan.

### Filosofi Inti
> "Bukan siapa yang benar, tapi siapa yang lebih cepat membaca pergerakan harga."

Polymarket adalah pasar. Harga bergerak berdasarkan informasi baru, sentiment, dan ketidakseimbangan antara pembeli dan penjual. TRITAN mencari gap antara harga pasar dan nilai statistik yang sebenarnya, lalu masuk sebelum pasar menyesuaikan diri.

---

## Bagaimana Cara Kerjanya?

```
Scan market (Gamma API)
    ↓
Statistical Gate — gap p_base vs harga pasar ≥ 8%
    ↓
AI Analysis (MiMo LLM) — apakah ada catalyst yang akan gerakkan harga?
    ↓
Confidence Gate — AI harus ≥ 60% yakin
    ↓
Kelly Position Sizing — ukuran bet proporsional dengan edge
    ↓
Execute (demo: catat | live: kirim order ke Polymarket CLOB)
    ↓
Auto-Exit:
  Sports → tunggu resolved (resolve cepat <24 jam)
  Crypto/Geo → trailing stop + max 24 jam
  Dynamic TP: edge ≥ 20% → TP 40%, edge ≥ 15% → TP 30%, default → TP 15%
    ↓
Resolver → cek outcome, hitung P&L, update Brier score
    ↓
AI Trade Monitor → analisis hasil, rekomendasikan perbaikan config
```

---

## Status Saat Ini (2026-05-08)

### System Status
| Komponen | Status |
|----------|--------|
| Agent (Python) | ✅ Running via PM2 |
| Dashboard (Next.js) | ✅ Running di port 3000 |
| Demo Mode | ✅ Aktif |
| Live Mode | ⏳ Siap, belum diaktifkan |

### Demo Performance (Fresh Start — Strategi Baru)
| Metric | Nilai |
|--------|-------|
| Total Trades | 11 |
| Open Positions | 10 |
| Resolved | 1 |
| Bankroll | $500 (virtual) |
| Bet Size | $2-5 per trade |

> Data masih sangat awal (11 trades). Target: 300 trades untuk validasi statistik.

### Config Aktif
| Setting | Nilai | Keterangan |
|---------|-------|------------|
| `MIN_STAT_EDGE` | 8% | Gap minimum model vs pasar |
| `MIN_STAT_EDGE_HIGH_RISK` | 10% | Untuk crypto/geo/politics |
| `MIN_CONFIDENCE` | 60% | Confidence minimum AI |
| `MAX_OPEN_POSITIONS` | 20 | Maksimum posisi terbuka |
| `MAX_OPEN_PER_CATEGORY` | 8 | Batas per kategori |
| `EXIT_TAKE_PROFIT` | 15% | TP floor (dinamis berdasarkan edge) |
| `EXIT_STOP_LOSS` | 12% | SL (dinamis berdasarkan leverage) |
| `MIN_HOLD_MINUTES` | 30 | Minimum hold sebelum exit |
| `EXIT_MAX_HOURS` | 24 | Max hold non-sports |

---

## Progress Dev — Apa yang Sudah Selesai

### ✅ Core Agent (Python)
- [x] Scanner — ambil market dari Gamma API dengan filter volume/liquidity/days
- [x] Statistical prior — logistic regression dari 19,624 resolved markets
- [x] Calibration model per kategori (sports, crypto, geo, politics, other)
- [x] Agentic LLM analyzer — MiMo v2.5 dengan tool calls (search, crypto price, sports data)
- [x] Kelly position sizing dengan bankroll compounding (level system)
- [x] Executor — demo simulation + live CLOB order execution
- [x] Monitor — auto-exit: TP dinamis, SL dinamis per leverage, trailing stop, time limit
- [x] Resolver — cek outcome dari Gamma API, hitung P&L dan Brier score
- [x] Learner — evolution lessons, pattern library, overconfidence tracking
- [x] Correlation control — max posisi per kategori, max exposure per kategori

### ✅ Bug Fixes (Audit Lengkap)
- [x] `datetime.now()` naive → `timezone.utc` di semua file
- [x] Hardcoded Alchemy API key → `POLYGON_RPC_URL` env var
- [x] Live bankroll → `clob_client.get_balance()` bukan RPC call
- [x] Bankroll state pisah demo/live (`bankroll_state.json` vs `bankroll_state_live.json`)
- [x] `_update_calibration` dead code diperbaiki
- [x] `_get_token_id` — token_id sudah list, tidak perlu `json.loads()`
- [x] P&L NO bets — pakai `1 - price_at_entry` bukan `price_at_entry`
- [x] Monitor exit defaults align dengan `.env.example`
- [x] `effective_sl_pct` used before assignment — reorder fixed
- [x] Duplikat bet — pakai full question sebagai key bukan `[:60]`
- [x] Pure stat bet tanpa catalyst diblokir

### ✅ Strategy Updates
- [x] Prompt analyzer: dari "predict outcome" → "predict price movement"
- [x] Sports: tunggu resolved (tidak ada time limit)
- [x] Crypto/Geo: max 24 jam hold
- [x] Dynamic TP berdasarkan edge awal (15-40%)
- [x] Dynamic SL berdasarkan leverage entry (12-36%)
- [x] Minimum hold 30 menit sebelum exit
- [x] Catalyst required untuk bet (pure stat tidak cukup)

### ✅ Dashboard (Next.js)
- [x] Overview tab — KPI cards, P&L chart, model accuracy, LLM cost
- [x] Positions tab — open trades dengan stats dan reasoning
- [x] Trades tab — full history dengan filter, search, pagination
- [x] Learning tab — evolution lessons, exit breakdown, winning patterns
- [x] Proof tab — model vs market, calibration table, audit trail
- [x] Config tab — semua env vars dengan deskripsi, accordion layout, SVG icons
- [x] AI Trade Monitor Assistant — floating chat 🤖, auto-fill config, trade close trigger
- [x] Onboarding guide — popup pertama masuk, 2 bahasa (EN/ID)
- [x] Mobile-first design — bottom navigation bar, card layout
- [x] Stats API — bankroll dari .env, semua resolved trades (bukan 20 terakhir)
- [x] Settings API — GET/POST env vars, pm2 restart otomatis

---

## Yang Masih Perlu Dikerjakan (Private Phase)

### 🔄 Immediate (Minggu Ini)
- [ ] Kumpulkan 300 trade data dengan strategi baru
- [ ] Monitor WR dan avg win per trade
- [ ] Validasi: WR ≥ 55%, avg win ≥ $0.22, profit > 3x LLM cost

### 📋 Short Term (2-4 Minggu)
- [ ] Tutorial/Guide page lengkap (EN/ID) — step by step setup
- [ ] Login form — single user, token-based auth
- [ ] Credential input form — Polymarket API keys dari dashboard
- [ ] Twitter/X integration untuk early signal (crypto & geo)
- [ ] Tambah `MIN_HOLD_MINUTES` dan `MIN_CATALYST_SCORE` ke Config tab

### 📋 Medium Term (1-2 Bulan)
- [ ] Validasi 3 bulan profit konsisten sebelum launch publik
- [ ] Performance sharing — generate equity curve image untuk social media
- [ ] Telegram notification — alert saat trade close, win/loss summary harian

---

## Roadmap Publik (Setelah Private Phase Selesai)

### Fase 1 — Beta Launch (Bulan 4-5)
**Trigger:** 300 trades, WR ≥ 52% konsisten 3 bulan

- Multi-user backend (PostgreSQL + encrypted credentials)
- Google OAuth login
- Waitlist system (50 slots free 1 bulan)
- Per-user bot instance

### Fase 2 — Paid Launch (Bulan 6)
**Subscription tiers:**
| Tier | Harga | Fitur |
|------|-------|-------|
| Free | $0 | Signal crypto/geo saja, manual bet |
| Starter | $29/mo | Auto-execute up to $50 exposure |
| Pro | $79/mo | Full auto-execute up to $500, semua kategori |
| Fund | $299/mo | Unlimited, multi-wallet, API access |

### Fase 3 — Growth (Bulan 7-12)
- Analytics dashboard per user
- Leaderboard anonymous
- "Share your month" — equity curve image
- Knowledge base query
- Social layer (copy top performer)

### Fase 4 — Scale (Tahun 2)
- Mobile app / Telegram bot
- API access untuk Pro/Fund
- Target valuation: $500k-$1M (4-5x ARR)

---

## Security Model (Untuk Publik)

**Non-custodial** — platform tidak pernah pegang private key user.

```
User input L2 API credentials (apiKey + secret + passphrase)
    ↓
Encrypted dengan Fernet (AES-128-CBC)
key = PBKDF2(MASTER_KEY + user_id)
    ↓
Simpan ciphertext di DB (plain text tidak pernah tersimpan)
    ↓
Saat execute: decrypt in-memory → pakai → discard
    ↓
User bisa revoke kapanpun dari Polymarket settings
```

**Yang user perlu tahu:**
- Dana tetap di wallet user — platform hanya bisa place orders, tidak bisa withdraw
- Revoke API credentials kapanpun = bot berhenti instantly
- Setiap trade ter-log dan bisa diaudit

---

## Kalkulasi Viabilitas (Live Mode)

### Asumsi: $50 bankroll, bet $1-2
| WR | Avg Win | Gross/hari | LLM Cost | Net/hari |
|----|---------|------------|----------|----------|
| 55% | $0.30 | +$0.84 | $0.59 | +$0.25 |
| 60% | $0.50 | +$2.28 | $0.59 | +$1.69 |
| 65% | $0.50 | +$2.62 | $0.59 | +$2.03 |

**Break-even:** avg win per trade > $0.22 (14.6% return per winning trade)

### Token Budget
- Total token limit: 200M
- Terpakai: ~5.7M (2.9%)
- Sisa: ~194M → cukup untuk ~68 hari di rate sekarang
- Setelah 300 trade demo: masih ~182M → cukup 10+ bulan live mode

---

## Filosofi Pengembangan

1. **Prove first, launch later** — 3 bulan data sebelum publik
2. **Demo = Live** — semua logic identik, hanya eksekusi yang berbeda
3. **Audit trail** — setiap keputusan tercatat: p_base, confidence, edge, tool calls
4. **Non-custodial** — user selalu kontrol dana mereka
5. **Transparent** — performance publik, verifiable, tidak ada klaim palsu

---

## Moat (Keunggulan yang Sulit Ditiru)

1. **Proprietary dataset** — 19,624 resolved markets dengan calibration model. Kompetitor butuh 2-3 tahun untuk replicate.
2. **Calibration model** — terus improve setiap hari berjalan. Kompetitor yang baru mulai selalu tertinggal.
3. **Track record** — 3 tahun performance history yang verified dan auditable.
4. **User behavior data** — setelah ribuan trades, tau pattern mana yang work per profil user.
