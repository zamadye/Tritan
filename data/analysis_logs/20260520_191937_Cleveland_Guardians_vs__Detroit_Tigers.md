# Market Analysis — 2026-05-20 19:19 UTC

## Market
- **Question:** Cleveland Guardians vs. Detroit Tigers
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 7
- **Volume 24h:** $53,522
- **Liquidity:** $244,820

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,314 (+0.5% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,324 (+0.5% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- [SPORTS] Recent games:
- CLE @ DET | Scheduled | Detroit Tigers(home) 20-29 score:0 vs Cleveland Guardians(away) 28-22 score:0
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: cleveland guardians detroit tigers
- [Bing News]
- [Wed, 20 May 2026] cleveland guardians detroit tigers
- → The Cleveland Guardians have walked 11 times in the first two games of the series against the Tigers. Five of those walks turned into runs.
- [Wed, 20 May 2026] Tigers feel direct and collateral damage of walking Guardians hitters
- → Here's how to watch Wednesday's Detroit Tigers vs Cleveland Guardians game, including start times, TV channels, scores and how to stream.
- [Wed, 20 May 2026] Where to watch Cleveland Guardians vs Detroit Tigers: TV channel, start time, streaming for May 20
- → The Cleveland Guardians and the Detroit Tigers play the third of a 4-game series Wednesday in Detroit, Michigan. First pitch is set for 6:40 p.m. ET

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.60

### Reasoning
Markets at 53% historically resolve YES only 44.7% of the time (n=13,967), indicating systematic overpricing of YES. Pattern data confirms Entry 50-60% has only 33% win rate. Injury report shows Tigers have more significant injuries, but the statistical edge is the primary catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Cleveland Guardians'})` → INJURY [cleveland guardians] Gabriel Arias (SS): 10-Day-IL
INJURY [cleveland guardians] Peyton Palle
- `get_sports_data({'sport': 'mlb', 'team': 'Detroit Tigers'})` → INJURY [detroit tigers] Jackson Jobe (SP): 60-Day-IL
INJURY [detroit tigers] Troy Melton (RP): 60-Da
- `search_web({'query': 'Cleveland Guardians vs Detroit Tigers game preview September 2025'})` → [Wed, 24 Sep 2025] Google News
[Wed, 24 Sep 2025] Detroit Tigers at Cleveland Guardians Preview - 09
- `search_web({'query': 'Cleveland Guardians recent performance September 2025'})` → [Tue, 23 Sep 2025] Google News
[Mon, 27 Oct 2025] Guardians rally in the 6th inning - MLB.com
[Sat, 
- `get_market_context({'query': 'Cleveland Guardians Detroit Tigers'})` → [YES=50% vol=$6,544,356] Will Austria win the 2026 FIFA World Cup?
[YES=50% vol=$5,874,452] Trump ki
- `search_web({'query': 'Jackson Jobe Detroit Tigers pitcher 2025 season'})` → [Tue, 28 Apr 2026] Google News
[Mon, 30 Mar 2026] Jackson Jobe throws first bullpen in return from T
- `get_odds({'sport': 'baseball_mlb', 'team': 'Cleveland Guardians'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*