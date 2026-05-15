from enum import Enum

class TipoA(Enum):
    CIUDAD = "CIUDAD"
    SUBCOMPACTO = "SUBCOMPACTO"
    COMPACTO = "COMPACTO"
    FAMILIAR = "FAMILIAR"
    EJECUTIVO = "EJECUTIVO"
    SUV = "SUV"

class TipoColor(Enum):
    BLANCO = "BLANCO"
    NEGRO = "NEGRO"
    ROJO = "ROJO"
    NARANJA = "NARANJA"
    AMARILLO = "AMARILLO"
    VERDE = "VERDE"
    AZUL = "AZUL"
    VIOLETA = "VIOLETA"
    
class TipoCom(Enum):
    GASOLINA = "GASOLINA"
    BIOETANOL = "BIOETANOL"
    DIESEL = "DIESEL"
    BIODIESEL = "BIODIESEL"
    GAS_NATURAL = "GAS_NATURAL"
        
    
class Automovil:
    def __init__(self, marca: str, modelo: int, motor: int, tipo_combustible: TipoCom, tipo_automovil: TipoA, numero_puertas: int, cantidad_asientos: int, velocidad_maxima: int, color: TipoColor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = 0
        
    def acelerar(self, incremento_velocidad: int):
        if self.velocidad_actual + incremento_velocidad <= self.velocidad_maxima:
            self.velocidad_actual += incremento_velocidad
        else:
            print("No se puede acelerar más allá de la velocidad máxima del automovil.")
            
    def desacelerar(self, decremento_velocidad: int):
        if (self.velocidad_actual - decremento_velocidad) >= 0:
            self.velocidad_actual -= decremento_velocidad
        else:
            print("No se puede desacelerar por debajo de 0 km/h.")
    
    def frenar(self):
        self.velocidad_actual = 0
    
    def calcular_tiempo_llegadad(self, distancia: int) -> float:
        if self.velocidad_actual == 0:
            return float('inf')  
        return distancia / self.velocidad_actual
    
    def imprimir(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor} cc")
        print(f"Tipo de Combustible: {self.tipo_combustible.value}")
        print(f"Tipo de Automóvil: {self.tipo_automovil.value}")
        print(f"Número de Puertas: {self.numero_puertas}")
        print(f"Cantidad de Asientos: {self.cantidad_asientos}")
        print(f"Velocidad Máxima: {self.velocidad_maxima} km/h")
        print(f"Color: {self.color.value}")
        print(f"Velocidad Actual: {self.velocidad_actual} km/h")
    
if __name__ == "__main__":
    auto1 = Automovil("Toyota", 2020, 1800, TipoCom.GASOLINA, TipoA.COMPACTO, 4, 5, 200, TipoColor.ROJO)
    
    auto1.imprimir()
    
    auto1.velocidad_actual = 100
    print(f"Tiempo estimado para recorrer 150 km: {auto1.calcular_tiempo_llegadad(150):.2f} horas")
    
    auto1.acelerar(50)
    print(f"Velocidad actual después de acelerar: {auto1.velocidad_actual} km/h")
    
    auto1.desacelerar(30)
    print(f"Velocidad actual después de desacelerar: {auto1.velocidad_actual} km/h")
    
    auto1.frenar()
    print(f"Velocidad actual después de frenar: {auto1.velocidad_actual} km/h")
    auto1.desacelerar(10) 