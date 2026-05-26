# Market Analysis — 2026-05-21 01:48 UTC

## Market
- **Question:** Athletics vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 6
- **Volume 24h:** $132,191
- **Liquidity:** $357,434

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,831 (+1.7% 24h) → risk-ON
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,762 (+1.5% 24h) → risk-ON
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: Gunnar Hoglund — 60-Day-IL (Surgery)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: athletics angeles angels
- [Bing News]
- [Wed, 20 May 2026] athletics angeles angels
- → The Los Angeles Angels couldn't build on the momentum from the wild walk-off win in the series opener against the Athletics, losing 14-6 in Game 2 o
- [Wed, 20 May 2026] Angels Looking To Take 2-1 Series Lead Over Athletics After Getting Blown Out
- → Athletics (24-24, first in the AL West) vs. Los Angeles Angels (17-32, fifth in the AL West) Anaheim, California; Wednesday, 9:38 p.m. EDT. PITCHING
- [Wed, 20 May 2026] Los Angeles Angels take on the Athletics Wednesday
- → Here's how to watch Wednesday's Los Angeles Angels vs Athletics game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 56.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_SIGNAL_ONLY
- **Catalyst Strength:** 0.40

### Reasoning
Strong statistical signal (n=13,967) suggests market overprices YES at 54% (historical YES resolution only 44.7%), but base rate gap is only +2%, failing the 5% gate threshold. Both previous analyses of this identical market were SKIP for same reason. No new catalyst or injury information changes the calculus. Consistent with past SKIP decisions.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Athletics'})` → INJURY [athletics] Gunnar Hoglund (SP): 60-Day-IL
INJURY [athletics] Jacob Wilson (SS): 10-Day-IL
IN
- `get_sports_data({'sport': 'mlb', 'team': 'Angels'})` → INJURY [los angeles angels] Travis d'Arnaud (C): 10-Day-IL
INJURY [los angeles angels] Ben Joyce (RP
- `get_market_context({'keyword': 'Athletics Angels'})` → No related markets found for 'Athletics Angels'
- `search_web({'query': 'Oakland Athletics recent results MLB 2025'})` → [Tue, 09 Sep 2025] Google News
[Mon, 25 Aug 2025] Boston Red Sox at Athletics Game Story, Scores/Hig
- `search_web({'query': 'Los Angeles Angels recent results MLB 2025'})` → [Tue, 05 May 2026] Google News
[Sun, 07 Sep 2025] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Athletics Angels series September 2025 results score'})` → [Fri, 05 Sep 2025] Google News
[Fri, 26 Sep 2025] Athletics at Los Angeles Angels Game Story, Scores
- `search_web({'query': 'Oakland Athletics vs Los Angeles Angels upcoming pitching matchup'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Athletics vs. Angels Prediction, Odds, &amp; Exper

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*