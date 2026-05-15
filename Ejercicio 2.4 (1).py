import math as math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self) -> float:
        return math.pi * math.pow(self.radio, 2)
    
    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self) -> float:
        return self.base * self.altura
    
    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
        
    def calcular_area(self) -> float:
        return math.pow(self.lado, 2)
    
    def calcular_perimetro(self) -> float:
        return 4 * self.lado

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2
    
    def calcular_hipotenusa(self, base, altura) -> float:
        return math.pow(base * base + altura * altura, 0.5) 
    
    def calcular_perimetro(self) -> float:
        return (self.base + self.altura) + self.calcular_hipotenusa(self.base, self.altura)
    
    def tipo_triangulo(self):
        if (self.base == self.altura) and (self.base == self.calcular_hipotenusa(self.base, self.altura)) and (self.altura == self.calcular_hipotenusa(self.base, self.altura)):
            return "Es un triángulo equilátero"
        elif (self.base != self.altura) and (self.base != self.calcular_hipotenusa(self.base, self.altura)) and (self.altura != self.calcular_hipotenusa(self.base, self.altura)):
            return "Es un triángulo escaleno"
        else:
            return "Es un triángulo isósceles"
        
class PruebaFiguras:
    def main():
        circulo = Circulo(5)
        print(f"Área del círculo: {circulo.calcular_area()}")
        print(f"Perímetro del círculo: {circulo.calcular_perimetro()}")
        
        rectangulo = Rectangulo(4, 6)
        print(f"Área del rectángulo: {rectangulo.calcular_area()}")
        print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")
        
        cuadrado = Cuadrado(4)
        print(f"Área del cuadrado: {cuadrado.calcular_area()}")
        print(f"Perímetro del cuadrado: {cuadrado.calcular_perimetro()}")
        
        triangulo = Triangulo(3, 4)
        print(f"Área del triángulo: {triangulo.calcular_area()}")
        print(f"Perímetro del triángulo: {triangulo.calcular_perimetro()}")
        print(triangulo.tipo_triangulo())

if __name__ == "__main__":    
    PruebaFiguras.main()