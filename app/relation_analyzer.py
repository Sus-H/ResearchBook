def analyze_soft_links(graph):
    indirect_links = {}
    for node in graph.nodes:
        neighbors = list(graph.neighbors(node))
        for neighbor in neighbors:
            second_degree = set(graph.neighbors(neighbor)) - {node}
            indirect_links[node] = indirect_links.get(node, set()) | second_degree
    return indirect_links
