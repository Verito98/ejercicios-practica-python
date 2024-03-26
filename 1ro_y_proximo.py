a = int (input('Dame el primer número: '))
b = int (input('Dame el segundo número: '))
c = int (input('Dame el tercer número: '))
d = int (input('Dame el cuarto número: '))
e = int (input('Dame el quinto número: '))
 
if (a > b):
    resta1 = a-b
else:
    resta1 = b-a

if (a > c):
    resta2 = a-c
else:
    resta2 = c-a
    
if (a > d):
    resta3 = a-d
else:
    resta3 = d-a

if (a > e):
    resta4 = a-e
else:
    resta4 = e-a

menor = resta1
if resta2 < menor:
    menor = resta2

if resta3 < menor:
    menor = resta3

if resta4 < menor:
    menor = resta4

menor_diferencia = menor

segundo_siguiente = menor_diferencia + a

# proximo = b

#if resta2 < resta1:
 #   proximo = c

#if resta3 < resta1:
 #   proximo = d

#if resta4 < resta1:
 #   proximo = e

print ('El primer número es: ', a, 'y el mas cercano de', a, 'es: ', segundo_siguiente)



