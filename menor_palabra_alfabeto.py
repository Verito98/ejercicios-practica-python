a = input ('1° palabra: ')
b = input ('2° palabra: ')
c = input ('3° palabra: ')
d = input ('4° palabra: ')

candi = a

if (b.lower()) < (candi.lower()):
    candi = b
    
if (c.lower()) < (candi.lower()):
    candi = c
    
if (d.lower()) < (candi.lower()):
    candi = d
    
print ('La menor palabra alfabeticamente es ', candi)