# app/services/fact_checker.py

import requests
from app.config import FACT_CHECK_API


def fact_check(query: str) -> str:
    try:
        response = requests.get(f"{FACT_CHECK_API}/{query}", timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("extract", "No summary found.")
    except requests.exceptions.RequestException as e:
        return f"Fact-checking failed: {e}"
    except ValueError:
        return "Fact-checking failed: invalid response format."