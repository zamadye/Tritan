# Market Analysis — 2026-05-17 23:52 UTC

## Market
- **Question:** Internationaux de Strasbourg: Madison Keys vs Cristina Bucsa
- **Category:** sports
- **YES Price:** 63.0%
- **Days Left:** 7
- **Volume 24h:** $70,167
- **Liquidity:** $30,405

## Statistical Prior
- **p_base:** 69.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 6.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,167 (-1.3% 24h) → risk-OFF
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,194 (-1.2% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: internationaux strasbourg: madison keys cristina
- [Bing News]
- [Fri, 15 May 2026] internationaux strasbourg: madison keys cristina
- → The Internationaux de Strasbourg takes place between 17-23 May in a WTA 500 tournament prior to the French Open. Elena Rybakina is defending champio
- [Thu, 14 May 2026] Internationaux de Strasbourg 2026: Results, Draw, Schedule, Entry List, Prize Money and Predictions
- → Everything you need to know about the WTA 500 Strasbourg event.
- [Tue, 28 Apr 2026] WTA Strasbourg 2026 Entry List, Draw Date: Victoria Mboko top seed; will Emma Raducanu be seeded?
- → Next month's Internationaux de Strasbourg will feature five Top 20 players in Ekaterina Alexandrova, Iva Jovic, Madison Keys, Clara Tauson and Liudm

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 69.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_FITNESS_UNCERTAINTY
- **Catalyst Strength:** 0.30

### Reasoning
Match confirmed (Keys vs Bucsa at Strasbourg), but cannot determine if market price (63%) is mispriced vs true odds. Market is pricing Keys LOWER than base rate (69%), suggesting crowd is already factoring in Keys' recent illness withdrawal from Madrid Open (April 24) and prior retirement from Paris Challenger final. Previous decisions on this same market correctly noted injury concerns as key uncertainty. Without verifiable update on Keys' current fitness status, the 6% gap could reflect genuine injury discount rather than market mispricing. No edge identified—market appears to be rationally accounting for known injury risk.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Madison Keys'})` → No injury data found for tennis Madison Keys
- `get_odds({'sport': 'tennis_atp', 'team': 'Keys'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Madison Keys injury status 2025 Strasbourg tournament'})` → [Tue, 12 May 2026] Google News
[Thu, 22 Jan 2026] Madison Keys cruises past Fiona Ferro, Clara Burel
- `search_web({'query': 'Cristina Bucsa form 2025 tennis results'})` → [Sun, 02 Nov 2025] Google News
[Wed, 27 Aug 2025] Mboko defeats Bucsa to capture Hong Kong title in 
- `get_market_context({'keyword': 'Strasbourg tennis'})` → No related markets found for 'Strasbourg tennis'
- `search_web({'query': 'Internationaux de Strasbourg 2026 draw Madison Keys Cristina Bucsa'})` → [Sat, 16 May 2026] Google News
[Thu, 14 May 2026] Internationaux de Strasbourg 2026: Draw, Schedule,
- `search_web({'query': '"Madison Keys" injury withdrawal 2026'})` → [Fri, 24 Apr 2026] Google News
[Fri, 24 Apr 2026] Keys, Tauson latest to withdraw from Madrid Open -
- `search_web({'query': 'Madison Keys Strasbourg 2026 entry list WTA'})` → [Thu, 14 May 2026] Google News
[Sat, 16 May 2026] Pegula, Anisimova, Mboko lead stacked Queen's entr
- `search_web({'query': 'Madison Keys health status May 2026'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Emma Raducanu: British No 1 in line for Madison Ke
- `search_web({'query': 'Internationaux Strasbourg 2026 draw first round Madison Keys opponent'})` → [Sun, 17 May 2026] Google News
[Wed, 13 May 2026] Meet Emma Raducanu's first Strasbourg opponent, wh
- `search_web({'query': 'WTA Strasbourg 2026 draw results day 1 May 17'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] WTA Strasbourg Day 2 Predictions Including Daria K
- `get_market_context({'keyword': 'tennis Keys Bucsa'})` → No related markets found for 'tennis Keys Bucsa'
- `search_web({'query': 'site:wtatennis.com Strasbourg 2026 draw'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] STRASBOURG: DRAW LS - wtafiles.wtatennis.com
[Wed,
- `search_web({'query': 'Madison Keys Cristina Bucsa head to head 2026'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] H2H, prediction of Marie Bouzkova vs Katerina Sini
- `search_web({'query': 'Madison Keys vs Cristina Bucsa prediction Strasbourg 2026 odds'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Madison Keys vs. Cristina Bucsa prediction, odds, 
- `search_web({'query': '"Madison Keys" "Cristina Bucsa" Strasbourg 2026'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Madison Keys vs. Cristina Bucsa prediction, odds, 

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*