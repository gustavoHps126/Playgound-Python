import random

def jogo ():
    jogador = input('Escolha o que jogar ').lower()
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_computador = random.choice(opcoes)
    if jogador == escolha_computador:
        print('Empate')
        return
    elif ( 
    (jogador == "pedra" and escolha_computador == "tesoura") or 
    (jogador == "papel" and escolha_computador == "pedra") or 
    (jogador == "tesoura" and escolha_computador == "papel") 
    ): 
        print('Você venceu')
    elif jogador not in opcoes:
        print('Escolha invalida')
    else:
        print('Você perdeu')
        

jogo()