# Market Analysis — 2026-05-21 11:57 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $104,491
- **Liquidity:** $196,206

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,174 (-0.2% 24h) → neutral
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
- → The Atlanta Braves and Miami Marlins meet Thursday to complete a 4-game series at Loan Depot Park in Miami, Florida. First pitch is at 6:40 p.m. ET.
- [Thu, 21 May 2026] Atlanta Braves at Miami Marlins odds, picks, and predictions
- → Atlanta Braves (34-16, first in the NL East) vs. Miami Marlins (22-28, fourth in the NL East) Miami; Thursday, 6:40 p.m. EDT PITCHING PROBABLES: Bra

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 47.6%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICE
- **Catalyst Strength:** 0.82

### Reasoning
Strong statistical evidence (n=13,967) shows markets at 57% YES historically resolve YES only 44.7% of the time, indicating a 12.3% edge for NO. Pattern data confirms weakness in 50-60% entry range (38% WR). Braves have injury concerns (Baldwin, Waldrep, Farmer on IL) and recent pitching decision issues flagged by media. Market overprices YES by ~12% vs historical resolution rate.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves Marlins'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins game today 2025 preview'})` → [Tue, 19 May 2026] Google News
[Tue, 26 Aug 2025] Braves vs Marlins Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'Atlanta Braves recent form MLB 2025'})` → [2026-05-15] MLB Power Rankings Week 7: Mets, Phillies, Brewers and Braves Climb — We’re approaching
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins MLB'})` → No related markets found for 'Atlanta Braves Miami Marlins MLB'
- `search_web({'query': '"Braves" "Marlins" series May 2026 pitching matchup'})` → [2026-05-19] Who are Brewers probable pitchers vs Cubs? Jacob Misiorowski up next — Jacob Misiorowsk
- `search_web({'query': 'MLB standings 2026 NL East Braves Marlins win loss record'})` → [2026-05-05] Ranking MLB's eight new managers at the one-quarter mark of the 2026 season — From Walt
- `search_web({'query': 'Braves Marlins head to head 2026 results'})` → [2026-05-01] Two-start pitchers: Tarik Skubal headlines a gaggle of elite options as we steamroll in
- `search_web({'query': 'Atlanta Braves pitching rotation May 2026'})` → [2026-05-20] Philadelphia Phillies Rolling With Zack Wheeler Leading The Rotation — Zack Wheeler has
- `search_web({'query': '"Braves" "pitching decisions" "red flags" Anthopoulos Weiss 2026'})` → [2026-05-17] Braves writer raises red flags for GM Alex Anthopoulos, Walt Weiss over one drawn-out d
- `search_web({'query': 'Miami Marlins 2026 season record performance'})` → [2026-05-19] Atlanta Braves' Walt Weiss Shares Reason for JR Ritchie Decision — Atlanta Braves manag
- `search_web({'query': 'Braves Marlins MLB game odds lines May 20 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Braves vs Marlins Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'MLB game tomorrow Atlanta Braves opponent'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] 2026 MLB Season: Schedule Information, Latest Rule
- `search_web({'query': 'Braves vs Marlins May 20 2026 probable pitchers starting lineup'})` → [2026-05-19] Who are Brewers probable pitchers vs Cubs? Jacob Misiorowski up next — Jacob Misiorowsk
- `search_web({'query': 'FanDuel Braves Marlins odds moneyline May 20 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Braves vs Marlins Prediction, Odds, Moneyline, Spr

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*