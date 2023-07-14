def write_graph_to_file(graph, filename):
    with open(filename, 'w') as file:
        num_nodes = len(graph)
        num_edges = sum(len(adjacent) for adjacent in graph.values()) // 2
        file.write(f"{num_nodes} {num_edges}\n")
        for node, adjacent in graph.items():
            for neighbor, weight in adjacent.items():
                file.write(f"{node} {neighbor} {weight}\n")

def count_votings_per_deputy(graph):
    voting_count = {}
    for deputy in graph:
        voting_count[deputy] = len(graph[deputy])
    return voting_count
