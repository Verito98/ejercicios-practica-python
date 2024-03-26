# Diseñar un procedimiento que reciba las dos listas y muestre por pantalla el nombre de todos
# los estudiantes que obtuvieron la máxima nota.

def mayor_nota(alumnos:list, notas:list)->list:
    maxima_nota=[]
    i=0
    for nota in notas:
        if nota == 10:
            maxima_nota.append(alumnos[i])
        i=i+1
    print(maxima_nota)
    
niños=["ale","Juan","Pedro","carla"]
calificacion=[10,5,10,2]

mayor_nota(niños,calificacion)