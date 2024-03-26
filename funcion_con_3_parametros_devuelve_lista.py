def min_max_lista(lista:list)->list:
    max=lista[0]
    min=lista[0]
    for numero in lista:
        if max < numero:
            max=numero
        if numero < min:
            min=numero
    return [min,max]

a=[1,2,3]
print(min_max_lista(a))