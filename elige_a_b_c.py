from math import pi

radio = float (input('Dame el radio de un círculo: '))

#menu
print ('Escoge una opción: ')
print ('a) Calcular el diámetro.')
print ('b) Calcular el perímetro.')
print ('c) Calcular el área.')
opcion = input ('Teclea a, b, o c y pulsa el retorno del carro: ')

if opcion == 'a' or 'A': #Calcular diametro.
    diametro = 2 * radio
    print ('El diámetro es {0}.'.format (diametro))
else:
    if opcion == 'b' or 'B': #calcula perimetro
        perimetro = 2 * pi * radio
        print ('El perimetro es {0}.'.format (perimetro))
    else:
        if opcion == 'c' or 'B': #calculo area
            area = pi * radio ** 2
            print ('El área es {0}.'.format (area))
        else:
            
            print ('Tu has tecleado "{0}".'.format (opcion))