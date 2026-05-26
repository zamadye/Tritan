# Market Analysis — 2026-05-21 18:31 UTC

## Market
- **Question:** New York Mets vs. Washington Nationals
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 7
- **Volume 24h:** $65,947
- **Liquidity:** $192,190

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,751 (+0.4% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,739 (+0.4% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%
- [SPORTS] Recent games:
- NYM @ WSH | Scheduled | Washington Nationals(home) 25-25 score:0 vs New York Mets(away) 21-28 score:0
- TOR @ NYY | Scheduled | New York Yankees(home) 30-20 score:0 vs Toronto Blue Jays(away) 22-27 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: york mets washington nationals
- [Bing News]
- [Thu, 21 May 2026] york mets washington nationals
- → The Mets have seen firsthand why the Nationals are the top-scoring offense in Major League Baseball through the opening three games of their series.
- [Thu, 21 May 2026] NY Mets announce lineup today vs Nationals as they seek a series split
- → As the Mets prepare to close out their series against the Nationals, manager Carlos Mendoza made a crucial pitching decision.
- [Thu, 21 May 2026] Mets make David Peterson move for series finale with Nationals
- → The New York Mets, ranked fifth in the NL East with a 21-28 record, face the Washington Nationals, who are third in the NL East with a 25-25 record.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 44.3%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.68

### Reasoning
Statistical signal shows markets at 51% YES historically resolve YES only 44.7% of the time (n=13,967), creating a 6.3% edge for NO. This exceeds the 5% threshold. Injury data shows both teams have significant absences (Mets missing SP Clay Holmes, Nationals missing 2 SPs) but doesn't clearly favor either side. Pattern data confirms entry 50-60% range has weak 44% win rate. Market overprices YES by ~6.3% - concrete statistical mispricing backed by large sample size.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'New York Mets'})` → INJURY [new york mets] A.J. Minter (RP): 60-Day-IL
INJURY [new york mets] Clay Holmes (SP): 60-Day-I
- `get_sports_data({'sport': 'mlb', 'team': 'Washington Nationals'})` → INJURY [washington nationals] DJ Herz (SP): 60-Day-IL
INJURY [washington nationals] Cole Henry (RP):
- `search_web({'query': 'New York Mets vs Washington Nationals 2025'})` → [Mon, 18 May 2026] Google News
[Sat, 20 Sep 2025] Game Notes: New York Mets vs Washington Nationals 
- `search_web({'query': 'Mets Nationals game today 2025'})` → [Sun, 21 Sep 2025] Google News
[Sat, 20 Sep 2025] Washington Nationals at New York Mets Game Story, 
- `search_web({'query': 'Mets Nationals series May 2026'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Mets vs. Nationals (May 21, 2026) Live Score - ESP
- `get_market_context({'keyword': 'Washington Nationals'})` → No related markets found for 'Washington Nationals'
- `get_market_context({'keyword': 'New York Mets'})` → No related markets found for 'New York Mets'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*