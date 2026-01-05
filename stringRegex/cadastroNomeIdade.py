import re

dados = "Gustavo Pereira - 21"
padrao = r'(\w+) (\w+) - (\d{4})'

resultado = re.search(padrao, dados)

def cadastradoF(resultado):
    if resultado:
        primeiro_nome = resultado.group(1)
        sobrenome = resultado.group(2)
        ano_nascimentp = resultado.group(3)
        print(f"Primeiro Nome: {primeiro_nome}")
        print(f"Sobrenome: {sobrenome}")
        print(f"Ano de Nascimento: {ano_nascimento}")
    else:
        print("Formato inválido!")

