# Market Analysis — 2026-05-17 19:13 UTC

## Market
- **Question:** Kansas City Royals vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $345,992
- **Liquidity:** $8,354

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,229 (+0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,197 (-0.0% 24h) → neutral
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
- → Royals -104; over/under is 9 runs. BOTTOM LINE: The Kansas City Royals will try to stop a five-game road losing streak when they visit the St. Louis
- [Sun, 17 May 2026] Royals aim to stop road slide, take on the Cardinals
- → Here's how to watch Sunday's St. Louis Cardinals vs Kansas City Royals game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 59.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] Matt Strahm (RP)
- `get_sports_data({'sport': 'mlb', 'team': 'Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `search_web({'query': 'Kansas City Royals vs St. Louis Cardinals 2025 matchup preview'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Where to watch Kansas City Royals vs St. Louis Car
- `search_web({'query': 'Royals Cardinals game today odds prediction'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Royals vs Cardinals Prediction, Odds &amp; Player 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Royals'})` → [ODDS] baseball_mlb — 2 events
  St. Louis Cardinals vs Kansas City Royals (2026-05-17)
    [FanDuel
- `get_market_context({'keyword': 'Royals Cardinals'})` → No related markets found for 'Royals Cardinals'
- `search_web({'query': 'Kansas City Royals St. Louis Cardinals 2025 schedule upcoming games'})` → [Sat, 16 May 2026] Google News
[Tue, 03 Jun 2025] Cardinals vs. Royals rain delay: Details, updates 
- `search_web({'query': 'Royals Cardinals starting pitchers today 2025'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Cardinals vs Royals Prediction, Odds, Moneyline, S
- `search_web({'query': '"Kansas City Royals" "St. Louis Cardinals" 2025 schedule series'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Cardinals vs. Royals rain delay: Details, updates 

## Outcome
**✅ WIN** | P&L: $+0.37 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*