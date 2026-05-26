"""Multi-source news aggregator — collects from multiple independent sources
and provides consensus signal for LLM analysis.

Sources by category:
- General: Bing, Al Jazeera, Guardian, Sky News, ABC News
- Crypto: CoinTelegraph, Decrypt, Bing crypto
- Sports: BBC Sport, Sky Sports, TheSportsDB, ESPN
- Geopolitik: Al Jazeera, Guardian, BBC World, Sky News
"""
import os
import re
import requests
from functools import lru_cache
from datetime import datetime, timezone


HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; NewsBot/1.0)"}
TIMEOUT = 6


def _fetch_rss(url: str, query_words: set, max_items: int = 3) -> list[dict]:
    """Fetch RSS and return relevant items with title + description."""
    try:
        r = requests.get(url, timeout=TIMEOUT, headers=HEADERS)
        if r.status_code != 200:
            return []
        titles = re.findall(r"<title>(.*?)</title>", r.text)[1:]
        descs  = re.findall(r"<description>(.*?)</description>", r.text)[1:]
        dates  = re.findall(r"<pubDate>(.*?)</pubDate>", r.text)

        results = []
        for i, title in enumerate(titles):
            t_clean = re.sub(r"<[^>]+>|&[a-z]+;", " ", title).strip()
            d_clean = re.sub(r"<[^>]+>|&[a-z]+;", " ", descs[i] if i < len(descs) else "").strip()[:200]
            date = dates[i][:16] if i < len(dates) else ""

            # Filter by relevance
            combined = (t_clean + " " + d_clean).lower()
            if query_words and not any(w in combined for w in query_words):
                continue

            results.append({"title": t_clean, "desc": d_clean, "date": date})
            if len(results) >= max_items:
                break
        return results
    except Exception:
        return []


def _fetch_bing(query: str, max_items: int = 3) -> list[dict]:
    """Fetch Bing News RSS with snippets."""
    try:
        r = requests.get("https://www.bing.com/news/search",
            params={"q": query, "format": "rss"},
            headers=HEADERS, timeout=TIMEOUT)
        if r.status_code != 200:
            return []
        titles = re.findall(r"<title>(.*?)</title>", r.text)[1:]
        descs  = re.findall(r"<description>(.*?)</description>", r.text)[1:]
        dates  = re.findall(r"<pubDate>(.*?)</pubDate>", r.text)
        results = []
        for i, title in enumerate(titles[:max_items]):
            d = re.sub(r"<[^>]+>", " ", descs[i] if i < len(descs) else "").strip()[:200]
            results.append({"title": title, "desc": d, "date": dates[i][:16] if i < len(dates) else ""})
        return results
    except Exception:
        return []


def get_multi_source_news(question: str, category: str = "other") -> str:
    """Aggregate news from multiple sources. Returns formatted string for LLM."""
    stopwords = {"will","the","and","for","are","was","has","have","been","that","this","with","from"}
    words = [w.strip("?.,!()").lower() for w in question.split() if len(w) > 3 and w.lower() not in stopwords]
    query = " ".join(words[:5])
    query_words = set(words[:6])

    all_results = {}

    # ── Bing News (all categories) ──────────────────────────────────────
    bing = _fetch_bing(query, 3)
    if bing:
        all_results["Bing News"] = bing

    # ── Category-specific sources ────────────────────────────────────────
    if category in ("crypto",):
        ct = _fetch_rss("https://cointelegraph.com/rss", query_words, 2)
        if ct: all_results["CoinTelegraph"] = ct
        dc = _fetch_rss("https://decrypt.co/feed", query_words, 2)
        if dc: all_results["Decrypt"] = dc

    elif category in ("sports",):
        bbc_sport = _fetch_rss("https://feeds.bbci.co.uk/sport/rss.xml", query_words, 2)
        if bbc_sport: all_results["BBC Sport"] = bbc_sport
        sky_sport = _fetch_rss("https://www.skysports.com/rss/12040", query_words, 2)
        if sky_sport: all_results["Sky Sports"] = sky_sport

    elif category in ("geopolitik", "politics"):
        aj = _fetch_rss("https://www.aljazeera.com/xml/rss/all.xml", query_words, 2)
        if aj: all_results["Al Jazeera"] = aj
        guardian = _fetch_rss("https://www.theguardian.com/world/rss", query_words, 2)
        if guardian: all_results["The Guardian"] = guardian
        sky = _fetch_rss("https://feeds.skynews.com/feeds/rss/world.xml", query_words, 2)
        if sky: all_results["Sky News"] = sky

    else:
        # General: use multiple sources
        abc = _fetch_rss("https://feeds.abcnews.com/abcnews/topstories", query_words, 2)
        if abc: all_results["ABC News"] = abc
        bbc = _fetch_rss("https://feeds.bbci.co.uk/news/world/rss.xml", query_words, 2)
        if bbc: all_results["BBC World"] = bbc

    # ── Metaculus community predictions ─────────────────────────────────
    metaculus_key = os.getenv("METACULUS_API_KEY", "")
    if metaculus_key:
        try:
            r = requests.get("https://www.metaculus.com/api2/questions/",
                params={"status": "open", "order_by": "-activity", "limit": 3, "search": " ".join(words[:3])},
                headers={"Authorization": f"Token {metaculus_key}"}, timeout=6)
            if r.status_code == 200:
                results = r.json().get("results", [])
                if results:
                    meta_items = []
                    for q in results[:3]:
                        pred = q.get("community_prediction", {})
                        prob = pred.get("full", {}).get("q2")
                        title = q.get("title", "")[:70]
                        if prob is not None:
                            meta_items.append({"title": title, "desc": f"Community: {prob:.0%}", "date": ""})
                        else:
                            meta_items.append({"title": title, "desc": "Community: pending", "date": ""})
                    if meta_items:
                        all_results["Metaculus"] = meta_items
        except Exception:
            pass

    if not all_results:
        return ""

    # Format output
    lines = [f"[MULTI-SOURCE NEWS] {len(all_results)} sources for: {query}"]
    for source, items in all_results.items():
        lines.append(f"  [{source}]")
        for item in items:
            lines.append(f"    [{item['date']}] {item['title']}")
            if item['desc']:
                lines.append(f"    → {item['desc'][:150]}")

    # Consensus signal: count how many sources have relevant content
    total_sources = len(all_results)
    lines.append(f"  [COVERAGE] {total_sources} independent sources found relevant content")

    return "\n".join(lines)
