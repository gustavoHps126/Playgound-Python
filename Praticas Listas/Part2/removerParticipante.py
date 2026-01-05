
participantes = { 

    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

} 

def remover(lista):
     nomeRemover = input('Quem você quer remover? ')
     for workshop, pessoas in participantes.items():
        if nomeRemover in pessoas:
            pessoas.discard(nomeRemover)
            print(f'{nomeRemover} removido do {workshop}')
            print(participantes)
            return
     print('Não achei esse mlk')
     print(participantes)

remover(participantes)