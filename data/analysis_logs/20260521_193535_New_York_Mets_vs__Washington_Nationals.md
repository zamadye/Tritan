# Market Analysis — 2026-05-21 19:35 UTC

## Market
- **Question:** New York Mets vs. Washington Nationals
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 7
- **Volume 24h:** $111,954
- **Liquidity:** $176,609

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,492 (+0.0% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,357 (+0.1% 24h) → neutral
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
- → Washington's potent offense continues to chug along in our Mets vs. Nationals predictions and MLB picks on Thursday, May 21.
- [Thu, 21 May 2026] Mets vs Nationals Prediction, Picks &amp; Odds for Today's MLB Game
- → WASHINGTON, D.C. — There are a majority of factors that have led David Peterson back into the Mets starting rotation for at least one start. The Nat

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 41.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows 51% markets resolve YES only 44.7% of the time, creating ~6.3% edge. Market overprices YES outcome. No game-specific information found to contradict pattern. Both teams have injuries but no clear advantage.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'New York Mets'})` → INJURY [new york mets] Kodai Senga (SP): 15-Day-IL
INJURY [new york mets] A.J. Minter (RP): 60-Day-I
- `get_sports_data({'sport': 'mlb', 'team': 'Washington Nationals'})` → INJURY [washington nationals] DJ Herz (SP): 60-Day-IL
INJURY [washington nationals] Cole Henry (RP):
- `search_web({'query': 'New York Mets vs Washington Nationals May 2025 series preview'})` → [Thu, 21 May 2026] Google News
[Mon, 18 May 2026] New York Mets at Washington Nationals prediction, 
- `search_web({'query': 'Mets Nationals injury report today May 2025'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Latest O's injuries &amp; transactions - MLB.com
[
- `get_market_context({'keyword': 'Mets Nationals'})` → No related markets found for 'Mets Nationals'
- `search_web({'query': 'New York Mets Washington Nationals game today score'})` → [Tue, 19 May 2026] Google News
[Thu, 21 May 2026] New York Mets at Washington Nationals Game Story, 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Mets'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*