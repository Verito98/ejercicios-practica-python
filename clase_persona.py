class Persona:
    def __init__ (self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        
class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def acelerar(velocidad):
        print("vas a una velocidad de: ", velocidad)

class Ventas:
    def calcularIva(precio):
        precio * 1.21

toni = Persona("Antonio Pérez","98761234Q",20)
juan = Persona("Juan Perez","12345678Z",19)

auto1 = Auto("Gol", 2010)

#print(juan.edad, auto1.marca)
auto1.acelerar("1")




