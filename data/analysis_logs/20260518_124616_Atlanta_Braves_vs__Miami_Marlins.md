# Market Analysis — 2026-05-18 12:46 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 7
- **Volume 24h:** $60,624
- **Liquidity:** $251,268

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,601 (-1.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,669 (-1.0% 24h) → neutral
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
- **Confidence:** 52%
- **p_true:** 51.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_UPDATE
- **Catalyst Strength:** 0.30

### Reasoning
Stat signal clearly shows YES is overpriced at 51% (historically resolves YES only 44.7%), but gap vs base rate is only 1% - fails the 5% gate threshold. Braves have significant injuries (Acuña Jr., Eli White on IL), but no concrete evidence that specific injuries will decisively impact this particular game outcome. No bookmaker odds available to confirm edge. Two prior SKIP decisions on same market with identical reasoning. Pattern shows 88% WR on sports bets overall, but entry points in 50-60% range have only 25% WR (4 trades). Insufficient verifiable catalyst despite statistical overpricing signal.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'braves'})` → INJURY [atlanta braves] Eli White (CF): 7-Day IL
INJURY [atlanta braves] Ronald Acuna Jr. (RF): 10-D
- `get_sports_data({'sport': 'mlb', 'team': 'marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 15-Day-IL
INJURY [miami marlins] Ronny Henriquez (RP): 6
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025'})` → [Sat, 09 Aug 2025] Google News
[Sat, 09 Aug 2025] Braves 7-1 Marlins (Aug 9, 2025) Final Score - ESP
- `search_web({'query': 'Braves Marlins injury update August 2025'})` → [Thu, 30 Apr 2026] Google News
[Thu, 07 Aug 2025] Spencer Strider Injury Update: Nearing 2026 Return
- `get_market_context({'keyword': 'Braves Marlins'})` → No related markets found for 'Braves Marlins'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'MLB'})` → No related markets found for 'MLB'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*