# Define una función que convierta grados Farenheit en grados centígrados.
# (Para calcular los grados centígrados has de restar 32 a los grados Farenheit y multiplicar
# el resultado por cinco novenos).
def convertidor(farenheit:int)->float:
    resultado_centi = (farenheit-32)*(5/9)
    return resultado_centi

grados_faren=int(input("Ingrese grados farenheit: "))

print(convertidor(grados_faren))