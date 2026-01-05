def cadastrarProd():
    prods = []
    terminar = False
    while terminar == False:
        nome = input('Digite o nome do produto(Digite Sair para terminar): ')
        quantidade = input('Digite a quantidade do produto(Digite Sair para terminar): ')
        
        if nome == 'sair' or quantidade == 'sair':
            print(prods)
            break
        else:
            produto = ({
                'Nome': nome,
                'Quantidade':quantidade
            })
            prods.append(produto)
            print(prods)
        

cadastrarProd()