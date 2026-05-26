# Market Analysis — 2026-05-19 13:23 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 7
- **Volume 24h:** $106,489
- **Liquidity:** $45,674

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,742 (-0.8% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,742 (-0.8% 24h) → neutral

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
- [Mon, 18 May 2026] RR Vs LSG Live Cricket Score, IPL 2026: Playoffs-Eyeing Royals Desperate For First Win At Sawai Mansingh Stadium
- → Read the full preview for IPL 2026 Match 64 between Rajasthan Royals and Lucknow Super Giants on May 19, featuring player form, team analysis, head-
- [Tue, 19 May 2026] Match Predictions: Indian Premier League 2026 - Match 64 - Rajasthan Royals vs Lucknow Super Giants - May 19th
- → RR vs LSG IPL 2026 preview featuring Rajasthan Royals’ playoff battle against eliminated Lucknow Super Giants in a crucial clash at Jaipur, know eve

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 53.1%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.72

### Reasoning
Strong statistical signal (n=13,967) shows markets priced at 58% YES resolve YES only 44.7% of time, indicating ~13.3 point overpricing of YES. This implies NO true probability ~55.3% vs 42% market price = ~13% expected value edge on NO. While the 4% gap (58% vs 62% base rate) was insufficient for previous SKIP decisions, the actual mispricing edge from the resolution data is substantially larger. Sports-specific tools unavailable for IPL cricket; no team-specific news found to contradict stat signal. Confidence tempered by lack of match-specific data (injuries, form, conditions) and weak 50-60% entry pattern (WR=33%).

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'nba', 'team': 'Rajasthan Royals'})` → No injury data found for nba Rajasthan Royals
- `get_odds({'sport': 'soccer_epl', 'team': 'Rajasthan Royals'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'IPL Rajasthan Royals Lucknow Super Giants'})` → No related markets found for 'IPL Rajasthan Royals Lucknow Super Giants'
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants IPL 2025 match preview'})` → [Mon, 18 May 2026] Google News
[Tue, 12 May 2026] IPL 2026, RR vs LSG 64th Match Match Preview - RR 
- `search_web({'query': 'Rajasthan Royals injury news form IPL 2025'})` → [Thu, 10 Jul 2025] Google News
[Sun, 18 May 2025] Jofra Archer earns praise from England captain Ben
- `search_web({'query': 'Lucknow Super Giants team news injuries IPL 2025'})` → [Tue, 24 Mar 2026] Google News
[Wed, 25 Mar 2026] LSG team in IPL 2026: Lucknow Super Giants on a ti
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants May 2025 IPL head to head'})` → [Thu, 07 May 2026] Google News
[Fri, 10 Apr 2026] RCB vs LSG, IPL match today: Predicted playing XIs
- `search_web({'query': '"Rajasthan Royals" "Lucknow Super Giants" 2025 IPL form standings'})` → [Fri, 27 Mar 2026] Google News
[Tue, 21 Apr 2026] IPL 2026 preview: From CSK’s recruitment shift to 
- `search_web({'query': 'IPL RR vs LSG head to head record all matches'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] RR vs LSG Head-To-Head Record: Who Holds Edge Ahea
- `search_web({'query': 'Rajasthan Royals Lucknow Super Giants IPL 2025 who will win prediction'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Who Will Win RR vs LSG IPL 2026 Match 64? (Winner 
- `search_web({'query': 'site:espncricinfo.com RR vs LSG 2025 IPL match preview'})` → [Mon, 18 May 2026] Google News
[Fri, 14 Nov 2025] IPL 2026, RR vs LSG 64th Match Match Preview - RR 
- `search_web({'query': '"Rajasthan Royals" "Lucknow Super Giants" IPL 2025 team form wins losses'})` → [Tue, 21 Apr 2026] Google News
[Sun, 01 Jun 2025] IPL 2026, LSG vs RR 32nd Match Match Preview - RR 
- `get_sports_data({'sport': 'nba', 'team': 'Rajasthan Royals'})` → No injury data found for nba Rajasthan Royals
- `get_market_context({'keyword': 'IPL cricket India'})` → No related markets found for 'IPL cricket India'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*