#Diseñar un procedimiento que reciba las dos listas y muestre por pantalla el nombre de todos
#los estudiantes cuya calificación es igual o superior a la calificación media.
def media_de_notas(alumnos:list, notas:list)->list:
    sumatoria_de_nota=0
    for nota in notas:
        sumatoria_de_nota=sumatoria_de_nota+nota
    media_nota=sumatoria_de_nota/len(notas)
    
    estudiantes=[]
    i=0
    for alumno in range(len(alumnos)):
        if notas[i] >= media_nota:
            estudiantes.append(alumnos[len(alumno)-1])
    print(estudiantes)


niños=["ale","Juan","Pedro","carla"]
calificacion=[10,5,10,2]

media_de_notas(niños,calificacion)


        
        