# Market Analysis — 2026-05-21 15:35 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 7
- **Volume 24h:** $133,292
- **Liquidity:** $513,555

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,159 (-0.5% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,159 (-0.5% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- [SPORTS] Recent games:
- PIT @ STL | Scheduled | St. Louis Cardinals(home) 28-20 score:0 vs Pittsburgh Pirates(away) 25-24 score:0
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)

### Bing/Google News
- 6 articles found:
- [NewsAPI] Don Kelly Reveals What He Saw From Top Prospect In Pirates Debut: Pittsburgh's manager broke down Jhostynxon Garcia's first game for the Pir
- [NewsAPI] Pirates Are 'Likely Buyers' At Trade Deadline, MLB Insider Says: Tuesday's 9-6 loss to the St. Louis Cardinals was the fourth straight defea
- [NewsAPI] Top Prospect Excited For New Opportunity With Pirates: After making his MLB debut with the Red Sox last year, Jhostynxon Garcia is excited f
- [NewsAPI] Pirates 'Frustrated' With Loss Walk-Off Loss To Cardinals: Pittsburgh tied the game in the top of the ninth.
- [NewsAPI] Tigers fans show some skin for 'Tarps Off.' How did this all start?: Late in Tuesday night's game at Comerica Park, a small group of Tigers 
- [NewsAPI] Pirates bring 4-game losing streak into matchup against the Cardinals: Pittsburgh Pirates (24-24, fifth in the NL Central) vs. St. Louis Car
- [CAUSAL CHAINS] Relevant cause-effect patterns:

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: pittsburgh pirates louis cardinals
- [Bing News]
- [Thu, 21 May 2026] pittsburgh pirates louis cardinals
- → The St. Louis Cardinals look to win the series at home against the Pittsburgh Pirates on Thursday afternoon. The Cardinals won Game 1, 9-6, while th
- [Thu, 21 May 2026] Pirates vs. Cardinals prediction, odds, time: 2026 MLB picks for Thursday, May 21 from proven model
- → After ending a four-game skid Wednesday night, the Pittsburgh Pirates are now looking to take their midweek series against the Cardinals outright in
- [Thu, 21 May 2026] After ending losing skid, Pirates look to build on win against Cardinals
- → The Pittsburgh Pirates (24-24) are on their way to Busch Stadium on Thursday where they will attempt to beat the St. Louis Cardinals (28-19). The li

## LLM Decision
- **Action:** SKIP
- **Confidence:** 53%
- **p_true:** 51.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.40

### Reasoning
Stat signal indicates YES overpriced (51% market vs 44.7% historical, 6.3% edge), but: (1) base rate gap only +1% - below 5% gate threshold, (2) entry range 50-60% has poor 41% WR historically (n=17), (3) past decisions for same market both SKIP, (4) no verifiable catalyst found - injuries balanced (Pirates lose SP Jones, Cardinals lose OF Nootbaar), (5) no breaking news or matchup intel available. Crowd appears to overprice YES without justification, but insufficient direct evidence to act on the stat edge with confidence.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Nathan Church (LF): Day-To-Day
INJURY [st. louis cardinals] Ramon Urias
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals game preview May 2025'})` → [2026-05-01] Knicks set NBA records in eliminating Hawks; 76ers take Celtics to Game 7; Kentucky Der
- `search_web({'query': 'Pirates Cardinals May 2025 MLB starting pitchers'})` → [2026-05-18] 2026 MLB Power Rankings: Who Are The Standouts Who Need To Step Up? — It’s been a forge
- `get_market_context({'keyword': 'Pittsburgh Pirates'})` → No related markets found for 'Pittsburgh Pirates'
- `get_market_context({'keyword': 'St. Louis Cardinals'})` → No related markets found for 'St. Louis Cardinals'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pittsburgh Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*