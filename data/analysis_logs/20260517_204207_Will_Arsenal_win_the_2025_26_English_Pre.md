# Market Analysis — 2026-05-17 20:42 UTC

## Market
- **Question:** Will Arsenal win the 2025–26 English Premier League?
- **Category:** other
- **YES Price:** 83.0%
- **Days Left:** 9
- **Volume 24h:** $77,976
- **Liquidity:** $69,555

## Statistical Prior
- **p_base:** 64.8%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 18.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,297 (+0.1% 24h) → neutral
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
- [Sun, 17 May 2026] arsenal 2025–26 english premier league
- → Arsenal return to the Emirates for their final home match of the 2025/26 Premier League season as they host Burnley for a match with massive title s
- [Tue, 05 May 2026] Arsenal vs Burnley Premier League preview: The home finale
- → Manchester City were held to a 3‑3 draw by Everton in the English Premier League, leaving Pep Guardiola’s side five points behind leaders Arsenal wi
- [Fri, 24 Apr 2026] EPL 2025-26 Points Table: When Can Arsenal Win Premier League Title – Check State Of Play After Everton Vs Man City Draw
- → The Gunners sit second in the table and have lost back‑to‑back league games Find out when and where to watch the Arsenal vs Newcastle match live on 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 64.8%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Market price (83%) appears fairly priced relative to available evidence. Arsenal is 91% favorite in final match vs Burnley (May 18), and the title race with Man City is ongoing with 9 days left. However, I cannot determine exact current standings or points gap - the April 22 article showed Man City had seized the lead. Without knowing if Arsenal needs just a win or other results, I cannot identify a clear information edge. The -18% gap suggests market is overpriced vs base rate, but without direct evidence of Arsenal's position, this may be rational pricing. No verifiable catalyst to exploit.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_sports_data({'sport': 'soccer', 'team': 'Arsenal'})` → No injury data found for soccer Arsenal
- `get_odds({'sport': 'soccer_epl', 'team': 'Arsenal'})` → [ODDS] soccer_epl — 1 events
  Arsenal vs Burnley (2026-05-18)
    [Betfred (UK)] Arsenal: 1.09 | Bu
- `search_web({'query': 'Arsenal 2025-26 Premier League title odds'})` → [2026-05-15] Chelsea v Manchester City: Preview, predicted line-ups and where to watch FA Cup final 
- `search_web({'query': 'Arsenal Premier League champions 2026'})` → [2026-05-16] Xabi Alonso to Chelsea? Ex-Real Madrid boss nearing deal, per reports — Chelsea has fir
- `search_web({'query': 'Premier League 2025-26 title race standings table May 2026'})` → [2026-05-12] Premier League standings 2026: Arsenal and Manchester City fight to finish — Manchester
- `search_web({'query': '"Arsenal" "Manchester City" title race 2026 Premier League'})` → [2026-05-16] Chelsea vs Manchester City: Line-ups confirmed for FA Cup final — Catch up with all the
- `search_web({'query': 'Premier League 2025-26 standings table current May 17 2026'})` → [2026-04-18] Ballon d'Or rankings 2026: Top candidates, potential award winners with Harry Kane, Lam

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*