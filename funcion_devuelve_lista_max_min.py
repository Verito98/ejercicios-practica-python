# Diseña una función que reciba una lista de enteros y devuelva los números mínimo
# y máximo de la lista simultáneamente
def max_min(lista:list)->list:
    max=lista[0]
    min=lista[0]
    for elemento in lista:
        if elemento>max:
            max=elemento
        if elemento<min:
            min=elemento
    
    return [max, min]

a=[1,3,7,2,-3]
print(max_min(a))