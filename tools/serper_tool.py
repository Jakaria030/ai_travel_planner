import os
import requests
from dotenv import load_dotenv
from crewai.tools import tool

load_dotenv()

# Get the Serper API key from environment variables
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
SERPER_SEARCH_URL = os.getenv("SERPER_SEARCH_URL", "https://google.serper.dev/search")


@tool("Web Search Tool")
def serper_search(query: str) -> list[dict]:
    """
    Searches Google using Serper API and returns top 5 results in a formatted list of dictionaries.
    
    Args:
        query (str): The search query.
    
    Returns:
        list[dict]: A list of dictionaries containing the title, snippet, and link of the top search results.
    """

    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {"q": query}

    try:
        response = requests.post(SERPER_SEARCH_URL, headers=headers, json=payload)

        if response.status_code != 200:
            raise Exception(f"Serper API error: {response.status_code} - {response.text}")

        data = response.json()

        results = [
            {
                "title": result.get("title", ""),
                "snippet": result.get("snippet", ""),
                "link": result.get("link", "")
            }
            for result in data.get("organic", [])[:5]
        ]

        return results

    except Exception as e:
        raise Exception(f"Error occurred while calling Serper API: {str(e)}")