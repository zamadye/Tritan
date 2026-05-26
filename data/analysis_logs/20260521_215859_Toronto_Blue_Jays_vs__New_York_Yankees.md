# Market Analysis — 2026-05-21 21:58 UTC

## Market
- **Question:** Toronto Blue Jays vs. New York Yankees
- **Category:** sports
- **YES Price:** 44.0%
- **Days Left:** 7
- **Volume 24h:** $200,240
- **Liquidity:** $561,825

## Statistical Prior
- **p_base:** 41.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,596 (+0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,711 (+0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- [SPORTS] Recent games:
- NYM @ WSH | In Progress | Washington Nationals(home) 25-25 score:1 vs New York Mets(away) 21-28 score:2
- TOR @ NYY | Scheduled | New York Yankees(home) 30-20 score:0 vs Toronto Blue Jays(away) 22-27 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Spencer Giesting — Day-To-Day (Not Specified)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: toronto blue jays york yankees
- [Bing News]
- [Thu, 21 May 2026] toronto blue jays york yankees
- → Ahead of the Yankees’ matchup against the Blue Jays, Judge announced a new partnership with David Seeds on his Instagram page. The collaboration int
- [Thu, 21 May 2026] Yankees' Aaron Judge Announces New Partnership Before Blue Jays Game
- → New York Yankees outfielder Trent Grisham shared a positive injury update after leaving Wednesday’s game against the Toronto Blue Jays with knee dis
- [Thu, 21 May 2026] NY Yankees’ Trent Grisham provides encouraging injury update after scare vs Blue Jays
- → Toronto Blue Jays (22-27, third in the AL East) vs. New York Yankees (30-20, second in the AL East) New York; Thursday, 7:05 p.m. EDT. PITCHING PROB

## LLM Decision
- **Action:** SKIP
- **Confidence:** 42%
- **p_true:** 41.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market gap of 3% (44% vs 41% base) falls below the 5% statistical threshold required for a actionable edge. Both teams have significant pitching injuries (Yankees missing Cole, Blue Jays missing Berrios/Bieber) that roughly offset each other. No breaking news, lineup announcements, or recent form data suggest mispricing. Previous two evaluations on identical market correctly resulted in SKIP.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Blue Jays'})` → INJURY [toronto blue jays] Jesus Sanchez (RF): Day-To-Day
INJURY [toronto blue jays] Shane Bieber (S
- `get_sports_data({'sport': 'mlb', 'team': 'Yankees'})` → INJURY [new york yankees] Trent Grisham (CF): Day-To-Day
INJURY [new york yankees] Jasson Dominguez 
- `search_web({'query': 'Toronto Blue Jays vs New York Yankees April 2025 series preview'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] Toronto Blue Jays vs. New York Yankees prediction,
- `search_web({'query': 'Blue Jays Yankees injury update rotation April 2025'})` → [Thu, 21 May 2026] Google News
[Mon, 18 May 2026] MLB 2026 Buzz: Mariners’ J.P. Crawford Open To Mov
- `get_market_context({'keyword': 'Blue Jays Yankees'})` → No related markets found for 'Blue Jays Yankees'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*