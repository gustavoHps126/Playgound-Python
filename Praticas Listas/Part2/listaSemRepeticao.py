convidados = []

sair = False

while sair == False:
    nome = input('Digite o nome do convidado (Ou "Sair" para encerrar): ')
    if nome in convidados :
        print('Este nome já foi adicionado à lista de convidados.')
    elif nome.lower() == 'sair':
        sair = True
        print(convidados)
    else:
        convidados.append(nome)
