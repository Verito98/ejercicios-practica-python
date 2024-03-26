cadena = input ("Ingrese frase: ")
k = int(input("Ingrese numero: "))

letras=0

for caracter in cadena:
    if caracter == ' ':
        if letras == k:
            print ("la cadena contiene letra longitud ",k)
        
        else:
            letras = 0
    
    else:
        letras = letras + 1
        