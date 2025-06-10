import os
from scholarly import scholarly
from serpapi.google_search import GoogleSearch

def fetch_scholar_author(author_name: str, num_papers: int = 20):
        params = {
            "engine": "google_scholar_author",
            "author_id": author_name,
            "api_key": os.getenv("SERPAPI_API_KEY"),
            "hl": "en"
        }
        search = GoogleSearch(params)
        results = search.get_dict()

        profile = results.get("author_profile", {})
        papers = results.get("articles", [])[:num_papers]

        return {
            "name": profile.get("name"),
            "affiliations": profile.get("affiliations"),
            "papers": [
                {"title": p.get("title"), "authors": p.get("authors", [])}
                for p in papers
            ],
        }