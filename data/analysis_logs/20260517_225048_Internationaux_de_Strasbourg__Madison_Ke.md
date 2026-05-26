# Market Analysis — 2026-05-17 22:50 UTC

## Market
- **Question:** Internationaux de Strasbourg: Madison Keys vs Cristina Bucsa
- **Category:** sports
- **YES Price:** 66.0%
- **Days Left:** 7
- **Volume 24h:** $69,693
- **Liquidity:** $29,699

## Statistical Prior
- **p_base:** 73.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,982 (-0.3% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,973 (-0.3% 24h) → neutral
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
- **Confidence:** 42%
- **p_true:** 73.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_NEWS
- **Catalyst Strength:** 0.60

### Reasoning
Madison Keys retired injured from Paris Challenger final just 1-2 days before this match. Market already appears to have priced in injury risk (66% vs 73% base rate). Without medical details on injury severity, cannot determine if current price offers edge. High uncertainty on both sides.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 42%<52%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Madison Keys'})` → No injury data found for tennis Madison Keys
- `search_web({'query': 'Madison Keys vs Cristina Bucsa Strasbourg 2025'})` → [Sat, 16 May 2026] Google News
[Wed, 27 Aug 2025] Emma Raducanu could play Grand Slam champion at he
- `search_web({'query': 'Madison Keys recent form results 2025'})` → [Thu, 08 Jan 2026] Google News
[Thu, 15 Jan 2026] Keys wins first triple-tiebreak match of career ov
- `get_market_context({'keyword': 'Strasbourg tennis Keys'})` → No related markets found for 'Strasbourg tennis Keys'
- `get_odds({'sport': 'tennis_atp', 'team': 'Madison Keys'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Internationaux de Strasbourg 2025 results scores'})` → [Thu, 09 Oct 2025] Google News
[Fri, 09 Jan 2026] Internationaux de Strasbourg presented by Mammotio
- `get_sports_data({'sport': 'tennis', 'team': 'Cristina Bucsa'})` → No injury data found for tennis Cristina Bucsa
- `search_web({'query': 'Madison Keys tennis 2026 results form'})` → [Thu, 08 Jan 2026] Google News
[Thu, 15 Jan 2026] Keys wins first triple-tiebreak match of career ov
- `search_web({'query': 'Cristina Bucsa tennis 2026 ranking results'})` → [Sun, 02 Nov 2025] Google News
[Wed, 22 Apr 2026] Tennis: Victoria Mboko triumphs in Hong Kong, defe
- `search_web({'query': 'Strasbourg tennis tournament 2026 draw results'})` → [Sat, 16 May 2026] Google News
[Fri, 15 May 2026] Internationaux de Strasbourg 2026: Draw, Schedule,
- `search_web({'query': '"Madison Keys" vs "Cristina Bucsa" Strasbourg 2026'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Madison Keys vs. Cristina Bucsa prediction, odds, 
- `search_web({'query': 'Madison Keys Strasbourg 2026 match preview'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': 'Madison Keys injury retirement Paris Challenger final 2026'})` → [Sun, 17 May 2026] Google News
[Mon, 11 May 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': 'Madison Keys injury status Strasbourg update'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': '"Madison Keys" retirement injury details what injury'})` → [Sun, 17 May 2026] Google News
[Fri, 24 Apr 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': 'Keys Bucsa odds prediction Strasbourg 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Madison Keys vs. Cristina Bucsa prediction, odds, 
- `search_web({'query': 'dimers.com Madison Keys Cristina Bucsa Strasbourg prediction odds'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Madison Keys vs. Cristina Bucsa prediction, odds, 
- `search_web({'query': '"Madison Keys" "Cristina Bucsa" head to head record'})` → [Sun, 17 May 2026] Google News
[Wed, 06 May 2026] News, Predictions, H2H, Live Scores, stats - Tenni

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*