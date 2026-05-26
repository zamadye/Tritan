# Market Analysis — 2026-05-21 10:51 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $65,991
- **Liquidity:** $180,238

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,240 (-0.3% 24h) → neutral
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
- → Here's how to watch Thursday's St. Louis Cardinals vs Pittsburgh Pirates game, including start times, TV channels, scores and how to stream.
- [Thu, 21 May 2026] Where to watch Pittsburgh Pirates vs St. Louis Cardinals: TV channel, start time, streaming for May 21
- → Pittsburgh Pirates (25-24, fifth in the NL Central) vs. St. Louis Cardinals (28-20, second in the NL Central) St. Louis; Thursday, 1:15 p.m. EDT PIT
- [Thu, 21 May 2026] Pirates play the Cardinals after Griffin's 4-hit game
- → Spencer Horwitz homered, Konnor Griffin had four singles, and the Pittsburgh Pirates beat the St. Louis Cardinals 7-0 on Wednesday night to snap a f

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 57.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.60

### Reasoning
Strong stat signal (n=13,967) shows markets at 55% resolve YES only 44.7% of the time, suggesting ~10% overpricing of YES. However, gate check fails: gap=2% < 5% threshold. No concrete game-specific catalyst found. Both teams have minor injuries but nothing decisive. Entry 50-60% historically has poor WR=25% (n=12). Pattern suggests info gap trades only 55% WR. Past decisions on identical market correctly skipped. Recommend SKIP until gap widens or specific catalyst emerges.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals preview July 2025'})` → [Sun, 24 Aug 2025] Google News
[Wed, 29 Apr 2026] Pittsburgh Pirates at St. Louis Cardinals Preview 
- `search_web({'query': 'MLB Pirates Cardinals prediction July 2025'})` → [Tue, 01 Jul 2025] Google News
[Fri, 01 May 2026] Pirates vs. Cardinals Prediction, Odds, Picks - Ju
- `get_market_context({'keyword': 'Pittsburgh Pirates'})` → No related markets found for 'Pittsburgh Pirates'
- `get_market_context({'keyword': 'St. Louis Cardinals'})` → No related markets found for 'St. Louis Cardinals'
- `get_market_context({'keyword': 'Pirates Cardinals'})` → No related markets found for 'Pirates Cardinals'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Pirates Cardinals July 2025 game odds prediction'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Pirates vs Cardinals Prediction, Odds, Moneyline, 
- `search_web({'query': 'Pittsburgh Pirates recent results July 2025'})` → [Mon, 21 Jul 2025] Google News
[Wed, 23 Jul 2025] Detroit Tigers at Pittsburgh Pirates Game Story, S
- `search_web({'query': 'St. Louis Cardinals recent results July 2025'})` → [Mon, 28 Jul 2025] Google News
[Thu, 24 Jul 2025] Miami Marlins at St. Louis Cardinals Game Story, S

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*