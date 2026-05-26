# Market Analysis — 2026-05-21 13:33 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $86,173
- **Liquidity:** $244,529

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,200 (+0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,189 (-0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: Gunnar Hoglund — 60-Day-IL (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: pittsburgh pirates louis cardinals
- [Bing News]
- [Thu, 21 May 2026] pittsburgh pirates louis cardinals
- → The Pittsburgh Pirates (24-24) are on their way to Busch Stadium on Thursday where they will attempt to beat the St. Louis Cardinals (28-19). The li
- [Thu, 21 May 2026] Pittsburgh Pirates vs St. Louis Cardinals Prediction, 5/21/2026 MLB Picks, Best Bets &amp; Odds
- → Pittsburgh Pirates (25-24, fifth in the NL Central) vs. St. Louis Cardinals (28-20, second in the NL Central) St. Louis; Thursday, 1:15 p.m. EDT PIT
- [Wed, 20 May 2026] Pirates play the Cardinals after Griffin's 4-hit game
- → Spencer Horwitz homered, Konnor Griffin had four singles, and the Pittsburgh Pirates beat the St. Louis Cardinals 7-0 to snap a four-game losing str

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 48.7%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MARKET_INEFFICIENCY
- **Catalyst Strength:** 0.72

### Reasoning
Strong stat signal (n=13,967) shows markets at 55% resolve YES only 44.7% of time - a 10.3% overpricing gap. While the base rate gap (+2%) is small, the historical resolution data provides concrete evidence that YES at 55% is overpriced. Pirates have key injuries (O'Hearn, Jones, Bart) which may further weaken their position. The edge is statistical but verifiable with large sample size.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals May 2025 preview'})` → No search results for: Pittsburgh Pirates vs St. Louis Cardinals May 2025 preview
- `search_web({'query': 'Pittsburgh Pirates game today 2025'})` → [Tue, 19 May 2026] Google News
[Wed, 24 Sep 2025] 2026 MLB Standings and Records: Wild Card - MLB.co
- `search_web({'query': 'St. Louis Cardinals game today 2025'})` → [Sat, 16 May 2026] Google News
[Tue, 19 May 2026] Military Appreciation Day Theme Tickets | St. Loui
- `search_web({'query': 'Pirates vs Cardinals September 2025'})` → [Sun, 14 Sep 2025] Google News
[Wed, 24 Sep 2025] Pittsburgh Pirates at Washington Nationals Game St
- `get_market_context({'keyword': 'Pittsburgh Pirates'})` → No related markets found for 'Pittsburgh Pirates'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*