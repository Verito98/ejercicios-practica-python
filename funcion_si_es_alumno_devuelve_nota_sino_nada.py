#Diseñar una función que reciba las dos listas y un nombre (una cadena); si el nombre está
#en la lista de estudiantes, devolverá su nota, si no, devolverá None
def es_alumno(estudiantes:list, notas:list, cadena:str)->int:
    for alumno in range(len(estudiantes)):
        if estudiantes[alumno] == cadena:
            return print(notas[alumno])

a=["Ana", "Sol", "Juan", "Pedro"]
b=[10,5,3,4]
nombre=input("Ingrese nombre del alumno: ")

es_alumno(a,b,nombre)