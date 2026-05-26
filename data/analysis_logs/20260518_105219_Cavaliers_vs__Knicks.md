# Market Analysis — 2026-05-18 10:52 UTC

## Market
- **Question:** Cavaliers vs. Knicks
- **Category:** sports
- **YES Price:** 30.0%
- **Days Left:** 1
- **Volume 24h:** $43,803
- **Liquidity:** $229,593

## Statistical Prior
- **p_base:** 21.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.1%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,785 (-2.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,817 (-2.1% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Recent games:
- CLE @ DET | Final | Detroit Pistons(home) 60-22 score:94 vs Cleveland Cavaliers(away) 52-30 score:125
- [SPORTS] Injuries:
- ?: Keshon Gilbert — Out (Surgery)
- ?: Jock Landale — Out (Sprain)
- ?: Jayson Tatum — Out (Soreness)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: cavaliers knicks
- [Bing News]
- [Mon, 18 May 2026] cavaliers knicks
- → There is no more sitting back and watching to learn who their opponent will be in the Eastern Conference finals. It will be the Cavaliers, after the
- [Sun, 17 May 2026] Knicks will face Cavaliers in Eastern Conference finals — here’s how the two teams stack up
- → What channel are New York Knicks vs Cleveland Cavaliers games on? How to watch, how to stream Eastern Conference Finals with TV, times, streaming.
- [Sun, 17 May 2026] Cavaliers vs Knicks schedule, TV channel, how to watch NBA playoffs
- → 2026 NBA playoffs picks, predictions, odds for Cleveland Cavaliers vs New York Knicks Eastern Conference final postseason series. Who wins series?

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 21.9%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 0%<52%

## Tool Calls
- `get_sports_data({'sport': 'nba', 'team': 'Cavaliers'})` → INJURY [cleveland cavaliers] Larry Nance Jr. (F): Day-To-Day
- `get_sports_data({'sport': 'nba', 'team': 'Knicks'})` → INJURY [new york knicks] OG Anunoby (F): Out
- `get_odds({'sport': 'basketball_nba', 'team': 'Cavaliers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Cavaliers vs Knicks tonight game odds'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Cleveland Cavaliers vs New York Knicks odds for NB
- `search_web({'query': 'Cavaliers Knicks injury report OG Anunoby'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] Knicks’ OG Anunoby injury update suggests he’ll be
- `search_web({'query': 'OG Anunoby status Game 1 Eastern Conference Finals'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Knicks’ OG Anunoby injury update suggests he’ll be
- `search_web({'query': 'Cavaliers Knicks series odds Eastern Conference Finals'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] 2026 NBA playoffs second-round odds: Pistons favor

## Outcome
**✅ WIN** | P&L: $+0.45 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*