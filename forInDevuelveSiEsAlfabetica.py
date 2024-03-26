palabra = input("ingrese palabra: ")
es_alfabetica=True

for caracter in range(len(palabra)-1,-1,-1):
    if palabra[caracter-1] < palabra[caracter]:
        es_alfabetica = True
        
    else:
        es_alfabetica=False


if es_alfabetica==True:
    print("Es alfabetica")
    
else:
    print("no es alfabetica")