print ('Programa para calcular raices de la ecuación cuadrática')
from math import sqrt
a = float (input ('Valor de a: '))
b = float (input ('Valor de b: '))
c = float (input ('Valor de c: '))

discriminante = b**2 - 4 * a * c

if discriminante >= 0:
    if a != 0:
        x1 = -b + sqrt (b**2 - 4 * a * c) / 2 * a
        x2 = -b - sqrt (b**2 - 4 * a * c) / 2 * a
        print ('La solución para la ecuación cuadrática es x1 en {0:.2f} y en x2 {1:.2f}'.format(x1,x2))
    else: #a=0
        x = - c/b
        if b == 0:
            if c == 0:
                print ('la ecuación es lineal y tiene infinitas soluciones')
            else: #c!=0
                print ('La ecuacion no tiene solución')
        else: #b!=0
            print ('la ecuación es lineal y el valor de x es', x)  

else:
    print ('La ecuación no tiene solución en los reales')