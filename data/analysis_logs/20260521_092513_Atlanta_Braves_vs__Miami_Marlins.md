# Market Analysis — 2026-05-21 09:25 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $82,998
- **Liquidity:** $135,958

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,871 (+0.7% 24h) → neutral
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
- [MULTI-SOURCE NEWS] 1 sources for: atlanta braves miami marlins
- [Metaculus]
- [] Will a case of Bundibugyo Ebola disease be first confirmed in the US b
- → Community: pending
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending
- [] Will the Sentinel‑2 archive be compressed at a ratio of 1000× before 2
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 50%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Historical stat signal suggests NO value (57% markets resolve YES only 44.7%, n=13,967), indicating potential 12.3% edge. However: (1) No specific catalysts found via searches — injury reports show minor IL placements for both teams with no star players out; (2) Entry 50-60% pattern shows only 25% WR from 12 trades (weak); (3) Gap between market (57%) and base rate (60%) is only +3%, below 5% threshold; (4) Two prior decisions on this exact market both SKIPed with same reasoning. Without concrete team-specific evidence or a verifiable information gap, cannot confirm the historical edge applies to this specific matchup.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `search_web({'query': 'Atlanta Braves vs Miami Marlins June 2025 game preview'})` → [Tue, 26 Aug 2025] Google News
[Mon, 25 Aug 2025] Atlanta Braves at Miami Marlins Preview - 08/27/20
- `search_web({'query': 'Braves Marlins 2025 season series standings'})` → [Mon, 18 May 2026] Google News
[Mon, 11 Aug 2025] 2026 MLB Standings and Records: Regular Season - M
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Atlanta Braves'})` → No related markets found for 'Atlanta Braves'
- `search_web({'query': 'Atlanta Braves recent results August 2025'})` → [Sat, 16 Aug 2025] Google News
[Sun, 31 Aug 2025] Atlanta Braves at Cleveland Guardians Game Story, 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*