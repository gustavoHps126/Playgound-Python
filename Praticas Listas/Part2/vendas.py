
vendas = { 

    "Eletrônicos": [ 

        {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000}, 

        {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500} 

    ], 

    "Eletrodomésticos": [ 

        {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000}, 

        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800} 

    ], 

    "Livros": [ 

        {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50}, 

        {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100} 

    ] 

} 

def somarVendas(listaVendas):
    vendas1 = 0
    vendas2 = 0
    vendas3 = 0
    for i in range(len(listaVendas['Eletrônicos'])):
        quantidade = listaVendas['Eletrônicos'][i]['quantidade']
        valor = listaVendas['Eletrônicos'][i]['valor_unitario']
        vendas1 += quantidade * valor 
    

    for i in range(len(listaVendas['Eletrodomésticos'])):
        quantidade = listaVendas['Eletrodomésticos'][i]['quantidade']
        valor = listaVendas['Eletrodomésticos'][i]['valor_unitario']
        vendas2 += quantidade * valor

    for i in range(len(listaVendas['Livros'])):
        quantidade = listaVendas['Livros'][i]['quantidade']
        valor = listaVendas['Livros'][i]['valor_unitario']
        vendas3 += quantidade * valor

    print(f'Eletrônicos: {vendas1}\nEletrodomésticos: {vendas2}\nLivros: {vendas3}')
    return

somarVendas(vendas)