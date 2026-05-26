# Market Analysis — 2026-05-18 12:35 UTC

## Market
- **Question:** Geneva Open: Adrian Mannarino vs Raphael Collignon
- **Category:** sports
- **YES Price:** 14.0%
- **Days Left:** 6
- **Volume 24h:** $90,061
- **Liquidity:** $15,486

## Statistical Prior
- **p_base:** 6.2%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,405 (-1.3% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,290 (-1.4% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: geneva open: adrian mannarino raphael
- [Bing News]
- [Sat, 16 May 2026] geneva open: adrian mannarino raphael
- → May in Switzerland and sees Novak Djokovic as the defending champion but unlike previous years, he won't return to play in the tournament in ...
- [] Geneva Open 2026: Results, Draw, Schedule, Entry List, Prize Money and Predictions
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 6.2%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE_IDENTIFIED
- **Catalyst Strength:** 0.20

### Reasoning
YES price (14%) already trades 8 points above historical base rate (6%), suggesting market has incorporated positive information. No verifiable catalyst found (injury news, form advantage, or head-to-head edge). Unable to confirm specific outcome YES represents. Gap is negative (market more bullish than base rate), eliminating the typical edge opportunity. Confidence below 0.55 threshold for action.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Mannarino'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Adrian Mannarino vs Raphael Collignon Geneva Open 2025 odds'})` → [Sun, 17 May 2026] Google News
[Wed, 04 Mar 2026] Mannarino vs. Collignon Prediction at the Gonet Ge
- `search_web({'query': 'Adrian Mannarino recent form ATP rankings 2025'})` → [Fri, 26 Sep 2025] Google News
[Wed, 13 Aug 2025] Zverev, De Minaur among Turin contenders to advanc
- `search_web({'query': 'Raphael Collignon ATP player profile ranking 2025'})` → [Mon, 21 Jul 2025] Google News
[Tue, 18 Nov 2025] Raphael Collignon Player Profile | Official Site o
- `get_market_context({'keyword': 'Geneva Open Mannarino Collignon'})` → No related markets found for 'Geneva Open Mannarino Collignon'
- `search_web({'query': '"Mannarino" "Collignon" Geneva Open prediction'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Mannarino vs. Collignon Prediction at the Gonet Ge
- `search_web({'query': 'Bleacher Nation Mannarino Collignon prediction odds Geneva Open 2026'})` → [Sun, 17 May 2026] Google News
[] Mannarino vs. Collignon Prediction at the Gonet Geneva Open – Mond
- `search_web({'query': 'Adrian Mannarino ATP ranking May 2026'})` → [Tue, 12 Aug 2025] Google News
[Mon, 08 Jan 2024] ATP: Unseeded trio bring French flair to Cincy - R

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*