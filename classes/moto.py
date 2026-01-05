from veiculo import Veiculo
class Moto(Veiculo):
    def __init__(self, marca, modelo, ligado, estilo):
        super().__init__(marca, modelo, ligado)
        self.estilo = estilo

    def __str__(self):
        return f"Moto: {self.marca} {self.modelo} - Estilo: {self.estilo} - Ligada: {self._ligado}"