# OSINT UPGRADE PLAN — Polymarket Agent
# Tujuan: Naik dari Tier 3 (lagging news) ke Tier 1/2 (leading signals)
# Target WR: 64% → 75%+

## SPRINT 1 — SPORTS (mayoritas trade, impact tertinggi)

### 1a. The Odds API (Vegas lines)
- URL: https://api.the-odds-api.com/v4/sports
- Key: butuh signup (free 500 req/month, $10/month untuk lebih)
- Data: moneyline odds dari 40+ bookmakers
- Why: Vegas aggregate semua injury/lineup info → Tier 1 signal
- Env: ODDS_API_KEY

### 1b. ESPN Injury API (real-time)
- URL: https://site.api.espn.com/apis/site/v2/sports/{sport}/injuries
- Key: tidak butuh (public)
- Data: injury status, return timeline
- Why: lineup confirmation sebelum game

### 1c. OpenWeather API (outdoor sports)
- URL: https://api.openweathermap.org/data/2.5/weather
- Key: free tier (1000 req/day)
- Data: wind, rain, temperature
- Why: affects baseball, tennis, outdoor football
- Env: OPENWEATHER_API_KEY

---

## SPRINT 2 — GEOPOLITIK (Iran, konflik, politik)

### 2a. ADS-B Exchange (pesawat militer)
- URL: https://adsbexchange.com/api/ (atau rapidapi)
- Key: free tier tersedia
- Data: military aircraft positions, tankers, command planes
- Why: tanker aktif = operasi militer imminent
- Env: ADSB_API_KEY

### 2b. Google Trends (public awareness)
- URL: pytrends library (unofficial Google Trends API)
- Key: tidak butuh
- Data: search volume untuk keywords
- Why: spike = market awareness naik = edge berkurang
- Install: pip install pytrends

### 2c. MarineTraffic (kapal perang)
- URL: https://www.marinetraffic.com/api/
- Key: free tier (100 req/month)
- Data: vessel positions, carrier groups
- Why: carrier group di area = escalation signal
- Env: MARINETRAFFIC_API_KEY

---

## SPRINT 3 — CRYPTO & ECONOMICS

### 3a. Binance Funding Rate (crypto)
- URL: https://fapi.binance.com/fapi/v1/fundingRate
- Key: tidak butuh (public)
- Data: perpetual futures funding rate
- Why: negatif = bearish pressure, positif = bullish

### 3b. CME FedWatch (economics)
- URL: scrape dari https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html
- Key: tidak butuh
- Data: implied Fed rate probability
- Why: Tier 1 untuk Fed rate markets

### 3c. FRED API (economic data)
- URL: https://api.stlouisfed.org/fred/series/observations
- Key: free (signup di fred.stlouisfed.org)
- Data: CPI, unemployment, GDP
- Env: FRED_API_KEY

---

## SPRINT 4 — CROSS-CORRELATION ENGINE

### Logic:
```
signals = fetch_all_relevant_signals(market)
score = cross_correlate(signals)  # -1 to +1
conviction = base_confidence * (1 + score * 0.3)  # boost up to 30%
```

### Scoring:
- Each signal votes: +1 (bullish YES), -1 (bearish YES), 0 (neutral)
- Weighted by signal reliability
- If 4/5 signals agree → conviction HIGH → Kelly fraction naik ke 0.35

---

## IMPLEMENTATION ORDER

1. Debug setiap API standalone (test file)
2. Buat agent/osint.py dengan dynamic source selector
3. Integrate ke analyzer.py
4. Test dengan 10 markets sebelum deploy
5. Monitor WR impact setelah 20 trades

## FILES TO CREATE
- agent/osint.py          # main OSINT aggregator
- agent/osint_sports.py   # Vegas odds + injury + weather
- agent/osint_geo.py      # ADS-B + Google Trends + Marine
- agent/osint_crypto.py   # Binance + on-chain
- agent/osint_econ.py     # CME + FRED
- tests/test_osint.py     # debug each API before deploy
