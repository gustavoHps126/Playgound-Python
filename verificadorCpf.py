cpf = input('Digite seu CPF:')

def verificarCPF(cpf):
    tamanhoCpf = len(cpf)
    if tamanhoCpf != 10 or type(cpf) == str:
        return 'Digite um cpf valido'
    else:
        return f'O cpf {cpf} é valido'

print(verificarCPF(cpf))
