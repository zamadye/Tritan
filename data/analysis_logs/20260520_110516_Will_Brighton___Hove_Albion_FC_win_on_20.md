# Market Analysis — 2026-05-20 11:05 UTC

## Market
- **Question:** Will Brighton & Hove Albion FC win on 2026-05-24?
- **Category:** other
- **YES Price:** 51.0%
- **Days Left:** 4
- **Volume 24h:** $57,444
- **Liquidity:** $565,522

## Statistical Prior
- **p_base:** 38.4%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 12.6%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,443 (+0.6% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,443 (+0.6% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: brighton hove albion 2026-05-24
- [Bing News]
- [Sun, 17 May 2026] brighton hove albion 2026-05-24
- → Brighton &amp; Hove has a chance to solidify top-8 position in the English Premier League on Sunday with a road match on tap against Leeds United.
- [Mon, 18 May 2026] Where to watch Brighton &amp; Hove vs. Leeds United today free during FuboTV, NBC dispute
- → It's still possible that next year Brighton could play in the Champions League, Europa League, Conference League, or not be in Europe at all ...
- [Sun, 17 May 2026] Brighton could still qualify for any European competition – what are the pros, cons and chances of each?
- → The late defeat by Leeds means Fabian Hurzeler's team go into the clash against Manchester United on the final day with a lot to do still ...

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 30.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL REVERSION
- **Catalyst Strength:** 0.70

### Reasoning
Market overpriced at 51% vs historical 44.7% resolution rate for 51% markets, 13% above base rate (38%), and poor 50-60% entry zone performance (33% WR from 9 trades). Brighton has good form but market has incorporated this, with statistical signals indicating overvaluation.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `get_odds({'sport': 'soccer_epl', 'team': 'Brighton'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Brighton Hove Albion FC upcoming match May 24 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Premier League 2025-26 fixtures: Dates, schedule, 
- `search_web({'query': 'Brighton FC form 2026 season results'})` → [Wed, 20 May 2026] Google News
[Sat, 11 Apr 2026] Premier League 2025-26 table — Latest standings - 
- `get_market_context({'keyword': 'Brighton win'})` → No related markets found for 'Brighton win'
- `search_web({'query': 'Brighton vs Manchester United May 24 2026 preview'})` → [Tue, 19 May 2026] Google News
[Fri, 15 May 2026] Brighton vs Man United Prediction, Odds &amp; Matc
- `search_web({'query': 'Brighton last 5 matches results 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Burnley 0-2 Brighton (Apr 11, 2026) Final Score - 
- `search_web({'query': 'Brighton vs Man United May 24 2026 odds preview'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Brighton vs Man United Prediction, Odds &amp; Matc
- `get_market_context({'keyword': 'Brighton Manchester United'})` → No related markets found for 'Brighton Manchester United'
- `search_web({'query': 'Brighton injury report May 2026'})` → [Fri, 15 May 2026] Google News
[Sat, 16 May 2026] Southbound US 85 in Brighton reopens after fatal c
- `search_web({'query': 'Manchester United injury report May 2026'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] Man United injury list: Players out, potential ret

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*