n = int ( input ('Ingrese el primer numero del intervalo: '))
m = int ( input ('Ingrese el máximo valor del intervalo: '))
i = n
sumatoria = 0

while i <= m:
    sumatoria = sumatoria + i
    i = i + 1

print (sumatoria)