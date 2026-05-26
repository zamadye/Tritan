# Market Analysis — 2026-05-18 13:39 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 7
- **Volume 24h:** $64,846
- **Liquidity:** $256,561

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,121 (-1.5% 24h) → risk-OFF
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
- **Confidence:** 65%
- **p_true:** 47.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE_INJURY_IMPACT
- **Catalyst Strength:** 0.60

### Reasoning
Stat signal shows 51% YES markets resolve YES only 44.7% of the time (n=13,967), indicating YES is overpriced by ~6.3%. Braves missing star RF Ronald Acuna Jr. (10-Day IL) weakens their lineup significantly. NO at 49% has meaningful edge vs historical 44.7% YES resolution. Previous SKIP decisions focused on 1% gap between price and base rate, but the stat signal provides stronger evidence of overpricing. Macro risk-off sentiment adds caution but is not directly relevant.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Braves'})` → INJURY [atlanta braves] Eli White (CF): 7-Day IL
INJURY [atlanta braves] Ronald Acuna Jr. (RF): 10-D
- `get_sports_data({'sport': 'mlb', 'team': 'Marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 15-Day-IL
INJURY [miami marlins] Ronny Henriquez (RP): 6
- `search_web({'query': 'Atlanta Braves injury update Ronald Acuna Jr 2025'})` → [Sat, 16 May 2026] Google News
[Fri, 08 May 2026] Braves Injury Update: Sean Murphy's timeline, Rona
- `search_web({'query': 'Miami Marlins recent results 2025 MLB'})` → [Tue, 05 May 2026] Google News
[Sat, 13 Sep 2025] 2026 MLB Standings and Records: Spring Training - 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'query': 'Atlanta Braves Miami Marlins'})` → [YES=50% vol=$5,821,653] Will Bitcoin hit $150k by June 30, 2026?
[YES=50% vol=$4,717,943] Will Trum
- `search_web({'query': 'Braves vs Marlins May 2025 game prediction starting pitchers'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Miami Marlins vs. Atlanta Braves Series May 18-21:
- `search_web({'query': 'Miami Marlins recent performance winning streak 2025'})` → [Tue, 05 May 2026] Google News
[Fri, 22 Aug 2025] 2026 MLB Standings and Records: Spring Training - 
- `get_crypto_price({'coin': 'bitcoin'})` → bitcoin: $76,806.00 | 24h: -1.88%

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*