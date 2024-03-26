# Diseña una función que calcule el productorio de todos los números que componen
# una lista
def productorio(lista:list)->int:
    resultado=1
    for elemento in lista:
        resultado=1*elemento*resultado
    return resultado

a=[1,2,3]
print(productorio(a))