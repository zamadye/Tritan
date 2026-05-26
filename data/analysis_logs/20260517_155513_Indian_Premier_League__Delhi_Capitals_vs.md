# Market Analysis — 2026-05-17 15:55 UTC

## Market
- **Question:** Indian Premier League: Delhi Capitals vs Rajasthan Royals
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $553,962
- **Liquidity:** $74,638

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,004 (-0.3% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,004 (-0.3% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Denzel Clarke — 10-Day-IL (Bruise)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)

### Bing/Google News
- 6 articles found:
- [NewsAPI] Anshul Kamboj makes unwanted IPL history: Highest economy rate in a T20 match li: CSK and India international Anshul Kamboj made an unwanted
- [NewsAPI] LSG vs CSK IPL 2026 live score, toss winner, winning probability, result and hig: Lucknow Super Giants prepare to host Chennai Super Kings i
- [NewsAPI] PBKS vs MI IPL 2026 live score, toss winner, winning probability, result and hig: Punjab Kings are set to play their final IPL 2026 game in 
- [NewsAPI] Yesterday IPL Match RCB vs KKR: Virat Kohli's unbeaten 105 powers Royal Challeng: IPL Match yesterday: Virat Kohli's vintage 105* powered Ro
- [NewsAPI] Who is the most-capped player in IPL history? Virat Kohli scripts history during: Virat Kohli became the most-capped player in IPL history a
- [NewsAPI] RCB vs KKR IPL 2026 live score, toss winner, winning probability, result and hig: Royal Challengers Bengaluru will host Kolkata Knight Rider
- [CAUSAL CHAINS] Relevant cause-effect patterns:

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: indian premier league: delhi capitals
- [Bing News]
- [Sun, 17 May 2026] indian premier league: delhi capitals
- → Rajasthan Royals batter Vaibhav Sooryavanshi put forth a brilliant performance against Delhi Capitals in the 62nd game of the ongoing IPL (Indian Pr
- [Sun, 17 May 2026] Vaibhav Sooryavanshi surpasses Abhishek Sharma, achieves huge feat with quickfire start against Delhi Capitals
- → Delhi Capitals (DC) will take on Rajasthan Royals (RR) in match 62 of IPL 2026 at the Arun Jaitley Stadium on Sunday, May 17. It's a do-or-die match
- [Sun, 17 May 2026] DC Vs RR, IPL 2026: See Best Photos From Indian Premier League Match 62 At Delhi's Arun Jaitley Stadium
- → Get all the information you need ahead of the Indian Premier League 2026 match 62 between Delhi Capitals and Rajasthan Royals on Sunday, 17 May at A

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_VALUE
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal (n=13,967) shows markets at 56% resolve YES only 44.7% of the time, indicating ~8% overpricing of YES after adjusting for partial injury offset favoring DC. Net edge remains for NO.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'cricket', 'team': 'Delhi Capitals'})` → No injury data found for cricket Delhi Capitals
- `get_sports_data({'sport': 'cricket', 'team': 'Rajasthan Royals'})` → No injury data found for cricket Rajasthan Royals
- `search_web({'query': 'Delhi Capitals vs Rajasthan Royals IPL 2024 recent form head to head'})` → [Tue, 07 Apr 2026] Google News
[Tue, 07 Apr 2026] RR vs MI, Match 13 Preview: Head-to-Head Record, P
- `search_web({'query': 'IPL Delhi Capitals vs Rajasthan Royals injury news today'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] DC vs RR IPL 2026 Injury News: Are Riyan Parag And
- `get_market_context({'keyword': 'Delhi Capitals Rajasthan Royals IPL'})` → No related markets found for 'Delhi Capitals Rajasthan Royals IPL'
- `search_web({'query': 'Delhi Capitals vs Rajasthan Royals IPL 2025 match preview odds'})` → [Fri, 27 Mar 2026] Google News
[Sat, 16 May 2026] IPL 2026 preview: A new era at Rajasthan Royals, a
- `search_web({'query': 'Rajasthan Royals recent results IPL 2025'})` → [2026-05-14] IPL 2026: Full list of teams that qualified for the playoffs stage — The IPL 2026 playo
- `get_market_context({'keyword': 'IPL cricket'})` → No related markets found for 'IPL cricket'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*