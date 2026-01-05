"""Pratica 01"""

# clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

# for i in clientes:
#     print(i)

"""Pratica 02"""
# contador = 0

# while contador < 10:
#     contador += 1
#     print("Processando dados...")

"""Pratica 03"""
# for i in range(5):
#     print("Ohaio sekai, good morning world!!!")

"""Pratica 04"""
# valores = [10, 20, 30, 40, 50]
# valortotal = 0
# for i in valores:
#     valortotal +=i
# print(valortotal)

"""Pratica 05"""
# projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

# for i in projetos:
#     if i == "None": 
#         print("Projeto ausente")
#     else:  
#         print(i)

"""Pratica 06"""
# livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
# j = 0

# for i in livros:
#     if i == "O Hobbit":
#         j += 1   
#         print(f"O Hobbit foi encontrado na posição {livros.index("O Hobbit")+1}")
#         break

"""Pratica 07"""
# estoque = 10
# while estoque != 0:
#     print(f"Venda realizar: estoque atual: {estoque}")
#     estoque -= 1
# print("Estoque acabou")

"""Pratica 08"""
# for i in range (10,0,-1)
#     if regressiva%2 ==0:
#         print(f"Faltam apenas {regressiva} segundos - Não perca essa oportunidade!")
#     else:
#         print(f"A contagem continua: {regressiva} segundos restantes.")    
# print("Aproveite a promoção agora!")
"""Pratica 09"""
# livros = [
#     {"nome": "1984", "estoque": 5},
#     {"nome": "Dom Casmurro", "estoque": 0},
#     {"nome": "O Pequeno Príncipe", "estoque": 3},
#     {"nome": "O Hobbit", "estoque": 0},
#     {"nome": "Orgulho e Preconceito", "estoque": 2}
# ]

# for i in livros:
#     if (i["estoque"]) == 0:
#         print(f"Livro {i["nome"]} está indisponivel")
#     else:
#         print(f"Livro {i["nome"]} está disponivel")

"""Pratica 10"""
# usuario = input("Digite um nome de usuario com mais de 5 caracteres: ")
# senha = input("Digite uma senha com mais de 8 caracteres: ")

# while len(usuario) < 5 and len(senha) <8:
#         print("Senha ou Nome não condizem com as diretrizes, tente novamente")
#         usuario = input("Digite um nome de usuario com mais de 5 caracteres: ")
#         senha = input("Digite uma senha com mais de 8 caracteres: ")
# print("Usuario cadastrado")