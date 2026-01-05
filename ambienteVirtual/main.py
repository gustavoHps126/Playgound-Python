from fastapi import FastAPI, Query
import requests
app = FastAPI()

@app.get('/api/hello')
def hello_world():
    """
    Endpoint de teste que retorna uma mensagem simples. 

    
    """
    return {'Hello':'World!'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    """
    Endpoint que retorna o cardápio dos restaurantes.

    
    """
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    print(response)


    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        
        dadosRestaurantes = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dadosRestaurantes.append({
                'item': item['Item'],
                'price': item['price'],
                'description': item['description']
                })
        return {'Restaurante':restaurante, 'Cardapio': dadosRestaurantes}
    else:
        print(f'Erro ao acessar a API: {response.status_code} - {response.text}')
