# Market Analysis — 2026-05-16 18:33 UTC

## Market
- **Question:** Toronto Blue Jays vs. Detroit Tigers
- **Category:** sports
- **YES Price:** 51.5%
- **Days Left:** 6
- **Volume 24h:** $496,074
- **Liquidity:** $23,422

## Statistical Prior
- **p_base:** 52.2%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.7%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,163 (-1.2% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,163 (-1.2% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 31(Fear) → 43(Fear) → 34(Fear) → 42(Fear) | sentiment worsening
- Will the Fed decrease interest rates by 50+ bps after the Ju → YES=50%
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [SPORTS] Recent games:
- TOR @ DET | In Progress | Detroit Tigers(home) 20-25 score:0 vs Toronto Blue Jays(away) 19-25 score:0

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 46.2%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STAT_EDGE
- **Catalyst Strength:** 0.65

### Reasoning
Historical data shows markets at 52% resolve YES only 44.7% of the time (n=13,967), indicating systematic overpricing of YES outcomes by ~7.3 percentage points. No breaking news or unreported information found via search. No home bias, recency bias, or narrative bias detected—the crowd appears to be anchored to the base rate (52%) without accounting for the historical tendency of these markets to overprice the favorite. The STAT_EDGE is the primary catalyst: consistent, large sample size, but no fresh catalyst today.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<3%

## Tool Calls
- `search_web({'query': 'Toronto Blue Jays vs Detroit Tigers prediction market news today'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Best Bets, Picks &amp; Props to Target in Blue Jay
- `search_web({'query': 'Blue Jays Tigers injury report today lineup changes'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Fantasy baseball: Mets' Clay Holmes, Yankees' Max 
- `search_web({'query': 'Blue Jays vs Tigers odds movement prediction market sentiment'})` → [Wed, 05 Nov 2025] Google News
[Tue, 11 Nov 2025] MLB offseason bold predictions: Kyle Tucker gets p

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*