print ("Programa para decir quien es la persona mas jóven.")

edad_1 = int (input ("Ingresa la edad de la primera persona: "))
edad_2 = int (input ("Ingresa la edad de la segunda persona: "))

if edad_1 < edad_2:
    print ('La primer persona de ', edad_1, 'años es mas jóven')
    
if edad_1 > edad_2:
    print ('La segunda persona de ', edad_2, 'años es más jóven')
    
if edad_1 == edad_2:
    print ('Ambas personas tienen la misma edad')
