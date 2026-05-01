"""LLM client — Xiaomi MiMo via OpenAI-compatible endpoint with token tracking."""
import os
import time
import json
from pathlib import Path
from openai import OpenAI

# Token usage tracking file
_USAGE_FILE = Path("data/llm_usage.json")


def _load_usage() -> dict:
    if _USAGE_FILE.exists():
        try:
            return json.loads(_USAGE_FILE.read_text())
        except Exception:
            pass
    return {"total_input": 0, "total_output": 0, "total_calls": 0,
            "total_cost_usd": 0.0, "daily": {}}


def _save_usage(usage: dict):
    _USAGE_FILE.parent.mkdir(parents=True, exist_ok=True)
    _USAGE_FILE.write_text(json.dumps(usage, indent=2))


def _track(input_tokens: int, output_tokens: int):
    """Track token usage and estimated cost."""
    usage = _load_usage()
    # MiMo pricing: ~$0.15/1M input, $0.60/1M output (approximate)
    cost = (input_tokens / 1_000_000) * 0.15 + (output_tokens / 1_000_000) * 0.60
    usage["total_input"]    += input_tokens
    usage["total_output"]   += output_tokens
    usage["total_calls"]    += 1
    usage["total_cost_usd"] = round(usage["total_cost_usd"] + cost, 6)

    # Daily tracking
    from datetime import datetime, timezone
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if today not in usage["daily"]:
        usage["daily"][today] = {"input": 0, "output": 0, "calls": 0, "cost_usd": 0.0}
    usage["daily"][today]["input"]    += input_tokens
    usage["daily"][today]["output"]   += output_tokens
    usage["daily"][today]["calls"]    += 1
    usage["daily"][today]["cost_usd"] = round(usage["daily"][today]["cost_usd"] + cost, 6)

    _save_usage(usage)
    return cost


def get_daily_usage() -> dict:
    """Return today's usage stats."""
    from datetime import datetime, timezone
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    usage = _load_usage()
    return usage["daily"].get(today, {"input": 0, "output": 0, "calls": 0, "cost_usd": 0.0})


def get_client() -> OpenAI:
    return OpenAI(
        api_key=os.getenv("AI_API_KEY"),
        base_url=os.getenv("AI_BASE_URL", "https://api.xiaomimimo.com/v1"),
    )


def chat(prompt: str, max_tokens: int = None) -> str:
    client    = get_client()
    model     = os.getenv("AI_MODEL", "mimo-v2.5-pro")
    max_tokens = max_tokens or int(os.getenv("LLM_MAX_TOKENS", 1200))
    retries   = int(os.getenv("API_MAX_RETRIES", 3))

    # Daily cost guard — stop if >$2/day
    daily = get_daily_usage()
    daily_limit = float(os.getenv("LLM_DAILY_COST_LIMIT_USD", 2.0))
    if daily["cost_usd"] >= daily_limit:
        raise Exception(f"[LLM] Daily cost limit ${daily_limit} reached (used ${daily['cost_usd']:.3f}). Pausing.")

    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=model,
                max_tokens=max_tokens,
                messages=[{"role": "user", "content": prompt}],
            )
            content = response.choices[0].message.content

            # Track usage from response
            usage = getattr(response, "usage", None)
            if usage:
                cost = _track(usage.prompt_tokens, usage.completion_tokens)
                if cost > 0.01:  # log if single call costs >1 cent
                    print(f"[LLM] tokens: in={usage.prompt_tokens} out={usage.completion_tokens} cost=${cost:.4f} | daily=${get_daily_usage()['cost_usd']:.3f}")
            else:
                # Estimate if usage not returned
                _track(len(prompt)//4, max_tokens//2)

            return content

        except Exception as e:
            err = str(e)
            if "429" in err or "rate_limit" in err.lower():
                if attempt < retries - 1:
                    wait = (attempt + 1) * 20
                    print(f"[LLM] Rate limited, waiting {wait}s...")
                    time.sleep(wait)
                else:
                    raise
            elif "insufficient_balance" in err or "suspended" in err.lower():
                raise Exception(f"[LLM] Account suspended/no balance: {err[:100]}")
            else:
                raise
