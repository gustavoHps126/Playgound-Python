import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)


if response.status_code == 200:
    dados_json = response.json()
    dadosRestaurantes = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dadosRestaurantes:
            dadosRestaurantes[nome_do_restaurante] = []

        dadosRestaurantes[nome_do_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
            })
        
else:
    print(f'Erro ao acessar a API: {response.status_code}')

for nomeRestaurante, dados in dadosRestaurantes.items():
    nome_do_arquivo = f'{nomeRestaurante}.json'
    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante,indent=4)