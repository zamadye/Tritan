# Market Analysis — 2026-05-19 09:53 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $85,159
- **Liquidity:** $514,050

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,744 (-0.2% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,848 (-0.1% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Recent games:
- BOS @ KC | Final | Kansas City Royals(home) 20-28 score:1 vs Boston Red Sox(away) 20-27 score:3
- [SPORTS] Injuries:
- ?: James McCann — Out (Strain)
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: indian premier league: rajasthan royals
- [Bing News]
- [Mon, 18 May 2026] indian premier league: rajasthan royals
- → Rajasthan Royals face Lucknow Super Giants in a crucial IPL 2026 clash at the Sawai Mansingh Stadium as playoff pressure mounts. Here’s match previe
- [Mon, 18 May 2026] RR Vs LSG Match Prediction, IPL 2026: Who Will Win Today's Indian Premier League Match In Jaipur?
- → Read the full preview for IPL 2026 Match 64 between Rajasthan Royals and Lucknow Super Giants on May 19, featuring player form, team analysis, head-
- [Tue, 19 May 2026] Match Predictions: Indian Premier League 2026 - Match 64 - Rajasthan Royals vs Lucknow Super Giants - May 19th
- → Rajasthan Royals face Lucknow Super Giants in IPL 2026 Match 64 on Tuesday. Check RR’s playoff qualification scenarios ahead of the big match tonigh

## LLM Decision
- **Action:** SKIP
- **Confidence:** 63%
- **p_true:** 52.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal (n=13,967) shows markets at 57% YES historically resolve YES only 44.7% of the time — a 12.3% overpricing of YES. Pattern data confirms 50-60% entry range has only 33% win rate for YES. NO price of 43% vs true NO probability of ~54% yields ~26% expected value. Confidence moderate due to inability to verify cricket-specific injury/form data.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'nfl', 'team': 'Rajasthan Royals'})` → No injury data found for nfl Rajasthan Royals
- `get_sports_data({'sport': 'nfl', 'team': 'Lucknow Super Giants'})` → No injury data found for nfl Lucknow Super Giants
- `get_market_context({'keyword': 'Rajasthan Royals Lucknow Super Giants IPL'})` → No related markets found for 'Rajasthan Royals Lucknow Super Giants IPL'
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants IPL 2024 match preview prediction'})` → [Fri, 08 May 2026] Google News
[Tue, 21 Apr 2026] IPL RR VS LSG MATCH PREDICTION RAJASTHAN ROYALS VS
- `search_web({'query': 'Rajasthan Royals IPL recent results form 2024'})` → [Tue, 03 Jun 2025] Google News
[Thu, 21 Mar 2024] IPL 2025 schedule: The complete match list - olymp
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants head to head record IPL 2024'})` → [Thu, 14 May 2026] Google News
[Tue, 19 May 2026] LSG vs RR, IPL match 2026 today: Likely playing XI
- `search_web({'query': 'Lucknow Super Giants recent form IPL 2024 last 5 matches'})` → [Thu, 14 May 2026] Google News
[Wed, 01 Apr 2026] IPL 2026, LSG vs CSK 59th Match Match Preview - CS
- `get_market_context({'keyword': 'Rajasthan Royals win'})` → No related markets found for 'Rajasthan Royals win'
- `search_web({'query': 'LSG vs RR IPL 2026 match prediction odds betting'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] RR vs LSG IPL 2026 64th Match Prediction &amp; Odd
- `search_web({'query': 'Rajasthan Royals squad 2026 injuries players out'})` → No search results for: Rajasthan Royals squad 2026 injuries players out
- `get_market_context({'keyword': 'IPL cricket prediction market'})` → No related markets found for 'IPL cricket prediction market'
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants May 2026 odds prediction winner'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] RR vs LSG IPL 2026 64th Match Prediction &amp; Odd
- `search_web({'query': 'IPL 2026 RR LSG standings table points'})` → [Mon, 18 May 2026] Google News
[Sat, 09 May 2026] RR vs LSG IPL 2026: Players, standings, stats and 
- `search_web({'query': 'IPL 2026 points table current standings after RR vs LSG match'})` → [Wed, 22 Apr 2026] Google News
[Tue, 19 May 2026] IPL 2026 Points Table after Match 32: Rajasthan Ro
- `search_web({'query': '"RR vs LSG" IPL 2026 "match 64" prediction who will win'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] RR Vs LSG Match Prediction, IPL 2026: Who Will Win
- `search_web({'query': 'Rajasthan Royals key players missing IPL 2026 injuries'})` → [Fri, 20 Mar 2026] Google News
[Tue, 24 Mar 2026] IPL 2026: Complete list of injured and unavailable
- `search_web({'query': 'Lucknow Super Giants key players missing IPL 2026 injuries'})` → [Tue, 24 Mar 2026] Google News
[Tue, 24 Mar 2026] IPL 2026: Full list of key players missing matches

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*