import re

receita = "A receita 1087568 foi enviada pelo cliente."

def numeroR(receita):
    #finall encontra todos que batem com os parametros do regex, ele retornara uma lista, o [0] depois dos parametros
    #indica que queremos somente o primeiro itemd dessa lista
    numeroReceita = re.findall(r"\d+", receita)[0]
    print(f"O numero da receita é {numeroReceita}")
    return

numeroR(receita)

