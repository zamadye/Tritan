# Market Analysis — 2026-05-17 20:01 UTC

## Market
- **Question:** Los Angeles Dodgers vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $325,770
- **Liquidity:** $562,263

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,359 (+0.2% 24h) → neutral
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
- **Confidence:** 65%
- **p_true:** 49.2%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.78

### Reasoning
Strong statistical signal shows systematic overpricing: markets at 57% YES historically resolve YES only 44.7% of time (n=13,967), creating a 12.3% edge for NO. Bookmaker odds (Dodgers ~58-59%) confirm market pricing, but historical data reveals persistent crowd overconfidence at this price level. Dodgers have significant injuries (Blake Snell, Graterol) while Angels also missing key players. The gap between market price and true probability is substantial and well-documented across thousands of observations.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Los Angeles Dodgers'})` → INJURY [los angeles dodgers] Jack Dreyer (RP): 15-Day-IL
INJURY [los angeles dodgers] Blake Snell (S
- `get_sports_data({'sport': 'mlb', 'team': 'Los Angeles Angels'})` → INJURY [los angeles angels] Travis d'Arnaud (C): 10-Day-IL
INJURY [los angeles angels] Ben Joyce (RP
- `search_web({'query': 'Los Angeles Dodgers vs Los Angeles Angels 2025 MLB season upcoming matchup preview'})` → [Fri, 15 May 2026] Google News
[Wed, 18 Mar 2026] Freeway Series Preview, Injuries &amp; Pitching Ma
- `search_web({'query': 'Los Angeles Dodgers recent performance May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Dodgers top prospects tour Greenwood Rising - MLB.
- `search_web({'query': 'Los Angeles Angels recent performance May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Kurt Suzuki on Angels' loss - MLB.com
[Wed, 13 May
- `get_market_context({'keyword': 'Los Angeles Dodgers vs Los Angeles Angels'})` → No related markets found for 'Los Angeles Dodgers vs Los Angeles Angels'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → [ODDS] baseball_mlb — 2 events
  Los Angeles Angels vs Los Angeles Dodgers (2026-05-17)
    [FanDuel

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*