from Repaso.vehiculo import vehiculo
from Repaso.coche import coche
class camioneta(vehiculo,coche):
    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        super().__init__(color,ruedas,velocidad,cilindrada,carga)
        self.carga = carga
    def catalogar(self):
        print(f'el vehiculo de color {self.color}, con {self.ruedas}, tiene una velocidad de {self.velocidad} km/h , una cilindrada de {self.cilindrada} cc y una carga de {self.carga} kg')