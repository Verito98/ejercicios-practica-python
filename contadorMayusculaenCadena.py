cadena = input ("Ingrese texto: ")
mayuscula = 0

for caracter in cadena:
    if "A" <= caracter <= "Z":
        mayuscula = mayuscula + 1
        
print ("La cantidad de mayusculas son: ", mayuscula)