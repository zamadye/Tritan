# Market Analysis — 2026-05-17 18:24 UTC

## Market
- **Question:** Kansas City Royals vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 6
- **Volume 24h:** $273,990
- **Liquidity:** $11,527

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,985 (-0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,985 (-0.2% 24h) → neutral
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
- [MULTI-SOURCE NEWS] 2 sources for: kansas city royals louis cardinals
- [Bing News]
- [Sun, 17 May 2026] kansas city royals louis cardinals
- → The Cardinals will try to sweep the Royals on Sunday as Andre Pallante will get the start for St. Louis. Kansas City will send Stephen Kolek to the 
- [Sun, 17 May 2026] Game Discussion for St. Louis Cardinals vs Kansas City Royals Sunday
- → Here's how to watch Sunday's St. Louis Cardinals vs Kansas City Royals game, including start times, TV channels, scores and how to stream.
- [Sun, 17 May 2026] Where to watch Kansas City Royals vs St. Louis Cardinals: TV channel, start time, streaming for May 17
- → View the latest in Kansas City Royals, MLB team news here. Trending news, game recaps, highlights, player information, rumors, videos and more from 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 47.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_REPORT
- **Catalyst Strength:** 0.60

### Reasoning
Historical data shows markets at 51% YES price resolve YES only 44.7% of the time, indicating systematic overpricing of YES. Injury reports indicate key Royals pitchers are on the IL, weakening their chances. Bookmaker odds imply ~52% win probability for Royals, but the statistical edge favors NO bet at current price.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] Matt Strahm (RP)
- `get_sports_data({'sport': 'mlb', 'team': 'Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Royals'})` → [ODDS] baseball_mlb — 2 events
  St. Louis Cardinals vs Kansas City Royals (2026-05-17)
    [FanDuel
- `search_web({'query': 'Kansas City Royals vs St. Louis Cardinals game 2026'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Kansas City Royals at St. Louis Cardinals Game Sto
- `search_web({'query': 'Royals Cardinals prediction'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Royals vs. Cardinals Prediction, MLB Picks for Sat
- `get_market_context({'keyword': 'Royals'})` → [YES=50% vol=$2,230,232] Indian Premier League: Delhi Capitals vs Rajasthan Royals
- `get_market_context({'keyword': 'Cardinals'})` → No related markets found for 'Cardinals'

## Outcome
**✅ WIN** | P&L: $+0.37 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*