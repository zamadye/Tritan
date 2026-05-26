# Market Analysis — 2026-05-19 12:26 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 7
- **Volume 24h:** $95,493
- **Liquidity:** $265,259

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,746 (-0.9% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,669 (-0.9% 24h) → neutral

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
- [Tue, 19 May 2026] indian premier league: rajasthan royals
- → Rajasthan Royals have 12 points from 12 games, while Lucknow Super Giants have eight points from 12 matches and are out of playoff contention. Follo
- [Mon, 18 May 2026] RR Vs LSG Live Cricket Score, IPL 2026: Playoffs-Seeking Royals Desperate For First Win In Jaipur
- → Read the full preview for IPL 2026 Match 64 between Rajasthan Royals and Lucknow Super Giants on May 19, featuring player form, team analysis, head-
- [Tue, 19 May 2026] Match Predictions: Indian Premier League 2026 - Match 64 - Rajasthan Royals vs Lucknow Super Giants - May 19th
- → RR vs LSG IPL 2026 preview featuring Rajasthan Royals’ playoff battle against eliminated Lucknow Super Giants in a crucial clash at Jaipur, know eve

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 51.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 58% YES resolve YES only 44.7% of the time — clear ~13% systematic overpricing. While gap metric (4%) is below 5% threshold and past similar decisions skipped, the large-sample stat edge is substantial and directly applicable. Sports category WR=81% supports contrarian approach. News shows RR at home Jaipur but LSG described as 'resurgent' with no clear catalyst favoring YES. Entry range 50-60% has weak WR=33%, further supporting NO.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'cricket', 'team': 'Rajasthan Royals'})` → No injury data found for cricket Rajasthan Royals
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants 2025 IPL recent form'})` → [Tue, 21 Apr 2026] Google News
[Tue, 03 Jun 2025] IPL 2026, LSG vs RR 32nd Match Match Preview - RR 
- `search_web({'query': 'Rajasthan Royals Lucknow Super Giants team news injuries 2025'})` → [Fri, 18 Apr 2025] Google News
[Mon, 21 Apr 2025] IPL 2025, RR vs LSG 36th Match Match Preview - RR 
- `get_market_context({'keyword': 'Rajasthan Royals Lucknow Super Giants'})` → No related markets found for 'Rajasthan Royals Lucknow Super Giants'
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants 2026 IPL match preview team news'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] RR vs LSG IPL 2026 Playing 11 Today Match: Ravindr
- `search_web({'query': '"RR vs LSG" IPL 2026 Jaipur match preview pitch report predicted XI'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] RR vs LSG IPL 2026 Preview: When, where to watch, 
- `search_web({'query': 'ESPNcricinfo RR vs LSG IPL 2026 64th match preview team form playoff'})` → [Mon, 18 May 2026] Google News
[Fri, 14 Nov 2025] IPL 2026, RR vs LSG 64th Match Match Preview - RR 
- `search_web({'query': 'IPL 2026 standings Rajasthan Royals Lucknow Super Giants recent results'})` → [Mon, 18 May 2026] Google News
[Sat, 09 May 2026] RR vs LSG IPL 2026: Players, standings, stats and 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*