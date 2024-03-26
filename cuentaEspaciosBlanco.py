cadena = input ("Ingrese frase: ")
anterior = ''
espacio = 0
for caracter in cadena:
    if caracter == ' ' and anterior != ' ':
        espacio = espacio + 1
    anterior = caracter
print ('La cantidad de espacios en blanco es: ', espacio)
