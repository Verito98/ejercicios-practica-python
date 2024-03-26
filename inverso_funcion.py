#Implementa un procedimiento Python tal que, dado un número entero, muestre por pantalla sus cifras en orden inverso.
#Por ejemplo, si el procedimiento recibe el número 324,mostrará por pantalla el 4, el 2 y el 3 (en líneas diferentes)
def inverso(numero:int)->None:
    inverso=''
    num_str= str(numero)
    for i in range(len(num_str)-1,-1):
        inverso = num_str[i]+''
        print(inverso)

print(inverso(321))
