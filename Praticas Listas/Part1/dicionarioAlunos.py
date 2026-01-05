def dicionarioAlunos():
    dados = input('Digite os dados do aluno separados por , Nome,Idade,Nota: ')
    dadosSeparados = dados.split(',')
    dicionarioDados = {}
    dicionarioDados['nome'] = dadosSeparados[0]
    dicionarioDados['idade'] = dadosSeparados[1]
    dicionarioDados['nota'] = dadosSeparados[2]
    return dicionarioDados

print(dicionarioAlunos())