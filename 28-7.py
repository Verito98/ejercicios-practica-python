print ('Programa para informar si el numero es el doble de un impar')

numero = int ( input ('Dame el número: '))

mitad_num = int (numero / 2)

if (mitad_num % 2) != 0:
    print ('El número', numero, 'es el doble de', mitad_num, 'y,', mitad_num, 'es impar')