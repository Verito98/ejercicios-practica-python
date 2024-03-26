# Define una función que, dado el valor de los tres lados de un triángulo, devuelva la
# longitud de su perímetro.
def perimetro (x:int, y:int, z:int)->int:
    perimetro_triangulo=x*y*z
    return perimetro_triangulo

ladox=int(input("Ingrese largo del lado del triangulo"))
ladoy=int(input("Ingrese largo del lado del triangulo"))
ladoz=int(input("Ingrese largo del lado del triangulo"))

print("el perimetro del tringulo es: ", perimetro(ladox,ladoy,ladoz))