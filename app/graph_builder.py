import networkx as nx

def build_graph(author_data):
    G = nx.Graph()
    author_name = author_data.get("name")
    G.add_node(author_name, type="author")

    for paper in author_data.get("papers", []):
        for co in paper.get("authors", []):
            if co != author_name:
                G.add_node(co, type="coauthor")
                G.add_edge(author_name, co, paper=paper.get("title"))
    return G
