import csv

def cadastrarnotas():
    sair = False
    with open('dados.csv', 'w') as f:
        escritor = csv.writer(f)
        escritor.writerow(['nome', 'nota'])

    while sair == False:
        op = input('Digite o que gostaria de fazer:\n1 - Cadastrar novo usuario\n2 - Sair\n ')

        if op == '1':

            nome = input('Digite o nome do aluno: ')
            nota = input('Digite a nota do aluno: ')

            with open('dados.csv', 'a') as f:
                escritor = csv.writer(f)
                escritor.writerow([nome, nota])

        else:
            with open('dados.csv', 'r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # pula o cabeçalho

                for row in reader:
                    nota = float(row[1])  # CSV lê tudo como texto
                    if nota >= 7:
                        print(row)

            sair = True
            break

cadastrarnotas()
        
