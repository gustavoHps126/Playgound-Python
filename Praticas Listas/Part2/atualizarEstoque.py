
estoque = { 

    "Caderno universitário": 50, 

    "Caneta azul": 120, 

    "Borracha branca": 30 

} 
def atualizar(lista):
    prodName = input('Digite o nome do produto a ser atualizaddor: ')
    prodQuantidade = input('Digite a nova quantidade do produto: ')
    
    lista.update({prodName: prodQuantidade})
    print(lista)

atualizar(estoque)