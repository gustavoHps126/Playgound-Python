class Veiculo:
    def __init__(self, marca, modelo, ligado):
        self.marca = marca
        self.modelo = modelo
        self._ligado = ligado

        def __str__(self):
            return f"Veículo: {self.marca} {self.modelo} - Ligado: {self._ligado}"