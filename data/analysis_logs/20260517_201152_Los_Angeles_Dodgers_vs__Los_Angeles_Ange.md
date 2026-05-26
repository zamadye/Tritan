# Market Analysis — 2026-05-17 20:11 UTC

## Market
- **Question:** Los Angeles Dodgers vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 6
- **Volume 24h:** $349,487
- **Liquidity:** $522,109

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,313 (+0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,359 (+0.1% 24h) → neutral
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
- → The Los Angeles Dodgers, first in the NL West with a 28-18 record, face the Los Angeles Angels, who are fifth in the AL West with a 16-30 record. Th
- [Sun, 17 May 2026] Where to watch Los Angeles Dodgers vs. Los Angeles Angels: Live stream, TV channel, odds for Sunday, May 17
- → The Los Angeles Dodgers’ lineup, pitching matchups and how to watch Sunday's game against the Los Angeles Angels.
- [Sat, 16 May 2026] Dodgers lineup vs Angels: Mookie Betts and Will Smith out
- → Shohei Ohtani had five RBIs, Mookie Betts homered and the Los Angeles Dodgers pummeled the Los Angeles Angels 15-2 for their fourth straight win.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Market at 57% is close to bookmaker consensus (~61% implied) and below base rate (60%). Gap of only 3% fails the 5% gate threshold. Bookmakers favor Dodgers consistently across multiple shops. No new injury updates, lineup changes, or breaking news to create an edge. Prior evaluations correctly identified this as a SKIP — the thin gap offers no profitable entry point despite Dodgers being genuine favorites.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Los Angeles Dodgers'})` → INJURY [los angeles dodgers] Jack Dreyer (RP): 15-Day-IL
INJURY [los angeles dodgers] Blake Snell (S
- `get_sports_data({'sport': 'mlb', 'team': 'Los Angeles Angels'})` → INJURY [los angeles angels] Travis d'Arnaud (C): 10-Day-IL
INJURY [los angeles angels] Ben Joyce (RP
- `search_web({'query': 'Los Angeles Dodgers vs Los Angeles Angels game 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Los Angeles Dodgers at Los Angeles Angels Game Sto
- `search_web({'query': 'Dodgers Angels matchup news 2026'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Dodgers bring road win streak into matchup with th
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → [ODDS] baseball_mlb — 2 events
  Los Angeles Angels vs Los Angeles Dodgers (2026-05-17)
    [FanDuel
- `get_market_context({'keyword': 'Dodgers'})` → No related markets found for 'Dodgers'
- `get_market_context({'keyword': 'Los Angeles Angels'})` → No related markets found for 'Los Angeles Angels'
- `get_market_context({'keyword': 'MLB'})` → No related markets found for 'MLB'
- `get_sports_data({'sport': 'mlb', 'team': 'Angels'})` → INJURY [los angeles angels] Travis d'Arnaud (C): 10-Day-IL
INJURY [los angeles angels] Ben Joyce (RP
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Jack Dreyer (RP): 15-Day-IL
INJURY [los angeles dodgers] Blake Snell (S

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*