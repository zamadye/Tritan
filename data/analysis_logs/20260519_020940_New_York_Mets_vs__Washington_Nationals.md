# Market Analysis — 2026-05-19 02:09 UTC

## Market
- **Question:** New York Mets vs. Washington Nationals
- **Category:** sports
- **YES Price:** 17.0%
- **Days Left:** 6
- **Volume 24h:** $583,211
- **Liquidity:** $19,575

## Statistical Prior
- **p_base:** 8.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,634 (-0.6% 24h) → neutral
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
- → Follow along as the Nats kick off a crucial four game home set against the Mets ...
- [Mon, 18 May 2026] Washington Nationals vs New York Mets game thread
- → The New York Mets announced multiple roster moves on Monday ahead of their game against the Washington Nationals.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 8.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market at 17% YES is overpriced vs 8% base rate (-9% gap in wrong direction for YES bet). Season is over, no catalyst found to justify overpricing. Cannot determine what specific event this market resolves on. Past similar markets were also skipped. Pattern suggests 10-20% entries work when UNDERPRICED, but here market is OVERPRICED. No verifiable edge exists.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Mets'})` → INJURY [new york mets] A.J. Minter (RP): 60-Day-IL
INJURY [new york mets] Mike Tauchman (RF): Day-To
- `get_sports_data({'sport': 'mlb', 'team': 'Nationals'})` → INJURY [washington nationals] Jacob Young (CF): Day-To-Day
INJURY [washington nationals] Clayton Bee
- `search_web({'query': 'New York Mets recent game results 2025'})` → [Fri, 29 Aug 2025] Google News
[Fri, 12 Sep 2025] Miami Marlins at New York Mets Game Story, Scores/
- `search_web({'query': 'Washington Nationals recent performance 2025'})` → [Sun, 21 Sep 2025] Google News
[Mon, 13 Oct 2025] Jacob Young's stupendous defensive performance | 0
- `get_market_context({'keyword': 'New York Mets vs Washington Nationals'})` → No related markets found for 'New York Mets vs Washington Nationals'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Mets'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb', 'team': 'Nationals'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Mets vs Nationals MLB odds today 2025'})` → [Sun, 21 Sep 2025] Google News
[Sat, 20 Sep 2025] Mets vs. Nationals Prediction, Odds, Picks - Septe
- `search_web({'query': 'New York Mets vs Washington Nationals prediction analysis'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Mets vs. Nationals Prediction, Odds, &amp; Expert 
- `search_web({'query': 'Mets vs Nationals November 2025 MLB game'})` → [Sat, 02 May 2026] Google News
[Thu, 06 Nov 2025] Washington Nationals News &amp; Analysis: National
- `search_web({'query': 'MLB schedule November 2025 playoffs'})` → [Sun, 02 Nov 2025] Google News
[Tue, 11 Nov 2025] 2025 World Series: Analysis, results from Dodgers'
- `search_web({'query': 'Polymarket Mets vs Nationals prediction market'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Polymarket Promo Code CUSE launches $50 Memorial D
- `search_web({'query': 'baseball prediction market November 2025'})` → [Thu, 19 Mar 2026] Google News
[Thu, 26 Mar 2026] Major League Baseball names Polymarket exclusive p
- `search_web({'query': 'Mets vs Nationals 2026 opening day MLB'})` → [Sun, 17 May 2026] Google News
[Thu, 19 Mar 2026] New York Mets at Washington Nationals Preview - 05
- `search_web({'query': '"New York Mets" "Washington Nationals" November 2025 schedule'})` → [Sat, 02 May 2026] Google News
[Fri, 06 Feb 2026] Washington Nationals News &amp; Analysis: National

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*