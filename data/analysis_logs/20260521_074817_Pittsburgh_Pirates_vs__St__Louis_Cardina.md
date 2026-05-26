# Market Analysis — 2026-05-21 07:48 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $56,576
- **Liquidity:** $154,053

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,647 (+0.6% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,551 (+0.3% 24h) → neutral

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
- [NewsAPI] Iván Herrera's 10th-Inning Blast Propels Cardinals to 15th Comeback Victory: Even on a night when the Cardinals squandered a two-run lead in
- [NewsAPI] Cardinals keep proving they’re built for chaos in thrilling walk-off win: St. Louis has something building.
- [NewsAPI] Pirates Predicted to Jump Cardinals for Paul Skenes Reason: Who would have thought that the National League Central would be the best divisi
- [NewsAPI] Iván Herrera's 3-run, walk-off homer in the 10th inning lifts Cardinals past Pir: Iván Herrera hit a three-run, walk-off home run in the bot
- [NewsAPI] Ivan Herrera’s Extra Inning Homer Gives Cardinals Walk-off Win Over Pirates: Matthew Liberatore had another strong start, but another not st
- [NewsAPI] Pirates Tie it in 9th But Fall To Cardinals in Extras on Walk-Off Home Run: The Pittsburgh Pirates rallied to tie the game in the ninth inni

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: pittsburgh pirates louis cardinals
- [Bing News]
- [Wed, 20 May 2026] pittsburgh pirates louis cardinals
- → Spencer Horwitz homered, Konnor Griffin had four singles, and the Pittsburgh Pirates beat the St. Louis Cardinals 7-0 to snap a four-game losing str
- [Wed, 20 May 2026] Spencer Horwitz homers, Konnor Griffin has four hits to help Pirates blank Cardinals 7-0
- → The Pittsburgh Pirates have a new look outfield vs. the Cardinals.
- [Wed, 20 May 2026] Pirates Make Big Outfield Adjustment Before Cardinals Game
- → The Pittsburgh Pirates got a home run from Spencer Horwitz as they emphatically snapped their four-game losing streak with a 7-0 win Wednesday night

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.15

### Reasoning
STAT SIGNAL from n=13,967 shows YES at 55% overpriced (true ~44.7%), suggesting BET_NO edge. However, conflicting PATTERN data shows only 25% WR in 50-60% entry zone from 12 trades, and no direct catalyst exists. Injuries are balanced, no news edge. Statistical mean reversion is speculative without a driving event. Insufficient confidence to overcome poor execution history in this entry zone.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pirates Cardinals'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Pirates Cardinals MLB'})` → No related markets found for 'Pirates Cardinals MLB'
- `search_web({'query': 'Pittsburgh Pirates 2025 season record standings'})` → [2026-05-18] National League West report: Feasting on American League — Dodgers and Padres both swep
- `search_web({'query': 'St. Louis Cardinals 2025 season record standings'})` → [Mon, 18 May 2026] Google News
[Fri, 11 Jul 2025] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Pirates vs Cardinals upcoming game preview 2025'})` → [Thu, 28 Aug 2025] Google News
[Thu, 28 Aug 2025] Pittsburgh Pirates at St. Louis Cardinals Preview 
- `search_web({'query': 'Pittsburgh Pirates recent games results May 2026'})` → [Thu, 21 May 2026] Google News
[Sat, 16 May 2026] Pittsburgh Pirates vs. Toronto Blue Jays - Boxscor
- `search_web({'query': 'St. Louis Cardinals recent performance 2026'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Jesús Made's four-RBI performance - MLB.com
[Thu, 
- `search_web({'query': '"Pirates" "Cardinals" May 20 2026 prediction odds pitcher'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] How to watch Pirates vs. Cardinals: TV channel and
- `search_web({'query': 'Pirates vs Cardinals May 20 2026 odds DraftKings prediction'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] St. Louis Cardinals vs. Pittsburgh Pirates predict
- `search_web({'query': 'Pirates Cardinals 2026 head to head record season series'})` → [Thu, 21 May 2026] Google News
[Mon, 18 May 2026] Pirates vs Cardinals Prediction, Odds, Moneyline, 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*