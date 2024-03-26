a = input ('1° palabra: ')
b = input ('2° palabra: ')
c = input ('3° palabra: ')
d = input ('4° palabra: ')
e = input ('5° palabra: ')

menor = a

if b < menor:
    menor = b
    
if c < menor:
    menor = c
    
if d < menor:
    menor = d
    
if e < menor:
    menor = e
    
print ('La menor palabra para ASCII es ', menor)