a = int (input('Dame el primer número: '))
b = int (input('Dame el segundo número: '))
c = int (input('Dame el tercer número: '))
d = int (input('Dame el cuarto número: '))
e = int (input('Dame el quinto número: '))
 
candidato = a

if candidato < b:
    candidato = b
    print (candidato)

if candidato < c:
    candidato = c
    print (candidato)
        
if candidato < d:
    candidato = d
    print (candidato)
    
if candidato < e:
    candidato = e
    print (candidato)
    
print ('El mas grande es ', candidato)