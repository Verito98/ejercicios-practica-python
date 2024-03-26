multiplo = int ( input ('Que tabla quiere repasar?: '))
print ("perfecto!")

producto = 1
i = 0
while i <= 10:
    producto = i * multiplo
    print (multiplo, "*", i, " = ", producto)
    i = i + 1