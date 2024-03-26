#Diseña un programa que pida el valor de los dos lados de un rectángulo
#y muestre el valor de su perímetro y el de su área.
#(Prueba que tu programa funciona correctamente con este ejemplo:
#si un lado mide 1 y el otro 5, el perímetro será 12.0, y el área 5.0).


lado_1 = input ("ingrese valor de lado 1º: ")
lado_2 = input ("ingrese valor de lado 2º: ")
lado1_rectangulo = float (lado_1)
lado2_rectangulo = float (lado_2)
perimetro_rectangulo = 2 * lado1_rectangulo + 2 * lado2_rectangulo
area_rectangulo = lado1_rectangulo * lado2_rectangulo
print ("El perimetro del rectangulo es: " + str(perimetro_rectangulo))
print ("El area del rectangulo es: " + str (area_rectangulo))