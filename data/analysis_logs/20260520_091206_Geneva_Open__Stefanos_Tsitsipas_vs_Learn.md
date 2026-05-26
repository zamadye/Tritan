# Market Analysis — 2026-05-20 09:12 UTC

## Market
- **Question:** Geneva Open: Stefanos Tsitsipas vs Learner Tien
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 6
- **Volume 24h:** $111,298
- **Liquidity:** $44,934

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,370 (+0.5% 24h) → neutral
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
- [] Geneva Open 2026: Results, Draw, Schedule, Entry List, Prize Money and Predictions
- [Metaculus]

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 61.9%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Tsitsipas'})` → No injury data found for tennis Tsitsipas
- `get_sports_data({'sport': 'tennis', 'team': 'Tien'})` → No injury data found for tennis Tien
- `search_web({'query': 'Geneva Open 2025 Tsitsipas Tien results'})` → [Tue, 19 May 2026] Google News
[Wed, 13 May 2026] ATP Geneva Best Bets Including Taylor Fritz vs Ale
- `search_web({'query': 'Tsitsipas Tien head to head tennis 2025'})` → [Wed, 20 May 2026] Google News
[Mon, 15 Dec 2025] ATP Geneva Day 4 Predictions Including Taylor Frit
- `get_market_context({'keyword': 'Tsitsipas Tien Geneva'})` → No related markets found for 'Tsitsipas Tien Geneva'
- `search_web({'query': 'Tsitsipas 2025 form clay court season results'})` → [Thu, 09 Apr 2026] Google News
[Fri, 16 Jan 2026] Clay power rankings: 2026 ATP Tour - Tennisnerd
[T
- `search_web({'query': 'Learner Tien 2025 season clay court results ATP'})` → [Sun, 29 Mar 2026] Google News
[Mon, 30 Mar 2026] Shelton, Darderi, Diallo headline fields in Housto
- `get_odds({'sport': 'tennis_atp', 'team': 'Tsitsipas'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp_italian_open'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*