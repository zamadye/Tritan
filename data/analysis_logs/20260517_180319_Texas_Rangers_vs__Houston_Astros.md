# Market Analysis — 2026-05-17 18:03 UTC

## Market
- **Question:** Texas Rangers vs. Houston Astros
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $108,118
- **Liquidity:** $380,577

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,035 (-0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,047 (-0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
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
- → The Houston Astros (19-28) will play the final game of their seven-game homestand today as they go for a sweep in the first round of the Silver Boot
- [Sun, 17 May 2026] Astros vs. Rangers Game Thread: Game 48, 5/17/2026
- → Jose Altuve will undergo an MRI after leaving the Astros' 4-1 win over the Rangers amid Houston's 14-player IL crisis.
- [Sun, 17 May 2026] Astros’ Jose Altuve injury deals injury blow to Houston amid rough start to season
- → Here's how to watch Sunday's Houston Astros vs Texas Rangers game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 56.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'houston astros'})` → INJURY [houston astros] Jose Altuve (2B): Day-To-Day
INJURY [houston astros] Jeremy Pena (SS): 10-Da
- `get_sports_data({'sport': 'mlb', 'team': 'texas rangers'})` → INJURY [texas rangers] Corey Seager (SS): Day-To-Day
INJURY [texas rangers] Josh Smith (2B): 10-Day-
- `get_odds({'sport': 'baseball_mlb', 'team': 'texas rangers'})` → [ODDS] baseball_mlb — 1 events
  Houston Astros vs Texas Rangers (2026-05-17)
    [FanDuel] Houston 
- `search_web({'query': 'Texas Rangers vs Houston Astros game odds prediction April 2024'})` → [Sun, 26 Apr 2026] Google News
[Thu, 16 Apr 2026] Yankees vs Astros Prediction, Odds, Moneyline, Spr
- `get_market_context({'keyword': 'Texas Rangers Houston Astros'})` → No related markets found for 'Texas Rangers Houston Astros'
- `search_web({'query': 'Houston Astros vs Texas Rangers game May 17 2026 pitcher matchup'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Rangers vs. Astros (May 17, 2026) Live Score - ESP

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*