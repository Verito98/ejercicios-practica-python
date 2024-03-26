cantidad_elementos= int(input("Ingrese el total de elementos de la lista: "))
lista = []
for i in range(cantidad_elementos):
    elemento = int(input ("ingrese elemento "))
    if elemento < 0:
        elemento = 0
    lista.append(elemento)
    print(lista)
    
# for valor in lista:
#     if valor < 0:
#         valor = 0 #no funciona
        
# for k in range(len(lista)):
#     if lista[k] < 0:
#         lista[k] = 0

print (lista)