# Market Analysis — 2026-05-21 19:01 UTC

## Market
- **Question:** Toronto Blue Jays vs. New York Yankees
- **Category:** sports
- **YES Price:** 44.0%
- **Days Left:** 7
- **Volume 24h:** $167,535
- **Liquidity:** $594,218

## Statistical Prior
- **p_base:** 41.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,462 (+0.1% 24h) → neutral
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
- → The Toronto Blue Jays shared news regarding the pitching rotation ahead of a matchup against the New York Yankees on Thursday, May 21.
- [Thu, 21 May 2026] Blue Jays Announce Pitching Plans for Game Against Yankees
- → Trey Yesavage outpitched Cam Schlittler in a marquee matchup between young aces, and the Toronto Blue Jays edged the New York Yankees 2-1 on Wednesd
- [Thu, 21 May 2026] Trey Yesavage outduels Cam Schlittler in marquee matchup as Blue Jays top Yankees 2-1
- → The Toronto Blue Jays, ranked third in the AL East with a 22-27 record, face the New York Yankees, who are second in the AL East with a 30-20 record

## LLM Decision
- **Action:** SKIP
- **Confidence:** 40%
- **p_true:** 41.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Injuries cancel out (Blue Jays: Bieber/Berrios; Yankees: Cole). Gap only 3% (<5% threshold). No new information or catalyst. Historical base rate 41% vs market 44% suggests slight overpricing but not enough for concrete edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Toronto Blue Jays'})` → INJURY [toronto blue jays] Jesus Sanchez (RF): Day-To-Day
INJURY [toronto blue jays] Shane Bieber (S
- `get_sports_data({'sport': 'mlb', 'team': 'New York Yankees'})` → INJURY [new york yankees] Trent Grisham (CF): Day-To-Day
INJURY [new york yankees] Jasson Dominguez 
- `search_web({'query': 'Toronto Blue Jays injury update April 2025'})` → [Tue, 19 May 2026] Google News
[Thu, 26 Mar 2026] Blue Jays Announce Alejandro Kirk News Before Yank
- `search_web({'query': 'New York Yankees injury report April 2025'})` → [Thu, 11 Dec 2025] Google News
[Wed, 18 Feb 2026] Yankees injuries: Latest on Gerrit Cole, Giancarlo
- `get_market_context({'keyword': 'Blue Jays Yankees'})` → No related markets found for 'Blue Jays Yankees'
- `get_market_context({'keyword': 'MLB'})` → No related markets found for 'MLB'
- `search_web({'query': 'Blue Jays vs Yankees series April 2025 pitching matchup'})` → [Sat, 04 Oct 2025] Google News
[Tue, 28 Oct 2025] Yankees-Blue Jays schedule, pitching matchups and 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*