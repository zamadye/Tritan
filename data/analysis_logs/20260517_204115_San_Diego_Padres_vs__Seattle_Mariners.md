# Market Analysis — 2026-05-17 20:41 UTC

## Market
- **Question:** San Diego Padres vs. Seattle Mariners
- **Category:** sports
- **YES Price:** 41.0%
- **Days Left:** 7
- **Volume 24h:** $221,891
- **Liquidity:** $421,314

## Statistical Prior
- **p_base:** 36.7%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,297 (+0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,242 (+0.0% 24h) → neutral
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
- → SportsLine's model simulated San Diego Padres vs. Seattle Mariners 10,000 times and revealed its MLB predictions and Sunday Night Baseball picks ...
- [Sun, 17 May 2026] Padres vs. Mariners prediction, odds, time: 2026 MLB picks for Sunday Night Baseball from advanced model
- → The San Diego Padres, second in the NL West with a 27-18 record, face the Seattle Mariners, who are second in the AL West with a 22-25 record. The s
- [Sun, 17 May 2026] Where to watch San Diego Padres vs. Seattle Mariners: Live stream, TV channel, odds for Sunday, May 17
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
Market price (41%) aligns with bookmaker consensus (Padres implied odds: 42.4% FanDuel, 41.8% BetOnline). Gap (4%) below 5% gate threshold. Entry 40-50% price range has historically poor win rate (9% from 11 trades). No new information or catalysts identified. Previous decisions for this exact market also SKIP.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] Matt Waldron (SP): 15-Day-IL
INJURY [san diego padres] German Marquez (SP)
- `get_odds({'sport': 'baseball_mlb', 'team': 'Padres'})` → [ODDS] baseball_mlb — 2 events
  Seattle Mariners vs San Diego Padres (2026-05-17)
    [FanDuel] San
- `search_web({'query': 'San Diego Padres vs Seattle Mariners May 2026 preview'})` → [2026-05-15] How to watch the San Diego Padres vs Seattle Mariners: Live stream info, schedule, prev
- `search_web({'query': 'Padres Mariners pitching matchup injuries'})` → [2026-05-15] Two-start pitchers: Jacob Misiorowski leads a plethora of terrific options as we pass t
- `get_market_context({'keyword': 'Padres Mariners'})` → No related markets found for 'Padres Mariners'
- `search_web({'query': 'Seattle Mariners recent form last 10 games May 2026'})` → [2026-05-15] Fantasy Baseball Waiver Wire: JJ Bleday continues to rake, A.J. Ewing makes good first 
- `search_web({'query': 'Padres Mariners starting pitchers May 16 2026'})` → [2026-05-15] Two-start pitchers: Jacob Misiorowski leads a plethora of terrific options as we pass t
- `search_web({'query': 'Seattle Mariners injuries roster May 2026'})` → [2026-05-16] Detroit Tigers make progress on defense in win over Blue Jays — On Friday against Toron
- `get_sports_data({'sport': 'mlb', 'team': 'Mariners'})` → INJURY [seattle mariners] Brendan Donovan (3B): Day-To-Day
INJURY [seattle mariners] Cal Raleigh (C)

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*