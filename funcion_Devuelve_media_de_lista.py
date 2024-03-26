# Haz una función que reciba una lista de números y devuelva la media de dichos
# números. Ten cuidado con la lista vacía (su media es cero).
def media(a:list)->float:
    sumatoria=0
    for i in a:
        sumatoria = sumatoria + i
    promedio=sumatoria/len(a)
    
    return promedio

b=[1,2,3]
print(media(b))