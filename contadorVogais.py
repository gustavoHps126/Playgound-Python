texto = input('Digite um texto para contarmos suas vogais: ')

def contador(texto):
    total = 0
    vogais = 'aeiou'

    for i in texto.lower():
        if i in vogais:
            total += 1
    return total 

print(contador(texto))