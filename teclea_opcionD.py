from math import pi

radio = float (input('Dame el radio: '))

print ('Escoge la opcion: ')
print ('a) Calcular diametro')
print ('b) Calcular perimetro')
print ('c) Calcular area')

opcion = input ('teclea a,b o c y pulsa enter')

if opcion == 'a':
    diametro = 2 * radio
    print('diametro {0}' . format (diametro))

else:
    if opcion == 'b':
        perimetro = 2 * pi * radio
        print('perimetro {0}' . format (perimetro))
    else:
        if opcion == 'c':
            area = pi * radio ** 2
            print ('area {0}'.format (area))
        else:
            print ('solo hay tres opciones',end=' ')
            print ('tu has tecleado {0}'.format (opcion))
    