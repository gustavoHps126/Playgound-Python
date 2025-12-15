"""Pratica 01"""

# maca = int(input("Digite a quantidade de maças vendidas: "))
# banana = int(input("Digite a quantidade de bananas vendidas: "))

# if maca > banana:
#     print(f"Foram vendidas {maca - banana} maças a mais do que bananas")
# elif maca == banana:
#     print(f"Foi um empate ambas, venderam: {maca}")
# else:
#     print(f"Foram vendidas {banana - maca} bananas a mais do que maças")

"""Pratica 02"""
# atv1 = int(input("Digite o tempo necessario para realizar a atv1 : "))
# atv2 = int(input("Digite o tempo necessario para realizar a atv2 : "))
# atv3 = int(input("Digite o tempo necessario para realizar a atv3 : "))

# if atv1 < 0 or atv2 < 0 or atv3 < 0:
#     print("Erro, não pode ser inserido um valor negativo")
# else:
#     print(f"O tempo total para realizar a atividade é: {atv1+atv2+atv3}")

"""Pratica 03"""
# temperatura = int(input("Digite a temperatudo do servidor em Celsius: "))

# if temperatura > 25:
#     print("Alerta! Temperatura acima do limete permitido")
# else:
#     print("Status: OKay")

"""Pratica 04"""
# peso = float(input("Digite seu peso: "))
# altura = float(input("Digite sua altura: "))

# imc =peso/(altura**2)
# imc_arredondado =round(imc,2)

# if imc_arredondado < 18.5:
#     print(f"Você está abaixo do peso, seu IMC é: {imc_arredondado}")
# elif imc_arredondado < 25:
#     print(f"Seu peso é normal, seu IMC é: {imc_arredondado}")
# else:
#     print(f"Você está acima do peso, seu IMC é: {imc_arredondado}")

"""Pratica 05"""

# gastos = float(input("Digite o quanto foi gasto esse mês: "))

# if gastos > 3000.00:
#     print("Atenção, você gatou mais do que deveria bobão")
# else:
#     print("Manteve abaixo do limite de gastos, parabens")

"""Pratica 06"""

# horario = int(input("Digite o horario de chegada: "))

# if horario > 8 and horario <18:
#     print("Acesso liberado")
# elif horario > 24 or horario <0:
#     print("O dia so vai até 24 genio, e abaixo também não tem como")
# else:
#     print("Ta querendo fazer hora extra? Vai pra casa")

"""Pratica 07"""
# n1 = int(input("Digite sua primeira nota : "))
# n2 = int(input("Digite sua primeira segunda : "))
# n3 = int(input("Digite sua primeira terceira : "))

# media = (n1+n2+n3)/3

# if media >= 7 :
#     print("Aprovado parabens")
# elif media < 7 and media >= 5 :
#     print("Tomou recuperação")
# else:
#     print("Reprovado")

"""Pratica 08"""
# distancia = int(input("Digite a distancia percorrida : "))

# if distancia > 200 :
#     print("O pedagio será de R$30,00")
# elif distancia > 100:
#     print("O pedagio será de R$20,00")
# elif distancia < 0:
#     print("Nunca vi viajar distancia negativa")
# else:
#     print("O pedagio será de R$10,00")

"""Pratica 09"""
# numero = int(input("Digite um numero : "))

# if numero%2 != 0:
#     print("Numero impar")
# else:
#     print("Numero par")

"""Pratica 10"""

# renda = int(input("Digite sua renda : "))
# valorp = int(input("Digite valor da parcela a ser paga : "))

# renda30 = renda*0.3

# if renda30 >= valorp and renda >= 2000:
#     print("Emprestimo aprovado")
# else:
#     print("Emprestimo negado, parcela supera 30% da renda ou renda inferior a 2000 ")
