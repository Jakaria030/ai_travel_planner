import os
import requests
from dotenv import load_dotenv
from crewai import tool

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
SERPER_SEARCH_URL = os.getenv("SERPER_SEARCH_URL", "https://google.serper.dev/search")

@tool("Web Search Tool")
def serper_search(query: str) -> list[dict]:
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {"q": query}

    response = requests.post(SERPER_SEARCH_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Serper API error: {response.text}")

    data = response.json()
    results = []

    # Top 5 organic results
    for result in data.get("organic", [])[:5]:
        results.append({
            "title": result.get("title", ""),
            "snippet": result.get("snippet", ""),
            "link": result.get("link", "")
        })

    return results