# Market Analysis — 2026-05-17 18:39 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $113,183
- **Liquidity:** $328,897

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,104 (-0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,103 (-0.1% 24h) → neutral
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
- → Here's how to watch Sunday's Colorado Rockies vs Arizona Diamondbacks game, including start times, TV channels, scores and how to stream.
- [Sat, 16 May 2026] Where to watch Arizona Diamondbacks vs Colorado Rockies: TV channel, start time, streaming for May 17
- → The Colorado Rockies notched a close win over the Arizona Diamondbacks in a bit of an odd game where the final score doesn’t quite reflect how many 
- [Sun, 17 May 2026] Rockies 4, Diamondbacks 2: Colorado bounces back in a game of small ball at Coors Field
- → Arizona Diamondbacks (21-23, third in the NL West) vs. Colorado Rockies (18-28, fifth in the NL West) Denver; Sunday, 3:10 p.m. EDT PITCHING PROBABL

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 48.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.80

### Reasoning
Strong statistical signal (n=13,967) shows markets at 57% resolve YES only 44.7% of the time, indicating significant overpricing. Pattern data supports sports betting (85% WR) and 50-60% entry range (86% WR). Market price of 57% appears inflated compared to historical resolution rates.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Diamondbacks'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_sports_data({'sport': 'mlb', 'team': 'Rockies'})` → INJURY [colorado rockies] Tyler Freeman (RF): paternity
INJURY [colorado rockies] Chase Dollander (S
- `get_odds({'sport': 'baseball_mlb', 'team': 'Diamondbacks'})` → [ODDS] baseball_mlb — 1 events
  Colorado Rockies vs Arizona Diamondbacks (2026-05-17)
    [FanDuel]
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies 2025 game odds'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Diamondbacks vs Rockies Prediction, Odds, Moneylin
- `get_market_context({'keyword': 'Arizona Diamondbacks Colorado Rockies MLB'})` → No related markets found for 'Arizona Diamondbacks Colorado Rockies MLB'
- `search_web({'query': 'Arizona Diamondbacks recent form 2026 MLB season'})` → [Sun, 17 May 2026] Google News
[Tue, 05 May 2026] Where to watch Arizona Diamondbacks vs Colorado Ro
- `search_web({'query': 'Colorado Rockies recent results 2026'})` → [Sat, 16 May 2026] Google News
[Thu, 14 May 2026] Arizona Diamondbacks at Colorado Rockies Game Stor
- `search_web({'query': 'Diamondbacks Rockies May 17 2026 starting pitcher'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Diamondbacks vs. Rockies (18 May, 2026) Live Score

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*