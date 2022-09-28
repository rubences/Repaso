from Repaso.vehiculo import vehiculo
from Repaso.bicicleta import bicicleta

class moto(vehiculo,bicicleta):
    def __init__(self,color,ruedas,velocidad,cilindrada,tipo):
        super().__init__(color,ruedas,tipo)
        self.velocidad = velocidad
        self.cilindrada =cilindrada
    def catalogar(self):
        print(f'el vehiculo de color {self.color}, con {self.ruedas}, tiene una velocidad de {self.velocidad} km/h , una cilindrada de {self.cilindrada} cc y es de tipo {self.tipo}')