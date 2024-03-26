palabra = input("Ingrese Palabra ")
alfabetica = True
for caracter in range (len(palabra)-1,-1,-1):
    if palabra[caracter] > palabra[caracter-1]:
        alfabetica = False
    
    else:
        alfabetica = True

if alfabetica==True:
    print(" es alfabetica ")

else:
    print("no es alfabetica")