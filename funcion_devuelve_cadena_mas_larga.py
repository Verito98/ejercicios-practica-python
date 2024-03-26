# Diseña una función que, dada una lista de cadenas, devuelva la cadena más larga.
# Si dos o más cadenas miden lo mismo y son las más largas, la función devolverá una cualquiera de ellas.
# (Ejemplo: dada la lista ['pepe', 'juan', 'maria', 'ana'], la función devolverá la cadena 'maria')

def cadena_mas_larga(lista:list)->str:
    maximo = lista[0]
    for elemento in lista:
        if len(maximo) < len(elemento):
            maximo=elemento
    return maximo

a=["sol","casa","arbol"]
print(cadena_mas_larga(a))