# Diseña un método que permita determinar si una persona es menor de edad devolviendo cierto, 
# si la edad es menor que 18, o falso, en caso contrario.
class Persona:
    def __init__(self, nombre_variable, edad_variable):
        self.nombre = nombre_variable
        self.edad = edad_variable
    
    def es_menor_de_edad(self):
        if self.edad < 18:
            print ("es menor")
        
        else:
            print("no es menor")
        
Pedir_nombre= input("ingrese el nombre de la persona: ")
Pedir_edad = int(input("ingrese la edad de la persona"))

objeto_persona = Persona(Pedir_nombre,Pedir_edad)

objeto_persona.es_menor_de_edad()