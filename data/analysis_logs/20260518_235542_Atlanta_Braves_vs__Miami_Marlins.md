# Market Analysis — 2026-05-18 23:55 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 36.0%
- **Days Left:** 6
- **Volume 24h:** $606,236
- **Liquidity:** $32,298

## Statistical Prior
- **p_base:** 29.7%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 6.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,037 (-0.1% 24h) → neutral
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,967 (-1.0% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- [SPORTS] Recent games:
- ATL @ MIA | In Progress | Miami Marlins(home) 21-26 score:0 vs Atlanta Braves(away) 32-15 score:0
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Mon, 18 May 2026] atlanta braves miami marlins
- → The Miami Marlins (21-25) will try to beat the Atlanta Braves (31-15) at LoanDepot Park on Tuesday. The line on this contest has the Braves at -160 
- [Mon, 18 May 2026] Atlanta Braves vs Miami Marlins Prediction, 5/19/2026 MLB Picks, Best Bets &amp; Odds
- → Plate umpire Alfonso M&#225;rquez left in the second inning of Monday's game between the Atlanta Braves and Miami Marlins after being hit in the mas
- [Mon, 18 May 2026] Umpire Alfonso M&#225;rquez leaves in 2nd inning of Braves-Marlins game after being struck by foul ball
- → The Atlanta Braves got a big boost to their roster ahead of their four-game road series against the Miami Marlins.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 42%
- **p_true:** 29.7%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
6% gap exceeds threshold (base rate 30% vs YES 36%), suggesting market overprices YES. However, no concrete evidence found to exploit this edge: bookmaker odds API failed, starting pitchers unknown, recent team form unavailable, and search results returned no useful matchup data. Both teams have only minor injuries. Without verifying WHY the gap exists (e.g., starter advantage, rest day, bullpen status), cannot confirm directional bet. Previous two decisions on same market were SKIPs with 1-2% gaps; current gap is larger but unverified. Pattern data (sports WR=85%, entry 30-40% WR=67%) is positive but insufficient without catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 42%<52%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `search_web({'query': 'Atlanta Braves vs Miami Marlins recent matchup 2024'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] How To Watch Marlins vs. Braves Game 1: Max Meyer 
- `search_web({'query': 'Braves Marlins injury report today 2024'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Marlins vs. Braves: Injury Report, Updates &amp; P
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins'})` → No related markets found for 'Atlanta Braves Miami Marlins'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves 2026 season record standings'})` → [Tue, 05 May 2026] Google News
[Thu, 23 Apr 2026] 2026 MLB Standings and Records: Spring Training - 
- `get_sports_data({'sport': 'mlb', 'team': 'Marlins'})` → INJURY [miami marlins] Kemp Alderman (RF): Day-To-Day
INJURY [miami marlins] Robby Snelling (SP): 15
- `search_web({'query': '"Braves" "Marlins" starting pitcher May 2025'})` → [Sat, 16 May 2026] Google News
[Fri, 16 Jan 2026] Miami Marlins vs. Atlanta Braves Series May 18-21:

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*