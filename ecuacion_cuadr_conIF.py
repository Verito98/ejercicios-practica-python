from math import sqrt
print ('ecuacion de segundo grado')

a = float (input ('Ingresa valor a'))
b = float (input ('Ingresa Valor b'))
c = float (input ('Ingresa Valor c'))

if a == 0:
    if b == 0:
        if c == 0:
            print ('la ecuacion tiene infinitas soluciones')
            
        else:
            print('la ecuacion no tiene solucion')
    else:
        x = -c/b
        print ('la solucion es ', x)
        
else:
    x1 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
    print ('La solucion de x1 es {0:.2f} y la solucion de x2 es {1:.2f}'.format (x1,x2))

