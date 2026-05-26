# Market Analysis — 2026-05-21 15:17 UTC

## Market
- **Question:** Indian Premier League: Gujarat Titans vs Chennai Super Kings
- **Category:** sports
- **YES Price:** 75.0%
- **Days Left:** 6
- **Volume 24h:** $250,311
- **Liquidity:** $107,033

## Statistical Prior
- **p_base:** 83.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $76,959 (-0.4% 24h) → neutral
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
- [Wed, 20 May 2026] Gujarat Titans vs Chennai Super Kings Live Score Updates, IPL 2026: Noor Ahmad delivers a tight ball to Gill
- → Venue: Narendra Modi Stadium Ahmedabad Match coverage has started! Live updates will appear here. This live blog is AI generated. A quiet over for G

## LLM Decision
- **Action:** SKIP
- **Confidence:** 40%
- **p_true:** 83.9%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
No verifiable edge. Base rate (84%) exceeds market (75%) suggesting +9% gap, but past identical GT vs CSK market was skipped because IPL base rate signals proved misleading (55% YES resolved to 44.7% YES). No cricket-specific tools available to verify team form, injuries, or bookmaker odds. Entry zone 70-80% has only 40% WR historically. Without independent confirmation of the edge, SKIP is appropriate.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 40%<52%

## Tool Calls
- `get_sports_data({'sport': 'nba', 'team': 'Gujarat Titans'})` → No injury data found for nba Gujarat Titans
- `search_web({'query': 'Gujarat Titans vs Chennai Super Kings IPL 2025 match preview prediction'})` → [Fri, 03 Apr 2026] Google News
[Tue, 24 Mar 2026] CSK vs PBKS, Match 7 Preview: Head-to-Head Record,
- `get_market_context({'keyword': 'IPL Gujarat Chennai'})` → No related markets found for 'IPL Gujarat Chennai'
- `search_web({'query': 'Gujarat Titans vs Chennai Super Kings 2025 IPL head to head record statistics'})` → No search results for: Gujarat Titans vs Chennai Super Kings 2025 IPL head to head record statistics
- `search_web({'query': 'Gujarat Titans Chennai Super Kings IPL odds betting 2025'})` → [Sat, 25 Apr 2026] Google News
[Sat, 24 May 2025] CSK vs GT IPL 2026 37th Match Prediction &amp; Odd
- `get_market_context({'keyword': 'Indian Premier League cricket'})` → No related markets found for 'Indian Premier League cricket'
- `search_web({'query': 'Gujarat Titans recent results IPL 2025 form'})` → [Sat, 31 May 2025] Google News
[Mon, 17 Feb 2025] GT's Sai Sudharsan scripts IPL history, signs off 
- `search_web({'query': 'Chennai Super Kings recent results IPL 2025 form'})` → [Fri, 03 Apr 2026] Google News
[Sat, 02 May 2026] CSK vs PBKS IPL Records: Head-to-head, most runs, 
- `search_web({'query': '"Gujarat Titans" vs "Chennai Super Kings" 2025 match injury team news'})` → [Sun, 29 Mar 2026] Google News
[Mon, 30 Mar 2026] Match Preview - Rajasthan Royals vs Chennai Super 
- `get_market_context({'keyword': 'cricket IPL betting'})` → No related markets found for 'cricket IPL betting'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*