# Market Analysis — 2026-05-17 23:50 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 93.7%
- **Days Left:** 6
- **Volume 24h:** $540,137
- **Liquidity:** $73,414

## Statistical Prior
- **p_base:** 98.3%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.6%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,167 (-1.3% 24h) → risk-OFF
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,169 (-1.3% 24h) → risk-OFF
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
- → The Colorado Rockies and Arizona Diamondbacks are in a rain delay as inclement weather moves through Denver on Sunday, May 17. Here's what you need 
- [Sun, 17 May 2026] Diamondbacks vs Rockies start time: Rain delay and weather updates from Coors Field
- → Here's how to watch Sunday's Colorado Rockies vs Arizona Diamondbacks game, including start times, TV channels, scores and how to stream.
- [Sun, 17 May 2026] Where to watch Arizona Diamondbacks vs Colorado Rockies: TV channel, start time, streaming for May 17
- → Arizona's finale matchup begins in a delay.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 92.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE_IDENTIFIED
- **Catalyst Strength:** 0.10

### Reasoning
Insufficient specific information to determine edge. Market at 94% vs base rate 98% shows apparent gap, but: (1) base rate may be inflated by selection bias, (2) cannot verify starting pitchers or current form for this specific game, (3) past decisions on same market flagged conflicting signals, (4) no bookmaker odds or related markets available for cross-validation. Gap of ~4-5% is marginal and unclear if statistically significant given missing context.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Arizona Diamondbacks'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_sports_data({'sport': 'mlb', 'team': 'Colorado Rockies'})` → INJURY [colorado rockies] Tyler Freeman (RF): paternity
INJURY [colorado rockies] Chase Dollander (S
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies series 2025'})` → [Sun, 17 Aug 2025] Google News
[Thu, 14 Aug 2025] Arizona Diamondbacks at Colorado Rockies Game Stor
- `search_web({'query': 'Diamondbacks Rockies injury update June 2025'})` → [Thu, 29 Jan 2026] Google News
[Sun, 22 Jun 2025] Report: D-backs sign righty reliever Derek Law to 
- `get_market_context({'keyword': 'Arizona Diamondbacks'})` → No related markets found for 'Arizona Diamondbacks'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Diamondbacks'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies August 2025 betting odds'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Diamondbacks vs Rockies Prediction, Odds, Moneylin

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*