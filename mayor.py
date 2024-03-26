# Nombre del Programa: mayor.py
# Programador: Vero
# Descripcion: este programa permite al usuario saber si la persona es mayor de edad

entrada = input ("cuantos años tiene: ")
edad = int (entrada)
mayor = edad >= 18

print ("La edad es: ", edad)
print ("Mayor de edad es:  " , mayor)

if edad >= 18:
    print ("Puede pasar")

else:
    print ("No puede pasar")