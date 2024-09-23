import math
import turtle

# Configuración inicial
turtle.bgcolor("black")
turtle.shape("turtle")
turtle.speed(0)
turtle.fillcolor("brown")

# Dibuja el tallo
turtle.penup()
turtle.goto(10, -300)
turtle.pendown()
turtle.setheading(90)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.forward(300)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(300)
turtle.end_fill()

turtle.penup()
turtle.goto(0, -180)
turtle.fillcolor("#8B4513")
turtle.begin_fill()
turtle.circle(0)
turtle.end_fill()

# Código del girasol 
phi = 137.508 * (math.pi / 180.0)
for i in range(160 + 40):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    if i < 160:
        turtle.stamp()
    else:
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.right(20)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.left(140)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.end_fill()

# Escribe "Te Quiero" en la parte superior del girasol
turtle.penup()
turtle.goto(0, 200)  # Ajusta la posición vertical según sea necesario
turtle.color("pink")  # Color del texto
turtle.write("Te Amo Almojabana", align="center", font=("Arial", 24, "bold"))

# Oculta el cursor de la tortuga antes de salir
turtle.hideturtle()

# Cierra la ventana al hacer clic
turtle.exitonclick()