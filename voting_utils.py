from request_utils import make_request

def get_voting_details(voting_id, graph):
    url = f'https://dadosabertos.camara.leg.br/api/v2/votacoes/{voting_id}/votos'
    data = make_request(url)
    if data:
        votes = data['dados']
        if votes:  # Verifica se existem votos
            print('\n' "Votação " + voting_id)  # Imprime o código da votação
            for i in range(len(votes)):
                for j in range(i + 1, len(votes)):
                    vote_i = votes[i]
                    vote_j = votes[j]
                    if 'deputado_' in vote_i and 'deputado_' in vote_j:
                        deputado_i = vote_i['deputado_']['nome']
                        deputado_j = vote_j['deputado_']['nome']
                        tipoVoto_i = vote_i['tipoVoto']
                        tipoVoto_j = vote_j['tipoVoto']
                        if tipoVoto_i == 'Sim' and tipoVoto_j == 'Sim':
                            if deputado_i not in graph:
                                graph[deputado_i] = {}
                            if deputado_j not in graph:
                                graph[deputado_j] = {}
                            if deputado_j not in graph[deputado_i]:
                                graph[deputado_i][deputado_j] = 1
                            else:
                                graph[deputado_i][deputado_j] += 1
                            if deputado_i not in graph[deputado_j]:
                                graph[deputado_j][deputado_i] = 1
                            else:
                                graph[deputado_j][deputado_i] += 1
                            print(f"Deputado {deputado_i} e Deputado {deputado_j} votaram em acordo.")
        else:
            return  # Retorna sem imprimir nada caso não haja dados de votação

def get_all_votings():
    url = 'https://dadosabertos.camara.leg.br/api/v2/votacoes?dataInicio=2022-01-01&ordem=DESC&ordenarPor=dataHoraRegistro'
    data = make_request(url)
    graph = {}
    if data:
        for votacao in data['dados']:
            voting_id = votacao['id']
            get_voting_details(voting_id, graph)
    return graph
