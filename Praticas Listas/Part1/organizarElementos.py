convidados = ['Ana', 'Pedro', 'Carlos']

def organizar(convidados):
    print(convidados)
    pessoa = input('Digite o nome da pessoa que quer mudar de posição: ')
    posicao = input('Digite a posição nova dessa pessoa: ')
    convidados.remove(pessoa)
    convidados.insert(int(posicao)-1, pessoa)
    return convidados

print(organizar(convidados))