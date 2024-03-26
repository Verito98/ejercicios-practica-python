# Diseñar un procedimiento que reciba las dos listas y muestre por pantalla el nombre de todos
# los estudiantes que aprobaron el examen.

def aprobados(alumnos:list,notas:list)->list:
     aprobados=[]
     i=0
     for elemento in alumnos:
         if notas[i] >= 4:
             aprobados.append(elemento)
         i=i+1
     print(aprobados)


niños=["Juan","Pedro","Alexis","Sole"]
calificacion=[10,2,6,1]

aprobados(niños,calificacion)





