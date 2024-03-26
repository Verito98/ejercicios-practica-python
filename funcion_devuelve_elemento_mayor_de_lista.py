def maximo(lista:list)->int:
    maximo = lista[0]
    for elemento in lista:
        if maximo < elemento:
            maximo = elemento
    return maximo

cantidad=int(input("cuantos elementos tiene la lista?: "))
valores=[]
for elemento in range (cantidad):
    valor=int(input("ingrese elemento de la lista: "))
    valores.append(valor)

print(maximo(valores))