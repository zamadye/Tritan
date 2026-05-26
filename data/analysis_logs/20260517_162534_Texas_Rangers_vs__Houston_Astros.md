# Market Analysis — 2026-05-17 16:25 UTC

## Market
- **Question:** Texas Rangers vs. Houston Astros
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $90,422
- **Liquidity:** $344,359

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,036 (-0.3% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,055 (-0.3% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [SPORTS] Recent games:
- TEX @ HOU | Scheduled | Houston Astros(home) 19-28 score:0 vs Texas Rangers(away) 21-24 score:0
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: texas rangers houston astros
- [Bing News]
- [Sun, 17 May 2026] texas rangers houston astros
- → Jose Altuve will undergo an MRI after leaving the Astros' 4-1 win over the Rangers amid Houston's 14-player IL crisis.
- [Sun, 17 May 2026] Astros’ Jose Altuve injury deals injury blow to Houston amid rough start to season
- → Here's how to watch Sunday's Houston Astros vs Texas Rangers game, including start times, TV channels, scores and how to stream.
- [Sun, 17 May 2026] Where to watch Texas Rangers vs Houston Astros: TV channel, start time, streaming for May 17
- → Houston Astros: starting pitchers are Nathan Eovaldi for the Rangers and Peter Lambert for the Astros. Texas will attempt to avoid a sweep. They wil

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 48.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.70

### Reasoning
The stat signal shows markets priced at 54% historically resolve YES only 44.7% of the time (n=13,967) — a 9.3% overpricing. While bookmaker odds (Rangers ~55%) align with the base rate, the historical pattern strongly suggests systematic overpricing at this level. Sports category pattern shows 85% WR from 13 trades and 86% WR in the 50-60% entry range (7 trades). Injury context is mixed (both teams missing key players). The gap between market price (54%) and historical resolution rate (44.7%) represents a clear edge favoring NO.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Texas Rangers'})` → INJURY [texas rangers] Corey Seager (SS): Day-To-Day
INJURY [texas rangers] Josh Smith (2B): 10-Day-
- `get_sports_data({'sport': 'mlb', 'team': 'Houston Astros'})` → INJURY [houston astros] Jose Altuve (2B): Day-To-Day
INJURY [houston astros] Jeremy Pena (SS): 10-Da
- `search_web({'query': 'Texas Rangers vs Houston Astros game today 2025'})` → [Sat, 16 May 2026] Google News
[Mon, 15 Sep 2025] Rangers vs Astros Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'Texas Rangers Houston Astros upcoming series May 2026 odds'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Texas Rangers at Houston Astros odds, picks, and p
- `get_odds({'sport': 'baseball_mlb', 'team': 'Astros'})` → [ODDS] baseball_mlb — 1 events
  Houston Astros vs Texas Rangers (2026-05-17)
    [FanDuel] Houston 
- `get_market_context({'keyword': 'Texas Rangers Houston Astros'})` → No related markets found for 'Texas Rangers Houston Astros'
- `get_market_context({'keyword': 'MLB baseball'})` → No related markets found for 'MLB baseball'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*