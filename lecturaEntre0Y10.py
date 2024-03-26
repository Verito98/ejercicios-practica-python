valor = int ( input ('Ingrese un número entre 0 y 10: '))

while valor < 0 or valor > 10:
    print ("El valor ingresado esta fuera de rango")
    valor = int ( input ('Ingrese un número entre 0 y 10: '))

print ("El valor esta dentro del rango")