cadena = input ("Ingrese frase: ")
k = int(input("Ingrese numero: "))
todas_son_longitud_k= True

letras=0
palabras_long_k=0

for caracter in cadena:
    if caracter == ' ':
        if letras == k:
            palabras_long_k=palabras_long_k+1
            todas_son_longitud_k= True
            letras = 0
        else:
            todas_son_longitud_k= False 
    else:
        letras = letras + 1

if todas_son_longitud_k == True:
        print ("todas las palabras tienen longitud ",k)
    
else:
    print ("No todas las palabras tienen longitud ",k)  
