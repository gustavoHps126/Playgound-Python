def media():
    numeros = input('Digite os numeros separados por ,: ')
    lista = numeros.split(',')
    total = 0
    for i in lista:
        total += int(i)
    return total/len(lista)

print(media())