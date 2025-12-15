import os

def tarefas():
    encerrar = False
    tarefas = []
    
    while encerrar == False:
        os.system("cls")
        j = 0
        print('1. Adicionar tarefa\n2. Remover tarefa\n3. Visualizar tarefas\n4. Sair')
        escolha = int(input('Digite um menu que gostaria de acessar: '))
        
        if escolha == 1:
            os.system("cls")
            tarefaNova = input('Digite a tarefa que gostaria de adicionar: ')
            tarefas.append(tarefaNova)
            print('Tarefa adicionada')

        elif escolha == 2:
            os.system("cls")
            for i in tarefas:
                j += 1
                print(f'{j}: {i}')
            remover = int(input('Digite o numero do item que deseja remover da sua lista:'))
            del tarefas[remover-1]       

        elif escolha == 3:
            os.system("cls")
            for i in tarefas:
                j += 1
                print(f'{j}: {i}')
                input('Digite qualquer numero para retornar: ')

        elif escolha == 4:
            os.system("cls")
            encerrar = True

tarefas()


