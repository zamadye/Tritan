# Market Analysis — 2026-05-19 13:06 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 7
- **Volume 24h:** $96,803
- **Liquidity:** $114,992

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,890 (-0.7% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,863 (-1.0% 24h) → risk-OFF

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
- **Confidence:** 55%
- **p_true:** 61.9%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.65

### Reasoning
Strong aggregate stat signal (n=13,967) shows markets at 58% YES resolve YES only 44.7% of time — suggesting ~13% edge on NO. However: (1) No cricket-specific data available via tools — injury reports, team form, bookmaker odds all inaccessible; (2) Gap metric (4%) is market-vs-base_rate, not market-vs-true_probability, so gate FAIL is misleading but actual edge exists; (3) Two prior SKIPs on same market with unresolved outcomes — no new information added; (4) News suggests RR dominant and LSG struggling, but cannot verify which team YES represents; (5) Base rate (62%) conflicts with stat signal (44.7%) — unclear which dominates in this specific matchup. Pattern shows 44.7% resolution at 58% pricing is robust, but without match-specific confirmation tools, cannot achieve 0.70+ confidence threshold. Would need injury/lineup data or bookmaker odds to convert statistical edge into actionable bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'nba', 'team': 'Rajasthan Royals Lucknow Super Giants'})` → No injury data found for nba Rajasthan Royals Lucknow Super Giants
- `get_market_context({'keyword': 'Rajasthan Royals Lucknow Super Giants IPL'})` → No related markets found for 'Rajasthan Royals Lucknow Super Giants IPL'
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants IPL 2025 recent form'})` → [Tue, 21 Apr 2026] Google News
[Tue, 03 Jun 2025] IPL 2026, LSG vs RR 32nd Match Match Preview - RR 
- `search_web({'query': 'Rajasthan Royals Lucknow Super Giants IPL 2026 head to head odds'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] RR vs LSG Playing 11: Check probable XIs, head-to-
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants April 2026 who will win'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] IPL 2026: Match 64, RR vs LSG Match Prediction – W
- `search_web({'query': '"Rajasthan Royals vs Lucknow Super Giants" IPL 2026 prediction odds betting'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Cricket matches today | List of best live fixtures
- `get_odds({'sport': 'soccer_epl'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'IPL cricket Rajasthan Lucknow'})` → No related markets found for 'IPL cricket Rajasthan Lucknow'
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants IPL 2025 match result who won'})` → [Thu, 09 Apr 2026] Google News
[Wed, 22 Apr 2026] Royal Challengers Bengaluru Royal Challengers Beng
- `search_web({'query': 'RR vs LSG IPL 2026 standings points table current form'})` → [Sun, 17 May 2026] Google News
[Tue, 28 Apr 2026] IPL 2026 playoffs: Qualified teams, standings and 
- `search_web({'query': 'Rajasthan Royals current form IPL 2026 wins losses'})` → [Sat, 16 May 2026] Google News
[Mon, 27 Apr 2026] Indian Premier League 2026 - Match 62 - Delhi Capi
- `search_web({'query': 'Lucknow Super Giants current form IPL 2026 wins losses'})` → [Sat, 16 May 2026] Google News
[Tue, 05 May 2026] How Chennai Super Kings Can Still Qualify For IPL 
- `search_web({'query': '"Rajasthan Royals" OR "Lucknow Super Giants" IPL 2026 April match winner prediction bookmaker odds'})` → [Fri, 10 Apr 2026] Google News
[Wed, 22 Apr 2026] RR vs RCB IPL 2026 16th Match Prediction &amp; Odd
- `get_market_context({'keyword': 'IPL winner Rajasthan'})` → No related markets found for 'IPL winner Rajasthan'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*