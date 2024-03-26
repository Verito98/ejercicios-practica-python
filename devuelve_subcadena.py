cadena = input ("ingrese frase: ")
i = int (input("ingrese desde que posicion quiere la subcadena: "))
j = int (input("ingrese hasta que posicion quiere la subcadena: "))
         
cadena_vacia = ''
for caracter in range(i,j):
    cadena_vacia = cadena_vacia + cadena[caracter]
print (cadena_vacia)