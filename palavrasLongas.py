texto = input('Digite seu texto para contarmos as palavras longas: ')

def contador(texto):
    total = 0

    for i in texto.split():
        if len(i) >= 9:
            total += 1
        
        if total == 0:
            print('Nenhuma palavra grande identificada')
    return total

print(contador(texto)) 