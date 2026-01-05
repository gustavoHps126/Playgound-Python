from models.avaliacao import Avaliacao
from models.cardapio.itensCardapio import ItemCardapio


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✔' if self._ativo else '✘'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 <  nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Restaurante não avaliado'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_notas, 1)
        return media
       
    def adicionarCardapio(self, item):
        if isinstance(item, (ItemCardapio)):
            self._cardapio.append(item)
    @property
    def exibir_cardapio(self):
        print(f'Cardápio do Restaurante {self._nome}:\n')

        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_descricao'):
               print(f"{i}. Nome:{item._nome} | Preço: R${item._preco:.2f} | Descrição: {item._descricao}") 
            elif hasattr(item, '_tamanho'):
                print(f"{i}. Nome:{item._nome} | Preço: R${item._preco:.2f} | Tamanho: {item._tamanho}")