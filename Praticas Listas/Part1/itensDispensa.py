itens = ['Arroz','Açucar','Pão']

def listaCompras(itens):
    busca = input('Digite o item que procura: ')
    if busca in itens:
            return f'{busca} está em sua lista'
    else:
        return f'{busca} não foi encontrado'

print(listaCompras(itens))