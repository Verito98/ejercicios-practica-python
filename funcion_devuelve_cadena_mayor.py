# Diseña una función que, dada una lista de cadenas, devuelva la cadena más larga.
# Si dos o más cadenas miden lo mismo y son las más largas, la función devolverá una cualquiera
# de ellas.
#(Ejemplo: dada la lista ['pepe', 'juan', 'maria', 'ana'], la función devolverá la cadena 'maria')
def cadena_larga(lista:list)->str:
    mayor=lista[0]
    for elemento in lista:
        if len(mayor) < len(elemento):
            mayor = elemento
    
    return mayor

print(cadena_larga(["sol","casa","arbol"]))

        