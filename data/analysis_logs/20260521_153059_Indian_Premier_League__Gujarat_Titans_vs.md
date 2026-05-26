# Market Analysis — 2026-05-21 15:30 UTC

## Market
- **Question:** Indian Premier League: Gujarat Titans vs Chennai Super Kings
- **Category:** sports
- **YES Price:** 72.0%
- **Days Left:** 6
- **Volume 24h:** $268,935
- **Liquidity:** $47,116

## Statistical Prior
- **p_base:** 80.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,131 (-0.6% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,075 (-0.6% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Injuries:
- ?: Keshon Gilbert — Out (Surgery)
- ?: Jock Landale — Out (Sprain)
- ?: Jayson Tatum — Out (Soreness)
- ?: Nolan Traore — Out (Not Specified)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: indian premier league: gujarat titans
- [Bing News]
- [Thu, 21 May 2026] indian premier league: gujarat titans
- → Gujarat Titans (GT) to host Chennai Super Kings (CSK) in match 66 of the Indian Premier League 2026 at the Narendra Modi Stadium on Thursday, May 21
- [Thu, 21 May 2026] GT Vs CSK, IPL 2026: See Best Photos From Indian Premier League Match 66 At Ahmedabad's Narendra Modi Stadium
- → Chennai Super Kings' bowling unit is all set to face a tough challenge against a highly consistent Gujarat Titans in the upcoming IPL 2026 match at 
- [Thu, 21 May 2026] Gujarat Titans vs Chennai Super Kings Live Score Updates, IPL 2026: Noor Ahmad delivers to Buttler for a couple
- → Gujarat Titans will take aim to finish at the top two in IPL 2026 playoffs as they take on Chennai Super Kings at the Narendra Modi Stadium on Thurs

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 80.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
The 8% gap between market (72%) and base rate (80%, n=6077) appears attractive on surface, but I cannot verify it represents a real edge. No cricket-specific injury/form data available. Past identical market decisions both resulted in SKIP due to inability to confirm edge. The 70-80% entry band historically shows only 40% WR from 5 trades, suggesting this zone is prone to traps. Without current team news, venue context, or bookmaker odds to validate whether the 8% discount reflects legitimate information (CSK injuries, GT form dip, head-to-head dynamics) vs market mispricing, I cannot confirm a concrete catalyst. The large base rate sample is historical and may not reflect current season dynamics.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_sports_data({'sport': 'cricket', 'team': 'Gujarat Titans'})` → No injury data found for cricket Gujarat Titans
- `search_web({'query': 'Gujarat Titans vs Chennai Super Kings IPL 2024 match preview prediction'})` → [Wed, 22 Apr 2026] Google News
[Sun, 26 Apr 2026] Mumbai Indians vs Chennai Super Kings IPL 2026 Pre
- `search_web({'query': 'Gujarat Titans team news injuries IPL 2024 April'})` → [Tue, 31 Mar 2026] Google News
[Sat, 19 Apr 2025] IPL 2026, LSG vs DC 5th Match Match Preview - All 
- `get_market_context({'keyword': 'Gujarat Titans Chennai Super Kings'})` → No related markets found for 'Gujarat Titans Chennai Super Kings'
- `search_web({'query': 'Chennai Super Kings vs Gujarat Titans head to head record 2024'})` → [2026-05-18] CSK vs SRH head-to-head IPL: Last 5 matches, records at Chennai and Hyderabad home stad
- `search_web({'query': 'IPL 2024 Gujarat Titans Chennai Super Kings odds betting'})` → [2026-05-17] IPL 2026: CSK vs. SRH prediction, lineups, pitch report and betting tips as Pat Cummins
- `get_odds({'sport': 'cricket_ipl'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*