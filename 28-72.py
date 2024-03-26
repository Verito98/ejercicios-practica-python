from math import floor

grados = float ( input (' Dame angulo '))

cuadrante = floor (grados) % 360 #// 90
print (cuadrante)