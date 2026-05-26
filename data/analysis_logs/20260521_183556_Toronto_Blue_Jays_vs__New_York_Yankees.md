# Market Analysis — 2026-05-21 18:35 UTC

## Market
- **Question:** Toronto Blue Jays vs. New York Yankees
- **Category:** sports
- **YES Price:** 44.0%
- **Days Left:** 7
- **Volume 24h:** $166,503
- **Liquidity:** $583,171

## Statistical Prior
- **p_base:** 41.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,751 (+0.4% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,709 (+0.4% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%
- [SPORTS] Recent games:
- NYM @ WSH | Scheduled | Washington Nationals(home) 25-25 score:0 vs New York Mets(away) 21-28 score:0
- TOR @ NYY | Scheduled | New York Yankees(home) 30-20 score:0 vs Toronto Blue Jays(away) 22-27 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: toronto blue jays york yankees
- [Bing News]
- [Thu, 21 May 2026] toronto blue jays york yankees
- → Trey Yesavage outpitched Cam Schlittler in a marquee matchup between young aces, and the Toronto Blue Jays edged the New York Yankees 2-1 on Wednesd
- [Thu, 21 May 2026] Trey Yesavage outduels Cam Schlittler in marquee matchup as Blue Jays top Yankees 2-1
- → The Toronto Blue Jays, ranked third in the AL East with a 22-27 record, face the New York Yankees, who are second in the AL East with a 30-20 record
- [Thu, 21 May 2026] How to watch Toronto Blue Jays vs New York Yankees
- → The Toronto Blue Jays shared news regarding the pitching rotation ahead of a matchup against the New York Yankees on Thursday, May 21.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 41.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Both teams have significant injuries (Blue Jays: Bieber + Berrios out; Yankees: Cole out), making the matchup balanced. Information gap is small at 3%. No bookmaker odds available for cross-verification, no breaking news or clear catalyst, and weak pattern evidence (50% WR from only 4 trades in this price range). No actionable edge identified.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Blue Jays'})` → INJURY [toronto blue jays] Jesus Sanchez (RF): Day-To-Day
INJURY [toronto blue jays] Shane Bieber (S
- `get_sports_data({'sport': 'mlb', 'team': 'Yankees'})` → INJURY [new york yankees] Trent Grisham (CF): Day-To-Day
INJURY [new york yankees] Jasson Dominguez 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Blue Jays'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb', 'team': 'Yankees'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Toronto Blue Jays vs New York Yankees matchup 2025 preview'})` → [Mon, 18 May 2026] Google News
[Thu, 29 Jan 2026] Yankees vs. Blue Jays: Series preview, probable pi
- `search_web({'query': 'Yankees vs Blue Jays who will win series 2025'})` → [Thu, 09 Oct 2025] Google News
[Fri, 03 Oct 2025] Blue Jays prove they're top dog, clinch ALCS berth
- `get_market_context({'keyword': 'Blue Jays Yankees'})` → No related markets found for 'Blue Jays Yankees'
- `search_web({'query': 'Toronto Blue Jays injury report May 2025'})` → [Tue, 26 Aug 2025] Google News
[Tue, 26 Aug 2025] Blue Jays Receive Discouraging Update on Veteran R
- `search_web({'query': 'New York Yankees injury report May 2025'})` → [Sun, 08 Mar 2026] Google News
[Tue, 22 Jul 2025] Yankees Get Encouraging Injury Update From Anthony

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*