# Market Analysis — 2026-05-21 20:26 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $214,413
- **Liquidity:** $268,236

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,640 (+0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,637 (+0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- [SPORTS] Recent games:
- ATL @ MIA | Scheduled | Miami Marlins(home) 22-28 score:0 vs Atlanta Braves(away) 34-16 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Spencer Giesting — Day-To-Day (Not Specified)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → The Atlanta Braves are looking to take the final three games of their series against the Miami Marlins after getting shut out 12-0 in the opener. Th
- [Thu, 21 May 2026] Braves vs. Marlins Prediction, Odds, Probable Pitchers, Prop Bets for Thursday, May 21
- → The Braves are the best team in baseball and there is no denying that. On Wednesday, they just did something for the first time in over two decades.
- [Thu, 21 May 2026] Atlanta Braves just did something the organization hasn't done since 2003 with win over Marlins
- → Atlanta Braves roster update: veteran pitcher Carlos Carrasco is back in the spotlight as the team faces the Marlins.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.15

### Reasoning
Same market previously attempted twice and failed both times due to insufficient gap (3% < 5%). Stat signal shows YES overpriced (57% market vs 44.7% historical), but: (1) gap between market and base rate is only +3%, below threshold; (2) Entry zone 50-60% has weak 42% WR (n=19); (3) Injury data shows balanced minor injuries on both sides with no significant pitching advantage; (4) No new catalyst or breaking information. The historical stat edge exists but is not actionable given the narrow gap and poor zone performance record.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Braves'})` → INJURY [atlanta braves] Hurston Waldrep (SP): 60-Day-IL
INJURY [atlanta braves] Drake Baldwin (C): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 60-Day-IL
INJURY [miami marlins] Leo Jimenez (3B): 7-day
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 recent results'})` → [Tue, 26 Aug 2025] Google News
[Wed, 27 Aug 2025] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'Atlanta Braves Miami Marlins series predictions August 2025'})` → [Tue, 19 May 2026] Google News
[Mon, 25 Aug 2025] Braves vs Marlins Prediction, Odds, Moneyline, Spr
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins'})` → No related markets found for 'Atlanta Braves Miami Marlins'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Braves Marlins starting pitcher August 27 2025'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Braves vs Marlins Prediction, Odds, Moneyline, Spr

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*