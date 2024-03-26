numero = int (input ("Ingrese valor limite positivo: "))
i = 2
while i <= numero:
    for i in range (i, numero+1):
        print (i, "esta entre 2 y ", numero, "; y es positivo")
    i = i+1