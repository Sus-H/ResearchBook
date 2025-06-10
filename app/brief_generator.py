def generate_brief(graph, author_name):
    coauthors = list(graph.neighbors(author_name))
    brief = f"{author_name} has {len(coauthors)} co-authors:\n"
    for c in coauthors:
        brief += f" - {c}\n"
    return brief
