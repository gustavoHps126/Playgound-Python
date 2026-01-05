import json
import os


def cadastro():
    arquivo = 'dadosCadatros.json'
    sair = False

    while sair == False:
        try:
#Adiciona os dados do arquivo dadosCadatros na lisa usuarios
            with open ('dadosCadatros.json','r') as f:
                    usuarios = json.load(f)
        except:
                print('Erro')
            

        op = input('Digite o que gostaria de fazer:\n1 - Cadastrar novo usuario\n2 - Sair\n ')

        if op == '2':
            sair = True
            break

        elif op == '1' and os.path.exists(arquivo) == True:

            nome = input('Digite o seu nome de usuario:')
            senha = input('Digite sua senha:' )
            idade = input('Digite sua idade:' )
            cidade = input('Digite sua cidade:' )

            dados = {'nome':nome,'senha':senha,'idade': idade, 'cidade':cidade}
#Adiciona os dados do novo usuario na lista usuario e reescreve o arquivo com a lista atualizada
            with open ('dadosCadatros.json','w') as f:
                usuarios.append(dados)
                json.dump(usuarios, f)
                f.write('\n')
            print('caminho1')
        
        elif op == '1':
            nome = input('Digite o seu nome de usuario:')
            senha = input('Digite sua senha:' )
            idade = input('Digite sua idade:' )
            cidade = input('Digite sua cidade:' )

            dados = {'nome':nome,'senha':senha,'idade': idade, 'cidade':cidade}
#Caso o arquivo não exista ele é criado e o primeiro cadastro é adicionado
            usuarios = []
            usuarios.append(dados)

            with open ('dadosCadatros.json','w') as f:
                json.dump(usuarios, f)
                f.write('\n')
            print('caminho2')

        else:
            op = input('Digite uma opção valida:\n1 - Cadastrar novo usuario\n2 - Sair')

cadastro()
        