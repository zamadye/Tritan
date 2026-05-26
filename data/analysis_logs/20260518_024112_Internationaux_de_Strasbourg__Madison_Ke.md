# Market Analysis — 2026-05-18 02:41 UTC

## Market
- **Question:** Internationaux de Strasbourg: Madison Keys vs Cristina Bucsa
- **Category:** sports
- **YES Price:** 72.0%
- **Days Left:** 7
- **Volume 24h:** $86,508
- **Liquidity:** $31,733

## Statistical Prior
- **p_base:** 80.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,925 (-1.2% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,879 (-1.3% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: internationaux strasbourg: madison keys cristina
- [Bing News]
- [Thu, 14 May 2026] internationaux strasbourg: madison keys cristina
- → Everything you need to know about the WTA 500 Strasbourg event.
- [Tue, 28 Apr 2026] WTA Strasbourg 2026 Entry List, Draw Date: Victoria Mboko top seed; will Emma Raducanu be seeded?
- → Next month's Internationaux de Strasbourg will feature five Top 20 players in Ekaterina Alexandrova, Iva Jovic, Madison Keys, Clara Tauson and Liudm
- [] Alexandrova, Jovic, Keys, Samsonova headline Strasbourg field
- [Metaculus]

## LLM Decision
- **Action:** YES
- **Confidence:** 52%
- **p_true:** 80.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_CONCERN
- **Catalyst Strength:** 0.40

### Reasoning
Statistical mispricing + catalyst: p_base=80% vs market=72% gap=8% (n=6077)

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET YES $1.00

## Tool Calls
- `search_web({'query': 'Madison Keys injury status Strasbourg 2025'})` → [Sun, 17 May 2026] Google News
[Thu, 22 Jan 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': 'Madison Keys vs Cristina Bucsa Strasbourg 2025 preview'})` → [Sat, 16 May 2026] Google News
[Wed, 27 Aug 2025] Emma Raducanu could play Grand Slam champion at he
- `get_market_context({'keyword': 'Strasbourg Madison Keys'})` → No related markets found for 'Strasbourg Madison Keys'
- `search_web({'query': '"Madison Keys" Strasbourg 2026 injury'})` → [Sun, 17 May 2026] Google News
[Fri, 24 Apr 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': 'Cristina Bucsa Strasbourg 2026 form'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Madison Keys vs. Cristina Bucsa prediction, odds, 
- `get_market_context({'keyword': 'tennis Strasbourg'})` → No related markets found for 'tennis Strasbourg'
- `search_web({'query': 'Madison Keys withdraw Strasbourg 2026'})` → [Sat, 16 May 2026] Google News
[Wed, 13 May 2026] Emma Raducanu: British No 1 in line for Madison Ke
- `search_web({'query': '"Internationaux de Strasbourg" Keys Bucsa odds'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] H2H, prediction of Ann Li vs Maya Joint in Strasbo
- `search_web({'query': 'dimers.com Madison Keys Cristina Bucsa Strasbourg 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Madison Keys vs. Cristina Bucsa prediction, odds, 
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Keys'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Madison Keys injury update May 2026'})` → [Sun, 17 May 2026] Google News
[Fri, 24 Apr 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': '"Madison Keys vs. Cristina Bucsa" odds Strasbourg 2026'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Madison Keys vs. Cristina Bucsa prediction, odds, 
- `search_web({'query': '"Madison Keys" injury "Strasbourg" 2026'})` → [Sun, 17 May 2026] Google News
[Fri, 24 Apr 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': 'Keys Bucsa head to head tennis'})` → [Sat, 16 May 2026] Google News
[Fri, 12 Nov 2021] Madison Keys vs Cristina Bucsa: Scores, Results Li
- `search_web({'query': 'dimers.com "Madison Keys" "Cristina Bucsa" prediction odds picks WTA Strasbourg Open 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Madison Keys vs. Cristina Bucsa prediction, odds, 
- `search_web({'query': 'statsinsider.com.au Madison Keys Cristina Bucsa prediction WTA Strasbourg 2026'})` → [Sat, 16 May 2026] Google News
[] Madison Keys vs Cristina Bucsa Prediction - WTA Strasbourg Open 20
- `search_web({'query': '"Madison Keys" Strasbourg 2026 match result'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': 'Keys Bucsa Strasbourg 2026 score'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Madison Keys vs. Cristina Bucsa prediction, odds, 
- `get_market_context({'keyword': 'WTA Strasbourg'})` → No related markets found for 'WTA Strasbourg'

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*