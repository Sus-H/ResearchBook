def generate_brief(graph, author_name):
    coauthors = list(graph.neighbors(author_name))
    brief = f"{author_name} har {len(coauthors)} kända samarbetspartners:\n"
    for c in coauthors:
        brief += f" - {c}\n"
    return brief
