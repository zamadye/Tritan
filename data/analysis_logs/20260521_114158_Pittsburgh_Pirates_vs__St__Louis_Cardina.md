# Market Analysis — 2026-05-21 11:41 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $68,732
- **Liquidity:** $244,528

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,229 (-0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,244 (-0.2% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: Gunnar Hoglund — 60-Day-IL (Surgery)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)
- ?: Max Muncy — 10-Day-IL (Fracture)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: pittsburgh pirates louis cardinals
- [Bing News]
- [Thu, 21 May 2026] pittsburgh pirates louis cardinals
- → Pittsburgh Pirates (25-24, fifth in the NL Central) vs. St. Louis Cardinals (28-20, second in the NL Central) St. Louis; Thursday, 1:15 p.m. EDT PIT
- [Thu, 21 May 2026] Pirates play the Cardinals after Griffin's 4-hit game
- → Here's how to watch Thursday's St. Louis Cardinals vs Pittsburgh Pirates game, including start times, TV channels, scores and how to stream.
- [Wed, 20 May 2026] Where to watch Pittsburgh Pirates vs St. Louis Cardinals: TV channel, start time, streaming for May 21
- → Spencer Horwitz homered, Konnor Griffin had four singles, and the Pittsburgh Pirates beat the St. Louis Cardinals 7-0 to snap a four-game losing str

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 43.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.85

### Reasoning
Strong stat signal (n=13,967) shows markets priced at 55% resolve YES only 44.7% of the time — market is overpricing YES by ~10 points. Both teams have similar injury counts, no obvious competitive advantage for Pirates. Entry 50-60% pattern shows only 40% WR (15 trades), reinforcing that YES is overpriced in this range. No contradictory evidence found in news or injury data to override the statistical edge. Prior skips were due to gap gate (<5%), not lack of edge — the 10-point mispricing from stat signal exceeds threshold for action.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals series preview 2024'})` → [2026-05-01] Knicks set NBA records in eliminating Hawks; 76ers take Celtics to Game 7; Kentucky Der
- `search_web({'query': 'MLB injury report today 2024 Pirates Cardinals'})` → [2026-05-13] The Trade Desk: Upcoming Outlier Matchups — Reviewing the first period of outlier match
- `search_web({'query': 'Pittsburgh Pirates St. Louis Cardinals head to head 2024'})` → [2026-05-19] Early Verdict On Pirates' Surprising Start — The Pittsburgh Pirates (24-23) are in four
- `search_web({'query': 'Cardinals Pirates series preview 2024'})` → [2026-05-08] New York Yankees vs. Milwaukee Brewers: Series Preview — Prepare for plenty of high-oct
- `get_market_context({'keyword': 'Pittsburgh Pirates St. Louis Cardinals'})` → No related markets found for 'Pittsburgh Pirates St. Louis Cardinals'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*