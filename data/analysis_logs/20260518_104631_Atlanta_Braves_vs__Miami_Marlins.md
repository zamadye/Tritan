# Market Analysis — 2026-05-18 10:46 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 50.5%
- **Days Left:** 7
- **Volume 24h:** $52,921
- **Liquidity:** $187,966

## Statistical Prior
- **p_base:** 50.7%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,785 (-2.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,766 (-2.1% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Recent games:
- MIA @ TB | Final | Tampa Bay Rays(home) 30-15 score:6 vs Miami Marlins(away) 21-26 score:3
- BOS @ ATL | Final | Atlanta Braves(home) 32-15 score:8 vs Boston Red Sox(away) 19-27 score:1
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Mon, 18 May 2026] atlanta braves miami marlins
- → Here's how to watch Monday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.
- [Mon, 18 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 18
- → Here is your TV guide for the upcoming NL East slate between the Atlanta Braves and the Miami Marlins ...
- [Mon, 18 May 2026] How to Watch, Probable Starters for Braves vs Marlins Series
- → Atlanta Braves (32-15, first in the NL East) vs. Miami Marlins (21-26, fourth in the NL East) Miami; Monday, 6:40 p.m. EDT PITCHING PROBABLES: Brave

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 42.8%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.70

### Reasoning
Markets at 50% historically resolve YES only 44.7% of the time (n=13,967), creating a 5.3% edge for NO. Braves missing star Ronald Acuna Jr. adds context. Market overprices YES at coin-flip levels.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=0%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Eli White (CF): 7-Day IL
INJURY [atlanta braves] Ronald Acuna Jr. (RF): 10-D
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 15-Day-IL
INJURY [miami marlins] Ronny Henriquez (RP): 6
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 MLB matchup'})` → [Wed, 13 May 2026] Google News
[Tue, 14 Apr 2026] Atlanta Braves vs Miami Marlins | May 19, 2026 | M
- `search_web({'query': 'Braves Marlins prediction May 2025'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Miami Marlins vs. Atlanta Braves Series May 18-21:
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Braves Marlins'})` → No related markets found for 'Braves Marlins'
- `get_market_context({'keyword': 'Atlanta Braves'})` → No related markets found for 'Atlanta Braves'
- `search_web({'query': 'Atlanta Braves vs Miami Marlins head to head record 2025 2026'})` → [Mon, 18 May 2026] Google News
[Thu, 16 Apr 2026] Reason Ronald Acuña Jr. Likely Won't Play vs. Marl
- `search_web({'query': 'Braves Marlins series May 2026 starting pitchers'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'Miami Marlins 2026 record wins losses'})` → [Tue, 05 May 2026] Google News
[Sun, 01 Mar 2026] 2026 MLB Standings and Records: Spring Training - 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*