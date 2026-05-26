# Market Analysis — 2026-05-21 09:08 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $81,599
- **Liquidity:** $102,106

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,822 (+0.6% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,842 (+0.6% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- [SPORTS] Recent games:
- ATL @ MIA | Final | Miami Marlins(home) 22-28 score:1 vs Atlanta Braves(away) 34-16 score:9
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: Gunnar Hoglund — 60-Day-IL (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → Austin Riley and Dominic Smith hit three-run home runs, Chris Sale allowed just one run and struck out eight over seven innings, and the Atlanta Bra
- [Thu, 21 May 2026] Braves beat Marlins 9-1 behind Chris Sale and 3-run homers from Austin Riley, Dominic Smith
- → Atlanta Braves (34-16, first in the NL East) vs. Miami Marlins (22-28, fourth in the NL East) Miami; Thursday, 6:40 p.m. EDT PITCHING PROBABLES: Bra
- [Wed, 20 May 2026] Braves bring 2-1 series advantage over Marlins into game 4
- → The Atlanta Braves make headlines with their decision on Ha-Seong Kim amid a competitive series against the Miami Marlins.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins game today 2025'})` → [Tue, 26 Aug 2025] Google News
[Sat, 09 Aug 2025] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'Atlanta Braves injuries lineup news'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Fantasy baseball: Acuna returns for Braves and mor
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `get_market_context({'query': 'Atlanta Braves Miami Marlins'})` → [YES=50% vol=$7,729,478] Trump kiss by May 31?
[YES=50% vol=$5,821,653] Will Bitcoin hit $150k by Ju
- `search_web({'query': 'Miami Marlins injuries news August 2025'})` → [Thu, 21 May 2026] Google News
[Fri, 01 May 2026] What happened to Trent Grisham? Live injury update
- `search_web({'query': 'Braves vs Marlins pitching matchup August 2025 starting pitchers'})` → [Wed, 15 Apr 2026] Google News
[Thu, 14 Aug 2025] Predicting the winner of every MLB game on Wednesd

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*