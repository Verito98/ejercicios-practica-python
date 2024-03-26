car = input ('dame caracter ')

if 'a' <= car.lower() <= 'z' or car == '_':
    print ('caracter valido para identificador python')

else:
    if not (car < 'o' or '9' < car):
        print ('un digito es valido para un identificador', end =' ')
        print ('Siempre que no sea el primer caracter')
    
    else:
        print ('caracter no valido para identificador')