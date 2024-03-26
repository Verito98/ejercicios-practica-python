from math import sqrt
print ('ecuacion de segundo grado')

a = float (input ('valor de a: '))
b = float (input ('valor de b: '))
c = float (input ('valor de c: '))

if a != 0:
    x1 = float (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = float (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
    print ('La solucion de x1 es {0:.2f} y la solucion de x2 es {1:.2f}'.format(x1,x2))

else:        #a=0  y c,b != 0
    x = -c/b #si b = 0 tengo un problema
    print ('La ecuacion es lineal y el valor de x es ', x)


