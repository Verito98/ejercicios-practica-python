#158) Diseña un programa que lea una cadena y un número entero k y nos diga cuántas
#palabras tienen una longitud de k caracteres
cadena = input ("Ingrese frase: ")
k = int(input ("Ingrese un numero: "))

while cadena != '':
    contador = 0
    longitud = 0
    
    for caracter in cadena:
        cantidadLetra = 0
        contador = contador + 1
        
        if caracter != ' ':
            cantidadLetra = cantidadLetra + 1
        
        if cadena[(len(cadena)-1)] or cadena[contador] == ' ':
            if cantidadLetra == k:
                longitud = longitud + 1
    print ("la cantidad de palabras de ", k,"caracteres son: ", longitud)
    
    cadena = input ("Ingrese frase: ")
    k = int(input ("Ingrese un numero: "))