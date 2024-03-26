print ('Programa para calcular una acuación del tipo a*x+b=0')

a = float (input('Valor de a: '))
b = float (input('Valor de b: '))

if a != 0:
    x = - b/a
    print ('Solucion: ', x)
    
if a == 0:
    if b != 0:
        print ('La ecuación no tiene solución')
    if b == 0:
        print ('La ecuación tiene infinitas soluciones')