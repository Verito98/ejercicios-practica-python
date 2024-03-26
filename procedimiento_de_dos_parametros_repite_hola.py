# def repetir_mensaje(mensaje:str, repeticiones:int)->None:
#     for i in range(repeticiones):
#         print(mensaje)
# 
# print(repetir_mensaje("Hola", 5))

def repetir_mensaje(mensaje:str,veces:int)->None:
    for i in range(veces):
        print(mensaje)

repetir_mensaje("Hola Mundo",3)