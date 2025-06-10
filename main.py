from app.crawler import fetch_author
from app.graph_builder import build_graph
from app.brief_generator import generate_brief

from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    # Example usage:
    # For Google Scholar, use source="scholar" and identifier author name
    # For Chalmers ODR, use source="odr" and identifier researcher ID
    source = "scholar"
    identifier = "Marty Banks, Berkeley"
    author_data = fetch_author(source, identifier)
    print(author_data)
    graph = build_graph(author_data)
    print(f"Graph has {len(graph.nodes)} nodes.")
    print(generate_brief(graph, author_data['name']))
