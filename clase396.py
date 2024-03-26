# Diseña un procedimiento que, dada una lista de estudiantes y un grupo (la letra A,
#B o C), muestre por pantalla un listado completo de dicho grupo

class Persona:
    def __init__(self,nombre):
        self.nombre = nombre
       
    def mostrar_listado(self):
        print(self.nombre)
       

A = [Persona("carla"),Persona("sol"),Persona("sole")]

for elemento in A:
    elemento.mostrar_listado()

