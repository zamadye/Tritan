# Market Analysis — 2026-05-17 19:31 UTC

## Market
- **Question:** Kansas City Royals vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 73.0%
- **Days Left:** 6
- **Volume 24h:** $351,556
- **Liquidity:** $29,240

## Statistical Prior
- **p_base:** 81.6%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.6%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,215 (+0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,201 (-0.0% 24h) → neutral
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
- **Confidence:** 0%
- **p_true:** 81.6%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 0%<52%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Kansas City Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] Matt Strahm (RP)
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Royals'})` → [ODDS] baseball_mlb — 2 events
  St. Louis Cardinals vs Kansas City Royals (2026-05-17)
    [FanDuel
- `get_market_context({'keyword': 'Kansas City Royals'})` → No related markets found for 'Kansas City Royals'
- `get_market_context({'keyword': 'Cardinals'})` → No related markets found for 'Cardinals'
- `search_web({'query': 'Kansas City Royals vs St. Louis Cardinals May 2025 preview prediction'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Royals vs Cardinals Prediction, Odds &amp; Player 
- `search_web({'query': 'Royals Cardinals series 2025 odds analysis pitching matchup'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Royals vs. Cardinals Prediction, Odds &amp; Analys
- `search_web({'query': 'Kansas City Royals record standings 2026 MLB season'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'St. Louis Cardinals record standings 2026 MLB season'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Royals Cardinals May 17 2026 starting pitcher who is pitching'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Royals vs. Cardinals (May 17, 2026) Live Score - E

## Outcome
**✅ WIN** | P&L: $+0.37 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*