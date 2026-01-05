import re

texto = "O dia está bom, tudo está bom."
x = "bom"
y = "Otimo"

def substituir(texto, substituido, substitui):
    #O metodo sub, é o que faz a substituição dos valores,r e f juntos permite utilizar o regex com variaveis como argumentos, /b /b define o que vai ser substituido enquanto os dois
    # argumentos apos a , são o que vai entrar no lugar no antigo e o segundo o texto onde a operação ocorrera 
    x = re.sub(rf'\b{substituido}\b', substitui, texto)
    print(x)
    return

substituir(texto, x, y)

