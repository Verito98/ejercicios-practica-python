from math import sqrt
print ('ecuacion de segundo grado')

a = float (input ('valor de a: '))
b = float (input ('valor de b: '))
c = float (input ('valor de c: '))

if a == 0 and b == 0 and c==0:
    print ('la ecuacion tiene infinitas soluciones')

else:
    if  a==0 and b==0:
        print ('la ecuacion no tiene solucion')
        
    else:
        if a == 0:
            x = -c/b
            print ('la ecuacion tiene solucion en x: ', x)
            
        else:
             x1 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
             x2 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
             print ('La solucion de x1 es {0:.2f} y la solucion de x2 es {1:.2f}'.format (x1,x2))

