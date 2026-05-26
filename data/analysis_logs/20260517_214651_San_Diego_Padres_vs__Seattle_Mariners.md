# Market Analysis — 2026-05-17 21:46 UTC

## Market
- **Question:** San Diego Padres vs. Seattle Mariners
- **Category:** sports
- **YES Price:** 41.0%
- **Days Left:** 7
- **Volume 24h:** $233,239
- **Liquidity:** $529,107

## Statistical Prior
- **p_base:** 36.7%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,379 (+0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,386 (+0.2% 24h) → neutral
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
- → Sunday Night Baseball features an interesting matchup between two playoff hopefuls, as the Seattle Mariners host the San Diego Padres.&#160; San Die
- [Sun, 17 May 2026] Padres vs. Mariners Prediction Odds, Probable Pitchers, Prop Bets for Sunday, May 17
- → SportsLine's model simulated San Diego Padres vs. Seattle Mariners 10,000 times and revealed its MLB predictions and Sunday Night Baseball picks ...
- [Sun, 17 May 2026] Padres vs. Mariners prediction, odds, time: 2026 MLB picks for Sunday Night Baseball from advanced model
- → The San Diego Padres, second in the NL West with a 27-18 record, face the Seattle Mariners, who are second in the AL West with a 22-25 record. The s

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 36.7%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Market price (41%) aligns with bookmaker consensus (~42-43%) with no meaningful edge. Both teams have significant injuries already priced in. Pattern data shows 9% win rate for entries in 40-50% range - strong warning signal. Previous SKIP decisions for this exact market were correct. No new information or catalyst to create edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'San Diego Padres'})` → INJURY [san diego padres] Matt Waldron (SP): 15-Day-IL
INJURY [san diego padres] German Marquez (SP)
- `get_sports_data({'sport': 'mlb', 'team': 'Seattle Mariners'})` → INJURY [seattle mariners] Brendan Donovan (3B): 10-Day-IL
INJURY [seattle mariners] Cal Raleigh (C):
- `get_market_context({'keyword': 'Padres Mariners'})` → No related markets found for 'Padres Mariners'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Padres'})` → [ODDS] baseball_mlb — 2 events
  Seattle Mariners vs San Diego Padres (2026-05-17)
    [FanDuel] San
- `search_web({'query': 'San Diego Padres vs Seattle Mariners 2025 game preview odds'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] San Diego Padres at Seattle Mariners odds, picks a
- `search_web({'query': 'Padres Mariners injury report today'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Mariners vs. Padres: Injury Report, Updates &amp; 
- `search_web({'query': 'Padres Mariners May 2026 series starting pitchers'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Where to watch San Diego Padres vs. Seattle Marine
- `search_web({'query': 'Yu Darvish injury update Padres'})` → [Fri, 15 May 2026] Google News
[Wed, 25 Mar 2026] Latest Padres injuries and transactions - MLB.com

- `get_market_context({'keyword': 'MLB Padres win'})` → No related markets found for 'MLB Padres win'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*