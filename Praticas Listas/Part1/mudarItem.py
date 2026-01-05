lista = ['Ana', 'João', 'Pedro']
def trocarRegistro(lista):
    posicao = input(f'Digite a posição do item que deseja remover\n{lista}')
    novoItem = input(f'Digite o item que substuira o da posição {posicao}: ')
    del lista[int(posicao)-1]
    lista.insert(int(posicao)-1, novoItem)
    return lista

print(trocarRegistro(lista))
    