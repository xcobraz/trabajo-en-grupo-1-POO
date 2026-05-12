class Persona:
    def __init__(self,nombre, apellido, numeroDocumentoIdentidad,añoNacimiento):
        self.nombre = nombre
        self.apellido= apellido
        self.numeroDocumentoIdentidad= numeroDocumentoIdentidad
        self.añoNacimiento= añoNacimiento

    def message(self):
        self.message
        print(f"Nombre = {self.nombre}")
        print(f"Apellido = {self.apellido}")
        print(f"numero de documeto de identidad = {self.numeroDocumentoIdentidad}")
        print(f"año de nacimiento = {self.añoNacimiento}")

nombre=input("ingrese nombre: ")
apellido=input("ingrese apellidos: ")
numeroDocumentoIdentidad=input("ingrese numero de documento: ")
añoNacimiento=input("ingrese año de nacimiento: ")

persona1= Persona(nombre, apellido, numeroDocumentoIdentidad,añoNacimiento)
persona1.message()
