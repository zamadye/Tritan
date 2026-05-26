# Market Analysis — 2026-05-16 16:54 UTC

## Market
- **Question:** Philadelphia Phillies vs. Pittsburgh Pirates
- **Category:** sports
- **YES Price:** 60.0%
- **Days Left:** 7
- **Volume 24h:** $98,967
- **Liquidity:** $278,455

## Statistical Prior
- **p_base:** 64.8%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.7%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,176 (-1.3% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,154 (-1.3% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 31(Fear) → 43(Fear) → 34(Fear) → 42(Fear) | sentiment worsening
- Will the Fed decrease interest rates by 50+ bps after the Ju → YES=50%
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [SPORTS] Recent games:
- PHI @ PIT | Scheduled | Pittsburgh Pirates(home) 24-21 score:0 vs Philadelphia Phillies(away) 22-23 score:0

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 64.8%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 0%<52%

## Tool Calls
- `search_web({'query': 'Philadelphia Phillies vs Pittsburgh Pirates game today 2025'})` → [Sat, 07 Jun 2025] Google News
[Fri, 06 Jun 2025] Philadelphia Phillies at Pittsburgh Pirates Game S
- `get_sports_data({'sport': 'mlb', 'team': 'Philadelphia Phillies'})` → INJURY [philadelphia phillies] Kyle Backhus (RP): 15-Day-IL
INJURY [philadelphia phillies] Zach Pop 
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Jared Jones (SP): 60-Day-IL
INJURY [pittsburgh pirates] Joey Bart (C): 1
- `search_web({'query': 'Phillies Pirates June 7 2025 pitching matchup odds preview'})` → [Thu, 09 Apr 2026] Google News
[Tue, 07 Apr 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `get_market_context({'keyword': 'Phillies Pirates baseball'})` → No related markets found for 'Phillies Pirates baseball'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*