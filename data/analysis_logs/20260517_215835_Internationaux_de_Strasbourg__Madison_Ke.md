# Market Analysis — 2026-05-17 21:58 UTC

## Market
- **Question:** Internationaux de Strasbourg: Madison Keys vs Cristina Bucsa
- **Category:** sports
- **YES Price:** 66.0%
- **Days Left:** 7
- **Volume 24h:** $67,510
- **Liquidity:** $24,004

## Statistical Prior
- **p_base:** 73.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,363 (+0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,380 (+0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: internationaux strasbourg: madison keys cristina
- [Bing News]
- [Fri, 15 May 2026] internationaux strasbourg: madison keys cristina
- → The Internationaux de Strasbourg takes place between 17-23 May in a WTA 500 tournament prior to the French Open. Elena Rybakina is defending champio
- [Tue, 28 Apr 2026] Internationaux de Strasbourg 2026: Results, Draw, Schedule, Entry List, Prize Money and Predictions
- → Next month's Internationaux de Strasbourg will feature five Top 20 players in Ekaterina Alexandrova, Iva Jovic, Madison Keys, Clara Tauson and Liudm
- [Sat, 16 May 2026] Alexandrova, Jovic, Keys, Samsonova headline Strasbourg field
- → FILIPINA tennis ace Alex Eala is set to compete in the Internationaux de Strasbourg from May 17 to 23 in France as part of her preparations for the 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 73.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 0%<52%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Madison Keys'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Madison Keys vs Cristina Bucsa Strasbourg 2025'})` → [Sat, 16 May 2026] Google News
[Wed, 27 Aug 2025] Emma Raducanu could play Grand Slam champion at he
- `search_web({'query': 'Internationaux de Strasbourg 2026 draw'})` → [Sat, 16 May 2026] Google News
[Thu, 14 May 2026] Internationaux de Strasbourg 2026: Draw, Schedule,
- `search_web({'query': 'Madison Keys Strasbourg 2026'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': 'Injured Madison Keys retires from WTA 125 Paris Challenger final'})` → [Sun, 17 May 2026] Google News
[Tue, 12 May 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': 'Madison Keys injury Paris Challenger retirement'})` → [Sun, 17 May 2026] Google News
[Thu, 14 May 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': 'Madison Keys retires Paris final injury details'})` → [Sun, 17 May 2026] Google News
[Fri, 24 Apr 2026] Injured Madison Keys retires from WTA 125 Paris Ch

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*