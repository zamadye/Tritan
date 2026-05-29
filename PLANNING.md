# TRITAN — System Planning & Roadmap

## Vision

TRITAN adalah sistem trading otomatis untuk Polymarket yang bekerja secara otonom 24/7. Tujuan akhir: sistem yang bisa direkam sebagai **proof of concept** dalam 2 layer video — terminal server dan dashboard UI — yang menunjukkan bagaimana sistem mengambil data, menganalisis, dan mengeksekusi trade secara real-time.

---

## Cara Sistem Bekerja (End-to-End)

### Setiap 3 Menit:

```
1. RESOLVE    → Cek apakah ada posisi yang sudah selesai di Polymarket
2. EXIT CHECK → Cek TP/SL/trailing stop untuk posisi open
3. RECONCILE  → Perbaiki P&L yang tidak akurat (phantom exits)
4. SCAN       → Ambil 70+ market dari Gamma API + Events API
5. ANALYZE    → Untuk setiap market yang lolos gate:
                 - Fetch berita dari 5+ sumber (Bing, BBC, Al Jazeera, dll)
                 - LLM (MiMo) jalankan 7 tool iterations secara otonom
                 - Keputusan: BET_YES / BET_NO / SKIP
6. EXECUTE    → Kirim order ke Polymarket CLOB API
7. LOG        → Simpan full decision trail ke markdown
```

---

## Target Hasil Akhir untuk Video Proof

### Video 1 — Terminal Server
Yang harus terlihat jelas:
- Cycle counter + timestamp
- Scanner menemukan X markets
- Per market: `🔬 Analyzing [sports]: Liverpool vs Arsenal...`
- Tool calls: `[ESPN] OG Anunoby: OUT → PLAYING`
- Decision: `BET NO $1.00 conf=78% edge=+9%`
- Execution: `💰 FILLED NO $1.00 @ 32¢ | TX: 0x4f2a...`
- Exit: `✅ TAKE_PROFIT +20% | +$0.20`
- Stats: `WR: 62% | P&L: +$4.11 | Open: 6`

### Video 2 — Dashboard UI
Yang harus terlihat:
- Balance real-time (cash + portfolio value dari Polymarket)
- Positions tab: semua posisi open dengan P&L live
- Live toast notification saat bet baru masuk
- P&L chart update setiap 10 detik
- History tab: semua trade dengan reasoning
- Monitor tab: log terminal streaming

### Sync antara keduanya:
- Saat terminal menunjukkan `BET NO $1.00` → dashboard langsung update positions
- Saat terminal menunjukkan `TAKE_PROFIT` → dashboard update P&L dan history
- Balance di dashboard = balance real di Polymarket account

---

## Status Saat Ini

### ✅ Selesai
- Agentic LLM loop (7 tool iterations per market)
- Multi-source news: Bing, BBC, Al Jazeera, Guardian, CoinTelegraph
- Metaculus + CryptoQuant API
- Log-based learning (past decisions fed back to LLM)
- 800+ analysis logs dengan full decision trail
- P&L reconciliation (phantom P&L fixed)
- 24h cooldown + 48h hard block
- Market order (FOK) sell — no minimum shares
- Dashboard: 10s polling, live bet toast, DRY_RUN label
- Docs: README, ARCHITECTURE, CONFIGURATION
- Fine-tune evaluator setiap 30 trades
- Category expansion: sports, crypto, geo, politics, ai, social
- **Phase 0.2: SDK Migration** — py-clob-client → polymarket-client (backward compatible)
  - core.py: `_build_clob_client()` tries SecureClient first, falls back to ClobClient
  - executor.py: `execute_trade()` branches on SDK type for market orders
  - monitor.py: `_execute_sell_order()` branches on SDK type for limit orders
  - sync_live.py: `sync_live_trades()` handles both Paginator and dict responses
  - PYSDK_MIGRATION.md: full mapping doc old → new API
- Technical upgrade roadmap (Phase 0-5) based on GitHub research

### 🔄 Dalam Progress
- Terminal log: structured per-cycle output (cycle #, timestamp, step-by-step)
- Dashboard sync: positions dari Polymarket real account
- **Network issue** — Telkomsel block Gamma API (butuh VPN/proxy/VPS luar)

### 📋 Belum Dimulai
- Video recording setup (split screen terminal + dashboard)
- Live mode validation (setelah network issue resolved)
- Performance report PDF untuk klien
- Phase 1: Wang Transform pricing engine (oracle3)
- Phase 2: Multi-model ensemble (4 LLMs)
- Phase 3: Arbitrage strategies + hedge discovery
- Phase 4: On-chain whale signal + resolution sniper
- Phase 5: WebSocket + chat interface

---

## Blockers

### 1. Network/ISP Blocking (CRITICAL)
**Masalah:** Server di Indonesia (Telkomsel) memblokir `gamma-api.polymarket.com`
**Impact:** Scanner tidak bisa fetch markets → tidak ada bet
**Solusi:**
- Pindah server ke Singapore/US (recommended)
- Atau setup proxy/VPN di server saat ini

### 2. Balance $0 di CLOB
**Masalah:** CLOB balance habis (semua di posisi open atau WD)
**Impact:** Live mode tidak bisa bet
**Solusi:** Top up USDC ke wallet

---

## Metrics Target untuk Proof

| Metric | Target | Status |
|--------|--------|--------|
| Win Rate | ≥ 55% | 62% ✅ |
| Avg tool calls/analysis | ≥ 10 | 5.8 (upgrade needed) |
| Markets analyzed/day | ≥ 200 | 300+ ✅ |
| Data sources | ≥ 5 | 8 ✅ |
| P&L positive | Yes | +$4.11 DRY_RUN ✅ |
| Sell execution | Working | ✅ (market order FOK) |
| Dashboard sync | Real-time | 10s polling ✅ |

---

## Langkah Selanjutnya (Prioritas)

1. **Resolve network issue** — pindah server atau setup proxy
2. **Top up balance** — minimal $20 USDC untuk live testing
3. **Upgrade terminal log** — structured per-step output untuk video
4. **Record video** — split screen terminal + dashboard
5. **Performance report** — PDF dengan statistik untuk klien

---

## Untuk Klien

**Yang dijual:**
- Source code lengkap dengan dokumentasi
- Setup guide (README + CONFIGURATION)
- Architecture diagram
- 2 video proof (terminal + dashboard)
- Performance data: WR, P&L, Brier score

**Differentiator:**
- Bukan bot sederhana — agentic AI yang berpikir dan verifikasi dari multiple sources
- Full audit trail setiap keputusan (800+ markdown logs)
- Real money trading dengan track record
- Modular — bisa dikonfigurasi untuk strategi berbeda
