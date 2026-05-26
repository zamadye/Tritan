# Market Analysis — 2026-05-19 08:47 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $68,446
- **Liquidity:** $129,108

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,118 (+0.3% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,000 (+0.1% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Recent games:
- ATL @ MIA | Final | Miami Marlins(home) 22-26 score:12 vs Atlanta Braves(away) 32-16 score:0
- [SPORTS] Injuries:
- ?: James McCann — Out (Strain)
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Tue, 19 May 2026] atlanta braves miami marlins
- → Atlanta Braves (32-16, first in the NL East) vs. Miami Marlins (22-26, fourth in the NL East) Miami; Tuesday, 4:10 p.m. EDT PITCHING PROBABLES: Brav
- [Mon, 18 May 2026] Marlins try to keep home win streak going, host the Braves
- → According to Francys Romero of Beisbol FR, the Atlanta Braves are calling up a player to the MLB. They are in a series with the Marlins.
- [Tue, 19 May 2026] Atlanta Braves Make Roster Move After Marlins Game
- → Mack had a season-high four RBI and was stellar defensively behind the plate again as the Marlins shut out the Braves 12-0.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 63%
- **p_true:** 60.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MISPRICING
- **Catalyst Strength:** 0.60

### Reasoning
Historical signal strongly suggests YES is overpriced at 57% (resolves YES only 44.7% historically), but gap (3%) below gate threshold, and conflicting expert analysis ('Big Edge on the Mound' for Braves). No bookmaker odds available to confirm. Edge appears to be NO but insufficient concrete evidence for confident BET_NO.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Kemp Alderman (RF): Day-To-Day
INJURY [miami marlins] Robby Snelling (SP): 15
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves Marlins'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins'})` → No related markets found for 'Atlanta Braves Miami Marlins'
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 game preview prediction'})` → [Mon, 18 May 2026] Google News
[Tue, 14 Apr 2026] Braves vs. Marlins: Prediction, Lineups, How to Wa
- `search_web({'query': 'Atlanta Braves injuries lineup today May 2025'})` → [Sat, 16 May 2026] Google News
[Tue, 12 May 2026] Latest Braves injuries &amp; transactions - MLB.co
- `search_web({'query': 'Braves Marlins odds May 2026'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] How to watch Braves vs. Marlins: TV channel and st
- `search_web({'query': 'Atlanta Braves recent performance record 2026'})` → [Mon, 18 May 2026] Google News
[Tue, 05 May 2026] How to watch Braves-Marlins MLB game for free toda
- `search_web({'query': 'Miami Marlins recent performance record 2026'})` → [Sat, 16 May 2026] Google News
[Mon, 18 May 2026] Pete Fairbanks records strikeout after ABS challen
- `search_web({'query': 'Braves vs Marlins odds May 19 2026 moneyline'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Atlanta Braves vs Miami Marlins Odds - Tuesday May
- `search_web({'query': 'Atlanta Braves starting pitcher May 19 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'Miami Marlins starting pitcher May 19 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'site:oddsshark.com Braves Marlins odds'})` → [Mon, 13 Apr 2026] Google News
[Wed, 15 Apr 2026] Miami Marlins vs Atlanta Braves Odds - Monday Apri
- `search_web({'query': 'MLB odds today May 19 2026 Braves moneyline prediction'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] MLB Picks Today: Greg Peterson Best Bets Tuesday, 
- `search_web({'query': 'Action Network Braves Marlins prediction odds May 19 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Braves vs Marlins Prediction, Pick, Odds: Big Edge
- `search_web({'query': 'Braves Marlins pitcher matchup analysis May 2026'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': '"Braves" "Marlins" "May 19" odds moneyline favorite'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] How to watch Braves vs. Marlins: TV channel and st
- `search_web({'query': 'MLB standings 2026 Braves Marlins records'})` → [Sun, 17 May 2026] Google News
[Thu, 14 May 2026] 2026 Cardinals Standings and Record: Regular Seaso
- `search_web({'query': 'Braves Marlins Action Network big edge mound starting pitcher May 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Braves vs Marlins Prediction, Pick, Odds: Big Edge
- `search_web({'query': 'Atlanta Braves 2026 season record wins losses'})` → [Tue, 05 May 2026] Google News
[Tue, 14 Apr 2026] 2026 MLB Standings and Records: Spring Training - 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*