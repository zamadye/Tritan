# Market Analysis — 2026-05-20 23:58 UTC

## Market
- **Question:** Athletics vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $85,695
- **Liquidity:** $290,619

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,456 (+0.9% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,456 (+0.9% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
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
- → After mustering just one run in each of their previous two games, the Athletics broke out for 14 runs in a win over the Los Angeles Angels on Tuesda
- [Wed, 20 May 2026] A’s vs. Angels Prediction, Odds, Probable Pitchers, Prop Bets for Wednesday, May 20
- → The Los Angeles Angels couldn't build on the momentum from the wild walk-off win in the series opener against the Athletics, losing 14-6 in Game 2 o
- [Wed, 20 May 2026] Angels Looking To Take 2-1 Series Lead Over Athletics After Getting Blown Out
- → Athletics (24-24, first in the AL West) vs. Los Angeles Angels (17-32, fifth in the AL West) Anaheim, California; Wednesday, 9:38 p.m. EDT. PITCHING

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 52.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.60

### Reasoning
Strong statistical signal indicates market overpricing: markets at 54% historically resolve YES only 44.7% of time (n=13,967). This creates ~10% edge favoring NO. Injury data shows both teams have comparable losses (Angels: C, 2 RP; Athletics: SP, SS, 3B) - neutral impact. Pattern data shows entry at 50-60% range has only 33% WR (n=9), confirming weakness at this price point. While direct team-specific catalyst is absent, the historical mispricing pattern provides a quantifiable edge. Bet NO at 46% when true probability is ~44.7% yields positive EV.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Angels'})` → INJURY [los angeles angels] Travis d'Arnaud (C): 10-Day-IL
INJURY [los angeles angels] Ben Joyce (RP
- `get_sports_data({'sport': 'mlb', 'team': 'Athletics'})` → INJURY [athletics] Gunnar Hoglund (SP): 60-Day-IL
INJURY [athletics] Jacob Wilson (SS): 10-Day-IL
IN
- `search_web({'query': 'Oakland Athletics recent results April 2025'})` → [Sat, 21 Jun 2025] Google News
[Sat, 28 Jun 2025] Cleveland Guardians at Athletics Game Story, Score
- `search_web({'query': 'Athletics vs Angels head to head 2025 MLB'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Athletics vs Angels Prediction, Odds, Moneyline, S
- `get_odds({'sport': 'baseball_mlb', 'team': 'Athletics'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Athletics Angels'})` → No related markets found for 'Athletics Angels'
- `search_web({'query': 'Los Angeles Angels vs Athletics upcoming game June 2025 starting pitchers'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Padres vs Dodgers Series Preview: Pitching Probabl

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*