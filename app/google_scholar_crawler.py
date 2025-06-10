import os
from serpapi import GoogleSearch

def fetch_scholar_author(author_name: str, num_papers: int = 20):
    """
    Fetch basic author profile and publications from Google Scholar via SerpAPI.
    """
    params = {
        "engine": "google_scholar_author",
        "author": author_name,
        "hl": "en",
        "api_key": os.getenv("SERPAPI_API_KEY"),
    }
    search = GoogleSearch(params)
    data = search.get_dict()

    profile = data.get("author_profile", {})
    articles = data.get("articles", [])[:num_papers]

    return {
        "name": profile.get("name"),
        "affiliations": profile.get("affiliations"),
        "papers": [
            {"title": p.get("title"), "authors": p.get("authors", [])}
            for p in articles
        ],
    }
