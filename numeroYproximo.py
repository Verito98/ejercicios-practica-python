a = int (input ('1° numero: '))
b = int (input ('2° numero: '))
c = int (input ('3° numero: '))
d = int (input ('4° numero: '))
e = int (input ('5° numero: '))

valor = a
proximo = b

if (b < valor) and (b < c) and (b < d) and (b < e):
    proximo = b

if (c < valor) and (c < b) and (c < d) and (c < e):
    proximo = c

if (d < valor) and (d < b) and (d < e):
    proximo = d

if (e < valor) and (e < b):
    proximo = e

print ('el primer numero es ', valor, 'y el mas cercano a éste es', proximo)