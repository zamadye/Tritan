# Market Analysis — 2026-05-17 23:36 UTC

## Market
- **Question:** Internationaux de Strasbourg: Madison Keys vs Cristina Bucsa
- **Category:** sports
- **YES Price:** 63.0%
- **Days Left:** 7
- **Volume 24h:** $69,992
- **Liquidity:** $29,882

## Statistical Prior
- **p_base:** 69.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 6.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,748 (-0.6% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,768 (-0.6% 24h) → neutral
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
- **Catalyst Type:** INJURY_KNOWLEDGE
- **Catalyst Strength:** 0.30

### Reasoning
No edge. Madison Keys retired injured from Paris Challenger final and withdrew from Madrid - but this is public info already priced into the 63% market price (vs 69% base rate). Bucsa is in strong form (Merida champion). Market appears efficient; no verifiable information gap exists to exploit.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Madison Keys'})` → No injury data found for tennis Madison Keys
- `search_web({'query': 'Madison Keys injury status Internationaux de Strasbourg 2025'})` → [Tue, 11 Nov 2025] Google News
[Wed, 26 Nov 2025] WTA year in review: What was the best tournament o
- `search_web({'query': 'Madison Keys Cristina Bucsa Strasbourg head to head'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Madison Keys vs Cristina Bucsa: Scores, Results Li
- `get_market_context({'keyword': 'Madison Keys tennis'})` → No related markets found for 'Madison Keys tennis'
- `search_web({'query': 'Madison Keys 2026 results form WTA ranking'})` → [Wed, 14 Jan 2026] Google News
[Thu, 15 Jan 2026] WTA Power Rankings: Deep Field Ready to Vie for Au
- `search_web({'query': 'Cristina Bucsa 2026 tennis results WTA'})` → [Sun, 17 May 2026] Google News
[Mon, 02 Mar 2026] Italian Open 2026: All results live - full scores,
- `get_odds({'sport': 'tennis_atp', 'team': 'Madison Keys'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': '"Madison Keys" Strasbourg 2026 match preview prediction'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Madison Keys vs. Cristina Bucsa prediction, odds, 
- `search_web({'query': 'Cristina Bucsa form 2026 clay court results'})` → [Sun, 17 May 2026] Google News
[Wed, 22 Apr 2026] Italian Open 2026: All results live - full scores,
- `search_web({'query': 'Madison Keys injury retirement Paris 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': 'Cristina Bucsa Merida title WTA 2026'})` → [Mon, 02 Mar 2026] Google News
[Mon, 02 Mar 2026] Bucsa outlasts Frech to earn first singles title, 

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*