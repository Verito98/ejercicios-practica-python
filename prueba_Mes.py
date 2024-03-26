mes = int(input('mes '))

if 1 <= mes <= 3:
    print ('invierno')

else:
    if mes == 4 or mes == 5 or mes == 6:
        print ('primavera')
    
    else:
        if not (mes < 7 or 9 < mes):
            print ('verano')
        else:
            if not (mes != 10 and mes != 11 and mes != 12):
                print ('otoño')
            
            else:
                print ('ningun año tiene {0} mes'.format(mes))