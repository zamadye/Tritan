# Market Analysis — 2026-05-18 14:42 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 49.0%
- **Days Left:** 7
- **Volume 24h:** $126,029
- **Liquidity:** $310,221

## Statistical Prior
- **p_base:** 48.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,630 (-1.7% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,456 (-1.9% 24h) → risk-OFF
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
- → The Miami Marlins are in need of a momentum boost against the Atlanta Braves.
- [Mon, 18 May 2026] Marlins announce pitching probables for crucial series vs. Braves
- → Here is your TV guide for the upcoming NL East slate between the Atlanta Braves and the Miami Marlins ...

## LLM Decision
- **Action:** SKIP
- **Confidence:** 40%
- **p_true:** 48.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY
- **Catalyst Strength:** 0.10

### Reasoning
No verifiable edge. Gap is only -1% (market 49% vs base rate 48%), far below the 5% threshold required. Injury reports for key players (Acuna) likely already priced in. Past similar market skipped due to insufficient gap.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Eli White (CF): 7-Day IL
INJURY [atlanta braves] Ronald Acuna Jr. (RF): 10-D
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 15-Day-IL
INJURY [miami marlins] Ronny Henriquez (RP): 6
- `search_web({'query': 'Atlanta Braves vs Miami Marlins injury report'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Marlins vs. Braves: Injury Report, Updates &amp; P
- `search_web({'query': 'Braves vs Marlins odds prediction today'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Braves vs. Marlins Prediction, Odds &amp; Expert A
- `get_market_context({'keyword': 'Braves'})` → No related markets found for 'Braves'
- `get_market_context({'keyword': 'Marlins'})` → No related markets found for 'Marlins'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*