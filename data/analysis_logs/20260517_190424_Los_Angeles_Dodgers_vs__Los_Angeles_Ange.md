# Market Analysis — 2026-05-17 19:04 UTC

## Market
- **Question:** Los Angeles Dodgers vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $83,191
- **Liquidity:** $417,695

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,197 (-0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,124 (-0.2% 24h) → neutral
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
- [MULTI-SOURCE NEWS] 2 sources for: angeles dodgers angeles angels
- [Bing News]
- [Sun, 17 May 2026] angeles dodgers angeles angels
- → The Los Angeles Dodgers’ lineup, pitching matchups and how to watch Sunday's game against the Los Angeles Angels.
- [Sun, 17 May 2026] Dodgers lineup vs Angels: Mookie Betts and Will Smith out
- → The Los Angeles Angels activated Grayson Rodriguez from the injured list in advance of the right-hander's debut with the club in a home start agains
- [Sun, 17 May 2026] Angels activate RHP Grayson Rodriguez to face Dodgers
- → The Los Angeles Dodgers moved left-handed reliever Jack Dreyer to the injured list with left-shoulder discomfort.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 60%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_REPORT
- **Catalyst Strength:** 0.30

### Reasoning
Bookmaker odds imply Dodgers win probability ~59%, slightly above market price of 57%. However, gap is less than 5% threshold required for bet. Historical stat signal suggests overpricing YES at 57%, but specific game evidence does not show clear edge. No breaking news or direct catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Los Angeles Dodgers'})` → INJURY [los angeles dodgers] Jack Dreyer (RP): 15-Day-IL
INJURY [los angeles dodgers] Blake Snell (S
- `get_sports_data({'sport': 'mlb', 'team': 'Los Angeles Angels'})` → INJURY [los angeles angels] Travis d'Arnaud (C): 10-Day-IL
INJURY [los angeles angels] Ben Joyce (RP
- `search_web({'query': 'Los Angeles Dodgers recent news 2025'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Shohei Ohtani And Dodgers Square Off Against Angel
- `search_web({'query': 'Los Angeles Angels recent news 2025'})` → [Fri, 24 Oct 2025] Google News
[Tue, 02 Dec 2025] Angels News: 2 players from 2025 team elect free a
- `get_market_context({'keyword': 'Dodgers Angels'})` → No related markets found for 'Dodgers Angels'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Los Angeles Dodgers'})` → [ODDS] baseball_mlb — 1 events
  Los Angeles Angels vs Los Angeles Dodgers (2026-05-17)
    [FanDuel

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*