a = str (input('Dame el primera letra: '))
b = str (input('Dame el primera letra: '))
c = str (input('Dame el tercer letra: '))
d = str (input('Dame el cuarta letra: '))
e = str (input('Dame el quinto letra: '))
 
candidato = a

if b < candidato:
    candidato = b

if c < candidato:
    candidato = c

if d < candidato:
    candidato = d

if e < candidato:
    candidato = e

print ('La letra menor es: ', candidato)