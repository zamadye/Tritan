# 🤖 POLYMARKET AGENT — SETUP GUIDE

## Struktur Project

```
polymarket/
├── .env                          # Config (sudah ada, jangan commit!)
├── main.py                       # Entry point CLI
├── requirements.txt              # Dependencies
├── agent/
│   ├── llm.py                    # OpenClaw LLM client (custom base_url)
│   ├── core.py                   # Main agent loop
│   ├── scanner.py                # Market scanner (Gamma API)
│   ├── analyzer.py               # Probability estimation via LLM
│   ├── executor.py               # Order execution (demo + live)
│   ├── sizer.py                  # Kelly criterion position sizing
│   └── learner.py                # Post-resolution learning system
├── data/
│   ├── demo_trades.json
│   ├── live_trades.json
│   ├── calibration.json
│   └── blacklisted_categories.json
└── prompts/
    └── POLYMARKET_AGENT_PROMPT.md
```

---

## ⚙️ OpenClaw Setup (LLM Configuration)

Agent ini menggunakan **OpenClaw** (custom Anthropic-compatible endpoint) via `agent/llm.py`.

Semua LLM call di-route melalui `AI_BASE_URL` dari `.env` — **bukan** direct ke `api.anthropic.com`.

### Variabel `.env` yang relevan:

```env
AI_API_KEY=<your-openclaw-api-key>
AI_BASE_URL=https://api.z.ai/api/anthropic/v1   # OpenClaw endpoint
AI_MODEL=glm-5.1                                  # Model yang dipakai
LLM_MAX_TOKENS=600
```

### Cara kerja `agent/llm.py`:

```python
import anthropic, os

def get_client():
    return anthropic.Anthropic(
        api_key=os.getenv("AI_API_KEY"),
        base_url=os.getenv("AI_BASE_URL"),   # ← OpenClaw endpoint
    )

def chat(prompt):
    client = get_client()
    response = client.messages.create(
        model=os.getenv("AI_MODEL"),
        max_tokens=int(os.getenv("LLM_MAX_TOKENS", 600)),
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text
```

Semua modul (`analyzer.py`, `core.py`) import dari `agent.llm` — tidak ada direct `anthropic.Anthropic()` di tempat lain.

---

## 🚀 Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Cek `.env`

Pastikan nilai berikut sudah diisi:

```env
AI_API_KEY=...          # OpenClaw API key
AI_BASE_URL=...         # OpenClaw base URL
AI_MODEL=...            # Model name
POLYGON_PRIVATE_KEY=... # Wallet key (untuk live mode)
AGENT_MODE=demo         # Mulai dengan demo!
```

### 3. Jalankan agent (DEMO MODE — aman)

```bash
python3 main.py --mode demo
```

### 4. Commands tersedia

```bash
python3 main.py run              # Jalankan agent loop (scan otomatis)
python3 main.py scan             # Scan market sekali
python3 main.py status           # Lihat stats & bankroll
python3 main.py report           # Performance report per kategori
python3 main.py history          # 20 trade terakhir
python3 main.py learn            # Calibration & learning stats
python3 main.py analyze <query>  # Analisa market manual
```

### 5. Switch ke LIVE MODE (setelah win rate > 55% dari 30+ trades)

```bash
python3 main.py --mode live
```

---

## 🔄 Alur Agent

```
STARTUP
  └─ Load .env → print banner → init CLOB client (live only)
       │
       ▼
SCAN LOOP (setiap SCAN_INTERVAL_MINUTES)
  └─ scanner.py  → ambil candidate markets dari Gamma API
       │
       ▼
  analyzer.py → fetch news (Serper) → kirim ke LLM via OpenClaw
       │
       ▼
  sizer.py    → Kelly Criterion → hitung position size
       │
       ▼
  executor.py → DEMO: log ke demo_trades.json
              → LIVE: kirim order ke CLOB API
       │
       ▼
  learner.py  → setelah market resolve: update P&L, Brier score, calibration
```

---

## 🛡️ Risk Settings (di `.env`)

| Variable | Default | Keterangan |
|---|---|---|
| `MAX_BET_SIZE` | 3.00 | Hard cap per trade (USDC) |
| `MAX_BET_PCT_OF_BANKROLL` | 0.20 | Max 20% bankroll per trade |
| `KELLY_FRACTION` | 0.25 | Quarter Kelly (konservatif) |
| `EDGE_THRESHOLD` | 0.05 | Min 5% edge untuk bet |
| `MIN_CONFIDENCE` | 0.60 | Min 60% LLM confidence |
| `MAX_DAILY_LOSS_PCT` | 0.15 | Auto-pause jika rugi >15%/hari |
| `DRY_RUN` | false | `true` = tidak execute order |

---

## ⚠️ Catatan Penting

- **Selalu mulai dengan `AGENT_MODE=demo`** — validasi strategi dulu
- **Jangan commit `.env`** — berisi private key dan API keys
- Live mode hanya unlock setelah `DEMO_MIN_WIN_RATE` (55%) dari `DEMO_MIN_TRADES` (30) resolved markets
- Set `DRY_RUN=true` untuk test live flow tanpa eksekusi nyata
