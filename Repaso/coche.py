from Repaso.vehiculo import vehiculo
class coche(vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindrada):
        super().__init__(color,ruedas)
        self.velocidad = velocidad
        self.cilindrada =cilindrada
    def catalogar(self):
        print(f'el vehiculo de color {self.color}, con {self.ruedas}, tiene una velocidad de {self.velocidad} km/h y una cilindrada de {self.cilindrada} cc')