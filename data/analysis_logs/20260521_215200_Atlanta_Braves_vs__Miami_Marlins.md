# Market Analysis — 2026-05-21 21:52 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $242,931
- **Liquidity:** $175,665

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,596 (+0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,700 (+0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- [SPORTS] Recent games:
- ATL @ MIA | Scheduled | Miami Marlins(home) 22-28 score:0 vs Atlanta Braves(away) 34-16 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Spencer Giesting — Day-To-Day (Not Specified)
- ?: A.J. Puk — 60-Day-IL (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → The Atlanta Braves are looking to take the final three games of their series against the Miami Marlins after getting shut out 12-0 in the opener. Th
- [Thu, 21 May 2026] Braves vs. Marlins Prediction, Odds, Probable Pitchers, Prop Bets for Thursday, May 21
- → The Braves are the best team in baseball and there is no denying that. On Wednesday, they just did something for the first time in over two decades.
- [Thu, 21 May 2026] Atlanta Braves just did something the organization hasn't done since 2003 with win over Marlins
- → MIAMI (AP) — Austin Riley and Dominic Smith hit three-run home runs, Chris Sale allowed just one run and struck out eight over seven innings, and th

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 60.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Market overprices YES at 57% vs statistical signal of 44.7%, but base rate (60%) conflicts. No recent news/catalysts. Past decisions for same matchup were SKIP/NO with conf=65% but remain unresolved. Gap (3%) below 5% threshold. Conflicting signals create uncertainty.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Hurston Waldrep (SP): 60-Day-IL
INJURY [atlanta braves] Drake Baldwin (C): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 60-Day-IL
INJURY [miami marlins] Leo Jimenez (3B): 7-day
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins MLB'})` → No related markets found for 'Atlanta Braves Miami Marlins MLB'
- `search_web({'query': 'Atlanta Braves vs Miami Marlins today lineup starting pitcher'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] The Scouting Report: Braves vs Marlins, Game Four 
- `search_web({'query': 'Atlanta Braves recent record 2025 season standings'})` → [Thu, 14 May 2026] Google News
[Tue, 05 May 2026] MLB Power Rankings Week 7: New team replaces Dodge
- `search_web({'query': 'Atlanta Braves vs Miami Marlins May 2026 game 4 starting pitcher odds'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'Miami Marlins recent record May 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Braves vs. Marlins (May 21, 2026) Pregame - ESPN
[

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*