# Market Analysis — 2026-05-21 11:58 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $71,254
- **Liquidity:** $235,036

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,174 (-0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,133 (-0.2% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: Gunnar Hoglund — 60-Day-IL (Surgery)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)
- ?: Max Muncy — 10-Day-IL (Fracture)

### Bing/Google News
- 6 articles found:
- [NewsAPI] Pirates bring 4-game losing streak into matchup against the Cardinals: Pittsburgh Pirates (24-24, fifth in the NL Central) vs. St. Louis Car
- [NewsAPI] Iván Herrera's 10th-Inning Blast Propels Cardinals to 15th Comeback Victory: Even on a night when the Cardinals squandered a two-run lead in
- [NewsAPI] Cardinals keep proving they’re built for chaos in thrilling walk-off win: St. Louis has something building.
- [NewsAPI] Pirates Predicted to Jump Cardinals for Paul Skenes Reason: Who would have thought that the National League Central would be the best divisi
- [NewsAPI] Iván Herrera's 3-run, walk-off homer in the 10th inning lifts Cardinals past Pir: Iván Herrera hit a three-run, walk-off home run in the bot
- [NewsAPI] Ivan Herrera’s Extra Inning Homer Gives Cardinals Walk-off Win Over Pirates: Matthew Liberatore had another strong start, but another not st
- [CAUSAL CHAINS] Relevant cause-effect patterns:

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
- **Confidence:** 52%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Stat signal shows market overpricing YES (55% price vs 44.7% historical resolution), but base rate gap is only 2% (< 5% threshold). No concrete catalyst or team-specific edge found. Both teams have moderate injuries. Previous analyses on same market correctly identified lack of edge. 50-60% entry band historically underperforms (38% WR).

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `get_market_context({'keyword': 'Pittsburgh Pirates St Louis Cardinals'})` → No related markets found for 'Pittsburgh Pirates St Louis Cardinals'
- `search_web({'query': 'Pittsburgh Pirates vs St Louis Cardinals 2025 series preview'})` → [2026-05-01] Knicks set NBA records in eliminating Hawks; 76ers take Celtics to Game 7; Kentucky Der
- `search_web({'query': 'Pittsburgh Pirates injuries roster news May 2025'})` → [Sun, 22 Mar 2026] Google News
[Thu, 27 Nov 2025] Pirates Give New Injury Update on Jared Jones - Sp
- `search_web({'query': 'St Louis Cardinals injuries roster news May 2025'})` → [2026-05-15] Fantasy Baseball Waiver Wire: JJ Bleday continues to rake, A.J. Ewing makes good first 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': '"Pirates" "Cardinals" MLB head to head 2025'})` → [2026-05-20] Iván Herrera's 10th-Inning Blast Propels Cardinals to 15th Comeback Victory — Even on a

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*