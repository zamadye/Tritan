# Market Analysis — 2026-05-16 18:33 UTC

## Market
- **Question:** New York Yankees vs. New York Mets
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $313,484
- **Liquidity:** $388,943

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,163 (-1.2% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,131 (-1.4% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 31(Fear) → 43(Fear) → 34(Fear) → 42(Fear) | sentiment worsening
- Will the Fed decrease interest rates by 50+ bps after the Ju → YES=50%
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 46.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** CROWD_BIAS
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal shows markets at 54% resolve YES only 44.7% of the time (n=13,967) — a 9.3% systematic overpricing gap. Clay Holmes fracture is significant for Mets but likely already priced in; Yankees also missing Fried, Stanton, Dominguez. No breaking news <2h. Subway Series likely attracts casual bettors creating home/favorite bias. Sports category historically strong (WR=85%, n=13). Macro Fear (31) not directly relevant to single game but suggests risk-off sentiment. The price gap (+2% above base rate) combined with historical market inefficiency at this price level provides clear edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<3%

## Tool Calls
- `search_web({'query': 'New York Yankees vs New York Mets 2025 game today'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] MLB 2026: Scorecard for Mets, Yankees ahead of Sub
- `get_sports_data({'sport': 'mlb', 'team': 'Yankees'})` → INJURY [new york yankees] Max Fried (SP): 15-Day-IL
INJURY [new york yankees] Giancarlo Stanton (DH)
- `get_sports_data({'sport': 'mlb', 'team': 'Mets'})` → INJURY [new york mets] Clay Holmes (SP): Out
INJURY [new york mets] Jorge Polanco (1B): 10-Day-IL
IN
- `get_market_context({'keyword': 'Yankees Mets'})` → No related markets found for 'Yankees Mets'
- `search_web({'query': 'Yankees vs Mets May 15 2025 starting pitchers odds'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] Yankees vs Mets start time today, how to watch and
- `search_web({'query': 'Subway Series Yankees Mets 2025 injuries roster updates'})` → [Sat, 16 May 2026] Google News
[Fri, 15 May 2026] Mets' Clay Holmes struck by comebacker, fractures 
- `search_web({'query': '"Yankees vs Mets" "May 15" 2025 starting pitcher today'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] Yankees vs Mets start time today, how to watch and
- `search_web({'query': 'New York Yankees recent results last 5 games May 2025'})` → [Sun, 24 Aug 2025] Google News
[Tue, 05 Aug 2025] Boston Red Sox at New York Yankees Game Story, Sco
- `search_web({'query': 'New York Mets recent results last 5 games May 2025'})` → [Fri, 30 May 2025] Google News
[Tue, 10 Jun 2025] Colorado Rockies at New York Mets Game Story, Scor

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*