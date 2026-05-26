# Market Analysis — 2026-05-17 21:02 UTC

## Market
- **Question:** Will Arsenal win the 2025–26 English Premier League?
- **Category:** other
- **YES Price:** 83.0%
- **Days Left:** 9
- **Volume 24h:** $77,977
- **Liquidity:** $68,230

## Statistical Prior
- **p_base:** 64.8%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 18.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,245 (+0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,249 (+0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%

### Bing/Google News
- 6 articles found:
- [NewsAPI] Brilliant Semenyo flick sees off Chelsea to win City an eighth FA Cup: A moment of magic from Antoine Semenyo was enough for City to beat Ch
- [NewsAPI] Rodri starts as City make five changes for FA Cup final: Men's Team How can I watch Chelsea v City on TV? The Spaniard will make his first a
- [NewsAPI] Chelsea vs Manchester City FA Cup Final 2026: Maresca's Blues Aim to Dethrone Gu: Chelsea and Manchester City clash in the 2026 FA Cup Final
- [NewsAPI] PREVIEW | Newcastle vs West Ham: team news, lineups, predictions (Premier League: Newcastle and West Ham go head-to-head at St. James' Park 
- [NewsAPI] Premier League Soccer: Stream Aston Villa vs. Liverpool From Anywhere Live: The Arsenal vs. Newcastle Premier League match is this weekend. 
- [NewsAPI] Pep Guardiola issues new hidden message towards English match officials amid lon: Manchester City dismantled Crystal Palace 3-0 on Wednesday
- [CAUSAL CHAINS] Relevant cause-effect patterns:

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: arsenal 2025–26 english premier league
- [Bing News]
- [Tue, 05 May 2026] arsenal 2025–26 english premier league
- → Manchester City were held to a 3‑3 draw by Everton in the English Premier League, leaving Pep Guardiola’s side five points behind leaders Arsenal wi
- [Sun, 17 May 2026] EPL 2025-26 Points Table: When Can Arsenal Win Premier League Title – Check State Of Play After Everton Vs Man City Draw
- → Sports Mole rounds up all of the latest injury and suspension news ahead of Monday's Premier League match between Arsenal and Burnley.
- [Sun, 19 Apr 2026] Team News: Arsenal vs. Burnley injury, suspension list, predicted XIs
- → Manchester City are closing in on the Premier League title after a clinical victory over Arsenal, propelled by a decisive strike from Erling Haaland

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 64.8%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market is in final 9 days with 2 games remaining; title race between Arsenal and Man City is near conclusion but exact point totals unavailable. Market price (83%) suggests strong but uncertain lead. Past analysis concluded market was fairly priced at 83% with similar evidence. Base rate (65%) vs market (83%) shows possible 18-point overpricing, but without concrete standings data, cannot verify edge. With 7829 predictors and late-season efficiency, crowd likely has better information. No verifiable catalyst or breaking news to justify position.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_odds({'sport': 'soccer_epl', 'team': 'Arsenal'})` → [ODDS] soccer_epl — 1 events
  Arsenal vs Burnley (2026-05-18)
    [Betfred (UK)] Arsenal: 1.09 | Bu
- `search_web({'query': 'Arsenal Premier League title race 2025-26 standings'})` → [Sun, 17 May 2026] Google News
[Mon, 20 Apr 2026] Premier League 2025-26 table — Latest standings - 
- `search_web({'query': 'Arsenal injuries April 2026 squad news'})` → [Sat, 04 Apr 2026] Google News
[Sun, 26 Apr 2026] Southampton vs Arsenal: TV channel, kick-off time,
- `search_web({'query': 'Arsenal points lead Premier League May 2026 title race'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] The earliest dates Arsenal or Man City could win t
- `search_web({'query': 'Manchester City remaining fixtures May 2026 Premier League'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Arsenal and Man City's remaining Premier League fi
- `search_web({'query': 'Premier League standings May 17 2026 Arsenal Manchester City points'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Premier League 2025-26 table — Latest standings - 
- `search_web({'query': 'Arsenal remaining two Premier League games May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] How Arsenal or Man City can clinch Premier League 
- `search_web({'query': '"Arsenal" "Manchester City" points "May 2026" Premier League'})` → [Sun, 17 May 2026] Google News
[Wed, 13 May 2026] How Arsenal or Man City can clinch Premier League 
- `search_web({'query': 'Arsenal 82 points Manchester City 80 points'})` → [Sun, 17 May 2026] Google News
[Tue, 05 May 2026] The earliest dates Arsenal or Man City could win t
- `search_web({'query': 'Premier League table 2025-26 latest standings points May 17'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Premier League 2025-26 table — Latest standings - 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*