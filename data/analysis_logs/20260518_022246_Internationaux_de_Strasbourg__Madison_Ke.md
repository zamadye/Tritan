# Market Analysis — 2026-05-18 02:22 UTC

## Market
- **Question:** Internationaux de Strasbourg: Madison Keys vs Cristina Bucsa
- **Category:** sports
- **YES Price:** 70.0%
- **Days Left:** 7
- **Volume 24h:** $84,567
- **Liquidity:** $33,195

## Statistical Prior
- **p_base:** 78.1%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.1%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,041 (-1.0% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,114 (-0.9% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

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
- **p_true:** 78.1%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_STATUS
- **Catalyst Strength:** 0.30

### Reasoning
Madison Keys has documented injury red flags (Madrid withdrawal Apr 24, Paris Challenger retirement May 11), but market at 70% already discounts below 78% base rate. No current verification of Keys' status for this specific match. Past decisions on this same market were SKIP with low confidence (45-48%) due to injury uncertainty. Without concrete evidence of Keys' withdrawal or current fitness level for Strasbourg, cannot establish actionable edge. Market appears appropriately priced for injury risk.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'Madison Keys injury update Strasbourg 2025'})` → [Sun, 17 May 2026] Google News
[Thu, 22 Jan 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': 'Internationaux de Strasbourg 2025 Madison Keys Cristina Bucsa'})` → [Mon, 11 May 2026] Google News
[Thu, 08 May 2025] Victoria Mboko handed wildcard for Roland Garros w
- `search_web({'query': 'Madison Keys withdraws Strasbourg 2025'})` → [Sun, 17 May 2026] Google News
[Thu, 07 May 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `get_market_context({'keyword': 'Strasbourg'})` → No related markets found for 'Strasbourg'
- `get_market_context({'keyword': 'Madison Keys'})` → No related markets found for 'Madison Keys'
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Madison Keys'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Madison Keys injury 2025 status'})` → [Sun, 17 May 2026] Google News
[Sat, 01 Nov 2025] Injured Madison Keys retires from WTA 125 Paris Ch

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*