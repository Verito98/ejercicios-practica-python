total_ticket = int (input ("Ingrese cantidad de tickets: "))
while total_ticket < 0:
    print ("Imposible!")
    total_ticket = int(input("Ingrese cantidad de tickets: "))
    
if total_ticket == 0:
    print ("Usted no realizó compras")

else:
    sumatoria = 0
    ticket = 1
    while 1 <= ticket <= total_ticket:
        print ("El número de ticket ingresado es: ", ticket)
        monto = float (input("Ingrese monto del ticket: "))
        sumatoria = sumatoria + monto
        ticket = ticket + 1
    print ("El total gastado es: ", sumatoria)