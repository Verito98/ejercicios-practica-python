# diseña un programa que pida por teclado los datos de varias personas
# y los añada a una lista inicialmente vacia. Cada vez qus se lean los datos de una persona,
# el programa preguntará si se desea continuar introduciendo mas personas.
# Cuandor responda que no, se detiene

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
    
    persona1 = Persona(ape1, nom1, dni1, edad1)
    lista_personas.append(persona1)
    pedir = input ("Desea continuar introduciendo personas?: ")
    
print (lista_personas)
    
    
    
