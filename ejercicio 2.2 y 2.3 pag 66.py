from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrrestre"
    ENANO = "Enano"


class Planeta:
    def __init__(self,nombre,cantidad_satelites,masa, volumen , diametro,distancia_sol,tipo_planeta,es_observable):
        self.nombre= str(nombre)
        self.cantidad_satelites = int(cantidad_satelites)
        self.masa = float(masa)
        self.volumen = float(volumen)
        self.diametro = float(diametro)
        self.distancia_sol = float(distancia_sol)
        self.tipo_planeta = (tipo_planeta)
        self.es_observable = bool(es_observable)

    def message (self):
        print(f"Nombre del planeta: {self.nombre}")
        print(f"Numero de satelites: {self.cantidad_satelites}")
        print(f"Masa del planeta: {self.masa}")
        print(f"Volumen del planeta: {self.volumen}")
        print(f"Diametro del planeta{self.diametro}")
        print(f"Distanci al sol: {self.distancia_sol}")
        print(f"Tipo de planeta: {self.tipo_planeta.name}")
        print(f"es observable: {self.es_observable}")

    def calcular_densidad(self):
        return self.masa/self.volumen if self.volumen !=0 else 0
    
    def es_planeta_exterior(self):
        limite = 508632758.0
        return self.distancia_sol > limite

print("ingrese el nombre: ")
nombre = input()
print("ingrese el numero de satelites: ")
cantidad_satelites= input()
print("ingrese la masa : ")
masa= input()
print("ingrese el volumen : ")
volumen=input()
print("ingrese el diametro : ")
diametro= input()
print("ingrese la distancia del sol")
distancia_sol= input()

p1 =Planeta(nombre,cantidad_satelites,masa, volumen , diametro,distancia_sol, TipoPlaneta.TERRESTRE,True)

print("|||||||||||||||||||||||||||||||||||")
p1.message()
print(f"Densidad del planeta = {p1.calcular_densidad()}")
print(p1.es_planeta_exterior())
print("||||||||||||||||||||||||||||||||||||||")





