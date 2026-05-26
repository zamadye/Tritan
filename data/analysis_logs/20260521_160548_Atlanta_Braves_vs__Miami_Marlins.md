# Market Analysis — 2026-05-21 16:05 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $134,114
- **Liquidity:** $211,258

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,194 (-0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,148 (-0.5% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- [SPORTS] Recent games:
- ATL @ MIA | Scheduled | Miami Marlins(home) 22-28 score:0 vs Atlanta Braves(away) 34-16 score:0
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)

### Bing/Google News
- 6 articles found:
- [NewsAPI] 2026-27 Club Options: NL East: In recent weeks, MLBTR has looked forward to next winter’s option classes. We’ll move now to the NL
- [NewsAPI] Braves News: Drake Baldwin to injured list, series even against Fish, and more: ﻿Atlanta Braves news and notes from Tuesday.
- [NewsAPI] Miami Marlins play the Atlanta Braves Wednesday: Atlanta Braves (33-16, first in the NL East) vs. Miami Marlins (22-27, fourth in the NL Eas
- [NewsAPI] Acuña scores 3 times in return as Braves bounce back against Marlins: It was Acuña’s first game since being sidelined May 2 because of a lef
- [NewsAPI] Braves place star catcher Drake Baldwin on 10-day IL with strained oblique: The Atlanta Braves placed star catcher Drake Baldwin on the 10-d
- [NewsAPI] Philadelphia Phillies Rolling With Zack Wheeler Leading The Rotation: Zack Wheeler has been as effective as ever after his return to the Phi
- [CAUSAL CHAINS] Relevant cause-effect patterns:

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → Austin Riley and Dominic Smith hit three-run home runs, Chris Sale allowed just one run and struck out eight over seven innings, and the Atlanta Bra
- [Thu, 21 May 2026] Atlanta Braves beat Miami Marlins 9-1 behind Chris Sale and 3-run homers from Austin Riley, Dominic Smith
- → MLB betting picks for Braves vs. Marlins highlight Spencer Strider's strong stats and Atlanta's impressive 18-8 road record this season so far.
- [Thu, 21 May 2026] Atlanta's road dominance and history against Sandy Alcantara make them the play vs. Miami Marlins
- → The Atlanta Braves are looking to take the final three games of their series against the Miami Marlins after getting shut out 12-0 in the opener. Th

## LLM Decision
- **Action:** SKIP
- **Confidence:** 52%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Stat signal (n=13,967) shows market at 57% overprices YES (historical resolution only 44.7%), suggesting NO side value. However, skipping due to: (1) Gap=3% fails gate threshold (<5%), (2) Entry price 50-60% historically has weak WR=41%, (3) Both teams have comparable injuries with no clear edge, (4) Past decisions for same market correctly skipped. While crowd appears to overprice YES, no concrete catalyst or breaking information to capitalize on this edge within 7-day window.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins May 2025'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] Braves 8-4 Marlins (May 19, 2026) Game Recap - ESP
- `search_web({'query': 'Polymarket Atlanta Braves vs Miami Marlins'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Braves vs Marlins Prediction, Picks &amp; Odds for
- `search_web({'query': 'Atlanta Braves vs Miami Marlins May 21 2026 game prediction'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Atlanta Braves at Miami Marlins odds, picks, and p
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins'})` → No related markets found for 'Atlanta Braves Miami Marlins'
- `search_web({'query': 'Braves Marlins May 21 2026 Strider Alcantara starting pitchers odds'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Braves vs. Marlins Odds, Props, Picks &amp; Predic

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*