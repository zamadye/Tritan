# Market Analysis — 2026-05-20 18:45 UTC

## Market
- **Question:** Baltimore Orioles vs. Tampa Bay Rays
- **Category:** sports
- **YES Price:** 50.5%
- **Days Left:** 6
- **Volume 24h:** $951,812
- **Liquidity:** $50,389

## Statistical Prior
- **p_base:** 50.7%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,439 (+0.9% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,439 (+0.9% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- [SPORTS] Recent games:
- BAL @ TB | In Progress | Tampa Bay Rays(home) 32-15 score:1 vs Baltimore Orioles(away) 21-28 score:3
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: baltimore orioles tampa rays
- [Bing News]
- [Wed, 20 May 2026] baltimore orioles tampa rays
- → Here's how to watch Wednesday's Tampa Bay Rays vs Baltimore Orioles game, including start times, TV channels, scores and how to stream.
- [Wed, 20 May 2026] Where to watch Baltimore Orioles vs Tampa Bay Rays: TV channel, start time, streaming for May 20
- → SportsLine's model simulated Baltimore Orioles vs. Tampa Bay Rays 10,000 times and revealed its MLB picks for Wednesday's matinee matchup ...
- [Wed, 20 May 2026] Orioles vs. Rays prediction, odds, time: 2026 MLB picks for Wednesday, May 20 from proven model
- → The Baltimore Orioles and Tampa Bay Rays close out their 3-game series in St. Petersburg, Florida, Wednesday at 1:10 p.m. ET.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 48.8%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.55

### Reasoning
Strong statistical edge identified: markets priced at exactly 50% historically resolve YES only 44.7% of the time (n=13,967), creating a 5.3% edge on NO. Pattern data confirms Entry 50-60% range has only 33% WR for YES bets. Injuries appear balanced (Orioles: SP Povich IL; Rays: DH Diaz DTD, RF Fraley IL). No information gap exists (gap=0%), meaning no asymmetric catalyst. The sports pattern's 83% overall WR is misleading - the specific 50-60% entry zone shows weak outcomes for YES. This is a mean-reversion statistical play rather than a catalyst-driven bet, limiting confidence to moderate level.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=0%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Baltimore Orioles'})` → INJURY [baltimore orioles] Levi Wells (P): Day-To-Day
INJURY [baltimore orioles] Cade Povich (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Tampa Bay Rays'})` → INJURY [tampa bay rays] Yandy Diaz (DH): Day-To-Day
INJURY [tampa bay rays] Ben Williamson (2B): 10-
- `search_web({'query': 'Baltimore Orioles vs Tampa Bay Rays 2025 recent results'})` → [Tue, 23 Sep 2025] Google News
[Thu, 25 Sep 2025] Tampa Bay Rays at Baltimore Orioles Game Story, Sc
- `search_web({'query': 'Orioles Rays series prediction MLB'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Orioles vs. Rays prediction, odds, time: 2026 MLB 
- `search_web({'query': 'Baltimore Orioles vs Tampa Bay Rays June 2025 MLB matchup'})` → [Mon, 18 May 2026] Google News
[Sat, 02 May 2026] Where to watch Baltimore Orioles vs Tampa Bay Rays
- `get_odds({'sport': 'baseball_mlb', 'team': 'Orioles'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Orioles Rays MLB'})` → No related markets found for 'Orioles Rays MLB'
- `search_web({'query': 'Orioles vs Rays 2025 MLB standings record'})` → [Mon, 18 May 2026] Google News
[Tue, 05 May 2026] MLB Power Rankings: Why disappointing teams seem t
- `search_web({'query': '"Orioles" "Rays" MLB June 2025 game'})` → [Sat, 28 Jun 2025] Google News
[Tue, 17 Jun 2025] Tampa Bay Rays at Baltimore Orioles Game Story, Sc
- `search_web({'query': 'Baltimore Orioles recent wins losses June 2025'})` → [Mon, 18 May 2026] Google News
[Sat, 09 Aug 2025] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Orioles Rays head to head 2025 season'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] Baltimore Orioles: Series Preview vs. Tampa Bay Ra

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*