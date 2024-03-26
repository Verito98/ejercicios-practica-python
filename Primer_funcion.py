def sig(x):
    resultado = x + 1
    return resultado

def imprimir_hola (repeticiones):
    for i in range (repeticiones):
        print ("hola")
        
n=4
a = sig(n) + sig(n + 3)

imprimir_hola (a)