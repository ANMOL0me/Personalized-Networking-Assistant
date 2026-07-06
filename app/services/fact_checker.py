# app/services/fact_checker.py

import requests

WIKI_SEARCH_URL = "https://en.wikipedia.org/w/api.php"
WIKI_SUMMARY_URL = "https://en.wikipedia.org/api/rest_v1/page/summary"

HEADERS = {
    "User-Agent": "PersonalizedNetworkingAssistant/1.0 (contact: your-email@example.com)"
}
# app/services/fact_checker.py

import requests

WIKI_SEARCH_URL = "https://en.wikipedia.org/w/api.php"
WIKI_SUMMARY_URL = "https://en.wikipedia.org/api/rest_v1/page/summary"

HEADERS = {
    "User-Agent": "PersonalizedNetworkingAssistant/1.0 (contact: your-email@example.com)"
}


def _find_best_title(query: str):
    """Use Wikipedia's search API to find the closest matching page title."""
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": 1,
    }
    response = requests.get(WIKI_SEARCH_URL, params=params, headers=HEADERS, timeout=10)
    response.raise_for_status()
    results = response.json().get("query", {}).get("search", [])
    return results[0]["title"] if results else None


def fact_check(query: str) -> str:
    try:
        title = _find_best_title(query.strip())

        if not title:
            return "No matching topic found."

        formatted_title = title.replace(" ", "_")
        response = requests.get(
            f"{WIKI_SUMMARY_URL}/{formatted_title}",
            headers=HEADERS,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        return data.get("extract", "No summary found.")

    except requests.exceptions.RequestException as e:
        return f"Fact-checking failed: {e}"
    except ValueError:
        return "Fact-checking failed: invalid response format."

def _find_best_title(query: str) -> str | None:
    """Use Wikipedia's search API to find the closest matching page title."""
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": 1,
    }
    response = requests.get(WIKI_SEARCH_URL, params=params, headers=HEADERS, timeout=10)
    response.raise_for_status()
    results = response.json().get("query", {}).get("search", [])
    return results[0]["title"] if results else None


def fact_check(query: str) -> str:
    try:
        title = _find_best_title(query.strip())

        if not title:
            return "No matching topic found."

        formatted_title = title.replace(" ", "_")
        response = requests.get(
            f"{WIKI_SUMMARY_URL}/{formatted_title}",
            headers=HEADERS,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        return data.get("extract", "No summary found.")

    except requests.exceptions.RequestException as e:
        return f"Fact-checking failed: {e}"
    except ValueError:
        return "Fact-checking failed: invalid response format."