print("Programa para calcular cantidad de empanadas a cocinar")

def sumatorio(lista:list)->int:
    suma=0
    for i in lista:
        suma=suma + i
    return suma

ordenes=int(input("Cuantas Ordenes de Empanadas Hay?: "))
lista_ordenes=[]
for orden in range (ordenes):
    empanadas=int(input(f"Ingrese cuantas empanadas en la {orden+1}: "))
    lista_ordenes.append(empanadas)

print("Ordenes de empanadas ", lista_ordenes)
total_empanadas= sumatorio(lista_ordenes)
print("Tiene que cocinar: ", total_empanadas, "empanadas")
    
