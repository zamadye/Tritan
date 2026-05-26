# Market Analysis — 2026-05-17 21:36 UTC

## Market
- **Question:** San Diego Padres vs. Seattle Mariners
- **Category:** sports
- **YES Price:** 41.0%
- **Days Left:** 7
- **Volume 24h:** $233,156
- **Liquidity:** $528,846

## Statistical Prior
- **p_base:** 36.7%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,387 (+0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,232 (+0.0% 24h) → neutral
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
- → SportsLine's model simulated San Diego Padres vs. Seattle Mariners 10,000 times and revealed its MLB predictions and Sunday Night Baseball picks ...
- [Sun, 17 May 2026] Padres vs. Mariners prediction, odds, time: 2026 MLB picks for Sunday Night Baseball from advanced model
- → SportsLine expert Angelo &quot;Amags&quot; Magliocca has dug up some value bets for a same-game parlay for Padres vs. Mariners on the May 17 edition

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 36.7%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Market price (41%) matches bookmaker consensus (~41.4%) with no verifiable edge. Injury information for both teams (Padres: Darvish/Waldron/Marquez; Mariners: Raleigh/Donovan/Brash) appears fully priced in by bookmakers. Gap of -4% fails the 5% gate requirement. Historical data shows 40-50% entry range has only 9% win rate (11 trades). Two prior SKIP decisions on identical market confirm no edge exists.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] Matt Waldron (SP): 15-Day-IL
INJURY [san diego padres] German Marquez (SP)
- `get_sports_data({'sport': 'mlb', 'team': 'Mariners'})` → INJURY [seattle mariners] Brendan Donovan (3B): 10-Day-IL
INJURY [seattle mariners] Cal Raleigh (C):
- `get_odds({'sport': 'baseball_mlb', 'team': 'Padres'})` → [ODDS] baseball_mlb — 2 events
  Seattle Mariners vs San Diego Padres (2026-05-17)
    [FanDuel] San
- `get_odds({'sport': 'baseball_mlb', 'team': 'Mariners'})` → [ODDS] baseball_mlb — 2 events
  Seattle Mariners vs San Diego Padres (2026-05-17)
    [FanDuel] San
- `search_web({'query': 'San Diego Padres injury update May 2026 Yu Darvish'})` → [Fri, 15 May 2026] Google News
[Wed, 13 May 2026] Latest Padres injuries and transactions - MLB.com

- `search_web({'query': 'Seattle Mariners Cal Raleigh injury update May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Mariners Must Be Careful Not To Turn Cal Raleigh’s
- `search_web({'query': 'Padres vs Mariners May 17 2026 starting pitchers preview'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Padres vs. Mariners Prediction Odds, Probable Pitc
- `get_market_context({'keyword': 'Padres'})` → No related markets found for 'Padres'
- `get_market_context({'keyword': 'Mariners'})` → No related markets found for 'Mariners'
- `search_web({'query': '"Padres" "Mariners" "May 17" "starting pitcher" 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Good Morning San Diego: Padres hit pair of homers 
- `search_web({'query': '"Padres" "Mariners" "May 17 2026" recap'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Seattle Mariners vs. San Diego Padres - May 17, 20
- `search_web({'query': 'Padres Mariners May 17 2026 score live game today'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Padres vs. Mariners (May 17, 2026) Live Score - ES

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*