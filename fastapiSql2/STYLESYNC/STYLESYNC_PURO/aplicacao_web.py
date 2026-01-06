from wsgiref.simple_server import make_server


#Função basica para teste retornando um html 
def aplicacao(environ, start_response):

#Simulando dados de uma api/servidor
    produtos = [
        {'nome': 'Notebook', 'Valor': 7499.99},
        {'nome': 'PC', 'Valor': 10499.99},
        {'nome': 'Air fryer', 'Valor': 2499.9},
        {'nome': 'Monitor', 'Valor': 5499.99},
        {'nome': 'Impressora', 'Valor': 499.99}
    ]
#Listando produtos
    linhas_html = ''
    for produto in produtos:
        linhas_html += f'<li>{produto['nome']} - {produto['Valor']}</li>'

    start_response('200 Ok', [('Content-type', 'text;html;charset-utf-8')])


#Abre o arquivo html como read
    with open ('index.html', 'r', encoding='utf-8') as file:
        html = file.read()

#Substitui {{Produtos}} do arquivo html pela listagem dos itens
    html_final = html.replace('{{Produtos}}', linhas_html)
    
    return[html_final.encode('utf-8')]

#Configuração do servidor, host, porta, função, e metodo para manter ele rodando até quando for pedido para encerrar(serve_forever())
make_server('', 5000, aplicacao).serve_forever()