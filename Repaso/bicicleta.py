from Repaso.vehiculo import vehiculo
class bicicleta(vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo
    def catalogar(self):
        print(f'el vehiculo de color {self.color}, con {self.ruedas}, es de tipo {self.tipo}')