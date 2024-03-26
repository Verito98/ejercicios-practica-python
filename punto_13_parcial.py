entrada = int ( input ('Ingrese número: '))
x = str (entrada)

mod_3 = (entrada % 3)
mod_5 = (entrada % 5)


if mod_3 == 0 and mod_5 == 0:
    print ('El número ' + str (x) + ' es divisible por 3 y por 5')
    
if mod_3 != 0 and mod_5 != 0:
    print ('El número ' + str (x) + ' no es divisible por 3 y ni por 5')
    
if mod_3 == 0 and mod_5 != 0:
    print ('El número ' + str (x) + ' es divisible por 3 y no por 5')
    
if mod_3 != 0 and mod_5 == 0:
    print ('El número ' + str (x) + ' no es divisible por 3 y si por 5')