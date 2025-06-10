import os
from dotenv import load_dotenv
from .google_scholar_crawler import fetch_scholar_author

load_dotenv()

def fetch_author(author_name: str, num_papers: int = 20):
    """
    Hämtar författardata från Google Scholar.
    """
    return fetch_scholar_author(author_name, num_papers=num_papers)