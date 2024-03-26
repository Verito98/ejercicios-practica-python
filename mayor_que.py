a = int (input('Dame el primer número: '))
b = int (input('Dame el segundo número: '))
c = int (input('Dame el tercer número: '))

candidato = a

if b > candidato:
    candidato = b
    #if a>c:
if c> candidato:
    candidato = c
máximo = candidato
print ('El Máximo es', máximo)

#else:
 #   if a > c:
  #      máximo = b
    
   # else:
    #    máximo = c
