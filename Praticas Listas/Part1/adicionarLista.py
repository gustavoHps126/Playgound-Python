def countVoluntarios():
    voluntarios = []
    parar = False
    while parar != True:
        nome = input(f'Digite o nome do voluntarios(Ou {'Sair'} para encerrar): ')
        if nome == 'Sair':
            parar = True
        else:
            voluntarios.append(nome)
    return voluntarios

print(countVoluntarios())