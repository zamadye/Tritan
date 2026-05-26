# Market Analysis — 2026-05-18 11:03 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 7
- **Volume 24h:** $53,353
- **Liquidity:** $198,826

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,783 (-2.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,766 (-2.1% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Recent games:
- MIA @ TB | Final | Tampa Bay Rays(home) 30-15 score:6 vs Miami Marlins(away) 21-26 score:3
- BOS @ ATL | Final | Atlanta Braves(home) 32-15 score:8 vs Boston Red Sox(away) 19-27 score:1
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Mon, 18 May 2026] atlanta braves miami marlins
- → Here's how to watch Monday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.
- [Mon, 18 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 18
- → The Atlanta Braves and Miami Marlins play Monday at 6:40 p.m. ET in the first game of their 3-game series at loanDepot park in Miami, Florida.
- [Mon, 18 May 2026] Atlanta Braves at Miami Marlins odds, picks and predictions
- → Here is your TV guide for the upcoming NL East slate between the Atlanta Braves and the Miami Marlins ...

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 51.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** HISTORICAL_STATISTICAL_PATTERN
- **Catalyst Strength:** 0.40

### Reasoning
Stat signal indicates YES is overpriced (51% vs historical 44.7% resolution), suggesting a 6.3% edge for NO. However, the gap between YES price and base rate is only +1% (below the 5% gate threshold), and historical performance for trades in the 50-60% range is poor (25% WR). Injuries are known and likely priced in, with no direct catalyst to shift the line. Macro risk-off sentiment is unlikely to affect a single MLB game.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Eli White (CF): 7-Day IL
INJURY [atlanta braves] Ronald Acuna Jr. (RF): 10-D
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 15-Day-IL
INJURY [miami marlins] Ronny Henriquez (RP): 6
- `search_web({'query': 'Atlanta Braves vs Miami Marlins prediction 2025'})` → [Mon, 25 Aug 2025] Google News
[Mon, 13 Apr 2026] Braves vs. Marlins Prediction, Odds, Picks - Augus
- `search_web({'query': 'Braves Marlins game August 2025'})` → [Sat, 09 Aug 2025] Google News
[Wed, 27 Aug 2025] Miami Marlins at Atlanta Braves Game Story, Scores
- `search_web({'query': 'Atlanta Braves schedule September 2025'})` → [Thu, 02 Apr 2026] Google News
[Wed, 24 Sep 2025] How to Watch the Braves | Atlanta Braves - MLB.com
- `get_market_context({'keyword': 'Braves Marlins'})` → No related markets found for 'Braves Marlins'
- `search_web({'query': 'Miami Marlins vs Atlanta Braves September 1 2025 odds'})` → [Mon, 01 Sep 2025] Google News
[Mon, 01 Sep 2025] Braves at Cubs odds, picks and predictions - Sport
- `search_web({'query': 'Atlanta Braves vs Miami Marlins Polymarket'})` → [Mon, 18 May 2026] Google News
[Wed, 13 May 2026] Atlanta Braves vs Miami Marlins Odds - Monday May 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*