#Define un método está_aprobado que devuelva True si el alumno ha aprobado la
#asignatura y False en caso contrario.

class Persona:
    def __init__(self,alumno,nota):
        self.alumno = alumno
        self.nota = nota
    
    def esta_aprobado(self):
        if self.nota > 4:
            print ("True")
        
        else:
            print ("False")

nombre_alumno = input("ingrese nombre del alumno: ")
nota_alumno = int(input("ingrese la nota del alumno: "))

objeto_alumno = Persona(nombre_alumno,nota_alumno)

objeto_alumno.esta_aprobado()