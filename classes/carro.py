from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ligado, portas):
        super().__init__(marca, modelo, ligado)
        self.portas = portas

    def __str__(self):
        return f"Carro: {self.marca} {self.modelo} - Portas: {self.portas} - Ligado: {self._ligado}"