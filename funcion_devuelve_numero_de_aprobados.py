# Diseñar una función que reciba la lista de notas y devuelva el número de aprobados.
def cantidad_aprobados(notas:list)->int:
    contador=0
    for elemento in notas:
        if elemento >=4:
            contador=contador+1
    return contador

a=[10,5,6,1,2,3]
print(cantidad_aprobados(a))