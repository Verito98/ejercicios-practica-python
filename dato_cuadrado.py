# Nombre del Programa: datos_cuadrado.py
# Programador: Vero
# Descripcion: este programa perimte al usuario calcular el perimetro
# y el area de un cuadrado

#pido datos al usuario
entrada_usuario = input ("de que tamaño es el lado del cuadrado: ")
lado = float (entrada_usuario)

#calculo perimetro y area
perimetro = lado * 4
area = lado ** 2

#muestro los resultados al usuario
print ("el perimetro es: " + str (perimetro))
print (" el area es: " + str (area))