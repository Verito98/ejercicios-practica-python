print ('Programa para calcular perimetro y area de un rectángulo')

ladoA = float (input ('Ingresa el valor del lado A: '))
ladoB =float (input ('Ingresa el valor del lado B: '))
perimetro = ladoA * 2 + ladoB * 2

area = ladoA * ladoB

print('El perimetro del rectangulo es ' + str (perimetro))
print ('El area del rectangulo es ' + str (area))