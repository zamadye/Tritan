# Market Analysis — 2026-05-18 12:43 UTC

## Market
- **Question:** GP SAR La Princesse Lalla Meryem: Alycia Parks vs Moyuka Uchijima
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 6
- **Volume 24h:** $48,554
- **Liquidity:** $20,091

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,601 (-1.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,601 (-1.1% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: princesse lalla meryem: alycia parks
- [Bing News]
- [Fri, 26 May 2023] princesse lalla meryem: alycia parks
- → Also known as the Morocco Open or Rabat Grand Prix, the Grand Prix Sar La Princesse Lalla Meryem is an international WTA 250 event played on outdoor
- [] Grand Prix Son Altesse Royale La Princesse Lalla Meryem
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 57% historically resolve YES only 44.7% of the time, indicating ~12% edge for NO. Market overprices YES despite moderate base rate (60%). Confidence tempered by low historical win rate in 50-60% entry range.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Alycia Parks'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Alycia Parks'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Alycia Parks Moyuka Uchijima'})` → No related markets found for 'Alycia Parks Moyuka Uchijima'
- `search_web({'query': 'Alycia Parks vs Moyuka Uchijima GP SAR La Princesse Lalla Meryem 2025'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] PREDICTION, PREVIEW, H2H: Parks, Ferro, Belen Teic
- `search_web({'query': 'Alycia Parks recent form WTA 2025'})` → [Wed, 20 Aug 2025] Google News
[Mon, 27 Oct 2025] US Open 2025: Draws, dates, stats, prize money and
- `get_market_context({'keyword': 'GP SAR La Princesse Lalla Meryem'})` → No related markets found for 'GP SAR La Princesse Lalla Meryem'
- `search_web({'query': 'Moyuka Uchijima recent form clay court 2025'})` → [Mon, 20 Oct 2025] Google News
[Sun, 13 Jul 2025] Tennis, WTA – Tokyo Open 2025: Kalinskaya sees off
- `search_web({'query': '"Alycia Parks" clay court record 2025 WTA'})` → [Thu, 23 Apr 2026] Google News
[Mon, 06 Apr 2026] "You can’t just hit everything flat": Serena Willi
- `search_web({'query': 'Alycia Parks Moyuka Uchijima head to head tennis'})` → [Mon, 18 May 2026] Google News
[Sat, 07 Feb 2026] Tennis Picks Today: 5 Best Bets &amp; Predictions 
- `search_web({'query': '"Parks" "Uchijima" prediction May 2026'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Tennis Picks Today: 5 Best Bets &amp; Predictions 

## Outcome
**✅ WIN** | P&L: $+0.47 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*