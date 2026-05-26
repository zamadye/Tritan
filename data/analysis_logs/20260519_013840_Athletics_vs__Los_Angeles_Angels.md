# Market Analysis — 2026-05-19 01:38 UTC

## Market
- **Question:** Athletics vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $118,937
- **Liquidity:** $268,535

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,668 (-0.2% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,802 (+0.0% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)
- ?: Max Muncy — 10-Day-IL (Fracture)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: athletics angeles angels
- [Bing News]
- [Mon, 18 May 2026] athletics angeles angels
- → The Angels seem destined to waste another year of future Hall of Famer Mike Trout ’s career as their record (16-31) is the worst in MLB. First-year 
- [Mon, 18 May 2026] Game #47: Athletics at Angels Game Thread
- → The Sacramento Athletics (23-22) are headed to Angel Stadium on Monday where they will go up against the Los Angeles Angels (16-30). The moneyline o
- [Mon, 18 May 2026] Sacramento Athletics vs Los Angeles Angels Prediction, 5/18/2026 MLB Picks, Best Bets &amp; Odds
- → Athletics (23-23, first in the AL West) vs. Los Angeles Angels (16-31, fifth in the AL West) Anaheim, California; Monday, 9:38 p.m. EDT PITCHING PRO

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 46.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL INEFFICIENCY
- **Catalyst Strength:** 0.80

### Reasoning
Strong statistical signal (n=13,967) shows markets at 56% resolve YES only 44.7% of the time, indicating significant overpricing of YES. While the base rate gap is small (+3%), the large-sample historical resolution provides a clear edge for NO.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'team': 'Athletics, Los Angeles Angels', 'sport': 'mlb'})` → No injury data found for mlb Athletics, Los Angeles Angels
- `get_odds({'sport': 'baseball_mlb', 'team': 'Athletics, Los Angeles Angels'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Athletics vs Los Angeles Angels recent results injury report'})` → [Mon, 18 May 2026] Google News
[Fri, 15 May 2026] Athletics vs. Angels (May 18, 2026) Live Score - E
- `search_web({'query': 'Oakland Athletics vs LA Angels MLB odds analysis 2024'})` → [Mon, 18 May 2026] Google News
[Tue, 10 Feb 2026] MLB World Series Odds 2026 - Odds Shark
[Wed, 14 J
- `get_market_context({'keyword': 'Athletics Angels'})` → No related markets found for 'Athletics Angels'
- `search_web({'query': 'Oakland Athletics record 2026 MLB season'})` → [Tue, 12 May 2026] Google News
[Sat, 09 May 2026] Baseball Wraps Up 2026 Regular Season with Home Se
- `search_web({'query': 'Los Angeles Angels record 2026 MLB season'})` → [Mon, 18 May 2026] Google News
[Tue, 05 May 2026] Sacramento Athletics vs Los Angeles Angels Predict

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*