# Market Analysis — 2026-05-18 12:32 UTC

## Market
- **Question:** Geneva Open: Valentin Royer vs Francisco Comesana
- **Category:** sports
- **YES Price:** 41.0%
- **Days Left:** 6
- **Volume 24h:** $132,379
- **Liquidity:** $22,833

## Statistical Prior
- **p_base:** 36.7%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,405 (-1.3% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,377 (-1.3% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: geneva open: valentin royer francisco
- [Bing News]
- [Mon, 23 Feb 2026] geneva open: valentin royer francisco
- → Rublev has made a promising start to the season. Apart from semifinal runs in Hong Kong and Doha, he also reached the third round in Melbourne. The 
- [] Andrey Rublev vs Valentin Royer preview, head-to-head, prediction, odds, and betting tips | ATP Dubai Open 2026
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 40%
- **p_true:** 36.7%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.05

### Reasoning
No verifiable edge found. Market YES price (41%) is only 4 points above historical base rate (37%), below the 5% gate threshold. No injury news, form data, or head-to-head information found to differentiate from base rate. Same market was previously skipped for identical reason. Insufficient confidence (0.40 < 0.55 threshold) to place any bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Royer Comesana Geneva'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Geneva Open tennis Royer Comesana'})` → No related markets found for 'Geneva Open tennis Royer Comesana'
- `search_web({'query': 'Valentin Royer vs Francisco Comesana Geneva Open 2025 odds'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] H2H, prediction of Valentin Royer vs Francisco Com
- `search_web({'query': 'Royer Comesana head to head tennis 2025'})` → [Sun, 11 Jan 2026] Google News
[Fri, 03 Oct 2025] ATP Auckland Day 1 Predictions Including Cameron N
- `search_web({'query': 'Valentin Royer form recent results ATP 2025'})` → [Tue, 23 Sep 2025] Google News
[Tue, 28 Oct 2025] Bublik blazes to fourth title of 2025, new career 
- `search_web({'query': 'Francisco Comesana ATP ranking 2026 clay court results'})` → [Wed, 22 Apr 2026] Google News
[Fri, 31 Oct 2025] Madrid Open Draw 2026 - Perfect Tennis
[Wed, 25 Fe
- `search_web({'query': 'Valentin Royer ATP ranking clay court 2026'})` → [Mon, 20 Apr 2026] Google News
[Wed, 04 Feb 2026] "Everything works" for Roman Safiullin in return t

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*