# Market Analysis — 2026-05-18 23:35 UTC

## Market
- **Question:** Cavaliers vs. Knicks
- **Category:** sports
- **YES Price:** 31.0%
- **Days Left:** 1
- **Volume 24h:** $301,969
- **Liquidity:** $385,853

## Statistical Prior
- **p_base:** 23.1%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,999 (-1.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,980 (-1.1% 24h) → risk-OFF

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- [SPORTS] Injuries:
- ?: Keshon Gilbert — Out (Surgery)
- ?: Jock Landale — Out (Sprain)
- ?: Jayson Tatum — Out (Soreness)
- ?: Nolan Traore — Out (Not Specified)
- ?: Nic Claxton — Out (Sprain)
- ?: Ziaire Williams — Out (Inflammation)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: cavaliers knicks
- [Bing News]
- [Mon, 18 May 2026] cavaliers knicks
- → What channel are New York Knicks vs Cleveland Cavaliers games on? How to watch, how to stream Eastern Conference Finals with TV, times, streaming.
- [Mon, 18 May 2026] Cavaliers vs Knicks schedule, TV channel, how to watch NBA playoffs
- → The Cleveland Cavaliers have advanced to the Eastern Conference Finals to take on the New York Knicks. The Cavs have not been in this spot in over a
- [Mon, 18 May 2026] Cavaliers vs Knicks Tactical Breakdown: 3 Ways Cleveland Can Beat New York
- → Entering the 2025-26 season, the New York Knicks and Cleveland Cavaliers were viewed as the clear top teams in the East. And while the regular seaso

## LLM Decision
- **Action:** NO
- **Confidence:** 62%
- **p_true:** 15.1%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_UPDATE_REVERSAL
- **Catalyst Strength:** 0.70

### Reasoning
OG Anunoby (Knicks' key defender) was listed as 'Out' but multiple sources now report he is 'reportedly playing in Game 1' and practiced. The crowd priced Cavaliers YES at 31% (8% above base rate of 23%), likely reflecting the initial Anunoby-out assumption. With Anunoby returning, the Knicks' defensive strength increases significantly. The base rate of 23% (n=6077 large sample) is a more accurate reflection of Cavaliers' true win probability against a healthy Knicks team on the road. The crowd has not yet fully incorporated the Anunoby playing news, creating a ~6-8% overpricing of Cavaliers' chances. Caveat: Anunoby's status is not 100% confirmed officially, limiting confidence to moderate level.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `get_sports_data({'sport': 'nba', 'team': 'Cavaliers'})` → INJURY [cleveland cavaliers] Larry Nance Jr. (F): Day-To-Day
- `get_sports_data({'sport': 'nba', 'team': 'Knicks'})` → INJURY [new york knicks] OG Anunoby (F): Out
- `get_odds({'sport': 'basketball_nba'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Cavaliers vs Knicks game tomorrow prediction injury report'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Cavaliers vs. Knicks Game 1 odds update: Experts a
- `search_web({'query': 'NBA Cavaliers Knicks playoff odds 2025'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Cavaliers vs. Knicks Opening Odds for Game 1 of Ea
- `get_market_context({'keyword': 'Cavaliers Knicks'})` → No related markets found for 'Cavaliers Knicks'
- `search_web({'query': 'Knicks OG Anunoby injury status Game 1 Eastern Conference Finals'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Knicks' OG Anunoby reportedly playing in Game 1 ag
- `search_web({'query': 'Cavaliers Knicks Game 1 spread moneyline odds May 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Cavaliers vs. Knicks Game 1 odds update: Experts a
- `search_web({'query': '"Cavaliers vs Knicks" "Game 1" spread odds May 19 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Cavaliers vs. Knicks Game 1 odds update: Experts a
- `search_web({'query': 'Knicks Cavaliers Game 1 Eastern Conference Finals odds favorite 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] 2026 NBA playoffs betting: How to bet the conferen
- `search_web({'query': 'Cavaliers Knicks Game 1 prediction who wins analysis'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Cavaliers vs Knicks Prediction, Picks &amp; Odds f

## Outcome
**✅ WIN** | P&L: $+0.45 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*