from classes.banco import Banco

class Agencia(Banco):
    def __init__(self, nome, enderecos,numero_agencia):
        super().__init__(nome, enderecos)
        self.numero_agencia = numero_agencia