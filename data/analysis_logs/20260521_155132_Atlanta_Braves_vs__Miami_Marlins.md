# Market Analysis — 2026-05-21 15:51 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $132,216
- **Liquidity:** $203,058

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,206 (-0.3% 24h) → neutral
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
- → The Atlanta Braves are looking to take the final three games of their series against the Miami Marlins after getting shut out 12-0 in the opener. Th
- [Thu, 21 May 2026] Braves vs. Marlins Prediction, Odds, Probable Pitchers, Prop Bets for Thursday, May 21
- → Here's how to watch Thursday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Stat signal shows market overprices YES (57% vs 44.7% historical resolution, n=13,967), suggesting a ~12% edge for NO. However, gate FAILS: market-base rate gap is only +3% (<5% threshold). No new catalyst or breaking news since last two SKIP/NO decisions on this same market. Braves injuries (3 players on IL) slightly support NO but insufficient to override gate failure. Entry range 50-60% historically shows weak 41% WR. Edge exists but lacks actionable catalyst to justify position.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 schedule'})` → [Sat, 09 Aug 2025] Google News
[Sun, 10 Aug 2025] Miami Marlins at Atlanta Braves Game Story, Scores
- `search_web({'query': 'Braves Marlins injury report August 2025'})` → [Tue, 19 May 2026] Google News
[Thu, 30 Apr 2026] Braves reveal devastating injury news amid flurry 
- `get_market_context({'keyword': 'Braves'})` → No related markets found for 'Braves'
- `get_market_context({'keyword': 'Atlanta'})` → No related markets found for 'Atlanta'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves recent results August 2025'})` → [Sun, 31 Aug 2025] Google News
[Sat, 16 Aug 2025] Atlanta Braves at Philadelphia Phillies Game Story

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*