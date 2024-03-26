cadena = input ("Ingrese frase: ")
espacios = 0
for caracter in cadena:
    if caracter == ' ':
        espacios = espacios + 1
print ("La cantidad de espacios en blanco es: ", espacios)