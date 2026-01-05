"""Pratica 01"""
# def calc_idade (ano_N,ano_H):
#     return f"A idade é {ano_H-ano_N}"

# print(calc_idade(int(input("Digite o ano que nasceu ")),int(input("Digite o ano em que estamos "))))

"""Pratica 02"""
# def tamanho_palavra(palvra_lengh):
#     return f"A palavra tem {len(palvra_lengh)} caracteres"

# print(tamanho_palavra(input("Digite uma palavra ")))

"""Pratica 03"""
# def calc_saudacao(horario):
#     if horario <= 12:
#         saudacao = "Bom dia"
#     elif horario <= 18:
#         saudacao = "Boa tarde"
#     else:
#         saudacao = "Boa noite"
#     return saudacao

# print(calc_saudacao(int(input("Digite um horario entre 0-23 "))))

"""Pratica 04"""
# telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 
# def int_tel (telefones):
#     numeros_int = []
#     for i in telefones:

#         numeros_int.append(int(i))

#     return numeros_int

# print(int_tel(telefones))

"""Pratica 05"""
# valores = input("Digite os valores das vendas: ").split()
# total = sum(map(float, valores))
# print(f"O total de vends foi: {total}")

"""Pratica 06"""
# numeros = input("Digite os numeros separados por espaço: ").split()
# pares = filter(lambda x: int(x) % 2 == 0, numeros)
# print("Numeros pares:", "".join(pares))

"""Pratica 07"""
# prod = ["maca","banada","laranja","motoserra"]
# prec = [13,14,900,12]

# def nomeEpreco(nome, preco):
#     dic_for =  {}
#     j = 0
#     for i in nome:
#         dic_for[i] = preco[j]
#         num += 1
#     return dic_for

# print(nomeEpreco(prod,prec))

"""Pratica 08"""

# a = int(input())
# b = int(input())
# op = (input())


# soma = lambda a , b : a+b

# subtracao = lambda a , b : a-b

# divisao = lambda a , b : a/b if b != 0 else "Erro: Divisão por zero"

# multiplicacao = lambda a , b : a*b 


# if op == "+":
#        print(soma(a,b))
# elif op == "-":
#         print(subtracao(a,b))
# elif op == "/":
#         print(divisao(a,b))
# elif op == "*":
#         print(multiplicacao(a,b))
# else:
#         print("Operador invalido")

"""Pratica 09"""
# def criar_desconto(porcentagem):
#     def calcular_preco(valor):
#         return valor - (valor *(porcentagem / 100))
#     return calcular_preco
        
# desconto = float(input("Digite a porcentagem de desconto: "))  

# calcular_preco_final = criar_desconto(desconto) 

# valor = float(input("Digite o valor da compra: "))  

# print(f"Preço final com desconto: {calcular_preco_final(valor)}") 

"""Pratica 10"""
# def soma_recursiva(n):
#     if n == 1:
#         return 1
#     return n + soma_recursiva(n - 1)

# numero = int(input("Digite um número: ")) 
# print(f"A soma de 1 a {numero} é: {soma_recursiva(numero)}")