
participantes = { 

    "Mariana": 25, 

    "Carlos": 32, 

    "Beatriz": 28, 

    "Rafael": 35 

} 

def printfofo(lista):
    participantesN = []
    participantesI = []
    j = 0
    for i in lista:
        participantesN.append(i)
    for i in lista:
        participantesI.append(lista[i])
    print(participantesN)
    print(participantesI)
    print('Participantes e suas idade: ')
    for i in participantesN:
        print(f'- {i}: {participantesI[j]} anos' )
        j += 1
printfofo(participantes)