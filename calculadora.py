def calc():
    erro = True

    while erro == True:
        try:
             x = int(input('Digite o primeiro numero: '))
             operador = input('Digite o operador: ')
             y = int(input('Digite o segundo numero: '))
             if operador == '+':
                return x + y
                erro = False
             elif operador == '-':
                return x - y
                erro = False
             elif operador == '/':
                return x / y
                erro = False
             elif operador == '*':
                return x * y
                erro = False
             else:
                print("Operação inválida!")
                erro = True
        except:
            print('Algo deu errado tente novamente')
            erro = True

print(calc())