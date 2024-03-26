# Diseña una función que reciba una cadena y devuelva cierto si empieza por minúscula
# y falso en caso contrario
def minuscula(cadena:str)->bool:
    es_minuscula=True
    for i in cadena:
        if 'a' <= i <='z':
            es_minuscula=True
        else:
            es_minuscula = False
            
        return es_minuscula


print (minuscula("Hola mundo"))