# Market Analysis — 2026-05-17 19:36 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $204,511
- **Liquidity:** $112,068

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,193 (-0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,200 (-0.0% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Denzel Clarke — 10-Day-IL (Bruise)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: arizona diamondbacks colorado rockies
- [Bing News]
- [Sun, 17 May 2026] arizona diamondbacks colorado rockies
- → The Colorado Rockies vs Arizona Diamondbacks game originally scheduled to begin at 1:10 PM MDT has been delayed due to rain in the Denver Metro area
- [Sun, 17 May 2026] Rockies vs Diamondbacks Rain Delay Updates
- → The Arizona Diamondbacks get seven home games. Three against the San Francisco Giants and four against the Colorado Rockies.
- [Sun, 17 May 2026] Diamondbacks wrap road trip, head home for Giants, Rockies series
- → Here's how to watch Sunday's Colorado Rockies vs Arizona Diamondbacks game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 48.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_REVERSION
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 56% resolve YES only 44.7% of time, creating ~11.3% edge for NO at current 44% price. Past analysis of identical market also indicated NO with 62-65% confidence. SPORTS pattern shows 85% WR from 13 trades.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Diamondbacks'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_sports_data({'sport': 'mlb', 'team': 'Rockies'})` → INJURY [colorado rockies] Tyler Freeman (RF): paternity
INJURY [colorado rockies] Chase Dollander (S
- `get_odds({'sport': 'baseball_mlb'})` → [ODDS] baseball_mlb — 28 events
  Washington Nationals vs Baltimore Orioles (2026-05-17)
    [FanDue
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies 2026 preview'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Diamondbacks vs Rockies Prediction, Odds &amp; Pla
- `search_web({'query': 'Rockies vs Diamondbacks odds May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Diamondbacks vs Rockies Prediction, Odds &amp; Pla
- `get_odds({'sport': 'baseball_mlb', 'team': 'Diamondbacks'})` → [ODDS] baseball_mlb — 2 events
  Colorado Rockies vs Arizona Diamondbacks (2026-05-17)
    [FanDuel]
- `get_market_context({'keyword': 'Diamondbacks'})` → No related markets found for 'Diamondbacks'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*