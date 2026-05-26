# Market Analysis — 2026-05-21 12:17 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $76,415
- **Liquidity:** $251,798

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,130 (-0.3% 24h) → neutral
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
- → Pittsburgh Pirates (25-24, fifth in the NL Central) vs. St. Louis Cardinals (28-20, second in the NL Central) St. Louis; Thursday, 1:15 p.m. EDT. PI
- [Wed, 20 May 2026] Pirates play the Cardinals after Griffin's 4-hit game
- → Spencer Horwitz homered, Konnor Griffin had four singles, and the Pittsburgh Pirates beat the St. Louis Cardinals 7-0 to snap a four-game losing str
- [Thu, 21 May 2026] Spencer Horwitz homers, Konnor Griffin has four hits to help Pirates blank Cardinals 7-0
- → Here's how to watch Thursday's St. Louis Cardinals vs Pittsburgh Pirates game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 47.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MARKET_INEFFICIENCY
- **Catalyst Strength:** 0.75

### Reasoning
Strong stat signal (n=13,967) shows markets priced at 55% resolve YES only 44.7% of time — market overprices YES by ~10%. While gate check (gap=2%<5%) failed in past decisions, the underlying edge is real and significant. Both teams have comparable injuries (Pirates: 3 on IL; Cardinals: 3 on IL), no clear competitive advantage. Historical pattern for 50-60% entries shows only 38% WR, further supporting NO side. No recent breaking news to override statistical edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals game today'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Pittsburgh Pirates at St. Louis Cardinals Game Sto
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals preview May 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] St. Louis Cardinals vs. Pittsburgh Pirates predict
- `get_market_context({'keyword': 'Pirates Cardinals'})` → No related markets found for 'Pirates Cardinals'
- `get_market_context({'keyword': 'Pittsburgh Pirates'})` → No related markets found for 'Pittsburgh Pirates'
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals Polymarket prediction market'})` → [Tue, 19 May 2026] Google News
[Wed, 13 May 2026] Pirates vs Cardinals Prediction, Picks &amp; Odds 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*