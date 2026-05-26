# Market Analysis — 2026-05-17 20:28 UTC

## Market
- **Question:** San Diego Padres vs. Seattle Mariners
- **Category:** sports
- **YES Price:** 42.0%
- **Days Left:** 7
- **Volume 24h:** $219,982
- **Liquidity:** $394,715

## Statistical Prior
- **p_base:** 38.1%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,258 (-0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,350 (+0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Denzel Clarke — 10-Day-IL (Bruise)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: diego padres seattle mariners
- [Bing News]
- [Sun, 17 May 2026] diego padres seattle mariners
- → The San Diego Padres, second in the NL West with a 27-18 record, face the Seattle Mariners, who are second in the AL West with a 22-25 record. The s
- [Sun, 17 May 2026] Where to watch San Diego Padres vs. Seattle Mariners: Live stream, TV channel, odds for Sunday, May 17
- → Randy Arozarena and Julio Rodriguez will be dialed in when they face Lucas Giolito and the Padres tonight. Free Padres vs. Mariners props for Sunday
- [Sun, 17 May 2026] Padres vs Mariners Prop Picks for Sunday Night Baseball
- → SportsLine's model simulated San Diego Padres vs. Seattle Mariners 10,000 times and revealed its MLB predictions and Sunday Night Baseball picks ...

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 38.1%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market price (42%) perfectly aligns with bookmaker consensus (Padres implied odds: 42.4% FanDuel, 41.8% BetOnline). No information edge exists. Gap of 4% falls below 5% threshold required for stat edge. Historical pattern shows 9% win rate for entries in 40-50% range (11 trades), which is severely underperforming. Both teams have comparable injury situations (Padres: Darvish + 2 SP on IL; Mariners: Raleigh + Brash on IL) with no asymmetric advantage. No breaking news or catalyst identified that would move this market away from efficient pricing.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'San Diego Padres'})` → INJURY [san diego padres] Matt Waldron (SP): 15-Day-IL
INJURY [san diego padres] German Marquez (SP)
- `get_sports_data({'sport': 'mlb', 'team': 'Seattle Mariners'})` → INJURY [seattle mariners] Brendan Donovan (3B): Day-To-Day
INJURY [seattle mariners] Cal Raleigh (C)
- `search_web({'query': 'San Diego Padres vs Seattle Mariners May 2025 preview'})` → [Tue, 14 Apr 2026] Google News
[Mon, 25 Aug 2025] Seattle Mariners at San Diego Padres Preview - 04/
- `search_web({'query': 'San Diego Padres recent form standings 2025 MLB'})` → [Tue, 05 May 2026] Google News
[Sun, 02 Nov 2025] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Seattle Mariners recent results April 2025 MLB'})` → [Mon, 30 Jun 2025] Google News
[Fri, 27 Jun 2025] Kansas City Royals at Seattle Mariners Game Story,
- `search_web({'query': 'Padres Mariners injury report starting pitchers'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Another Seattle Mariners pitching prospect is on a
- `get_odds({'sport': 'baseball_mlb', 'team': 'Padres'})` → [ODDS] baseball_mlb — 2 events
  Seattle Mariners vs San Diego Padres (2026-05-17)
    [FanDuel] San

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*