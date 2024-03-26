print ('Programa para calcular perimetro y área de un triángulo')

from math import sqrt

ladoA = float( input('Valor de lado A: '))
ladoB = float( input('Valor de lado B: '))
ladoC = float( input('Valor de lado C: '))

perimetro = ladoA + ladoB + ladoC

sup = (ladoA + ladoB + ladoC) / 2

area = float (sqrt(sup * (sup-ladoA) * (sup-ladoB) * (sup-ladoC)))

print ('El perímetro del triángulo es: ' + str(perimetro))
print ('El área del triángulo es: ' + str(area))