# Market Analysis — 2026-05-18 12:24 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 7
- **Volume 24h:** $60,599
- **Liquidity:** $256,825

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,405 (-1.3% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,311 (-1.4% 24h) → risk-OFF
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
- → The Atlanta Braves and Miami Marlins play Monday at 6:40 p.m. ET in the first game of their 3-game series at loanDepot park in Miami, Florida.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 60%
- **p_true:** 51.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** INJURY
- **Catalyst Strength:** 0.60

### Reasoning
Stat signal suggests YES overpriced (51% vs 44.7% historical resolution), but gap vs base rate only 1% fails 5% gate. Entry 50-60% pattern shows poor 25% win rate. Acuna injury hurts Braves but may be partially priced in. Insufficient edge for confident bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Eli White (CF): 7-Day IL
INJURY [atlanta braves] Ronald Acuna Jr. (RF): 10-D
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 15-Day-IL
INJURY [miami marlins] Ronny Henriquez (RP): 6
- `search_web({'query': 'Atlanta Braves vs Miami Marlins May 2025 preview'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Reason Ronald Acuña Jr. Likely Won't Play vs. Marl
- `search_web({'query': 'Braves Marlins injury update pitching rotation 2025'})` → [Sat, 16 May 2026] Google News
[Wed, 24 Sep 2025] Fantasy Baseball Reliever Depth Chart - ESPN
[Thu,
- `get_market_context({'query': 'Atlanta Braves Miami Marlins baseball'})` → [YES=50% vol=$5,821,653] Will Bitcoin hit $150k by June 30, 2026?
[YES=50% vol=$4,544,389] Will Trum
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*