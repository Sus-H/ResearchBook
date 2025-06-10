import os
import requests

def fetch_odr_author(researcher_id: str):
    """
    Fetch author publications and affiliations from Chalmers ODR.
    """
    base_url = "https://api.odr.chalmers.se/researcher"
    headers = {"Authorization": f"Bearer {os.getenv('CHALMERS_ODR_API_KEY')}"}
    r = requests.get(f"{base_url}/{researcher_id}", headers=headers)
    r.raise_for_status()
    data = r.json()

    # Example structure adaptation
    return {
        "name": data.get("name"),
        "affiliations": data.get("affiliations"),
        "papers": [
            {"title": pub.get("title"), "authors": pub.get("authors", [])}
            for pub in data.get("publications", [])
        ],
    }
