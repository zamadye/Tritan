# Market Analysis — 2026-05-18 23:39 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 45.0%
- **Days Left:** 6
- **Volume 24h:** $585,359
- **Liquidity:** $100,346

## Statistical Prior
- **p_base:** 42.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,999 (-1.1% 24h) → risk-OFF
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
- → The Atlanta Braves got a big boost to their roster ahead of their four-game road series against the Miami Marlins.
- [Mon, 18 May 2026] Braves Make Ronald Acuna Jr. Announcement Before Marlins Game
- → Acu&#241;a left in the second inning against the Rockies on May 2 with hamstring tightness before an MRI revealed the strain.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 42%
- **p_true:** 42.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
No verifiable edge. Gap is only -2% (market 45% vs base rate 43%), far below the 5% threshold. Both teams have minor injuries with no star players out. No specific news catalyst identified. Historical pattern shows same matchup has been skipped twice before. Entry 40-50% zone has weak 33% WR historically. Insufficient evidence for a confident bet in either direction.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Kemp Alderman (RF): Day-To-Day
INJURY [miami marlins] Robby Snelling (SP): 15
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 series preview prediction'})` → [Tue, 14 Apr 2026] Google News
[Mon, 13 Apr 2026] Miami Marlins vs. Atlanta Braves prediction, pick 
- `search_web({'query': 'Atlanta Braves recent performance June 2025'})` → [Fri, 27 Jun 2025] Google News
[Wed, 28 Jan 2026] Phillies vs. Braves Highlights | 06/27/2025 | Atla
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins'})` → No related markets found for 'Atlanta Braves Miami Marlins'
- `search_web({'query': 'Miami Marlins recent performance June 2025'})` → [Sat, 16 May 2026] Google News
[Mon, 25 Aug 2025] Rays Look To Continue Red-Hot Performance Against 
- `search_web({'query': 'Atlanta Braves starting pitcher next game June 2025'})` → [Wed, 25 Feb 2026] Google News
[Sat, 23 Aug 2025] Opinion: Atlanta Braves boss Alex Anthopoulos make

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*