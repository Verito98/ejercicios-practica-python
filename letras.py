print ('lectura de letra')

caracter = input ('Ingrese la letra: ')

if 'a' <= caracter <= 'z' or 'á' <= caracter <= 'ú' or 'A' <= caracter <= 'Z' or 'Á' <= caracter <= 'Ú':
    
    if ('a' <= caracter <= 'z' or 'á' <= caracter <= 'ú'):
        print ('es minuscula')
    
    if ('A' <= caracter <= 'Z' or 'Á' <= caracter <= 'Ú'):
        print ('es MAYUSCULA')

else:
    print ('No es una letra')
# ingrese letra
#si esta entre la linea 5 es letra...
#linea 7. si es letra verificar si es minuscula
#si es letra verificar si es mayuscula
#linea 13. sino no es letra