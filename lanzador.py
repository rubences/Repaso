from Repaso.coche import coche
from Repaso.moto import moto
from Repaso.camioneta import camioneta
from Repaso.tipo import tipo
def vehiculos_ruedas(ruedas,list1,list2=[]):
    for i in list1:
        if i.ruedas==ruedas:
            list2.append(i)
            i.catalogar()
    print(f'Se han encontrado {len(list2)}, con {ruedas} ruedas')
def lanzar():
    toyota=coche("azul",4,120,90)
    suzuki=moto("rojo",2,120,125,tipo.urbana)
    mercedes=camioneta("verde",4,100,150)
    list=[toyota,suzuki,mercedes]
    for i in list:
        i.catalogar()
    vehiculos_ruedas(4,list)


