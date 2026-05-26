# Market Analysis — 2026-05-21 14:06 UTC

## Market
- **Question:** Indian Premier League: Gujarat Titans vs Chennai Super Kings
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $56,391
- **Liquidity:** $57,799

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,074 (-0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,119 (+0.0% 24h) → neutral
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
- → Gujarat Titans will take aim to finish at the top two in IPL 2026 playoffs as they take on Chennai Super Kings at the Narendra Modi Stadium on Thurs
- [Thu, 21 May 2026] GT Vs CSK Match Facts, IPL 2026: All You Need To Know About Today's Indian Premier League Match In Ahmedabad
- → Chennai Super Kings' bowling unit is all set to face a tough challenge against a highly consistent Gujarat Titans in the upcoming IPL 2026 match at 
- [Wed, 20 May 2026] Gujarat Titans vs Chennai Super Kings Live Score Updates, IPL 2026: Gujarat Titans' lineup against Chennai Super Kings
- → Check match prediction and probable playing 11s for Indian premier league 2026 match 66 between Gujarat Titans and Chennai Super Kings on Thursday, 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 60%
- **p_true:** 55.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.55

### Reasoning
Strong historical stat signal (n=13,967) shows markets at 55% YES resolve YES only 44.7% of the time, creating ~10% edge for NO at 45 cents (EV ~55¢). PATTERN confirms 50-60% entry range has only 38% WR for YES. No team-specific cricket data (injuries, form, head-to-head) available to further validate, capping confidence at 0.60. This is a crowd-bias trade: market overprices the favorite in a near-coin-flip matchup.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'cricket', 'team': 'Gujarat Titans'})` → No injury data found for cricket Gujarat Titans
- `get_sports_data({'sport': 'cricket', 'team': 'Chennai Super Kings'})` → No injury data found for cricket Chennai Super Kings
- `search_web({'query': 'IPL 2025 Gujarat Titans vs Chennai Super Kings match preview prediction'})` → [Fri, 03 Apr 2026] Google News
[Tue, 24 Mar 2026] CSK vs PBKS, Match 7 Preview: Head-to-Head Record,
- `search_web({'query': 'Gujarat Titans Chennai Super Kings injury news team news IPL 2025'})` → [Sun, 29 Mar 2026] Google News
[Mon, 30 Mar 2026] Match Preview - Rajasthan Royals vs Chennai Super 
- `get_market_context({'keyword': 'IPL Gujarat Titans Chennai Super Kings cricket'})` → No related markets found for 'IPL Gujarat Titans Chennai Super Kings cricket'
- `search_web({'query': 'Gujarat Titans vs Chennai Super Kings IPL 2025 April head to head form guide'})` → [Sat, 04 Apr 2026] Google News
[Fri, 17 Apr 2026] DC vs MI IPL Records: Head-to-head, most runs, mos
- `search_web({'query': 'IPL 2025 Gujarat Titans results form standings table April 2025'})` → [Tue, 03 Jun 2025] Google News
[Tue, 27 May 2025] IPL 2025 results: Get all cricket scores, points t
- `get_odds({'sport': 'cricket', 'team': 'Gujarat Titans'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': '"Gujarat Titans" "Chennai Super Kings" IPL April 2026'})` → [Tue, 19 May 2026] Google News
[Thu, 21 May 2026] IPL 2026: Complete schedule, match timings and ven
- `search_web({'query': 'IPL 2026 standings points table April Gujarat Titans Chennai Super Kings'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] IPL 2026 Points Table: Team Standings &amp; Rankin
- `get_market_context({'keyword': 'IPL cricket match winner'})` → No related markets found for 'IPL cricket match winner'
- `search_web({'query': 'Gujarat Titans recent form IPL 2026 results last 5 matches'})` → [Thu, 21 May 2026] Google News
[Wed, 08 Apr 2026] GT vs CSK Playing 11 Today Match: Predicted XI &am
- `search_web({'query': 'Chennai Super Kings recent form IPL 2026 results last 5 matches'})` → [Sat, 16 May 2026] Google News
[Thu, 21 May 2026] Indian Premier League 2026 | Dates, Format, Player
- `get_market_context({'keyword': 'Chennai Super Kings win'})` → No related markets found for 'Chennai Super Kings win'
- `search_web({'query': 'GT vs CSK IPL 2026 match prediction head to head record'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] GT vs CSK, IPL 2026: Head-to-head record, probable
- `search_web({'query': 'Gujarat Titans squad 2026 key players injury update'})` → [Thu, 21 May 2026] Google News
[Wed, 25 Mar 2026] GT vs CSK Dream11 Prediction, Match 66, IPL Fantas
- `get_market_context({'keyword': 'Gujarat Titans win'})` → No related markets found for 'Gujarat Titans win'
- `search_web({'query': 'GT vs CSK IPL 2026 Match 66 prediction who will win'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] GT Vs CSK Match Prediction, IPL 2026: Who Will Win
- `search_web({'query': 'IPL 2026 GT CSK playing XI pitch report Ahmedabad'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] GT vs CSK Dream11: Lineups, pitch report and score
- `get_market_context({'keyword': 'IPL cricket sports prediction'})` → No related markets found for 'IPL cricket sports prediction'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*