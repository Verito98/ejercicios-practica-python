print ("Programa para resolver la ecuación ax+b=0")
a = float (input ("Valor de a: "))
b = float (input ("Valor de b: "))

if a != 0:
    x = -b/a
    print ("La solución es: ", x)
    
if a == 0:
    print ("La ecuación no tiene solución.")