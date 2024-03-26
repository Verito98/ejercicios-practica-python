#Diseña un programa que lea una cadena y muestre el número de letras mayúsculas
#que contiene
a = input ("Ingrese frase: ")

while a != '':
    mayuscula = 0
    for i in range (len(a)):
        if 'A' <= a[i] <= 'Z':
             mayuscula = mayuscula + 1
    print ("la cantidad de mayúsculas en la frase es ", mayuscula)
    a = input ("Ingrese frase: ")