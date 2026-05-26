# Market Analysis — 2026-05-17 20:35 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 6
- **Volume 24h:** $223,232
- **Liquidity:** $120,061

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,297 (+0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,239 (-0.0% 24h) → neutral
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
- → “As we look outside the radio booth right now, tons of dark and not the most welcoming clouds,” Diamondbacks play-by-play voice Chris Garagiola said
- [Sun, 17 May 2026] Start of Diamondbacks-Rockies rubber match delayed due to weather
- → The Colorado Rockies vs Arizona Diamondbacks game originally scheduled to begin at 1:10 PM MDT has been delayed due to rain in the Denver Metro area
- [Sun, 17 May 2026] Rockies vs Diamondbacks Rain Delay Updates
- → The Arizona Diamondbacks and Colorado Rockies were to play their series finale in Denver on Sunday, May 17. The game was delayed by the weather.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 52.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.70

### Reasoning
Historical data (n=13,967) shows markets at 57% YES price resolve YES only 44.7% of the time, indicating significant market overpricing of YES. Sports pattern shows 86% win rate in 50-60% entry range from 7 trades. Edge of 12.3% for NO (Rockies win). Injuries affect both teams equally with no star players sidelined. Game delayed due to weather but no team-specific advantage identified.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Diamondbacks'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_sports_data({'sport': 'mlb', 'team': 'Rockies'})` → INJURY [colorado rockies] Tyler Freeman (RF): paternity
INJURY [colorado rockies] Chase Dollander (S
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies game today news'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Diamondbacks Game vs Rockies Delayed Due to Weathe
- `search_web({'query': 'Diamondbacks Rockies odds preview MLB May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Diamondbacks vs Rockies Prediction, Odds &amp; Pla
- `get_market_context({'keyword': 'Diamondbacks Rockies'})` → No related markets found for 'Diamondbacks Rockies'
- `search_web({'query': 'Diamondbacks Rockies starting pitchers May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Diamondbacks vs. Rockies (18 May, 2026) Live Score
- `search_web({'query': '"Diamondbacks vs. Rockies" probable starting pitchers May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Diamondbacks vs. Rockies Probable Starting Pitcher

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*