from models.cardapio.itensCardapio import ItemCardapio

class sobremesa(ItemCardapio):
    def __init__(self,nome,preco,descricao):
        super().__init__(nome, preco)
        self._descricao = descricao
        
    def __str__(self):
        return f"{self._nome} - R${self._preco:.2f}\nDescrição: {self._descricao}"
    
 
    def aplicarDesconto(self):
        self._preco -= (self._preco * 0.10)