def sumatorio(lista:list)->int:
    suma=0
    for i in lista:
        suma=suma + i
    return suma

a=[1,2,3]
print(sumatorio(a))