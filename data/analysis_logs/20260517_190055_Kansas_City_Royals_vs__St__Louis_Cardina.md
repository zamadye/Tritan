# Market Analysis — 2026-05-17 19:00 UTC

## Market
- **Question:** Kansas City Royals vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $345,576
- **Liquidity:** $68,776

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,197 (-0.0% 24h) → neutral
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
- **Confidence:** 65%
- **p_true:** 48.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical mispricing: markets at 56% YES price historically resolve YES only 44.7% of the time (n=13,967), creating an 11.3% edge for NO. The market is overpricing YES by ~11%. Injury data is neutral (both teams have significant IL absences). Past similar markets skipped due to narrow gap (+3%), but the conditional resolution data reveals a much stronger edge. SPORTS pattern shows 85% WR historically.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] Matt Strahm (RP)
- `get_sports_data({'sport': 'mlb', 'team': 'Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `search_web({'query': 'Kansas City Royals vs St. Louis Cardinals 2025 game'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Where to watch Kansas City Royals vs St. Louis Car
- `search_web({'query': 'Royals Cardinals series 2025 results'})` → [Thu, 05 Jun 2025] Google News
[Sat, 01 Nov 2025] Kansas City Royals at St. Louis Cardinals Game Sto
- `get_market_context({'keyword': 'Royals Cardinals'})` → No related markets found for 'Royals Cardinals'
- `get_market_context({'keyword': 'Kansas City Royals'})` → No related markets found for 'Kansas City Royals'
- `get_market_context({'keyword': 'St. Louis Cardinals'})` → No related markets found for 'St. Louis Cardinals'

## Outcome
**✅ WIN** | P&L: $+0.37 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*