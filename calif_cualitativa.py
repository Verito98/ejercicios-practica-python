#un programa que dado un número real que representa una calificación
#y proporcione la calificación en forma cualitativa:
#<<Suspenso»: nota < 5
#«Aprobado»: 5 <= nota < 7
#«Notable»: 7 <= nota < 9
# «Sobresaliente»: 9 <= nota < 10
#«Matrícula de Honor»: nota = 10
print ('Programa para pasar calificación numerica a cualitativa')

nota = float (input('Ingrese nota numérica de exámen: '))
if nota < 5:
    print ('<<Suspenso>>')

elif 5 <= nota < 7:
    print ('<<Aprobado>>')

elif 7 <= nota < 9:
    print ('<<Notable>>')
    
elif 9 <= nota < 10:
    print ('<<Sobresaliente>>')

elif nota == 10:
    print ('<< Matrícula de Honor>>')

