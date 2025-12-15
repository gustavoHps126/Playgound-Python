import random

def adivinha():
    numMaquina = random.randint(1,100)
    numUsuario = 0
    while numUsuario != numMaquina:
        numUsuario = int(input('Tente adivinhar o numero entro 0 e 100: '))
        if numUsuario > numMaquina:
            print('Numero muito alto, tente um menor')
        elif numUsuario < numMaquina:
            print('Numero muito pequeno, tente um maior')
        else:
            print('Você acertou!!!')
            break

adivinha()