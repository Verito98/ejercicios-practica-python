cadena = input ("Ingrese frase: ")
k = int(input("Ingrese numero: "))

letras=0

for caracter in cadena:
    if caracter == ' ':
        if letras < k:
            print ("Hay palabras cortas")
        
        else:
            print ("Hay palabras largas")