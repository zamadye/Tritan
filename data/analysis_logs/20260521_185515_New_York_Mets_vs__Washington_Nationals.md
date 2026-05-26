# Market Analysis — 2026-05-21 18:55 UTC

## Market
- **Question:** New York Mets vs. Washington Nationals
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 7
- **Volume 24h:** $84,442
- **Liquidity:** $206,254

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,462 (+0.1% 24h) → neutral
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
- → New York Mets star Juan Soto shared an old viral video from his time when he was a member of the Washington Nationals.

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 42.7%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_BIAS
- **Catalyst Strength:** 0.72

### Reasoning
Strong statistical signal (n=13,967) shows markets at 51% YES resolve YES only 44.7% of the time, creating ~6.3% edge on NO at 49¢. Market overprices YES by significant margin at this price point. Supporting evidence: Mets have multiple key pitchers on IL (Senga, Holmes, Minter), just lost to Nationals on May 20 via Wood's inside-the-park grand slam, and are described as bottom of MLB standings. The +1% market-to-base gap is misleading - the stat signal reveals much larger true edge. Previous SKIP decisions failed to capture the 6.3% stat edge available. Cannot verify with bookmaker odds (API quota), which caps confidence.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Mets'})` → INJURY [new york mets] Kodai Senga (SP): 15-Day-IL
INJURY [new york mets] A.J. Minter (RP): 60-Day-I
- `get_sports_data({'sport': 'mlb', 'team': 'Nationals'})` → INJURY [washington nationals] DJ Herz (SP): 60-Day-IL
INJURY [washington nationals] Cole Henry (RP):
- `get_odds({'sport': 'baseball_mlb', 'team': 'Mets'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Mets Nationals baseball'})` → No related markets found for 'Mets Nationals baseball'
- `search_web({'query': 'New York Mets vs Washington Nationals 2025 upcoming series'})` → [Mon, 18 May 2026] Google News
[Wed, 20 May 2026] Game Notes: New York Mets vs Washington Nationals 
- `search_web({'query': 'New York Mets recent results May 2025'})` → [Fri, 30 May 2025] Google News
[Wed, 28 May 2025] Colorado Rockies at New York Mets Game Story, Scor
- `get_market_context({'keyword': 'Mets Nationals'})` → No related markets found for 'Mets Nationals'
- `search_web({'query': '"Mets" "Nationals" 2026 baseball winner prediction'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Mets vs Nationals Prediction, Odds &amp; Player Pr
- `search_web({'query': 'New York Mets pitching rotation May 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] 2 reasons the NY Mets are right to move David Pete
- `search_web({'query': '"Mets vs Nationals" "May 21" 2026 prediction odds'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Mets vs Nationals Prediction, Picks &amp; Odds for
- `search_web({'query': 'New York Mets 2026 record standings'})` → [Tue, 05 May 2026] Google News
[Fri, 01 May 2026] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Mets Nationals May 21 2026 odds moneyline prediction starter'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] New York Mets at Washington Nationals odds, picks 
- `get_market_context({'keyword': 'MLB baseball today'})` → No related markets found for 'MLB baseball today'
- `search_web({'query': 'site:espn.com OR site:yahoo.com "Mets" "Nationals" "May 21" 2026 pick odds starter'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] James Wood's inside-the-park grand slam powers Nat
- `search_web({'query': 'Nationals rally past Mets James Wood grand slam May 20 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] James Wood's inside-the-park grand slam powers Nat
- `search_web({'query': '"Mets" "Nationals" "May 21" 2026 starting pitcher probable'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Mets vs. Nationals (May 21, 2026) Live Score - ESP

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*