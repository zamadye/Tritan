# Market Analysis — 2026-05-17 20:00 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $204,513
- **Liquidity:** $112,658

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,359 (+0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,333 (+0.1% 24h) → neutral
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
- → The Colorado Rockies and Arizona Diamondbacks are in a rain delay as inclement weather moves through Denver on Sunday, May 17. Here's what you need 
- [Sun, 17 May 2026] Diamondbacks vs Rockies start time: Rain delay and weather updates from Coors Field
- → “As we look outside the radio booth right now, tons of dark and not the most welcoming clouds,” Diamondbacks play-by-play voice Chris Garagiola said

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 46.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.80

### Reasoning
Strong statistical signal (n=13,967) shows markets priced at 56% resolve YES only 44.7% of the time, creating an ~11% edge for NO. Bookmaker odds (1.69/2.22) imply ~59% win probability for Diamondbacks, but the market price is 56%, indicating overpricing of YES. No direct catalyst or breaking news to justify current price.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_odds({'sport': 'baseball_mlb', 'team': 'Diamondbacks'})` → [ODDS] baseball_mlb — 2 events
  Colorado Rockies vs Arizona Diamondbacks (2026-05-17)
    [FanDuel]
- `get_sports_data({'sport': 'mlb', 'team': 'Diamondbacks'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_sports_data({'sport': 'mlb', 'team': 'Rockies'})` → INJURY [colorado rockies] Tyler Freeman (RF): paternity
INJURY [colorado rockies] Chase Dollander (S
- `search_web({'query': 'Arizona Diamondbacks Colorado Rockies game 2026 May 17'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Diamondbacks vs. Rockies (May 17, 2026) Live Score
- `search_web({'query': 'Diamondbacks Rockies preview series'})` → [Thu, 14 May 2026] Google News
[Sun, 17 May 2026] Series Preview #15: Diamondbacks @ Rockies - AZ Sn
- `get_market_context({'keyword': 'Diamondbacks'})` → No related markets found for 'Diamondbacks'
- `search_web({'query': 'Diamondbacks Rockies May 17 2026 pitching matchup'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Diamondbacks vs Rockies Prediction, Odds, Moneylin

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*