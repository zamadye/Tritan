# Market Analysis — 2026-05-21 12:40 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $77,355
- **Liquidity:** $253,827

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,180 (-0.4% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,191 (-0.3% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: Gunnar Hoglund — 60-Day-IL (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: pittsburgh pirates louis cardinals
- [Bing News]
- [Thu, 21 May 2026] pittsburgh pirates louis cardinals
- → Pittsburgh Pirates (25-24, fifth in the NL Central) vs. St. Louis Cardinals (28-20, second in the NL Central) St. Louis; Thursday, 1:15 p.m. EDT PIT
- [Wed, 20 May 2026] Pirates play the Cardinals after Griffin's 4-hit game
- → Spencer Horwitz homered, Konnor Griffin had four singles, and the Pittsburgh Pirates beat the St. Louis Cardinals 7-0 to snap a four-game losing str
- [Thu, 21 May 2026] Spencer Horwitz homers, Konnor Griffin has four hits to help Pirates blank Cardinals 7-0
- → Here's how to watch Thursday's St. Louis Cardinals vs Pittsburgh Pirates game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Strong stat signal (n=13,967) suggests market overprices YES at 55% (historical resolution 44.7%), but this conflicts with base rate (57%) suggesting market underprices YES. Gap is only 2% (below 5% threshold). No specific catalyst, injury update, or breaking news for this May 21 matchup beyond general injuries on both teams. Entry range 50-60% has poor historical win rate (38%). Previous decisions on identical market were SKIP. Cannot establish concrete edge without game-specific evidence.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `search_web({'query': 'Pittsburgh Pirates news today'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] Game #49: Pittsburgh Pirates vs. St. Louis Cardina
- `search_web({'query': 'St. Louis Cardinals news today'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Checking in on St. Louis Cardinals pitching prospe
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals May 21 2026 odds prediction starting pitchers'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Pirates vs Cardinals Prediction, Odds, Moneyline, 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pittsburgh Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Pittsburgh Pirates St. Louis Cardinals'})` → No related markets found for 'Pittsburgh Pirates St. Louis Cardinals'
- `search_web({'query': 'Pirates vs Cardinals May 21 2026 starting pitchers picks'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `get_odds({'sport': 'baseball_mlb', 'team': 'Cardinals'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*