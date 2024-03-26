# Diseña un procedimiento que, dada una lista de estudiantes, muestre por pantalla
# los datos de todos ellos.
# lista = [["vero","ramirez",18],["caro","gonzalez",13],["sol","perez",20]]

class Persona:
    def __init__(self, nombre1, apellido1, edad1):
        self.nombre = nombre1
        self.apellido = apellido1
        self.edad = edad1
    
    def mostrar_datos (self):
        print(self.nombre)
        print(self.apellido)
        print(self.edad)
        
    def saludar(self):
        print(self.nombre, "dice hola!")
        
lista_estudiantes = [Persona("vero", "ramirez", "44"), Persona("astrid", "solramirez", "22")]#Persona[["vero","ramirez",18],["caro","gonzalez",13],["sol","perez",20]]

for alumno in range(len(lista_estudiantes)):
    persona = lista_estudiantes[alumno]
    persona.mostrar_datos()
