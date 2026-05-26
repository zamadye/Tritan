# Market Analysis — 2026-05-17 19:17 UTC

## Market
- **Question:** Los Angeles Dodgers vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $85,038
- **Liquidity:** $417,833

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,229 (+0.0% 24h) → neutral
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
- → A bizarre netting bounce helped Shohei Ohtani score a Little League HR as the Dodgers routed the Angels 15-2 to claim the Freeway Series.
- [Sun, 17 May 2026] Dodgers’ Shohei Ohtani adds Little League home run to already insane resume
- → The Los Angeles Angels activated Grayson Rodriguez from the injured list in advance of the right-hander's debut with the club in a home start agains

## LLM Decision
- **Action:** SKIP
- **Confidence:** 60%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_CONTEXT
- **Catalyst Strength:** 0.40

### Reasoning
Market at 57% vs bookmaker consensus 58-59% (Dodgers). Stat signal suggests YES overpriced (44.7% historical resolution), but bookmaker odds actually imply Dodgers HIGHER than market price. Small gap (3%) below 5% threshold. Dodgers have key players out (Betts, Smith, Snell IL) but this is already likely priced in. Previous 2 decisions on same market were SKIP due to insufficient edge. No independent catalyst to break the stalemate.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Jack Dreyer (RP): 15-Day-IL
INJURY [los angeles dodgers] Blake Snell (S
- `get_sports_data({'sport': 'mlb', 'team': 'Angels'})` → INJURY [los angeles angels] Travis d'Arnaud (C): 10-Day-IL
INJURY [los angeles angels] Ben Joyce (RP
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → [ODDS] baseball_mlb — 1 events
  Los Angeles Angels vs Los Angeles Dodgers (2026-05-17)
    [FanDuel
- `search_web({'query': 'Los Angeles Dodgers vs Angels May 2025 series pitching matchup'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Dodgers Lineup vs Angels: Mookie Betts and Will Sm
- `search_web({'query': 'Los Angeles Dodgers recent performance May 2025'})` → [Sat, 18 Oct 2025] Google News
[Sun, 27 Jul 2025] Greatest game ever? Dodgers' Shohei Ohtani can't s
- `get_market_context({'keyword': 'Dodgers Angels baseball'})` → No related markets found for 'Dodgers Angels baseball'
- `search_web({'query': '"Dodgers" "Angels" probable pitcher May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] MLB Gameday: Dodgers at Angels, Probable Pitchers,
- `search_web({'query': 'Angels Dodgers May 17 2026 starting pitcher prediction preview'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Los Angeles Angels vs. Los Angeles Dodgers predict
- `get_market_context({'keyword': 'Dodgers Angels MLB'})` → No related markets found for 'Dodgers Angels MLB'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*