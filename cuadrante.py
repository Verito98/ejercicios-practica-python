from math import floor

grados = float ( input (' Dame angulo '))

cuadrante = floor (grados) % 360 // 90
if cuadrante == 0:
    print ('Primer Cuadrante')
if cuadrante == 1:
    print ('Segundo Cuadrante')
if cuadrante == 2:
    print ('Tercer Cuadrante')
if cuadrante == 4:
    print ('Cuarto Cuadrante')