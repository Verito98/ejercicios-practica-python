def es_mayor_de_edad(edad:int)->bool:
    if edad > 18:
        resultado=True
    else:
        resultado=False
    return resultado

pedir_edad=int(input("Ingrese la edad: "))
print(es_mayor_de_edad(pedir_edad))