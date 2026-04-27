"""LLM client — OpenAI-compatible (Moonshot AI / any OpenAI-compat endpoint)."""
import os
import time
from openai import OpenAI


def get_client() -> OpenAI:
    return OpenAI(
        api_key=os.getenv("AI_API_KEY"),
        base_url=os.getenv("AI_BASE_URL"),
    )


def chat(prompt: str, max_tokens: int = None) -> str:
    client = get_client()
    model = os.getenv("AI_MODEL", "moonshot-v1-8k")
    max_tokens = max_tokens or int(os.getenv("LLM_MAX_TOKENS", 600))
    retries = int(os.getenv("API_MAX_RETRIES", 3))

    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=model,
                max_tokens=max_tokens,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content
        except Exception as e:
            if "429" in str(e) and attempt < retries - 1:
                wait = (attempt + 1) * 20
                print(f"[LLM] Rate limited, waiting {wait}s...")
                time.sleep(wait)
            else:
                raise
