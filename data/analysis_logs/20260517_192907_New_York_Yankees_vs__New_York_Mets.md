# Market Analysis — 2026-05-17 19:29 UTC

## Market
- **Question:** New York Yankees vs. New York Mets
- **Category:** sports
- **YES Price:** 94.0%
- **Days Left:** 6
- **Volume 24h:** $1,006,532
- **Liquidity:** $34,702

## Statistical Prior
- **p_base:** 98.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,215 (+0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,206 (-0.0% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
- [SPORTS] Recent games:
- NYY @ NYM | In Progress | New York Mets(home) 19-26 score:1 vs New York Yankees(away) 28-18 score:5
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: york yankees york mets
- [Bing News]
- [Sun, 17 May 2026] york yankees york mets
- → Get ready for a classic Subway Series showdown on Sunday as the New York Yankees are in Flushing, Queens, to take on the New York Mets at Citi Field
- [Sun, 17 May 2026] Yankees vs Mets prediction for Sunday: Trade MLB action on Polymarket
- → Follow our live updates as the New York Mets take on the New York Yankees on Sunday at Citi Field.
- [Sun, 17 May 2026] NY Mets vs Yankees live updates, score and analysis of today's game
- → Here's how to watch Sunday's New York Mets vs New York Yankees game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 92.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** PRICE_DISCREPANCY
- **Catalyst Strength:** 0.65

### Reasoning
Market YES at 94% is mispriced vs bookmaker consensus (~96%) and base rate (98%). Both teams have significant injuries (Yankees: Cole, Fried, Stanton; Mets: Holmes, Alvarez, Polanco), but bookmakers still heavily favor Yankees at 1.04 odds (~96%). Francisco Alvarez surgery news suggests Mets injury situation may be worse. Gap of +4% below base rate indicates potential undervaluation. Pattern data shows 85% WR for sports trades and 100% WR when entering at 90-100% range, supporting this entry.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Yankees'})` → INJURY [new york yankees] Gerrit Cole (SP): 15-Day-IL
INJURY [new york yankees] Max Fried (SP): 15-D
- `get_sports_data({'sport': 'mlb', 'team': 'Mets'})` → INJURY [new york mets] Clay Holmes (SP): 15-Day-IL
INJURY [new york mets] Jorge Polanco (1B): 10-Day
- `get_odds({'sport': 'baseball_mlb', 'team': 'Yankees'})` → [ODDS] baseball_mlb — 2 events
  New York Mets vs New York Yankees (2026-05-17)
    [FanDuel] New Yo
- `search_web({'query': 'New York Yankees Mets 2026 May game prediction'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Yankees vs Mets Prediction, Picks &amp; Odds for T
- `search_web({'query': 'Yankees Mets May 17 2026 odds preview'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Yankees vs. Mets (May 17, 2026) Pregame - ESPN
[Su
- `search_web({'query': 'Yankees Mets injury update Cole Stanton May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Fantasy baseball: Gasser, Rodriguez called up for 
- `search_web({'query': 'Mets injury update Clay Holmes Francisco Alvarez May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Yankees vs. Mets (May 17, 2026) Pregame - ESPN
[Su
- `get_market_context({'keyword': 'Yankees Mets'})` → No related markets found for 'Yankees Mets'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*