import os
from .google_scholar_crawler import fetch_scholar_author
from .chalmers_odr_crawler import fetch_odr_author

def fetch_author(source: str, identifier: str):
    """
    Fetch author data from the given source.
    source: "scholar" for Google Scholar, "odr" for Chalmers ODR
    identifier: author name (scholar) or researcher ID (odr)
    """
    if source == "scholar":
        return fetch_scholar_author(identifier)
    elif source == "odr":
        return fetch_odr_author(identifier)
    else:
        raise ValueError(f"Unknown source: {source}")
