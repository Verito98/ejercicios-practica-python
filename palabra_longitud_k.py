cadena = input ("Ingrese frase: ")
k = int(input("ingrese numero: "))
letras=0
palabras=0

for caracter in cadena:
    if caracter != ' ':
        letras = letras + 1
    
    if letras == k and cadena[len(caracter)+1] == ' ':
        palabras = palabras + 1
        letras = 0

print("la cantidad de palabras de longitud", k, "es: ", palabras)