c= input ("Ingrese cadena: ")
i = int (input("Ingrese principio de subcadena :"))
n = int (input("Ingrese final de subcadena :"))
subcadena =''

for caracter in range(i, n+1):
    subcadena= subcadena + c[caracter]
print("la resultante es ", subcadena)