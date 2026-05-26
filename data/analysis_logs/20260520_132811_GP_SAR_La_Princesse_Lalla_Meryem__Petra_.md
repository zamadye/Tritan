# Market Analysis — 2026-05-20 13:28 UTC

## Market
- **Question:** GP SAR La Princesse Lalla Meryem: Petra Marcinko vs Yelyzaveta Kotliar
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $75,708
- **Liquidity:** $50,813

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,407 (+0.9% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,386 (+1.1% 24h) → risk-ON
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: princesse lalla meryem: petra marcinko
- [Bing News]
- [Wed, 20 May 2026] princesse lalla meryem: petra marcinko
- → Subscribe to Sky Sports to watch live, or stream on NOW. WTA Tour: Petra Marcinko versus Yelyzaveta Kotliar in the 2nd Round at the Grand Prix Son A
- [Wed, 20 May 2026] P. Marcinko v Y. Kotliar
- → Magali Kempen a remport&#233; le duel qui l'opposait &#224; Lara Salden en quarts de finale du double au Grand Prix son Altesse Royale la Princesse 
- [Sun, 17 May 2026] WTA Rabat - Magali Kempen triomphe de Lara Salden en quarts de finale du double
- → Clay-Court Swing 411: Dates, draws, prize money and everything you need to know Download on the app store Google play ...

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Conflicting signals prevent clear edge. YES is correctly overpriced (stat: 55% markets resolve YES only 44.7% of time), but the +2% base rate gap (57% vs 55%) contradicts this. The 2% gap is below the 5% gate threshold used in similar past decisions. Additionally, Entry 50-60% pattern shows weak 33% WR from 9 trades. No concrete catalyst or injury news found for either player. Kotliar upset Jones in R1 showing form; Marcinko has home court advantage. Insufficient edge to justify bet in either direction.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Marcinko'})` → No injury data found for tennis Marcinko
- `get_odds({'sport': 'tennis_atp', 'team': 'Marcinko Kotliar'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Petra Marcinko vs Yelyzaveta Kotliar GP SAR La Princesse Lalla Meryem 2025'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] WTA Rabat Day 3 Predictions Including Yuliia Staro
- `search_web({'query': 'Petra Marcinko tennis 2025 form results recent'})` → [Thu, 08 Jan 2026] Google News
[Tue, 20 Jan 2026] By the numbers: Eala punches Auckland quarterfinal
- `get_market_context({'keyword': 'GP SAR La Princesse Lalla Meryem tennis'})` → No related markets found for 'GP SAR La Princesse Lalla Meryem tennis'
- `search_web({'query': 'Petra Marcinko ranking 2025 WTA clay court'})` → [Thu, 30 Apr 2026] Google News
[Thu, 23 Apr 2026] Rome 411: Important dates, who's playing, prize mo
- `search_web({'query': 'Yelyzaveta Kotliar ranking 2025 WTA tennis results'})` → [Tue, 21 Oct 2025] Google News
[Thu, 11 Sep 2025] Liu upsets Eala in Guangzhou; first tour-level win
- `search_web({'query': 'WTA Rabat 2025 Marcinko Kotliar preview prediction'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] WTA Rabat Day 3 Predictions Including Yuliia Staro
- `search_web({'query': '"Yelyzaveta Kotliar" tennis profile stats'})` → [Tue, 14 Sep 2021] Google News
[Mon, 29 Nov 2021] Yelyzaveta Kotliar - WTA Tennis
[Thu, 14 Nov 2019]
- `search_web({'query': 'Marcinko vs Kotliar odds tennis Rabat 2026'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Petra Marcinko vs. Yelyzaveta Kotliar prediction, 
- `search_web({'query': 'WTA Rabat round of 16 predictions May 2026'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] WTA Rabat Day 3 Predictions Including Alycia Parks
- `search_web({'query': 'dimers.com Marcinko Kotliar prediction odds pick'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Petra Marcinko vs. Yelyzaveta Kotliar prediction, 
- `search_web({'query': 'Tennis Tonic Marcinko Kotliar H2H prediction odds'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] H2H, prediction of Petra Marcinko vs Yelyzaveta Ko
- `search_web({'query': 'Petra Marcinko WTA ranking May 2026'})` → [Mon, 04 May 2026] Google News
[Wed, 18 Mar 2026] WTA Rome Day 1 Predictions Including Barbora Krejc
- `search_web({'query': 'Yelyzaveta Kotliar WTA ranking May 2026'})` → [Mon, 29 Nov 2021] Google News
[Mon, 18 May 2026] Yelyzaveta Kotliar Stats | Player Stats &amp; More
- `search_web({'query': '"Marcinko" "Kotliar" tennis odds 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Petra Marcinko vs. Yelyzaveta Kotliar prediction, 
- `get_market_context({'keyword': 'Marcinko Kotliar'})` → No related markets found for 'Marcinko Kotliar'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*