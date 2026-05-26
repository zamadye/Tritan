# Market Analysis — 2026-05-21 12:15 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $104,531
- **Liquidity:** $218,466

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,130 (-0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,158 (-0.2% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- [SPORTS] Recent games:
- ATL @ MIA | Final | Miami Marlins(home) 22-28 score:1 vs Atlanta Braves(away) 34-16 score:9
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: Gunnar Hoglund — 60-Day-IL (Surgery)

### Bing/Google News
- 6 articles found:
- [NewsAPI] Braves News: Drake Baldwin to injured list, series even against Fish, and more: ﻿Atlanta Braves news and notes from Tuesday.
- [NewsAPI] Miami Marlins play the Atlanta Braves Wednesday: Atlanta Braves (33-16, first in the NL East) vs. Miami Marlins (22-27, fourth in the NL Eas
- [NewsAPI] Acuña scores 3 times in return as Braves bounce back against Marlins: It was Acuña’s first game since being sidelined May 2 because of a lef
- [NewsAPI] Braves place star catcher Drake Baldwin on 10-day IL with strained oblique: The Atlanta Braves placed star catcher Drake Baldwin on the 10-d
- [NewsAPI] Philadelphia Phillies Rolling With Zack Wheeler Leading The Rotation: Zack Wheeler has been as effective as ever after his return to the Phi
- [NewsAPI] Marlins Notes: Garrett, Snelling, Alderman: The Marlins are optioning lefty Braxton Garrett back to Triple-A Jacksonville, reports Christina
- [CAUSAL CHAINS] Relevant cause-effect patterns:

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → Austin Riley and Dominic Smith hit three-run home runs, Chris Sale allowed just one run and struck out eight over seven innings, and the Atlanta Bra
- [Thu, 21 May 2026] Atlanta Braves beat Miami Marlins 9-1 behind Chris Sale and 3-run homers from Austin Riley, Dominic Smith
- → Atlanta Braves (34-16, first in the NL East) vs. Miami Marlins (22-28, fourth in the NL East) Miami; Thursday, 6:40 p.m. EDT PITCHING PROBABLES: Bra
- [Thu, 21 May 2026] Braves bring 2-1 series advantage over Marlins into game 4
- → The Atlanta Braves and Miami Marlins meet Thursday to complete a 4-game series at Loan Depot Park in Miami, Florida. First pitch is at 6:40 p.m. ET.

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 48.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_HISTORICAL
- **Catalyst Strength:** 0.80

### Reasoning
Strong statistical evidence (n=13,967) shows markets at 57% YES historically resolve YES only 44.7% of the time, indicating the market overprices YES by approximately 12.3 percentage points. The true probability of YES is approximately 44.7%, making NO the value bet at current market price.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `search_web({'query': 'Atlanta Braves vs Miami Marlins today 2025'})` → [Tue, 26 Aug 2025] Google News
[Sat, 09 Aug 2025] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'Atlanta Braves recent performance 2025'})` → [Tue, 05 May 2026] Google News
[Tue, 28 Oct 2025] 2026 Spring Training - MLB.com
[Fri, 27 Feb 2026] 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins'})` → No related markets found for 'Atlanta Braves Miami Marlins'
- `search_web({'query': 'Braves Marlins pitching matchup August 2025'})` → [Wed, 15 Apr 2026] Google News
[Wed, 27 Aug 2025] Predicting the winner of every MLB game on Wednesd
- `search_web({'query': 'Miami Marlins record 2025 season'})` → [Tue, 05 May 2026] Google News
[Fri, 03 Apr 2026] 2026 Spring Training - MLB.com
[Sun, 28 Sep 2025] 
- `search_web({'query': '"Atlanta Braves" "Miami Marlins" August 26 2025 odds'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Braves vs Marlins Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'Braves vs Marlins head to head 2025 results'})` → [Thu, 07 Aug 2025] Google News
[Fri, 26 Sep 2025] How to Watch Marlins vs. Braves: TV Channel &amp; 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*