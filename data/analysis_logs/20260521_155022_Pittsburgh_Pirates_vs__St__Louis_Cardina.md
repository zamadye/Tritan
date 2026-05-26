# Market Analysis — 2026-05-21 15:50 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 52.0%
- **Days Left:** 7
- **Volume 24h:** $153,614
- **Liquidity:** $504,153

## Statistical Prior
- **p_base:** 53.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,206 (-0.3% 24h) → neutral
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
- → Here's how to watch Thursday's St. Louis Cardinals vs Pittsburgh Pirates game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 53.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Base rate gap only 1% (below 5% threshold). Stat signal shows YES overpriced (52% market vs 44.7% historical = 7.3% edge for NO), but: (1) no concrete catalyst found, (2) this exact market already skipped twice for same reason, (3) entry at 50-60% has poor 41% win rate historically, (4) no bookmaker odds or related markets available to confirm edge. Without verifiable catalyst or strong information asymmetry, this is a SKIP.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Jared Jones (SP): 60-Day-IL
INJURY [pittsburgh pirates] Ryan O'Hearn (RF
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Nathan Church (LF): Day-To-Day
INJURY [st. louis cardinals] Ramon Urias
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Pittsburgh Pirates St. Louis Cardinals'})` → No related markets found for 'Pittsburgh Pirates St. Louis Cardinals'
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals May 2025 series preview'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Pirates vs. Cardinals prediction, odds, time: 2026
- `search_web({'query': 'Pittsburgh Pirates starting pitcher lineup today May 2025'})` → [Thu, 02 Apr 2026] Google News
[Fri, 16 Jan 2026] Pirates Reveal Starting Pitcher for Home Opener - 
- `search_web({'query': 'Pirates Cardinals odds today May 2025 MLB'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Pirates vs. Cardinals prediction, odds, time: 2026
- `search_web({'query': 'MLB schedule Pirates Cardinals 2025'})` → [Thu, 28 Aug 2025] Google News
[Tue, 05 May 2026] Pittsburgh Pirates at St. Louis Cardinals Preview 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*