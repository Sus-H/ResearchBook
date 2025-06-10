import networkx as nx
from app.graph_builder import build_graph

def test_build_graph_empty():
    data = {"name": "Test", "papers": []}
    G = build_graph(data)
    assert isinstance(G, nx.Graph)
    assert "Test" in G.nodes
    assert G.number_of_edges() == 0
