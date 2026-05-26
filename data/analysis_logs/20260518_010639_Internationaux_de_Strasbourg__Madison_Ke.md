# Market Analysis — 2026-05-18 01:06 UTC

## Market
- **Question:** Internationaux de Strasbourg: Madison Keys vs Cristina Bucsa
- **Category:** sports
- **YES Price:** 62.0%
- **Days Left:** 7
- **Volume 24h:** $70,385
- **Liquidity:** $32,887

## Statistical Prior
- **p_base:** 67.6%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.6%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,157 (-0.9% 24h) → neutral
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,105 (-1.0% 24h) → neutral
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
- **Confidence:** 45%
- **p_true:** 67.6%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_UNCERTAINTY
- **Catalyst Strength:** 0.70

### Reasoning
Madison Keys has confirmed injury red flags (Madrid withdrawal Apr 24, Paris Challenger retirement May 11) on clay leading into Strasbourg. The 6% model gap (68% base vs 62% market) cannot be trusted without resolving the key variable: Keys' current fitness. Previous decisions correctly skipped at 45-48% confidence. Retirement in a final just ~2 weeks before this match suggests significant injury risk. Unable to confirm whether Keys will play at full capacity or even complete the match. Edge direction is ambiguous - if healthy, YES is underpriced; if injured, NO is underpriced. SKIP until injury status is clarified.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Madison Keys'})` → No injury data found for tennis Madison Keys
- `get_odds({'sport': 'tennis', 'team': 'Madison Keys'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Internationaux Strasbourg tennis'})` → No related markets found for 'Internationaux Strasbourg tennis'
- `search_web({'query': 'Madison Keys injury 2025 Internationaux de Strasbourg'})` → [Thu, 22 Jan 2026] Google News
[Wed, 26 Nov 2025] Pliskova will face reigning champion Keys in retur
- `search_web({'query': 'Madison Keys vs Cristina Bucsa Strasbourg 2025 head to head'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] H2H, prediction of Ann Li vs Maya Joint in Strasbo
- `search_web({'query': 'Cristina Bucsa form 2025 WTA ranking results'})` → [Sun, 02 Nov 2025] Google News
[Sun, 02 Nov 2025] Mboko defeats Bucsa to capture Hong Kong title in 
- `search_web({'query': 'Madison Keys Strasbourg 2025 draw results match'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] The Official Home of the Women's Tennis Associatio
- `search_web({'query': 'Madison Keys wrist injury withdrawal 2025'})` → [Fri, 24 Apr 2026] Google News
[Fri, 24 Apr 2026] Madison Keys deals hammer blow to Madrid Open minu
- `get_market_context({'keyword': 'Keys Bucsa'})` → No related markets found for 'Keys Bucsa'
- `search_web({'query': '"Madison Keys" retirement injury May 2025'})` → [Sun, 17 May 2026] Google News
[Fri, 16 Jan 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': '"Internationaux de Strasbourg" 2025 draw keys bucsa'})` → [Sat, 16 May 2026] Google News
[Thu, 14 May 2026] Emma Raducanu: British No 1 in line for Madison Ke

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*