# Market Analysis — 2026-05-19 02:22 UTC

## Market
- **Question:** New York Mets vs. Washington Nationals
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 6
- **Volume 24h:** $617,325
- **Liquidity:** $50,293

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,710 (-0.4% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,688 (-0.5% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Recent games:
- NYM @ WSH | In Progress | Washington Nationals(home) 23-24 score:5 vs New York Mets(away) 20-26 score:5
- TOR @ NYY | In Progress | New York Yankees(home) 28-19 score:7 vs Toronto Blue Jays(away) 21-25 score:5
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Pavin Smith — 60-Day-IL (Surgery)

### Bing/Google News
- 6 articles found:
- [NewsAPI] Carlos Mendoza proud to see Mets 'fight back' against Yankees: 'It's just a good: After the Mets big comeback win over the Yankees, Carlos M
- [NewsAPI] Gunnar Henderson hits 10th HR for 1st of 4 hits in Orioles' 7-3 win over Nationa: Gunnar Henderson hit his 10th homer and was 4 for 5 with t
- [NewsAPI] Sánchez’s 29 2/3-inning scoreless streak rolls as Phillies beat Pirates 6-0: Cristopher Sánchez struck out a career-high 13 while picking up
- [NewsAPI] Where do the Mets go next without Clay Holmes?: NEW YORK — Down by two in the bottom of the seventh after a Juan Soto home run, the Mets had
- [NewsAPI] MLB Rumors: Insider Addresses if New York Mets Plan to Sell at Trade Deadline: The New York Mets have been one of the worst teams in basebal
- [NewsAPI] Weekend Time Schedule: Chicago Cubs at Chicago White Sox, 7:10 p.m. Milwaukee at Minnesota, 7:10 p.m. San Diego at Seattle,
- [CAUSAL CHAINS] Relevant cause-effect patterns:

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: york mets washington nationals
- [Bing News]
- [Mon, 18 May 2026] york mets washington nationals
- → Follow our live updates as the New York Mets look to win their third straight game on Monday against the Nationals.
- [Mon, 18 May 2026] NY Mets vs Nationals live updates, score and analysis of today's game
- → The New York Mets announced multiple roster moves on Monday ahead of their game against the Washington Nationals.
- [Mon, 18 May 2026] Mets announce multiple roster moves before Nationals clash
- → Follow along as the Nats kick off a crucial four game home set against the Mets ...

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 45.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.65

### Reasoning
Stat signal shows markets at 51% YES historically resolve YES only 44.7% (n=13,967), indicating ~6.3% edge for NO. Market overprices YES. No current catalyst found through news search, but the historical pattern is significant. Injury data shows balanced absences for both teams, no clear advantage. News indicates Mets are in playoff contention (motivation) but this doesn't override the strong statistical edge favoring NO.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'New York Mets'})` → INJURY [new york mets] A.J. Minter (RP): 60-Day-IL
INJURY [new york mets] Mike Tauchman (RF): Day-To
- `get_sports_data({'sport': 'mlb', 'team': 'Washington Nationals'})` → INJURY [washington nationals] Jacob Young (CF): Day-To-Day
INJURY [washington nationals] Clayton Bee
- `search_web({'query': 'New York Mets vs Washington Nationals 2025'})` → [Sat, 20 Sep 2025] Google News
[Sat, 16 May 2026] Washington Nationals at New York Mets Game Story, 
- `search_web({'query': 'Mets Nationals series 2025'})` → [Thu, 21 Aug 2025] Google News
[Fri, 19 Sep 2025] Mets reverse momentum, head to Atlanta clinging to
- `get_market_context({'keyword': 'Mets Nationals'})` → No related markets found for 'Mets Nationals'
- `get_market_context({'keyword': 'MLB playoffs'})` → No related markets found for 'MLB playoffs'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Mets'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*