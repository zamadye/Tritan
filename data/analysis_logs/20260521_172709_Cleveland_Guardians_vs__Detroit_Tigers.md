# Market Analysis — 2026-05-21 17:27 UTC

## Market
- **Question:** Cleveland Guardians vs. Detroit Tigers
- **Category:** sports
- **YES Price:** 46.0%
- **Days Left:** 6
- **Volume 24h:** $281,017
- **Liquidity:** $36,819

## Statistical Prior
- **p_base:** 44.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,682 (+0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,738 (+0.4% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- [SPORTS] Recent games:
- CLE @ DET | In Progress | Detroit Tigers(home) 20-30 score:0 vs Cleveland Guardians(away) 29-22 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Tommy Henry — Day-To-Day ()
- ?: Spencer Giesting — Day-To-Day (Not Specified)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: cleveland guardians detroit tigers
- [Bing News]
- [Thu, 21 May 2026] cleveland guardians detroit tigers
- → The Cleveland Guardians go for the four-game series sweep when they battle the American League Central Division-rival Detroit Tigers on Thursday aft
- [Thu, 21 May 2026] Guardians vs. Tigers prediction, odds, time: 2026 MLB picks for Thursday, May 21 from advanced model
- → Here's how to watch Thursday's Detroit Tigers vs Cleveland Guardians game, including start times, TV channels, scores and how to stream.
- [Thu, 21 May 2026] Where to watch Cleveland Guardians vs Detroit Tigers: TV channel, start time, streaming for May 21
- → The Guardians (29-22) look to finish off a sweep of the Tigers (20-30) this afternoon at Comerica Park. It took scoring a couple runs in the tenth, 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 52%
- **p_true:** 44.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY
- **Catalyst Strength:** 0.35

### Reasoning
Tigers missing Skubal + Verlander is significant but injury news is 15 days old - market already adjusted (46% vs 44% base rate, only 2% gap). No new catalyst to drive further mispricing. Previous two decisions on same matchup were SKIPs. Gap (2%) below 5% threshold required for action. Market appears at fair value with no verifiable edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Cleveland Guardians'})` → INJURY [cleveland guardians] Gabriel Arias (SS): 10-Day-IL
INJURY [cleveland guardians] Peyton Palle
- `get_sports_data({'sport': 'mlb', 'team': 'Detroit Tigers'})` → INJURY [detroit tigers] Justin Verlander (SP): 60-Day-IL
INJURY [detroit tigers] Troy Melton (RP): 6
- `get_odds({'sport': 'baseball_mlb', 'team': 'Guardians Tigers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Cleveland Guardians vs Detroit Tigers 2025 MLB game preview prediction'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Cleveland Guardians vs. Detroit Tigers prediction,
- `search_web({'query': 'Cleveland Guardians Detroit Tigers injury report roster 2025'})` → [Tue, 19 May 2026] Google News
[Mon, 29 Sep 2025] Latest Guardians injuries and transactions - MLB.c
- `get_market_context({'keyword': 'Guardians Tigers MLB'})` → No related markets found for 'Guardians Tigers MLB'
- `search_web({'query': 'Tarik Skubal injury 2026 Tigers IL status update'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Tigers rotation updates: Troy Melton ready to go, 
- `search_web({'query': 'Cleveland Guardians starting pitcher today May 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `get_market_context({'keyword': 'MLB American League'})` → No related markets found for 'MLB American League'
- `search_web({'query': '"Guardians" "Tigers" betting odds moneyline May 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Guardians vs. Tigers prediction, odds, time: 2026 
- `search_web({'query': 'Guardians Tigers May 21 2026 moneyline odds favorite underdog'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Guardians vs. Tigers prediction, odds, time: 2026 
- `search_web({'query': 'Guardians Tigers May 21 2026 -150 -130 moneyline odds betting'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Guardians vs. Tigers prediction, odds, time: 2026 
- `search_web({'query': 'site:espn.com Guardians Tigers odds spread May 21 2026'})` → [Fri, 08 Jul 2016] Google News
[Sun, 17 May 2026] Tampa Bay Rays Scores, Stats and Highlights - ESPN
- `search_web({'query': '"Guardians" "Tigers" "moneyline" "May 21" odds 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Guardians vs. Tigers prediction: Odds, recent stat

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*