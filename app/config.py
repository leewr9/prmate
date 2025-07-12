import os
import requests

USE_OPENAI = True

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", None)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")

REVIEW_STRICT = os.getenv("REVIEW_STRICT", "False").lower() == "true"
REVIEW_LANG = os.getenv("REVIEW_LANG", "Korean")

if not GITHUB_TOKEN:
    raise EnvironmentError("GITHUB_TOKEN environment variable is not set.")

if not OPENAI_API_KEY:
    USE_OPENAI = False
    if not OLLAMA_HOST:
        raise EnvironmentError("Neither OPENAI_API_KEY nor OLLAMA_HOST is set.")

    try:
        response = requests.get(f"{OLLAMA_HOST}/api/tags", timeout=3)
        if response.status_code != 200:
            raise RuntimeError(
                f"Ollama server responded with status code {response.status_code}."
            )
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Cannot connect to Ollama server at {OLLAMA_HOST}: {e}")
