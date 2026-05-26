# Market Analysis — 2026-05-21 10:18 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $94,230
- **Liquidity:** $150,779

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,573 (+0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,556 (+0.1% 24h) → neutral

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
- → Atlanta Braves (34-16, first in the NL East) vs. Miami Marlins (22-28, fourth in the NL East) Miami; Thursday, 6:40 p.m. EDT PITCHING PROBABLES: Bra
- [Thu, 21 May 2026] Braves bring 2-1 series advantage over Marlins into game 4
- → Austin Riley and Dominic Smith hit three-run home runs, Chris Sale allowed just one run and struck out eight over seven innings, and the Atlanta Bra
- [Wed, 20 May 2026] Braves beat Marlins 9-1 behind Chris Sale and 3-run homers from Austin Riley, Dominic Smith
- → The Atlanta Braves make headlines with their decision on Ha-Seong Kim amid a competitive series against the Miami Marlins.

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 46.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL SIGNAL
- **Catalyst Strength:** 0.80

### Reasoning
Historical data (n=13,967) shows markets at 56% YES resolve YES only 44.7% of time, indicating market overprices YES by 11.3%. Edge for NO bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 recent game results standings'})` → [Mon, 18 May 2026] Google News
[Mon, 11 Aug 2025] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Braves vs Marlins May 2025 matchup preview predictions'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Braves vs. Marlins Odds, Props, Picks &amp; Predic
- `get_market_context({'keyword': 'Braves Marlins'})` → No related markets found for 'Braves Marlins'
- `get_market_context({'keyword': 'MLB baseball'})` → No related markets found for 'MLB baseball'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*