from turtle import Screen, Turtle #de la libreria turtle importa la pantalla y las herramientas Turtle

pantalla = Screen() #crea una pantalla y la almacena en la variable pantalla
pantalla.setup(425,425) #fija las dimensiones de la pantalla
pantalla.screensize(400,400) #fija el tamaño de la superficie del dibujo
pantalla.setworldcoordinates(-50,-150,350,250) #establece el sistema de coordenadas de la pantalla donde (-50,-150)
                            #es el vértice inferior izquierdo, y (350,250) es el vértice superior derecho

tortuga =Turtle() #crea la variable tortuga y almacena una referencia a ella 

tortuga.pensize(3) #usa un lápiz con trazo de 3 pixeles de grosor
tortuga.dot(10) #dibuja un punto de diámetro 10 centrado en la posicion en que se encuentra
tortuga.forward(100) #avanza 100 pasos
tortuga.dot(10) #dibuja un punto de diámetro 10 centrado en la posicion en que se encuentra
tortuga.forward(100) #avanza 100 pasos
tortuga.dot(10) #dibuja un punto de diámetro 10 centrado en la posicion en que se encuentra
tortuga.forward(100) #avanza 100 pasos
tortuga.dot(10) #dibuja un punto de diámetro 10 centrado en la posicion en que se encuentra

tortuga.penup() #levanta el lápiz
tortuga.goto(0,100) #ubica a la tortuga en la posición(0,100)
tortuga.pendown() #baja lápiz

tortuga.pencolor('red') #usa el color rojo
tortuga.pensize(5) #una el lápiz con trazo 5 pixeles 
tortuga.circle(20) #dibuja un círculo de radio 20
tortuga.forward(50) #avanza 50 pasos
tortuga.pensize(4) #una el lápiz con trazo 4 pixeles 
tortuga.left(20) #gira 20 grados a la izquierda
tortuga.circle(20) #dibuja un círculo de radio 20
tortuga.forward(50)#avanza 50 pasos
tortuga.pensize(3) #usa un lápiz con trazo de 3 pixeles de grosor
tortuga.left(20) #gira 20 grados a la izquierda
tortuga.circle(20) #dibuja un círculo de radio 20
tortuga.forward(50)#avanza 50 pasos
tortuga.pensize(2) #usa un lápiz con trazo de 2 pixeles de grosor
tortuga.left(20) #gira 20 grados a la izquierda
tortuga.circle(20) #dibuja un círculo de radio 20