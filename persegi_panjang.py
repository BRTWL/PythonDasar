import turtle
window = turtle.Screen()

pen = turtle.Turtle()

panjang = 200
lebar = 100

for i in range(2):
    pen.forward(panjang)
    pen.left(90)
    pen.forward(lebar)
    pen.left(90)

window.exitonclick()

