# Define una función llamada área_círculo que, a partir del radio de un círculo, devuelva
# el valor de su área. Utiliza el valor 3.1416 como aproximación de π o importa el valor de π que
# encontrarás en el módulo math.
# (Recuerda que el área de un círculo de radio r es πr**2).

def area_circulo(radio:int)->float:
    area=3.1416*(radio**2)
    return area

valor_radio=int(input("Ingrese el radio del circulo: "))

print(area_circulo(valor_radio))