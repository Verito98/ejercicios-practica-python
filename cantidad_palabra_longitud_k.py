cadena = input ("Ingrese texto: ")
k = int (input ("ingrese numero: ")) 
cantidad_k = 0
contador = 0

for caracter in cadena:
    if caracter != " " or caracter == '': #caracter in range (len(cadena,-1,-1))
        contador = contador + 1
    
    else:
        if contador == k:
            cantidad_k = cantidad_k + 1
            contador = 0
            
print ("La cantidad de palabras de longitud ", k, "son ", cantidad_k)