cadena = input ("Escribe una frase: ")
while cadena != '':
    cambios = 0
    anterior = ''
    for caracter in cadena:
        if caracter == ' ' and anterior != ' ':
             cambios = cambios + 1
        anterior = caracter
    palabras = cambios + 1
    print ("palabras: ", palabras)
    cadena = input ("Escribe una frase: ")
        