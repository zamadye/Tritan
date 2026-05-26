# Market Analysis — 2026-05-21 09:26 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $63,461
- **Liquidity:** $140,785

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,871 (+0.7% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,865 (+0.6% 24h) → neutral

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
- [Wed, 20 May 2026] Pirates play the Cardinals after Griffin's 4-hit game
- → Spencer Horwitz homered, Konnor Griffin had four singles, and the Pittsburgh Pirates beat the St. Louis Cardinals 7-0 to snap a four-game losing str
- [Thu, 21 May 2026] Spencer Horwitz homers, Konnor Griffin has four hits to help Pirates blank Cardinals 7-0
- → After ending a four-game skid on Wednesday, the Pittsburgh Pirates are now looking to take their midweek series against the Cardinals outright in th

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.30

### Reasoning
Stat signal (n=13,967) suggests market overprices YES at 55% (true ~44.7%), but +2% gap is below 5% gate threshold. Entry 50-60% historical win rate is poor (25%). Both teams have significant injuries (Pirates: SP Jared Jones; Cardinals: LF Nootbaar). No breaking news or direct catalyst identified. Two similar past decisions were SKIP.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `search_web({'query': 'Pittsburgh Pirates recent news results June 2025'})` → [Wed, 25 Jun 2025] Google News
[Sat, 28 Jun 2025] Pittsburgh Pirates at Milwaukee Brewers Game Story
- `search_web({'query': 'St. Louis Cardinals recent news results June 2025'})` → [Mon, 30 Mar 2026] Google News
[Sat, 21 Jun 2025] New York Mets at St. Louis Cardinals Game Story, S
- `search_web({'query': 'Pirates vs Cardinals 2025 matchup preview'})` → [Tue, 19 May 2026] Google News
[Wed, 27 Aug 2025] Cardinals vs Pirates Prediction, Odds, Moneyline, 
- `search_web({'query': '"Pittsburgh Pirates" "St. Louis Cardinals" June 2025 standings'})` → [Mon, 18 May 2026] Google News
[Wed, 20 Aug 2025] 2026 MLB Standings and Records: Regular Season - M
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pittsburgh Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*