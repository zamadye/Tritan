# Market Analysis — 2026-05-18 13:48 UTC

## Market
- **Question:** Geneva Open: Valentin Royer vs Francisco Comesana
- **Category:** sports
- **YES Price:** 38.0%
- **Days Left:** 6
- **Volume 24h:** $212,797
- **Liquidity:** $102,793

## Statistical Prior
- **p_base:** 32.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.6%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,916 (-1.7% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,236 (-1.3% 24h) → risk-OFF
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
- **p_true:** 32.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
No concrete edge found. Gap (6%) above threshold but no injury news, form updates, or verifiable catalyst. Past similar markets skipped for smaller gaps with no edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 40%<52%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Royer'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Valentin Royer Francisco Comesana Geneva Open odds'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Valentin Royer vs. Francisco Comesana prediction, 
- `get_market_context({'keyword': 'Geneva Open Royer Comesana'})` → No related markets found for 'Geneva Open Royer Comesana'
- `get_market_context({'keyword': 'Geneva Open'})` → No related markets found for 'Geneva Open'
- `search_web({'query': 'Valentin Royer injury status May 2026'})` → [Mon, 20 Apr 2026] Google News
[Sun, 01 Feb 2026] "Everything works" for Roman Safiullin in return t
- `search_web({'query': 'Francisco Comesana injury status May 2026'})` → [Wed, 21 Jan 2026] Google News
[Wed, 11 Feb 2026] Tennis, ATP – Australian Open 2026: Tiafoe beats C
- `search_web({'query': 'Valentin Royer recent results 2026 ATP'})` → [Mon, 18 May 2026] Google News
[Wed, 18 Feb 2026] ATP Geneva Day 2 Predictions Including Stan Wawrin

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*