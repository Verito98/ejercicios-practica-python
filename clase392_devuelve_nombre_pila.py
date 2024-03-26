# Diseña un método nombre_de_pila que devuelva el nombre de pila de una Persona.
# Supondremos que el nombre de pila es la primera palabra del atributo nombre (es decir, que no
# hay nombres compuestos).
class Persona:
    def __init__(self, nombre1, apellido1):
        self.nombre = nombre1
        self.apellido = apellido1
    
    def nombre_de_pila (self):
            print (persona.nombre)
        
nombre_persona = input("ingrese nombre de la persona: ")
apellido_persona = input("ingrese apellido de la persona: ")

persona = Persona(nombre_persona,apellido_persona)

persona.nombre_de_pila()