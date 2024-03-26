# Define una función que convierta grados centígrados en grados Farenheit

def convertidor(centigrados:int)->float:
    resultado_faren = (centigrados+32)/(5/9)
    return resultado_faren

grados_centi=int(input("Ingrese grados centigrados: "))

print(convertidor(grados_centi))