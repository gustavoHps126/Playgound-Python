def pedidos():
    pedidos = input('Digite os pedidos separados por ,: ')
    lista = pedidos.split(',')
    opcao = input(f'Gostaria de remover o ultimo item do pedido? S/N\n{lista}')
    if opcao == 'S':
        del lista[-1]
        return f'Item removido\n{lista}'
    else:
        return f'Lista não sofreu alteração\n{lista}'
print(pedidos())