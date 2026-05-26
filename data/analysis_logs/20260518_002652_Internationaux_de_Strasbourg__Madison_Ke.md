# Market Analysis — 2026-05-18 00:26 UTC

## Market
- **Question:** Internationaux de Strasbourg: Madison Keys vs Cristina Bucsa
- **Category:** sports
- **YES Price:** 64.0%
- **Days Left:** 7
- **Volume 24h:** $70,254
- **Liquidity:** $29,836

## Statistical Prior
- **p_base:** 70.3%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 6.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,232 (-1.2% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,165 (-1.2% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: internationaux strasbourg: madison keys cristina
- [Bing News]
- [Thu, 14 May 2026] internationaux strasbourg: madison keys cristina
- → Everything you need to know about the WTA 500 Strasbourg event.
- [Tue, 28 Apr 2026] WTA Strasbourg 2026 Entry List, Draw Date: Victoria Mboko top seed; will Emma Raducanu be seeded?
- → Next month's Internationaux de Strasbourg will feature five Top 20 players in Ekaterina Alexandrova, Iva Jovic, Madison Keys, Clara Tauson and Liudm
- [Sun, 17 May 2026] Alexandrova, Jovic, Keys, Samsonova headline Strasbourg field
- → A QUALIFIER will be Alex Eala’s opponent in the opening round of the Internationaux de Strasbourg being held in France. This was based on the offici

## LLM Decision
- **Action:** SKIP
- **Confidence:** 48%
- **p_true:** 70.3%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_STATUS
- **Catalyst Strength:** 0.35

### Reasoning
Multiple injury red flags for Keys (Madrid withdrawal April 24, Paris Challenger retirement May 11-14, premature Italian Open loss) create uncertainty, BUT no confirmed withdrawal from Strasbourg found. The 6% gap (YES 64% vs base 70%) appears to reflect injury discount. However, Keys did cruise past Fiona Ferro at Paris on May 16, suggesting she may be fit enough to compete. Cannot confirm if injury is serious enough to cause retirement or withdrawal. Prior decisions to SKIP at 45% confidence remain justified - not enough concrete evidence of mispricing. Match is 7 days away; injury status may update.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 48%<52%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Keys'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Strasbourg tennis Keys Bucsa'})` → No related markets found for 'Strasbourg tennis Keys Bucsa'
- `search_web({'query': 'Madison Keys vs Cristina Bucsa Strasbourg 2025'})` → [Sat, 16 May 2026] Google News
[Wed, 27 Aug 2025] Emma Raducanu could play Grand Slam champion at he
- `search_web({'query': 'Internationaux de Strasbourg 2025 draw Keys Bucsa'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] The Official Home of the Women's Tennis Associatio
- `search_web({'query': 'Madison Keys injury 2026 WTA retired Paris Challenger'})` → [Sun, 17 May 2026] Google News
[Thu, 14 May 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': 'Madison Keys retires from WTA 125 Paris Challenger final May 2026'})` → [Sun, 17 May 2026] Google News
[Mon, 11 May 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': 'Madison Keys withdraws Madrid 2026 injury update'})` → [Fri, 24 Apr 2026] Google News
[Fri, 24 Apr 2026] Keys, Tauson latest to withdraw from Madrid Open -

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*