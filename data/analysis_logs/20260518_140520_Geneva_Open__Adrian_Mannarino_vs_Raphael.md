# Market Analysis — 2026-05-18 14:05 UTC

## Market
- **Question:** Geneva Open: Adrian Mannarino vs Raphael Collignon
- **Category:** sports
- **YES Price:** 12.0%
- **Days Left:** 6
- **Volume 24h:** $91,260
- **Liquidity:** $28,152

## Statistical Prior
- **p_base:** 4.8%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,915 (-1.6% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,825 (-1.8% 24h) → risk-OFF
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
- **p_true:** 5.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** SPORTS_TENNIS_MATCH
- **Catalyst Strength:** 0.15

### Reasoning
YES price (12%) already trades 7 points above the historical base rate (5%), indicating the market has already incorporated information about this specific match. No concrete new evidence found (injuries, recent form, head-to-head) to justify additional edge. Previous similar decisions on this exact market were SKIP with similar reasoning. The gap suggests no information advantage remains - the market appears fairly priced given current information.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Mannarino'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Mannarino'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Adrian Mannarino Geneva Open 2025 form results'})` → [Wed, 01 Oct 2025] Google News
[Fri, 08 Aug 2025] Andrey Rublev - Adrian Mannarino 3:2 - Flashscore.
- `search_web({'query': 'Raphael Collignon ATP tennis 2025 recent results'})` → [Tue, 17 Mar 2026] Google News
[Tue, 03 Mar 2026] Joao Fonseca: Miami draw, history, recent results 
- `search_web({'query': 'Mannarino vs Collignon Geneva Open 2025'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Mannarino vs. Collignon Prediction at the Gonet Ge
- `get_market_context({'keyword': 'Geneva Open Mannarino Collignon'})` → No related markets found for 'Geneva Open Mannarino Collignon'
- `search_web({'query': '"Mannarino" "Collignon" prediction tennis 2025'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Mannarino vs. Collignon Prediction at the Gonet Ge

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*