# Market Analysis — 2026-05-21 08:48 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $58,725
- **Liquidity:** $140,901

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,832 (+0.5% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,832 (+0.5% 24h) → neutral

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
- → After ending a four-game skid on Wednesday, the Pittsburgh Pirates are now looking to take their midweek series against the Cardinals outright in th
- [Wed, 20 May 2026] After ending skid, Pirates look to build on win against Cardinals
- → Spencer Horwitz homered, Konnor Griffin had four singles, and the Pittsburgh Pirates beat the St. Louis Cardinals 7-0 to snap a four-game losing str

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 51.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.65

### Reasoning
Stat signal (n=13,967) shows YES at 55% overpriced with true probability ~44.7%, providing ~10% edge for NO. Both teams have balanced injuries. Recent Pirates wins may explain elevated YES pricing, but historical data suggests market correction likely. However, confidence tempered by: (1) small base rate gap of 2% vs 5% threshold, (2) weak WR in 50-60% entry range (25%), and (3) recent Pirates form supporting some YES premium.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals upcoming game 2025'})` → [Tue, 26 Aug 2025] Google News
[Wed, 27 Aug 2025] Pittsburgh Pirates at St. Louis Cardinals Game Sto
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals series schedule 2025'})` → [Tue, 26 Aug 2025] Google News
[Fri, 15 May 2026] Pittsburgh Pirates at St. Louis Cardinals Game Sto
- `get_market_context({'keyword': 'Pittsburgh Pirates'})` → No related markets found for 'Pittsburgh Pirates'
- `get_market_context({'keyword': 'Cardinals'})` → No related markets found for 'Cardinals'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pittsburgh Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*