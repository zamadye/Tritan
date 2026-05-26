# Market Analysis — 2026-05-17 17:42 UTC

## Market
- **Question:** Los Angeles Dodgers vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $72,445
- **Liquidity:** $416,315

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,915 (-0.4% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,946 (-0.4% 24h) → neutral
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
- **Confidence:** 0%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Blake Snell (SP): 15-Day-IL
INJURY [los angeles dodgers] Brusdar Grater
- `get_sports_data({'sport': 'mlb', 'team': 'Angels'})` → INJURY [los angeles angels] Travis d'Arnaud (C): 10-Day-IL
INJURY [los angeles angels] Ben Joyce (RP
- `search_web({'query': 'Dodgers vs Angels 2025 starting pitchers'})` → [Sat, 16 May 2026] Google News
[Mon, 23 Mar 2026] Dodgers Notes: Blake Snell Elbow Injury, Unfortuna
- `search_web({'query': 'Dodgers Angels game injury update'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Fantasy baseball: Gasser, Rodriguez called up for 
- `search_web({'query': 'Dodgers vs Angels today May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Dodgers 15-2 Angels (May 16, 2026) Game Recap - ES
- `search_web({'query': 'Los Angeles Dodgers vs Los Angeles Angels game'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Where to watch Los Angeles Dodgers vs. Los Angeles
- `get_market_context({'keyword': 'Dodgers Angels'})` → No related markets found for 'Dodgers Angels'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → [ODDS] baseball_mlb — 1 events
  Los Angeles Angels vs Los Angeles Dodgers (2026-05-17)
    [FanDuel
- `search_web({'query': 'Dodgers vs Angels May 17 2026 probable pitchers starting lineup'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] MLB Gameday: Dodgers at Angels, Probable Pitchers,

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*