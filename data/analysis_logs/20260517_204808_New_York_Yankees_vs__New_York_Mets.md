# Market Analysis — 2026-05-17 20:48 UTC

## Market
- **Question:** New York Yankees vs. New York Mets
- **Category:** sports
- **YES Price:** 49.0%
- **Days Left:** 6
- **Volume 24h:** $1,086,730
- **Liquidity:** $15,132

## Statistical Prior
- **p_base:** 48.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,255 (+0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,252 (+0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
- [SPORTS] Recent games:
- NYY @ NYM | In Progress | New York Mets(home) 19-26 score:6 vs New York Yankees(away) 28-18 score:6
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)

### Bing/Google News
- 6 articles found:
- [NewsAPI] Mets say Clay Holmes' broken leg likely to heal in time for return late this sea: New York Mets pitcher Clay Holmes' broken leg should heal 
- [NewsAPI] North America’s largest commuter rail system shuts down as workers strike: The Long Island Rail Road, North America’s largest commuter rail 
- [NewsAPI] Sleeper Fantasy Promo Code NYPBONUS: Get free $20 + 100% deposit match up to $10: Secure up to $120 in DFS bonus value for Sabres vs. Canadi
- [NewsAPI] Underdog promo code NYPOST: Play $5, get $50 in fantasy bonus entries for Subway: Play $5, get $50 in bonus entries with the Underdog promo 
- [NewsAPI] Yankees vs. Mets prediction: Subway Series picks, odds, best bets Saturday: Carlos Rodon will be looking to bounce back after a rocky season
- [NewsAPI] NY Mets announce lineup vs NY Yankees for today's game: Here's a look at the New York Mets' lineup for Saturday's game vs. the New York Yank
- [CAUSAL CHAINS] Relevant cause-effect patterns:

### Multi-Source
- [MULTI-SOURCE NEWS] 3 sources for: york yankees york mets
- [Bing News]
- [Sun, 17 May 2026] york yankees york mets
- → Follow our live updates as the New York Mets take on the New York Yankees on Sunday at Citi Field.
- [Sun, 17 May 2026] NY Mets vs Yankees live updates, score and analysis of today's game
- → Here's how to watch Sunday's New York Mets vs New York Yankees game, including start times, TV channels, scores and how to stream.
- [Sun, 17 May 2026] Where to watch New York Yankees vs New York Mets: TV channel, start time, streaming for May 17
- → The Yankees and Mets meet for Game 3 of the 2026 Subway Series after splitting the first two at Citi Field. Elmer Rodriguez gets the nod for the vis

## LLM Decision
- **Action:** SKIP
- **Confidence:** 52%
- **p_true:** 48.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.15

### Reasoning
No verifiable edge exists. Market YES at 49% aligns almost perfectly with base rate of 48% (gap only -1%, well below 5% threshold). Bookmaker odds show Mets as heavy favorites (~83%) vs Yankees (~23%), suggesting this market may be asking a different question than simple game outcome. Critical pattern: Entry 40-50% markets have only 9% win rate historically (n=11), which is a strong negative signal. Both teams have significant injuries (Yankees: Cole, Fried, Stanton; Mets: Holmes, Polanco, Alvarez) balancing each other out. Prior similar decisions (SKIP at -1% gap, NO at +4% gap) correctly identified no edge. No breaking news or catalysts identified that would shift probabilities meaningfully. Confidence below 0.55 threshold for action.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Yankees'})` → INJURY [new york yankees] Gerrit Cole (SP): 15-Day-IL
INJURY [new york yankees] Max Fried (SP): 15-D
- `get_sports_data({'sport': 'mlb', 'team': 'Mets'})` → INJURY [new york mets] Clay Holmes (SP): 15-Day-IL
INJURY [new york mets] Jorge Polanco (1B): 10-Day
- `get_odds({'sport': 'baseball_mlb', 'team': 'Yankees'})` → [ODDS] baseball_mlb — 2 events
  New York Mets vs New York Yankees (2026-05-17)
    [FanDuel] New Yo
- `search_web({'query': 'New York Yankees vs New York Mets May 2026 prediction market Polymarket'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Polymarket referral code “CUSE” extends $50 MLB bo
- `search_web({'query': 'Yankees vs Mets today May 17 2026 odds prediction starting pitchers'})` → [2026-05-15] Yankees vs Mets Prediction: Odds, recent stats, trends, and best bets for May 15 — New 
- `get_market_context({'keyword': 'New York Yankees Mets'})` → No related markets found for 'New York Yankees Mets'
- `search_web({'query': 'New York Yankees vs New York Mets May 17 2026 starting pitchers game time'})` → [2026-05-15] Two-start pitchers: Jacob Misiorowski leads a plethora of terrific options as we pass t

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*