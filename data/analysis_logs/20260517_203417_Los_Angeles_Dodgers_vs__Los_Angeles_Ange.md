# Market Analysis — 2026-05-17 20:34 UTC

## Market
- **Question:** Los Angeles Dodgers vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 6
- **Volume 24h:** $393,128
- **Liquidity:** $3,873

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,297 (+0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,297 (+0.1% 24h) → neutral
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
- [Sun, 17 May 2026] Los Angeles Dodgers vs. Los Angeles Angels: Live stream, TV channel, odds for Sunday, May 17
- → The Los Angeles Dodgers removed Mookie Betts from the lineup.
- [Sat, 16 May 2026] Mookie Betts status update: Dodgers remove shortstop from lineup before Angels game
- → Shohei Ohtani had five RBIs, Mookie Betts homered and the Los Angeles Dodgers pummeled the Los Angeles Angels 15-2 for their fourth straight win.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 51.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STAT_SIGNAL_INJURY
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 58% resolve YES only 44.7% of time - market overprices YES by ~13pp. Combined with Dodgers missing key SP Blake Snell on IL, creating a significant edge for NO bet at 42% price.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Jack Dreyer (RP): 15-Day-IL
INJURY [los angeles dodgers] Blake Snell (S
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers Angels'})` → [ODDS] baseball_mlb — 0 events
- `get_market_context({'keyword': 'Dodgers Angels'})` → No related markets found for 'Dodgers Angels'
- `search_web({'query': 'Los Angeles Dodgers vs Angels MLB series May 2025'})` → [Wed, 18 Mar 2026] Google News
[Thu, 26 Mar 2026] LA Dodgers vs. LA Angels: Upcoming Freeway Series 
- `search_web({'query': 'Dodgers Angels injury report roster update May 2025'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Angels vs. Dodgers: Injury Report, Updates &amp; P
- `get_sports_data({'team': 'Angels', 'sport': 'mlb'})` → INJURY [los angeles angels] Travis d'Arnaud (C): 10-Day-IL
INJURY [los angeles angels] Ben Joyce (RP
- `search_web({'query': 'Los Angeles Angels recent results form May 2025'})` → [Sun, 17 May 2026] Google News
[Sat, 17 May 2025] Where to watch Los Angeles Dodgers vs Los Angeles 
- `search_web({'query': 'Los Angeles Dodgers vs Los Angeles Angels May 17 2025 score result'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Where to watch Los Angeles Dodgers vs Los Angeles 
- `search_web({'query': 'Dodgers Angels starting pitcher May 2025'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Dodgers vs Angels Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'Los Angeles Dodgers winning percentage 2025 season'})` → [Fri, 15 May 2026] Google News
[Mon, 20 Oct 2025] 2026 MLB Standings and Records: Regular Season - M

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*