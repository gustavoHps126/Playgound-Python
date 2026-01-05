import re

nome = "joão"

def validarNome(nome):
    x = re.findall(r"[0-9]", nome)
    if x:
        print("Digite um nome valido sem numeros")
    else:
        print(f"{nome.capitalize()} cadastrado")

    return

validarNome(nome)

#re.fullmatch() verifica se a string inteira corresponde ao padrão especificado, [A-Z] exige que o nome comece com letra maiuscula e [a-z]* aceita qualquer
#quantidade de letras minusculas depois

#nome = input("Digite o nome do cliente para validação: ")  
#if re.fullmatch(r'[A-Z][a-z]*', nome):
#    print("Nome válido!")
#else:
#    print("Nome inválido!")
