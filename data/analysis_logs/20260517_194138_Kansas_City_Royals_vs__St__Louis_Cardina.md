# Market Analysis — 2026-05-17 19:41 UTC

## Market
- **Question:** Kansas City Royals vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 76.0%
- **Days Left:** 6
- **Volume 24h:** $364,050
- **Liquidity:** $82,139

## Statistical Prior
- **p_base:** 84.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,193 (-0.1% 24h) → neutral
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
- **Confidence:** 45%
- **p_true:** 84.9%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Bookmaker odds (Royals at 1.25-1.29) imply ~77-80% probability, closely matching market price of 76%. While base rate shows 85%, this likely reflects historical favorites win rate that doesn't account for current matchup specifics. Both teams have moderate injuries (Royals: Cole Ragans SP on IL; Cardinals: Lars Nootbaar LF on 60-day IL). No breaking news or specific catalyst identified. Historical entry in 70-80% zone has only 57% win rate. Market appears efficiently priced - no verifiable edge exists.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Kansas City Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] Matt Strahm (RP)
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `search_web({'query': 'Kansas City Royals vs St. Louis Cardinals 2025 game preview'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Cardinals vs Royals Prediction, Odds, Moneyline, S
- `search_web({'query': 'Royals Cardinals upcoming series betting odds'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Kansas City Royals @ St. Louis Cardinals Odds - Fa
- `get_market_context({'keyword': 'Kansas City Royals vs St. Louis Cardinals'})` → No related markets found for 'Kansas City Royals vs St. Louis Cardinals'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Kansas City Royals'})` → [ODDS] baseball_mlb — 2 events
  St. Louis Cardinals vs Kansas City Royals (2026-05-17)
    [FanDuel
- `search_web({'query': 'Royals Cardinals May 2026 starting pitchers probable'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Royals vs. Cardinals (May 17, 2026) Live Score - E
- `search_web({'query': 'Kansas City Royals recent form last 10 games'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Royals vs Cardinals Picks, Odds and Best Bet, May 
- `search_web({'query': 'Kansas City Royals starting pitcher May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Royals vs. Cardinals (May 17, 2026) Live Score - E
- `search_web({'query': 'St. Louis Cardinals starting pitcher May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Royals vs. Cardinals (May 17, 2026) Live Score - E
- `search_web({'query': '"base rate" 85% n=6077 prediction market'})` → No search results for: "base rate" 85% n=6077 prediction market

## Outcome
**✅ WIN** | P&L: $+0.37 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*