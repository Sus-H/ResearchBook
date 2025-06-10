from app.crawler import fetch_author
from app.graph_builder import build_graph
from app.brief_generator import generate_brief

if __name__ == "__main__":
    # Example usage:
    # For Google Scholar, use source="scholar" and identifier author name
    # For Chalmers ODR, use source="odr" and identifier researcher ID
    source = "scholar"
    identifier = "Albert Einstein"
    author_data = fetch_author(source, identifier)
    graph = build_graph(author_data)
    print(f"Graph has {len(graph.nodes)} nodes.")
    print(generate_brief(graph, author_data['name']))
