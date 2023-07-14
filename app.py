from request_utils import make_request
from voting_utils import get_all_votings, get_voting_details
from file_utils import write_graph_to_file, count_votings_per_deputy

graph = get_all_votings()
write_graph_to_file(graph, 'grafo.txt')
votings_per_deputy = count_votings_per_deputy(graph)

with open('num_votings.txt', 'w') as file:
    for deputy, count in votings_per_deputy.items():
        file.write(f"{deputy} {count}\n")
