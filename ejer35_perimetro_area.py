#Diseña un programa que pida el valor del lado de un cuadrado y muestre el valor de su perímetro y el de su área.
#(Prueba que tu programa funciona correctamente con este ejemplo:
#si el lado vale 1.1, el perímetro será 4.4, y el área 1.21).


valor_lado= input ("ingrese el valor del lado: ")
lado = float (valor_lado)
perimetro = lado * 4
area = lado ** 2
print ("el perimetro del cuadrado es: " + str (perimetro))
print ("el area del cuadrado es: " + str (area))
