# Market Analysis — 2026-05-17 18:27 UTC

## Market
- **Question:** Los Angeles Dodgers vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $80,840
- **Liquidity:** $334,939

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,985 (-0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,099 (-0.0% 24h) → neutral
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
- → The Los Angeles Dodgers set their lineup for the final game of a three-game series against the Los Angeles Angels. The Dodgers ran rampant in the se
- [Sat, 16 May 2026] Dodgers Looking For Freeway Series Sweep: Lineup
- → Shohei Ohtani had five RBIs, Mookie Betts homered and the Los Angeles Dodgers pummeled the Los Angeles Angels 15-2 for their fourth straight win.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 32%
- **p_true:** 60.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.40

### Reasoning
Market overprices YES at 57% (historical resolution 44.7%), but gap (3%) is below 5% gate. Dodgers have pitching injuries but are on a hot streak. No concrete edge to bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Los Angeles Dodgers'})` → INJURY [los angeles dodgers] Blake Snell (SP): 15-Day-IL
INJURY [los angeles dodgers] Brusdar Grater
- `get_sports_data({'sport': 'mlb', 'team': 'Los Angeles Angels'})` → INJURY [los angeles angels] Travis d'Arnaud (C): 10-Day-IL
INJURY [los angeles angels] Ben Joyce (RP
- `get_odds({'sport': 'baseball_mlb', 'team': 'Los Angeles Dodgers'})` → [ODDS] baseball_mlb — 1 events
  Los Angeles Angels vs Los Angeles Dodgers (2026-05-17)
    [FanDuel
- `search_web({'query': 'Los Angeles Dodgers vs Los Angeles Angels May 2025 game preview'})` → [Sat, 16 May 2026] Google News
[Fri, 15 May 2026] Dodgers vs Angels Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'Dodgers Angels recent results 2026 MLB season'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Los Angeles Dodgers at Los Angeles Angels Game Sto
- `get_market_context({'keyword': 'Dodgers Angels'})` → No related markets found for 'Dodgers Angels'
- `search_web({'query': '"Los Angeles Dodgers" "Los Angeles Angels" "May 17" 2026 starting pitcher'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Fantasy baseball: Gasser, Rodriguez called up for 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*