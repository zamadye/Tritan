# Market Analysis — 2026-05-21 11:24 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $66,587
- **Liquidity:** $180,300

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,253 (-0.2% 24h) → neutral
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
- → Here's how to watch Thursday's St. Louis Cardinals vs Pittsburgh Pirates game, including start times, TV channels, scores and how to stream.
- [Wed, 20 May 2026] Where to watch Pittsburgh Pirates vs St. Louis Cardinals: TV channel, start time, streaming for May 21
- → Spencer Horwitz homered, Konnor Griffin had four singles, and the Pittsburgh Pirates beat the St. Louis Cardinals 7-0 to snap a four-game losing str
- [Thu, 21 May 2026] Spencer Horwitz homers, Konnor Griffin has four hits to help Pirates blank Cardinals 7-0
- → Pittsburgh Pirates (25-24, fifth in the NL Central) vs. St. Louis Cardinals (28-20, second in the NL Central) St. Louis; Thursday, 1:15 p.m. EDT PIT

## LLM Decision
- **Action:** SKIP
- **Confidence:** 52%
- **p_true:** 57.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.55

### Reasoning
Strong stat signal (n=13,967) suggests markets at 55% resolve YES only 44.7% of time (~10% overpricing), BUT base rate for this matchup is 57% (contradicting stat signal). Gap only 2%, below 5% gate. Entry 50-60% range historically weak (WR=36%). Both teams have comparable injury lists. Conflicting signals prevent confident action.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pittsburgh Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb', 'team': 'St. Louis Cardinals'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Pittsburgh Pirates'})` → No related markets found for 'Pittsburgh Pirates'
- `get_market_context({'keyword': 'St. Louis Cardinals'})` → No related markets found for 'St. Louis Cardinals'
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals 2025 preview'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] Pirates vs Cardinals Prediction, Odds, Moneyline, 
- `search_web({'query': 'Pittsburgh Pirates injuries update 2025'})` → [Tue, 12 Aug 2025] Google News
[Fri, 20 Mar 2026] Oneil Cruz leaves game with apparent injury - MLB.
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals odds today 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Pirates vs. Cardinals (May 21, 2026) Odds and Spre
- `search_web({'query': 'St. Louis Cardinals recent results form May 2026'})` → [Wed, 20 May 2026] Google News
[Sat, 02 May 2026] Where to watch Pittsburgh Pirates vs St. Louis Car
- `search_web({'query': '"Pittsburgh Pirates" "St. Louis Cardinals" May 21 2026 pitchers'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Pittsburgh Pirates vs. St. Louis Cardinals - Boxsc
- `search_web({'query': 'Pirates Cardinals series standings 2026 MLB'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Pirates vs Cardinals May 2026 series schedule'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] Pirates vs. Cardinals (21 May, 2026) Live Score - 
- `search_web({'query': 'Pittsburgh Pirates 2026 season record wins losses'})` → [Mon, 18 May 2026] Google News
[Wed, 20 May 2026] 2026 MLB Standings and Records: Regular Season - M

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*