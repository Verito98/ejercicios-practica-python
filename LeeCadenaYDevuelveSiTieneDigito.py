cadena = input ("Ingrese texto: ")
digito = False

for caracter in cadena:
    if "0" <= caracter <= "9":
        digito = True

if digito == True:
    print ("El texto contiene digito")

else:
    print("El texto no contiene digito")
