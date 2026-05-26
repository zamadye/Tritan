# Market Analysis — 2026-05-17 20:22 UTC

## Market
- **Question:** Los Angeles Dodgers vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $365,804
- **Liquidity:** $19,312

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,258 (-0.0% 24h) → neutral
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
- [Sat, 16 May 2026] Los Angeles Dodgers vs. Los Angeles Angels: Live stream, TV channel, odds for Sunday, May 17
- → Shohei Ohtani had five RBIs, Mookie Betts homered and the Los Angeles Dodgers pummeled the Los Angeles Angels 15-2 for their fourth straight win.
- [Sun, 17 May 2026] Shohei Ohtani has 5 RBIs and Dodgers take advantage of Angels’ mistakes in 15-2 rout
- → Los Angeles Dodgers designated hitter Shohei Ohtani (17) gets high fives after scoring a run during the MLB game between the Los Angeles Dodgers ver

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 51.7%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** SYSTEMATIC_MARKET_OVERPRICING
- **Catalyst Strength:** 0.68

### Reasoning
Strong stat signal: markets at 56% historically resolve YES only 44.7% (n=13,967), creating ~11% edge on NO. Blake Snell (SP) on IL weakens Dodgers. Ohtani narrative may be inflating YES pricing. Entry at 50-60% range shows 86% WR historically. Confidence tempered by narrative uncertainty.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Jack Dreyer (RP): 15-Day-IL
INJURY [los angeles dodgers] Blake Snell (S
- `get_sports_data({'sport': 'mlb', 'team': 'Angels'})` → INJURY [los angeles angels] Travis d'Arnaud (C): 10-Day-IL
INJURY [los angeles angels] Ben Joyce (RP
- `search_web({'query': 'Los Angeles Dodgers vs Los Angeles Angels prediction June 2025'})` → [Wed, 13 Aug 2025] Google News
[Tue, 12 Aug 2025] How to Watch Dodgers vs. Angels: TV Channel &amp; 
- `search_web({'query': 'Dodgers Angels game preview injury update'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Angels vs. Dodgers: Injury Report, Updates &amp; P
- `search_web({'query': 'Dodgers vs Angels August 2025 odds pitcher'})` → [Wed, 13 Aug 2025] Google News
[Wed, 13 Aug 2025] Dodgers vs. Angels Prediction, Odds, Picks - Augus
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → [ODDS] baseball_mlb — 2 events
  Los Angeles Angels vs Los Angeles Dodgers (2026-05-17)
    [FanDuel
- `get_odds({'sport': 'baseball_mlb', 'team': 'Angels'})` → [ODDS] baseball_mlb — 2 events
  Los Angeles Angels vs Los Angeles Dodgers (2026-05-17)
    [FanDuel
- `get_market_context({'keyword': 'Dodgers Angels'})` → No related markets found for 'Dodgers Angels'
- `search_web({'query': '"Dodgers" "Angels" August 13 2025 prediction odds'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Dodgers vs Angels Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'Shohei Ohtani Dodgers Angels August 2025'})` → [Mon, 11 Aug 2025] Google News
[Wed, 13 Aug 2025] Shohei Ohtani's first HR back at Angel Stadium (42

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*