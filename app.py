import requests

# Função para fazer a requisição à API
def make_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Função para obter as informações de votos de uma votação específica
def get_voting_details(voting_id):
    url = f'https://dadosabertos.camara.leg.br/api/v2/votacoes/{voting_id}/votos'
    data = make_request(url)
    if data:
        votes = data['dados']
        for vote in votes:
            if 'deputado_' in vote:
                deputado = vote['deputado_']['nome']
                tipoVoto = vote['tipoVoto']
                print(f"Deputado: {deputado} | Seu Voto: {tipoVoto}")
            else:
                print("Informações do deputado não encontradas")
        else:
            print("null")
    else:
        print("Erro de requisição")

# Função para obter todas as votações
def get_all_votings():
    url = 'https://dadosabertos.camara.leg.br/api/v2/votacoes'
    data = make_request(url)
    if data:
        for votacao in data['dados']:
            voting_id = votacao['id']
            print('\n'+ voting_id)
            get_voting_details(voting_id)
            

# Executa a função para obter todas as votações
get_all_votings()
