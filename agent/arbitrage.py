"""
Edge Type 3 — Cross-platform arbitrage detector.

Compares Polymarket prices with:
- Manifold Markets (free API, no key)
- Metaculus community predictions (free API)

If gap > 12% on equivalent market → arbitrage signal.
"""
import os
import json
import requests
import re
from pathlib import Path
from datetime import datetime, timezone
import time

CACHE_FILE = Path("data/arb_cache.json")
CACHE_TTL  = 600  # 10 minutes


def _load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            d = json.loads(CACHE_FILE.read_text())
            now = time.time()
            return {k: v for k, v in d.items() if now - v.get("ts", 0) < CACHE_TTL}
        except Exception:
            pass
    return {}


def _save_cache(cache: dict):
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(json.dumps(cache, indent=2))


def _extract_keywords(question: str) -> list:
    """Extract key terms from market question for fuzzy matching."""
    stopwords = {"will","the","and","for","are","was","has","have","been","that",
                 "this","with","from","they","their","reach","april","may","june",
                 "july","august","by","in","on","at","to","a","an","be","is"}
    words = [w.strip("?.,!()$%").lower() for w in question.split()
             if len(w) > 3 and w.lower() not in stopwords]
    return words[:6]


def _similarity(q1: str, q2: str) -> float:
    """Simple word overlap similarity."""
    w1 = set(_extract_keywords(q1))
    w2 = set(_extract_keywords(q2))
    if not w1 or not w2:
        return 0.0
    return len(w1 & w2) / max(len(w1), len(w2))


def check_manifold(question: str, polymarket_price: float) -> dict:
    """Find equivalent market on Manifold and compare prices."""
    result = {"has_arb": False, "platform": "manifold", "their_price": None,
              "gap": 0.0, "market_title": "", "url": ""}
    try:
        keywords = " ".join(_extract_keywords(question)[:3])
        r = requests.get("https://api.manifold.markets/v0/search-markets",
            params={"term": keywords, "limit": 10, "filter": "open"}, timeout=8)
        if r.status_code != 200:
            return result

        markets = r.json()
        best_match = None
        best_sim = 0.0

        for m in markets:
            sim = _similarity(question, m.get("question", ""))
            if sim > best_sim and sim >= 0.4:
                best_sim = sim
                best_match = m

        if not best_match:
            return result

        prob = best_match.get("probability")
        if prob is None:
            return result

        gap = abs(float(prob) - polymarket_price)
        if gap >= 0.12:  # 12% minimum gap
            result["has_arb"] = True
            result["their_price"] = round(float(prob), 3)
            result["gap"] = round(gap, 3)
            result["market_title"] = best_match.get("question", "")[:60]
            result["url"] = f"https://manifold.markets/{best_match.get('slug','')}"
            result["similarity"] = round(best_sim, 2)

    except Exception:
        pass
    return result


def check_metaculus(question: str, polymarket_price: float) -> dict:
    """Find equivalent market on Metaculus and compare predictions."""
    result = {"has_arb": False, "platform": "metaculus", "their_price": None,
              "gap": 0.0, "market_title": "", "url": ""}
    try:
        keywords = " ".join(_extract_keywords(question)[:3])
        r = requests.get("https://www.metaculus.com/api2/questions/",
            params={"search": keywords, "limit": 5, "type": "forecast",
                    "status": "open"}, timeout=8)
        if r.status_code != 200:
            return result

        questions = r.json().get("results", [])
        best_match = None
        best_sim = 0.0

        for q in questions:
            sim = _similarity(question, q.get("title", ""))
            if sim > best_sim and sim >= 0.4:
                best_sim = sim
                best_match = q

        if not best_match:
            return result

        # Get community prediction
        pred = best_match.get("community_prediction", {})
        prob = pred.get("full", {}).get("q2") or pred.get("q2")
        if prob is None:
            return result

        gap = abs(float(prob) - polymarket_price)
        if gap >= 0.12:
            result["has_arb"] = True
            result["their_price"] = round(float(prob), 3)
            result["gap"] = round(gap, 3)
            result["market_title"] = best_match.get("title", "")[:60]
            result["url"] = f"https://www.metaculus.com/questions/{best_match.get('id','')}"
            result["similarity"] = round(best_sim, 2)

    except Exception:
        pass
    return result


def detect_arbitrage(market: dict) -> dict:
    """
    Check for cross-platform arbitrage opportunity.
    Returns best arbitrage signal found.
    """
    question = market.get("question", "")
    price    = market.get("price", 0.5)

    cache = _load_cache()
    cache_key = question[:60]
    if cache_key in cache:
        return cache[cache_key]

    result = {"has_arb": False, "platform": "none", "their_price": None,
              "gap": 0.0, "detail": ""}

    # Check Manifold
    manifold = check_manifold(question, price)
    if manifold["has_arb"]:
        direction = "YES_cheap" if manifold["their_price"] > price else "NO_cheap"
        result = {
            "has_arb": True,
            "platform": "manifold",
            "their_price": manifold["their_price"],
            "our_price": price,
            "gap": manifold["gap"],
            "direction": direction,
            "detail": (f"Manifold: {manifold['their_price']:.0%} vs Polymarket: {price:.0%} "
                       f"= {manifold['gap']:.0%} gap | {manifold['market_title'][:50]}"),
            "url": manifold["url"],
        }
        cache[cache_key] = {**result, "ts": time.time()}
        _save_cache(cache)
        return result

    # Check Metaculus
    metaculus = check_metaculus(question, price)
    if metaculus["has_arb"]:
        direction = "YES_cheap" if metaculus["their_price"] > price else "NO_cheap"
        result = {
            "has_arb": True,
            "platform": "metaculus",
            "their_price": metaculus["their_price"],
            "our_price": price,
            "gap": metaculus["gap"],
            "direction": direction,
            "detail": (f"Metaculus: {metaculus['their_price']:.0%} vs Polymarket: {price:.0%} "
                       f"= {metaculus['gap']:.0%} gap | {metaculus['market_title'][:50]}"),
            "url": metaculus["url"],
        }

    cache[cache_key] = {**result, "ts": time.time()}
    _save_cache(cache)
    return result
