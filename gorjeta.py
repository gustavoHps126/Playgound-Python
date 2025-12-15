valorConta = int(input('Digite o valor da conta: '))
valorGorjeto = int(input('Digeite a porcentagem da gorjeta: '))

def calcularGorjeta(valor,gorjeta):
    try:
        gorjeta = gorjeta/100
        gorjetaAplicada = valorConta*gorjeta
        contaTotal = valorConta+gorjetaAplicada
    except:
        return 'Digite um valor valido, somente numeros'
    return f'Valor da gorjeta: {gorjetaAplicada:.2f}R$\nValor total da conta: {contaTotal:.2f}R$'

print(calcularGorjeta(valorConta,valorGorjeto))