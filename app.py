import requests

params = {
    'itens': 20  
}

response = requests.get('https://dadosabertos.camara.leg.br/api/v2/votacoes', params=params)

if response.status_code == 200:
    data = response.json()  
    votacoes = data['dados']
    
    # Itera sobre as votações
    for votacao in votacoes:
        votacao_id = votacao['id']
        print(f'ID da votação: {votacao_id}')
        
        votos_response = requests.get(f'https://dadosabertos.camara.leg.br/api/v2/votacoes/{votacao_id}/votos')
        
        if votos_response.status_code == 200:
            votos_data = votos_response.json()
            votos = votos_data['dados']
            print(votos)
            
            for voto in votos:
                deputado_nome = voto['nome']
                voto_votou = voto['voto']
                
                print(f'Deputado: {deputado_nome} - Voto: {voto_votou}')
                
        else:
            print('Erro ao obter os votos da votação.')
        print('---')
else:
    print('Erro ao obter as votações.')
