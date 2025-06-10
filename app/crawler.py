import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_author_data(author_id: str):
    base_url = "https://api.semanticscholar.org/graph/v1/author"
    fields = "name,affiliations,papers.title,papers.authors"
    headers = {"x-api-key": os.getenv("SEMANTIC_SCHOLAR_API_KEY")}
    response = requests.get(f"{base_url}/{author_id}?fields={fields}", headers=headers)

    if response.status_code != 200:
        raise Exception(f"API-fel: {response.status_code}")
    
    return response.json()
