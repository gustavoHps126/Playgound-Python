nome = input("Digite seu nome: ")
cidade = input("Digite sua cidade: ")

def saudacao(nome, cidade):
    return f"Olá, {nome}! Bem-vinda ao sistema da cidade de {cidade}."

print(saudacao(nome, cidade))