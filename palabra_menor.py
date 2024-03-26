a = input('Dame el primera palabra: ')
b = input('Dame el segunda palabra: ')
c = input('Dame el tercer palabra: ')
d = input('Dame el cuarta palabra: ')
e = input('Dame el quinto palabra: ')
 
candidato = a

if b < candidato:
    candidato = b

if c < candidato:
    candidato = c

if d < candidato:
    candidato = d

if e < candidato:
    candidato = e

print ('La palabra menor es: ', candidato)