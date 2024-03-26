# Inicio código
class Persona:
    def __init__ (self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

toni = Persona("Antonio Pérez","98761234Q",20)
juan = Persona("Juan Perez","12345678Z",19)
pedro = Persona("Pedro Lopez", "23456789D",18)

print("-- Datos de toni --")
print (toni.nombre)
print (toni.dni)
print (toni.edad)

alumnos = [toni]
alumnos.append(juan)
alumnos.append(pedro)

print("-- DNI de alumnos --")
for alumno in alumnos:
    print(alumno.dni)

print("-- Nombre de alumnos --")
for i in range(len(alumnos)):
    print(alumnos[i].nombre)

# Fin código
