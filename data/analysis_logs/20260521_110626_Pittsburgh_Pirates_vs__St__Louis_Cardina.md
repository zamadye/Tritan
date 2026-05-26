# Market Analysis — 2026-05-21 11:06 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $66,359
- **Liquidity:** $177,135

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,174 (-0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,265 (-0.3% 24h) → neutral

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
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Stat signal strongly suggests market overprices YES (44.7% historical resolution vs 55% price), but gap of +2% fails the 5% gate threshold. Past decisions on same market also SKIPPED for identical reason. No new catalysts or breaking news found. Injury data shows both teams have similar IL counts with no asymmetric advantage. Pattern data shows Entry 50-60% has only 31% WR (13 trades), indicating this price range is historically unprofitable. Despite the ~10% theoretical edge from stat signal, the gap gate prevents action.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals recent results'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Pittsburgh Pirates at St. Louis Cardinals Game Sto
- `search_web({'query': 'Pittsburgh Pirates 2026 season performance record'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] 2026 Pittsburgh Pirates Top 30 Prospects May Updat
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pittsburgh Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Pittsburgh Pirates St. Louis Cardinals'})` → No related markets found for 'Pittsburgh Pirates St. Louis Cardinals'
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals odds May 2026'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] St. Louis Cardinals vs. Pittsburgh Pirates - May 2
- `search_web({'query': 'St. Louis Cardinals recent form May 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Where to watch Pittsburgh Pirates vs St. Louis Car

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*