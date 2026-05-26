# Market Analysis — 2026-05-19 11:17 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $89,219
- **Liquidity:** $515,256

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,934 (+0.3% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,707 (-0.2% 24h) → neutral

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
- **Confidence:** 65%
- **p_true:** 50.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.75

### Reasoning
Statistical signal (n=13,967) shows markets at 57% YES resolve YES only 44.7% of the time - clear ~12% edge favoring NO. Despite RR being home favorites with Jadeja returning and LSG on a 6-match losing streak, the crowd consistently overprices favorites in this price range. The market at 57% is overpriced by ~12 points versus historical resolution rates. Prior SKIP decisions lacked this stat edge justification - now we have strong quantitative evidence. However, confidence tempered by (1) entry 50-60% pattern showing only 33% WR historically and (2) conflicting fundamentals supporting RR at home.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'cricket', 'team': 'Rajasthan Royals'})` → No injury data found for cricket Rajasthan Royals
- `get_sports_data({'sport': 'cricket', 'team': 'Lucknow Super Giants'})` → No injury data found for cricket Lucknow Super Giants
- `search_web({'query': 'IPL 2025 Rajasthan Royals vs Lucknow Super Giants match preview'})` → [Mon, 18 May 2026] Google News
[Sun, 10 May 2026] IPL 2026, RR vs LSG 64th Match Match Preview - RR 
- `search_web({'query': 'Rajasthan Royals Lucknow Super Giants head to head recent form 2025'})` → [Fri, 15 May 2026] Google News
[Wed, 01 Apr 2026] CSK vs LSG Head To Head Records In IPL (2026 Updat
- `get_market_context({'keyword': 'IPL Rajasthan Lucknow'})` → No related markets found for 'IPL Rajasthan Lucknow'
- `search_web({'query': 'Rajasthan Royals current form IPL 2026 wins losses'})` → [Sat, 16 May 2026] Google News
[Mon, 27 Apr 2026] Indian Premier League 2026 - Match 62 - Delhi Capi
- `search_web({'query': 'Lucknow Super Giants current form IPL 2026 wins losses'})` → [Sat, 16 May 2026] Google News
[Tue, 05 May 2026] How Chennai Super Kings Can Still Qualify For IPL 
- `search_web({'query': '"Rajasthan Royals vs Lucknow Super Giants" IPL 2026 match prediction May'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] RR vs LSG IPL 2026 Playing 11 Today Match: Ravindr
- `search_web({'query': 'IPL 2026 points table standings current'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] IPL 2026 playoffs: Qualified teams, standings and 
- `search_web({'query': 'Rajasthan Royals team news injuries IPL May 2026'})` → [Tue, 19 May 2026] Google News
[Fri, 15 May 2026] RR vs LSG Injury News: Is Ravindra Jadeja Playing 
- `search_web({'query': 'Lucknow Super Giants team news injuries IPL May 2026'})` → No search results for: Lucknow Super Giants team news injuries IPL May 2026
- `search_web({'query': 'RR vs LSG today match prediction who will win May 19 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] RR Vs LSG Match Facts, IPL 2026: All You Need To K
- `get_odds({'sport': 'cricket', 'team': 'Rajasthan Royals'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*