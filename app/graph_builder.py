import networkx as nx

def build_graph(author_data):
    G = nx.Graph()
    main_author = author_data["name"]
    G.add_node(main_author, type="author")

    for paper in author_data.get("papers", []):
        for coauthor in paper.get("authors", []):
            if coauthor["name"] != main_author:
                G.add_node(coauthor["name"], type="coauthor")
                G.add_edge(main_author, coauthor["name"], paper=paper["title"])
    return G
