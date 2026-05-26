# Market Analysis — 2026-05-19 00:31 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 52.0%
- **Days Left:** 6
- **Volume 24h:** $182,006
- **Liquidity:** $83,442

## Statistical Prior
- **p_base:** 53.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,194 (+0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,194 (+0.1% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Recent games:
- BOS @ KC | In Progress | Kansas City Royals(home) 20-27 score:0 vs Boston Red Sox(away) 19-27 score:0
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: boston kansas city royals
- [Bing News]
- [Mon, 18 May 2026] boston kansas city royals
- → The Royals are scheduled to kick off their 9-game homestand with a series opener against Boston at The K on Monday night.
- [Mon, 18 May 2026] With eye on weather, Royals move up Monday game time for series opener vs. Red Sox
- → The Kansas City Royals and Boston Red Sox will open this week’s series in Missouri at 6:10 p.m. ET rather than 6:40 p.m. ET “out of an abundance of 
- [Mon, 18 May 2026] Royals change time of Monday’s Red Sox game due to threat of severe weather
- → Here's how to watch Monday's Kansas City Royals vs Boston Red Sox game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 45.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.70

### Reasoning
Historical stat signal (n=13,967) shows markets at 52% YES resolve only 44.7% of the time, indicating systematic overpricing of YES. This provides a concrete edge with a 7.3 percentage point gap. Minor weather change and balanced injuries are not significant catalysts. Pattern data shows 40% win rate for bets in the 50-60% range, supporting contrarian NO bets in this bracket.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Boston Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `get_sports_data({'sport': 'mlb', 'team': 'Kansas City Royals'})` → INJURY [kansas city royals] Kris Bubic (SP): 15-Day-IL
INJURY [kansas city royals] Cole Ragans (SP):
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals today game'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Royals game vs. Red Sox moved up due to severe wea
- `search_web({'query': 'Red Sox Royals game news recent results'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Red Sox vs. Royals series matches two struggling t
- `get_market_context({'keyword': 'Red Sox'})` → No related markets found for 'Red Sox'
- `get_market_context({'keyword': 'Kansas City Royals'})` → No related markets found for 'Kansas City Royals'
- `search_web({'query': '"Boston Red Sox" "Kansas City Royals" prediction odds'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Red Sox vs Royals Prediction, Picks &amp; Odds for

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*