import re

cpf = "181.191.206-04"

def validandoCpf(cpf):
    # definindo um padrão para o cpf,\d{3}\ define que vai ter 3 digitos e então um . e no final que terá 2 um - e depois 2 digitos
    padrao = r'\d{3}\.\d{3}\.\d{3}-\d{2}'
    
    if re.search(padrao, cpf):
        print("O cpf está correto")
    else:
        print("Digite um cpf valido")
    return

validandoCpf(cpf)