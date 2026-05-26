# Market Analysis — 2026-05-18 13:29 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 7
- **Volume 24h:** $64,825
- **Liquidity:** $255,626

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,331 (-1.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,304 (-1.2% 24h) → risk-OFF
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
- **Confidence:** 48%
- **p_true:** 51.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Stat signal shows YES overpriced at 51% (historical resolution 44.7%), but gap of only 1% falls below 5% threshold. No fresh catalyst or breaking news to exploit the mispricing. 50-60% entry range shows weak 25% WR historically. Consistent with two prior SKIP decisions on this exact market.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Braves'})` → INJURY [atlanta braves] Eli White (CF): 7-Day IL
INJURY [atlanta braves] Ronald Acuna Jr. (RF): 10-D
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 matchup preview prediction'})` → [Mon, 18 May 2026] Google News
[Tue, 14 Apr 2026] Braves vs. Marlins Prediction, Odds &amp; Expert A
- `search_web({'query': 'Atlanta Braves injury report April 2026'})` → [Sat, 16 May 2026] Google News
[Tue, 28 Apr 2026] Latest Braves injuries &amp; transactions - MLB.co
- `search_web({'query': 'Miami Marlins 2026 roster news'})` → [Fri, 20 Mar 2026] Google News
[Tue, 27 Jan 2026] Updated 2026 Marlins Opening Day roster projection
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 season series results'})` → [Wed, 27 Aug 2025] Google News
[Fri, 08 May 2026] Atlanta Braves at Miami Marlins Game Story, Scores

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*