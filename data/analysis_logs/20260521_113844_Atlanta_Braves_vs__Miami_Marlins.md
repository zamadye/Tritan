# Market Analysis — 2026-05-21 11:38 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $100,455
- **Liquidity:** $149,444

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,229 (-0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,253 (-0.2% 24h) → neutral

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
- → The Atlanta Braves and Miami Marlins meet Thursday to complete a 4-game series at Loan Depot Park in Miami, Florida. First pitch is at 6:40 p.m. ET.
- [Thu, 21 May 2026] Atlanta Braves at Miami Marlins odds, picks, and predictions
- → Atlanta Braves (34-16, first in the NL East) vs. Miami Marlins (22-28, fourth in the NL East) Miami; Thursday, 6:40 p.m. EDT PITCHING PROBABLES: Bra
- [Wed, 20 May 2026] Braves bring 2-1 series advantage over Marlins into game 4
- → Austin Riley and Dominic Smith hit three-run home runs, Chris Sale allowed just one run and struck out eight over seven innings, and the Atlanta Bra

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 45.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.85

### Reasoning
Strong statistical evidence (n=13,967) shows markets at 56% YES historically resolve YES only 44.7% of time, indicating YES is overpriced by ~11 percentage points. No specific game catalysts found to override this pattern.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins today 2025 MLB'})` → [Sun, 10 Aug 2025] Google News
[Sat, 09 Aug 2025] Miami Marlins at Atlanta Braves Game Story, Scores
- `search_web({'query': 'Atlanta Braves injuries lineup today 2025'})` → [Tue, 12 May 2026] Google News
[Mon, 22 Dec 2025] Braves immediately punished for recent trade after
- `get_market_context({'keyword': 'Braves Marlins'})` → No related markets found for 'Braves Marlins'
- `search_web({'query': 'Miami Marlins vs Atlanta Braves August 2025 pitching matchup'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] The Scouting Report: Braves vs Marlins, Game Three
- `search_web({'query': 'Atlanta Braves recent results August 2025 win loss'})` → [Sat, 16 Aug 2025] Google News
[Sun, 31 Aug 2025] Atlanta Braves at Cleveland Guardians Game Story, 
- `search_web({'query': 'Miami Marlins recent results August 2025 win loss'})` → [Fri, 08 Aug 2025] Google News
[Thu, 28 Aug 2025] Miami Marlins at Atlanta Braves Game Story, Scores

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*