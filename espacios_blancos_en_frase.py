#Diseña un programa que lea una cadena y muestre el número de espacios en blanco
#que contiene

a= input ("Ingrese frase: ")
while a != '':
    blanco = 0
    for i in range (len(a)):
         if a[i] == ' ':
             blanco = blanco + 1
    print ("la cantidad de espacios en la frase es ", blanco)
    a= input ("Ingrese frase: ")