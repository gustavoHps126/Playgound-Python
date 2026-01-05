# Macacada
# equipe_a = ["planejar reunião", "revisar documento", "testar sistema"]

# equipe_b = ["testar sistema", "implementar funcionalidade", "corrigir bug"] 

# listaAb = equipe_a + equipe_b
# terminar = True
# j = 1
# while terminar == True:
#     equipe_a.append(equipe_b)
#     for i in listaAb:
#         print(f'{j}. {i}')
#         j += 1
#     idtarefa = input('Digite o numero da tarecfa que deseja remover: ')
#     del listaAb[int(idtarefa) - 1]
#     terminar = False
#     j= 1
#     for i in listaAb:
#         print(f'{j}. {i}')
#         j += 1

equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}  

equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}

tarefas_combinadas = equipe_a.union(equipe_b)
remover = input('Tarefa s ser removida: ').lower()
if remover in tarefas_combinadas:
    tarefas_combinadas.remove(remover)

print(f'Tarefas finais: {tarefas_combinadas}')


