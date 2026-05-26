# Market Analysis — 2026-05-20 08:55 UTC

## Market
- **Question:** Geneva Open: Stefanos Tsitsipas vs Learner Tien
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 6
- **Volume 24h:** $98,056
- **Liquidity:** $75,902

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,408 (+0.4% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,390 (+0.4% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: geneva open: stefanos tsitsipas learner
- [Bing News]
- [Wed, 20 May 2026] geneva open: stefanos tsitsipas learner
- → Live Geneva Open coverage: follow Casper Ruud, Taylor Fritz and more with real-time scores, match updates, key results and expert talking points fro
- [Sat, 16 May 2026] LIVE Geneva Open Day Four | Fritz-Popyrin, Norrie, Tsitsipas-Tien, Ruud in action
- → May in Switzerland and sees Novak Djokovic as the defending champion but unlike previous years, he won't return to play in the tournament in ...
- [Mon, 18 May 2026] Geneva Open 2026: Results, Draw, Schedule, Entry List, Prize Money and Predictions
- → Stefanos Tsitsipas outlasts Giovanni Mpetshi Perricard in a gripping second-set tie-break to reach the second round in Geneva, boosting his morale a

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 60.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.30

### Reasoning
Conflicting signals with no clear resolution - base rate suggests YES edge (3% gap) while stat signal suggests NO edge (12% overpricing). Entry zone 50-60% historically weak (33% WR). No direct catalyst or specific information found for this match. Previous Tsitsipas decision required 8% gap for PASS.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tsitsipas'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Stefanos Tsitsipas vs Learner Tien Geneva Open 2025'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Tennis Picks Today: 5 Best Bets &amp; Predictions 
- `search_web({'query': 'Tsitsipas form 2026 results recent matches'})` → [Fri, 24 Apr 2026] Google News
[Wed, 29 Apr 2026] Stefanos Tsitsipas ‘In A Good Place’ Physically As
- `search_web({'query': 'Learner Tien 2026 results Geneva Open'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Geneva Open 2026: Results, Draw, Schedule, Entry L
- `get_market_context({'keyword': 'Geneva Open Tsitsipas'})` → No related markets found for 'Geneva Open Tsitsipas'
- `get_market_context({'keyword': 'tennis Tsitsipas Tien'})` → No related markets found for 'tennis Tsitsipas Tien'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*