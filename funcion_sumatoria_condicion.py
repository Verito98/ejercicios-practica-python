# Diseña una función que calcule SUMATORIA i hasta b desde i=a dados a y b. Si a es mayor que b, la función
# devolverá el valor 0
def sumatoria (a:int,b:int)->int:
    i=a
    suma_ab=0
    for i in range(b+1):
        if a<b:
            suma_ab=suma_ab+i
            i=i+1
        else:
            print("0")
    return suma_ab

inicio=int(input("ingrese el valor desde el que quiere sumar: "))
fin=int(input("ingrese el valor final que quiere sumar: "))
print("la sumatoria entre a y b es: ", sumatoria(inicio,fin))