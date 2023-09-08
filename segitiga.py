import turtle
window = turtle.Screen()

pen = turtle.Turtle()

for i in range(3):
    pen.forward(100)
    pen.left(120)

window.exitonclick()