# 390. modifica el programa del ejercicio anterior para que muestre el nombre de la persona de mas edad
# si dos o mas personas tienen la misma edad, el programa mostrará el nombre de todas ellas

class Persona:
    def __init__(self, apellido, nombre, dni, edad):
         self.apellido = apellido
         self.nombre = nombre
         self.dni = dni
         self.edad = edad
        
pedir = input ("Desea continuar introduciendo personas?: ")
lista_personas = []
while pedir == "si":
     ape1 = input ("ingresar apellido: ")
     nom1 = input ("ingresar nombre: ")
     dni1 = input ("ingresar dni: ")
     edad1 = input ("ingresar edad: ")
     persona1 = Persona("", nom1, "", edad1)
    
     persona1 = Persona(ape1, nom1, dni1, edad1)
     lista_personas.append(persona1)
     pedir = input ("Desea continuar introduciendo personas?: ")
    
mayor_edad = lista_personas[0].edad
mayores =[]
for i in range (len(lista_personas)):
    if (lista_personas[i].edad >= mayor_edad):
        mayor_edad = lista_personas[i].edad 
        mayores.append (lista_personas[i])
        
print (lista_personas)
print (mayores)