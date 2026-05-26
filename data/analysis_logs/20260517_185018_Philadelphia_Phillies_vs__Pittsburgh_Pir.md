# Market Analysis — 2026-05-17 18:50 UTC

## Market
- **Question:** Philadelphia Phillies vs. Pittsburgh Pirates
- **Category:** sports
- **YES Price:** 50.5%
- **Days Left:** 6
- **Volume 24h:** $166,903
- **Liquidity:** $34,315

## Statistical Prior
- **p_base:** 50.7%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,084 (-0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,087 (-0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
- [SPORTS] Recent games:
- PHI @ PIT | In Progress | Pittsburgh Pirates(home) 24-22 score:0 vs Philadelphia Phillies(away) 23-23 score:2
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: philadelphia phillies pittsburgh pirates
- [Bing News]
- [Sun, 17 May 2026] philadelphia phillies pittsburgh pirates
- → The Philadelphia Phillies first baseman Bryce Harper has seen his fair share high-profile pitchers in his career, but he has never faced one like Pi
- [Sun, 17 May 2026] Phillies’ Bryce Harper Sends Message to Paul Skenes Before Pirates Game
- → Here's how to watch Sunday's Pittsburgh Pirates vs Philadelphia Phillies game, including start times, TV channels, scores and how to stream.
- [Sun, 17 May 2026] Where to watch Philadelphia Phillies vs Pittsburgh Pirates: TV channel, start time, streaming for May 17
- → The Philadelphia Phillies visit the Pittsburgh Pirates Sunday for a 1:35 p.m. ET first pitch from PNC Park in Pittsburgh, Pennsylvania.

## LLM Decision
- **Action:** YES
- **Confidence:** 65%
- **p_true:** 60.8%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** FORM_PERFORMANCE
- **Catalyst Strength:** 0.75

### Reasoning
Massive 30% gap between Polymarket (50%) and bookmaker consensus (~80% for Phillies). FanDuel has Phillies at 1.27 (79% implied), Paddy Power at 1.25 (80% implied). Phillies are on a 6-game series win streak with Sánchez pitching a shutout yesterday. Sports pattern shows WR=85% from 13 trades. Market severely underpricing a strong favorite. Despite general stat suggesting 50% markets resolve YES only 44.7% of time, the specific sports evidence and bookmaker consensus overwhelmingly support Phillies victory.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=0%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Phillies'})` → INJURY [philadelphia phillies] Kyle Backhus (RP): 15-Day-IL
INJURY [philadelphia phillies] Zach Pop 
- `get_sports_data({'sport': 'mlb', 'team': 'Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `search_web({'query': 'Philadelphia Phillies vs Pittsburgh Pirates game preview'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Phillies vs Pirates Prediction, Picks &amp; Odds f
- `search_web({'query': 'Phillies Pirates series results recent 2026'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Philadelphia Phillies at Pittsburgh Pirates Game S
- `search_web({'query': '"Phillies" "Pirates" starting pitcher May 2026'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Bubba Chandler Poising Big Problem for Pirates - S
- `get_market_context({'keyword': 'Phillies Pirates'})` → No related markets found for 'Phillies Pirates'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Phillies'})` → [ODDS] baseball_mlb — 2 events
  Pittsburgh Pirates vs Philadelphia Phillies (2026-05-17)
    [FanDu
- `get_crypto_price({'coin': 'bitcoin'})` → bitcoin: $78,096.00 | 24h: -0.17%

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*