from enum import Enum

class TipoCuenta(Enum):
    AHORROS = "AHORROS"
    CORRIENTE = "CORRIENTE"
    
class CuentaBancaria:
    def __init__(self, NombreTitular: str, ApellidosTitular: str, NumeroCuenta: int, Tipocuenta: TipoCuenta, Saldo: float):
        self.NombreTitular = NombreTitular
        self.ApellidosTitular = ApellidosTitular
        self.NumeroCuenta = NumeroCuenta
        self.TipoCuenta = Tipocuenta
        self.Saldo = Saldo
    
    def imprimir(self):
        print(f"Nombre del titular: {self.NombreTitular} {self.ApellidosTitular}")
        print(f"Número de cuenta: {self.NumeroCuenta}")
        print(f"Tipo de cuenta: {self.TipoCuenta.value}")
        print(f"Saldo: ${self.Saldo}")
    
    def consultar_saldo(self) -> float:
        print(f"El saldo actual es: ${self.Saldo}")
    
    def consignar(self, valor: float):
        if (valor > 0):
            self.Saldo += valor
            print("Se ha consignado ${valor} a la cuenta")
        else:
            print("El valor a consignar debe ser mayor a cero")
    
    def retirar(self, valor: float):
        if (valor > 0) and (valor <= self.Saldo):
            self.Saldo -= valor
            print(f"Se ha retirado {valor} en la cuenta. El nuevo saldo es: ${self.Saldo}")
        else:
            print("El valor a retirar debe ser menor que el saldo actual")

def PruebaPrograma():
    cuenta1 = CuentaBancaria("Juan", "Pérez", 123456789, TipoCuenta.AHORROS, 1000.0)
    cuenta1.imprimir()
    cuenta1.consultar_saldo()
    cuenta1.consignar(500.0)
    cuenta1.retirar(200.0)
    
if __name__ == "__main__":
    PruebaPrograma()