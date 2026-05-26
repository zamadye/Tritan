# Market Analysis — 2026-05-17 21:48 UTC

## Market
- **Question:** Will Arsenal win the 2025–26 English Premier League?
- **Category:** other
- **YES Price:** 83.0%
- **Days Left:** 9
- **Volume 24h:** $78,379
- **Liquidity:** $83,802

## Statistical Prior
- **p_base:** 64.8%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 18.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,379 (+0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,380 (+0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: arsenal 2025–26 english premier league
- [Bing News]
- [Sun, 17 May 2026] arsenal 2025–26 english premier league
- → Arsenal return to the Emirates for their final home match of the 2025/26 Premier League season as they host Burnley for a match with massive title s
- [Tue, 05 May 2026] Arsenal vs Burnley Premier League preview: The home finale
- → Manchester City were held to a 3‑3 draw by Everton in the English Premier League, leaving Pep Guardiola’s side five points behind leaders Arsenal wi
- [Fri, 17 Apr 2026] EPL 2025-26 Points Table: When Can Arsenal Win Premier League Title – Check State Of Play After Everton Vs Man City Draw
- → The English Premier League 2025-26 title race comes down to Arsenal’s visit to Manchester City at the Etihad on Sunday. Let’s analyse where the matc

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 64.8%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Market is in final 9 days with 2 games remaining; title race between Arsenal and Man City is near completion but outcome still uncertain. Market price (83%) appears fairly priced relative to available evidence. No concrete catalyst or direct evidence found to suggest edge. Low confidence due to lack of specific standings data and high volatility in final matches.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'Arsenal Premier League title 2025-26 season final games remaining fixtures'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Arsenal and Man City's remaining Premier League fi
- `search_web({'query': 'Arsenal injury news update 2025-26 Premier League title race'})` → [Sat, 16 May 2026] Google News
[Sun, 10 May 2026] What could be decided in Premier League in Matchwe
- `get_odds({'sport': 'soccer_epl', 'team': 'Arsenal'})` → [ODDS] soccer_epl — 1 events
  Arsenal vs Burnley (2026-05-18)
    [Betfred (UK)] Arsenal: 1.09 | Bu
- `get_market_context({'keyword': 'Arsenal Premier League'})` → No related markets found for 'Arsenal Premier League'
- `search_web({'query': 'Arsenal vs West Ham Premier League result May 2026'})` → [Sun, 17 May 2026] Google News
[Tue, 12 May 2026] How Arsenal or Man City can clinch Premier League 
- `search_web({'query': 'Premier League 2025-26 standings table May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Premier League 2025-26 table — Latest standings - 
- `search_web({'query': 'Arsenal points lead over Manchester City Premier League 2026 May'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Premier League permutations: When can the title, r
- `search_web({'query': 'Arsenal Premier League points lead 2026 remaining games'})` → [Sun, 17 May 2026] Google News
[Tue, 12 May 2026] Premier League permutations: When can the title, r
- `search_web({'query': '"Premier League permutations" Arsenal Manchester City title race May 2026'})` → [Sun, 17 May 2026] Google News
[Wed, 13 May 2026] Premier League permutations: When can the title, r
- `search_web({'query': 'site:sportingnews.com "When can Arsenal win the title" Premier League permutations May 2026'})` → [Wed, 13 May 2026] Google News
[Tue, 15 Mar 2022] When can Arsenal win the title? Premier League per

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*