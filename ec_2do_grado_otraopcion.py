from math import sqrt
print ('ecuacion de segundo grado')

a = float (input ('valor de a: '))
b = float (input ('valor de b: '))
c = float (input ('valor de c: '))

if a == 0:
    if b == 0:
        if c == 0:
            print ('La ecuacion tiene infinitas soluciones')
        
        else: # c!=0 x=-c/b
            print ('la ecuacion no tiene solucion')
        
    else: # b!=0
        x = -c/b
        print ('la solucion de x es:', x)

else: # a!=0
    x1 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
    print ('La solucion de x1 es {0:.2f} y la solucion de x2 es {1:.2f}'.format (x1,x2))


            