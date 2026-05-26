# Market Analysis — 2026-05-18 14:09 UTC

## Market
- **Question:** Toronto Blue Jays vs. New York Yankees
- **Category:** sports
- **YES Price:** 36.0%
- **Days Left:** 7
- **Volume 24h:** $196,848
- **Liquidity:** $262,150

## Statistical Prior
- **p_base:** 29.7%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 6.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,915 (-1.6% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,819 (-1.6% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Recent games:
- NYY @ NYM | Final | New York Mets(home) 20-26 score:7 vs New York Yankees(away) 28-19 score:6
- TOR @ DET | Final | Detroit Tigers(home) 20-27 score:1 vs Toronto Blue Jays(away) 21-25 score:4
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: toronto blue jays york yankees
- [Bing News]
- [Mon, 18 May 2026] toronto blue jays york yankees
- → Ahead of the four-game series against the Yankees, Blue Jays players resolved to focus on the here and now rather than anything that happened in 202
- [Mon, 18 May 2026] ALDS win 'in the past' as Blue Jays face Yankees again
- → After breaking out of a slump on Sunday, Vladimir Guerrero Jr. headlines our Blue Jays vs. Yankees predictions and MLB picks on Monday, May 18.
- [Mon, 18 May 2026] Blue Jays vs Yankees Prediction, Odds &amp; Home Run Pick for Today's MLB Game
- → Last summer, the Toronto Blue Jays outplayed the New York Yankees and won the American League East via the head-to-head tiebreaker.

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 25.7%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.60

### Reasoning
Market prices YES at 36% while historical base rate from n=6077 games is 30%. The 6% gap suggests overpricing. Past pattern shows trades in 30-40% range have only 33% win rate. Both teams have significant injuries, but historical data remains the strongest signal.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Blue Jays'})` → INJURY [toronto blue jays] Tommy Nance (RP): 15-Day-IL
INJURY [toronto blue jays] Jose Berrios (SP):
- `get_sports_data({'sport': 'mlb', 'team': 'Yankees'})` → INJURY [new york yankees] Jasson Dominguez (LF): 10-Day-IL
INJURY [new york yankees] Giancarlo Stant
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Blue Jays vs Yankees series 2025 April'})` → [Mon, 13 Oct 2025] Google News
[Sat, 04 Oct 2025] Yankees vs. Blue Jays: Series Preview, How to Watc
- `search_web({'query': 'Toronto Blue Jays recent results'})` → [Mon, 18 May 2026] Google News
[Sat, 16 May 2026] Where to watch Toronto Blue Jays vs New York Yanke
- `get_market_context({'keyword': 'Blue Jays Yankees'})` → No related markets found for 'Blue Jays Yankees'
- `search_web({'query': 'New York Yankees recent performance October 2025'})` → [Wed, 08 Oct 2025] Google News
[Thu, 02 Oct 2025] Yankees' Aaron Judge meets his October moment at l
- `search_web({'query': 'Toronto Blue Jays win probability October 2025'})` → [Fri, 31 Oct 2025] Google News
[Wed, 22 Oct 2025] Dodgers vs. Blue Jays World Series Game 6 Predicti
- `search_web({'query': 'Yankees Blue Jays ALDS Game 4 starting pitchers'})` → [Wed, 08 Oct 2025] Google News
[Sat, 04 Oct 2025] LIVE: Blue Jays-Yankees ALDS Game 4 (FS1) - MLB.co
- `search_web({'query': '"Yankees vs Blue Jays" "Game 4" starting pitcher October 2025'})` → [Wed, 08 Oct 2025] Google News
[Sat, 04 Oct 2025] How to Watch Yankees vs. Blue Jays ALDS Game 4 - O

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*