# Market Analysis — 2026-05-21 17:13 UTC

## Market
- **Question:** Geneva Open: Alex Michelsen vs Learner Tien
- **Category:** sports
- **YES Price:** 24.0%
- **Days Left:** 6
- **Volume 24h:** $238,661
- **Liquidity:** $67,192

## Statistical Prior
- **p_base:** 15.1%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,163 (-0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,055 (-0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: geneva open: alex michelsen learner
- [Bing News]
- [Wed, 20 May 2026] geneva open: alex michelsen learner
- → Learner Tien's only victory over Alex Michelsen came at the 2024 Next Gen ATP Finals, a tournament with an accelerated format (sets to 4 games and t
- [Tue, 19 May 2026] Michelsen vs Tien • 1/4 final • Geneva 2026
- → We are even more excited to report that Learner Tien is playing doubles with Taylor Fritz this week at the Geneva Open than we were when Tien played
- [Thu, 21 May 2026] Learner Tien and Taylor Fritz win doubles match at Geneva Open
- → Alex Michelsen sends heartfelt message to Stan Wawrinka in Geneva. Michelsen said in his on-court interview: “Man, I mean, I could go on. “I watched

## LLM Decision
- **Action:** NO
- **Confidence:** 62%
- **p_true:** 11.1%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** PERFORMANCE_ANALYSIS
- **Catalyst Strength:** 0.60

### Reasoning
Market overprices Michelsen at 24% vs 15% base rate (-9% gap). Tien recently beat Tsitsipas (clay specialist) at this very tournament and is developing strong clay game under Chang. No evidence found justifying Michelsen's premium. NO shares (~76%) appear underpriced given Tien's superior form and surface suitability. Moderate confidence due to single-source confirmation of Tien's form advantage.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Michelsen'})` → No injury data found for tennis Michelsen
- `get_sports_data({'sport': 'tennis', 'team': 'Tien'})` → No injury data found for tennis Tien
- `get_odds({'sport': 'tennis_atp', 'team': 'Michelsen'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Geneva Open Michelsen Tien'})` → No related markets found for 'Geneva Open Michelsen Tien'
- `search_web({'query': 'Alex Michelsen vs Learner Tien Geneva Open 2025'})` → [Thu, 31 Jul 2025] Google News
[Sat, 18 Jan 2025] Alex Michelsen upsets Lorenzo Musetti in Toronto, 
- `search_web({'query': 'Alex Michelsen tennis ranking form 2025'})` → [Mon, 05 Jan 2026] Google News
[Sun, 21 Sep 2025] Ranking the best American tennis players as 2026 b
- `search_web({'query': 'Learner Tien tennis ranking form 2025'})` → [Fri, 16 Jan 2026] Google News
[Mon, 25 Aug 2025] Ranking the 2026 Australian Open top contenders - 
- `search_web({'query': 'Michelsen vs Tien head to head tennis'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Geneva QF previews and predictions: Tien vs. Miche
- `search_web({'query': 'Geneva Open 2025 draw tennis'})` → [Wed, 13 May 2026] Google News
[Thu, 21 Aug 2025] Gonet Geneva Open 2026: Draws, dates, history &amp
- `search_web({'query': 'Geneva Open 2025 Michelsen Tien quarterfinal'})` → [Thu, 21 May 2026] Google News
[Sun, 17 May 2026] Sports News, Transfers, Scores | Watch Live Sport 
- `search_web({'query': 'Alex Michelsen recent results clay court 2025'})` → [Tue, 05 May 2026] Google News
[Sat, 18 Oct 2025] Jannik Sinner: Rome draw, history, recent results 
- `search_web({'query': 'Learner Tien clay court results 2025'})` → [Wed, 20 May 2026] Google News
[Sun, 30 Nov 2025] Learner Tien sends Stefanos Tsitsipas tumbling out
- `search_web({'query': '"Michelsen" "Tien" tennis odds'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Alex Michelsen vs. Learner Tien prediction, odds, 
- `search_web({'query': 'dimers.com Michelsen Tien prediction odds Geneva 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Alex Michelsen vs. Learner Tien prediction, odds, 
- `search_web({'query': 'Tennis.com Learner Tien Geneva clay 2026'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] Learner Tien sends Stefanos Tsitsipas tumbling out
- `search_web({'query': 'Grandstand Geneva QF Tien Michelsen preview prediction'})` → [Thu, 21 May 2026] Google News
[Sat, 14 Mar 2026] Geneva QF previews and predictions: Tien vs. Miche
- `search_web({'query': 'Learner Tien beats Tsitsipas Geneva 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Highlights: Tien downs Tsitsipas, reaches fifth QF

## Outcome
**✅ WIN** | P&L: $+0.32 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*