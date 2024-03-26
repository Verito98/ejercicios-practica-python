cadena = input ("Ingrese frase: ")
k = int(input("Ingrese numero: "))

letras=0
palabras=0

for caracter in cadena:
    if caracter == ' ':
        if letras == k:
            palabras = palabras + 1
        
        else:
            letras = 0
    
    else:
        letras = letras + 1
        
print ("La cantidad de palabras de longitud", k, "es: ", palabras)