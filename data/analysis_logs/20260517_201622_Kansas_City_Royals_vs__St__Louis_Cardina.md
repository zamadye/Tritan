# Market Analysis — 2026-05-17 20:16 UTC

## Market
- **Question:** Kansas City Royals vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 73.0%
- **Days Left:** 6
- **Volume 24h:** $374,569
- **Liquidity:** $36,204

## Statistical Prior
- **p_base:** 81.6%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.6%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,313 (+0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,367 (+0.1% 24h) → neutral
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
- → Here's how to watch Sunday's St. Louis Cardinals vs Kansas City Royals game, including start times, TV channels, scores and how to stream.
- [Sun, 17 May 2026] Where to watch Kansas City Royals vs St. Louis Cardinals: TV channel, start time, streaming for May 17
- → The Cardinals will try to sweep the Royals on Sunday as Andre Pallante will get the start for St. Louis. Kansas City will send Stephen Kolek to the 
- [Sun, 17 May 2026] Game Discussion for St. Louis Cardinals vs Kansas City Royals Sunday
- → Royals -104; over/under is 9 runs. BOTTOM LINE: The Kansas City Royals will try to stop a five-game road losing streak when they visit the St. Louis

## LLM Decision
- **Action:** YES
- **Confidence:** 65%
- **p_true:** 92.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** BOOKMAKER_MARKET_DIVERGENCE
- **Catalyst Strength:** 0.82

### Reasoning
Bookmaker odds (Royals 1.10-1.13, implying 89-91% probability) significantly exceed the market YES price of 73%, creating a ~17% edge. Despite Cole Ragans being on the IL, bookmakers maintain strong Royals favoritism, suggesting the prediction market is overreacting to the injury news. Previous SKIP decisions were when odds matched market (77-80% vs 76%), but now a substantial gap has opened.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET YES $1.00

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Kansas City Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] Matt Strahm (RP)
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Royals'})` → [ODDS] baseball_mlb — 2 events
  St. Louis Cardinals vs Kansas City Royals (2026-05-17)
    [FanDuel
- `get_market_context({'keyword': 'Kansas City Royals Cardinals'})` → No related markets found for 'Kansas City Royals Cardinals'
- `search_web({'query': 'Kansas City Royals vs St. Louis Cardinals 2026 May series'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] How to watch Royals vs. Cardinals: TV channel and 
- `search_web({'query': 'Cole Ragans injury Kansas City Royals status'})` → [Fri, 08 May 2026] Google News
[Fri, 08 May 2026] Ragans to IL with 'pitcher's elbow'; Estévez diagn

## Outcome
**✅ WIN** | P&L: $+0.37 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*