palavra = "gustavoHenriquePereira"

def pistas(palavra):
    #Slicing, retorna a parte da string definida dentro das chaves, 3 depois do : devolve os 4 primeiros caracteres, e -3 antes dos :
    # os 4 ultimos, o depois dos : é o limite e o antes é o inicio
    pistaInicio = palavra[:3]
    pistaFim = palavra[-3:]

    print(f"Sua palavra começa com {pistaInicio} e termina com {pistaFim}")
    return

pistas(palavra)