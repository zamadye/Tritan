# Market Analysis — 2026-05-19 11:33 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $90,012
- **Liquidity:** $514,223

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,814 (+0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,822 (+0.0% 24h) → neutral

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
- → Read the full preview for IPL 2026 Match 64 between Rajasthan Royals and Lucknow Super Giants on May 19, featuring player form, team analysis, head-
- [Mon, 18 May 2026] Match Predictions: Indian Premier League 2026 - Match 64 - Rajasthan Royals vs Lucknow Super Giants - May 19th
- → Rajasthan Royals face Lucknow Super Giants in a crucial IPL 2026 clash at the Sawai Mansingh Stadium as playoff pressure mounts. Here’s match previe
- [Tue, 19 May 2026] RR Vs LSG Match Prediction, IPL 2026: Who Will Win Today's Indian Premier League Match In Jaipur?
- → Will the Rajasthan Royals get a step closer to their playoff aspirations, or will the Lucknow Super Giants spoil their party? Check out which team i

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 56.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** FORM/INJURIES
- **Catalyst Strength:** 0.60

### Reasoning
Stat signal (n=13,967) shows markets at 57% YES resolve YES only 44.7% of the time. Headlines suggest RR in poor form, LSG resurgent. Injury scare to key player Vaibhav Sooryavanshi. Market overprices YES by ~12%.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'cricket', 'team': 'Rajasthan Royals'})` → No injury data found for cricket Rajasthan Royals
- `get_market_context({'keyword': 'Rajasthan Royals'})` → No related markets found for 'Rajasthan Royals'
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants match preview'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] IPL 2026, RR vs LSG 64th Match Match Preview - RR 
- `search_web({'query': 'Rajasthan Royals recent form IPL results'})` → [Sun, 17 May 2026] Google News
[Thu, 26 Mar 2026] Who Will Win DC vs RR IPL 2026 Match 62? (Winner P
- `search_web({'query': 'Rajasthan Royals squad news IPL 2026 injuries'})` → [Tue, 19 May 2026] Google News
[Sun, 26 Apr 2026] RR vs LSG Injury News: Is Ravindra Jadeja Playing 
- `search_web({'query': 'Lucknow Super Giants squad news IPL 2026 injuries'})` → [Tue, 19 May 2026] Google News
[Fri, 15 May 2026] RR vs LSG Injury News: Is Ravindra Jadeja Playing 
- `search_web({'query': 'IPL 2026 standings table Rajasthan Royals Lucknow Super Giants'})` → [Mon, 18 May 2026] Google News
[Thu, 14 May 2026] IPL 2026 playoffs: Qualified teams, standings and 
- `search_web({'query': 'RR vs LSG head to head record IPL 2026'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] RR vs LSG IPL 2026 Preview: When, where to watch, 
- `get_odds({'sport': 'cricket_ipl', 'team': 'Rajasthan Royals'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants odds betting 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Where to watch RR vs LSG IPL 2026 match: TV channe

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*