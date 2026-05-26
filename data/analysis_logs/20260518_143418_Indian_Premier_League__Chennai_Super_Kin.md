# Market Analysis — 2026-05-18 14:34 UTC

## Market
- **Question:** Indian Premier League: Chennai Super Kings vs Sunrisers Hyderabad
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $305,963
- **Liquidity:** $68,653

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,630 (-1.7% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,630 (-1.7% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Injuries:
- ?: Keshon Gilbert — Out (Surgery)
- ?: Jock Landale — Out (Sprain)
- ?: Jayson Tatum — Out (Soreness)
- ?: Nolan Traore — Out (Not Specified)
- ?: Nic Claxton — Out (Sprain)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: indian premier league: chennai super
- [Bing News]
- [Mon, 18 May 2026] indian premier league: chennai super
- → The 63rd game of the ongoing IPL (Indian Premier League) 2026 sees Chennai Super Kings taking on Sunrisers Hyderabad. The two sides will meet at the
- [Mon, 18 May 2026] CSK vs SRH LIVE cricket score: Chennai Super Kings aim to keep playoffs race alive
- → Chennai Super Kings have 12 points from 12 games, while SunRisers Hyderabad have 14 points from 12 matches and must win to strengthen their playoff 
- [Mon, 18 May 2026] CSK Vs SRH Live Cricket Score, IPL 2026: Urvil Takes On Cummins In Powerplay | Chennai 43/1 (3)
- → CSK vs SRH Live: The business end of the Indian Premier League 2026 has officially arrived at the MA Chidambaram Stadium as the Chennai Super Kings 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 56.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NEGATIVE_INJURY_NEWS
- **Catalyst Strength:** 0.55

### Reasoning
MS Dhoni confirmed NOT playing (Gaikwad at toss: 'Dhoni is not fit enough') - major negative for CSK. However, stat signal shows market at 54% overprices YES (historical resolution only 44.7%, n=13,967). Gap of +2% (54% market vs 56% base) is below 5% threshold required for bet. Previous identical CSK vs SRH markets were SKIPped for same reason. Entry range 50-60% has terrible 25% WR (4 trades). While crowd bias exists (overpricing CSK), no actionable edge meets threshold - the negative Dhoni catalyst may already be reflected in the 2% discount to base rate. WAIT for better entry or clearer edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'nba'})` → INJURY [atlanta hawks] Keshon Gilbert (G): Out
INJURY [atlanta hawks] Jock Landale (C): Out
INJURY [
- `get_odds({'sport': 'soccer_epl'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Chennai Super Kings vs Sunrisers Hyderabad IPL 2024 2025 match preview odds'})` → [Mon, 18 May 2026] Google News
[Sat, 18 Apr 2026] CSK vs SRH Match 63 Dream11 Prediction IPL 2026 (1
- `search_web({'query': 'CSK vs SRH injury report team news IPL'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Why is MS Dhoni Not Playing in CSK vs SRH IPL 2026
- `get_market_context({'keyword': 'IPL Chennai Sunrisers cricket'})` → No related markets found for 'IPL Chennai Sunrisers cricket'
- `search_web({'query': 'MS Dhoni CSK SRH IPL 2026 injury status playing or not'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] MS Dhoni to turn up for CSK's game in Chennai, but
- `search_web({'query': 'Chennai Super Kings vs Sunrisers Hyderabad IPL 2026 winner prediction odds today'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] CSK vs SRH live win probability, prediction, odds 
- `search_web({'query': '"MS Dhoni" CSK IPL 2026 "not playing" OR "injured" OR "out" match 63'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Why is MS Dhoni Not Playing in CSK vs SRH IPL 2026
- `search_web({'query': 'Chennai Super Kings IPL 2026 standings form last 5 matches'})` → [Mon, 04 May 2026] Google News
[Thu, 14 May 2026] IPL 2026 playoffs: Qualified teams, standings and 
- `search_web({'query': 'CSK vs SRH IPL 2026 Match 63 pitch report team news playing XI'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] CSK vs SRH Dream11: Lineups, pitch report and scor
- `search_web({'query': 'Sunrisers Hyderabad IPL 2026 form standings recent results'})` → [Sun, 17 May 2026] Google News
[Sat, 25 Apr 2026] IPL 2026 playoffs: Qualified teams, standings and 
- `search_web({'query': '"MS Dhoni" CSK "not playing" "Sunrisers" 2026 why reason'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] MS Dhoni Ruled Out Again? Fresh Injury Update Shoc
- `search_web({'query': 'CSK vs SRH head to head record IPL history wins losses'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] CSK vs SRH Head-to-Head In IPL (2026 Stats &amp; R
- `search_web({'query': 'Chennai Super Kings IPL 2026 playoffs qualification scenario do or die'})` → [Mon, 18 May 2026] Google News
[Thu, 14 May 2026] IPL 2026 playoff scenario: MI, LSG eliminated - ho
- `search_web({'query': 'Sunrisers Hyderabad IPL 2026 playoffs qualified eliminated status'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] IPL 2026 playoffs: Qualified teams, standings and 
- `search_web({'query': 'CSK SRH IPL 2026 match 63 who will win prediction May 18'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] IPL 2026: Match 63, CSK vs SRH Match Prediction – 
- `search_web({'query': 'Ruturaj Gaikwad MS Dhoni injury update CSK captain'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Why is MS Dhoni Not Playing in CSK vs SRH IPL 2026

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*