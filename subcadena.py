# *192) Diseña un programa que, dados una cadena c, un índice i y un número n, muestre la
# subcadena de c formada por los n caracteres que empiezan en la posición de índice i.
cadena = input ("Ingrese frase: ")
i = int(input ("Ingrese un numero: "))
n = int(input ("Ingrese un numero: "))
subcadena = ''
for variable in range(i, n+1):
    subcadena = subcadena + cadena[variable]
print ("la subcadena es: ", subcadena)
    