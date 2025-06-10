from app.crawler import fetch_author
from app.graph_builder import build_graph
from app.brief_generator import generate_brief
from app.crawler import fetch_author

if __name__ == "__main__":
    author_id = "145689385"  # exempel från Semantic Scholar
    author_data = fetch_author(author_id)
    graph = build_graph(author_data)
    
    print(f"Grafen innehåller {len(graph.nodes)} noder.")
    print(generate_brief(graph, author_data['name']))
