# Market Analysis — 2026-05-21 07:34 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $56,506
- **Liquidity:** $148,968

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,549 (+0.3% 24h) → neutral
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
- [Tue, 19 May 2026] Pirates Make Big Outfield Adjustment Before Cardinals Game
- → The Pittsburgh Pirates and St. Louis Cardinals meet Wednesday at Busch Stadium in St. Louis, Missouri. First pitch is at 7:45 p.m. ET.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals upcoming game 2025'})` → [2026-04-30] The Reds ended April with 20 wins. Now, they face NL Central contenders — April was goo
- `search_web({'query': 'Pirates Cardinals series pitching matchup 2025'})` → [2026-05-15] Fantasy Baseball Waiver Wire: JJ Bleday continues to rake, A.J. Ewing makes good first 
- `get_market_context({'keyword': 'Pirates Cardinals'})` → No related markets found for 'Pirates Cardinals'
- `search_web({'query': 'Pirates vs Cardinals 2026 MLB schedule'})` → [2026-05-18] Live sports on TV today: Streaming options, leagues, schedule (May 18-May 24) — This we
- `search_web({'query': 'Pittsburgh Pirates St. Louis Cardinals 2026 results'})` → [2026-05-15] MLB Power Rankings Week 7: Mets, Phillies, Brewers and Braves Climb — We’re approaching
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Cardinals vs Pirates betting odds today MLB'})` → [2026-05-19] Free MLB home run picks, odds for May 19: Oneil Cruz in expert's best bets for Tuesday 
- `search_web({'query': 'St. Louis Cardinals 2026 record standings'})` → [2026-05-16] Who is Northeast Florida's all-time best baseball player? Vote now — Readers can vote h
- `search_web({'query': 'Pittsburgh Pirates record 2026'})` → [2026-05-20] Reds beat surging Phillies behind Chase Burns' latest strong start — Chase Burns tossed
- `search_web({'query': 'St. Louis Cardinals record 2026'})` → [2026-05-19] Use DraftKings promo code for $100 in bonus bets by targeting Knicks-Cavaliers, Padres-

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*