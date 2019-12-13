from turtle import Turtle, Screen

CURSOR_SIZE = 20

def sierpinski(depth, turtle, size):

    turtle.shapesize(size / CURSOR_SIZE)
    turtle.stamp()

    if depth < 1:
        return

    half = size / 2
    circumradius = half * 3 ** 0.5 / 3

    for _ in range(3):
        turtle.forward(circumradius)  # to
        sierpinski(depth - 1, turtle, half)
        turtle.backward(circumradius)  # and fro
        turtle.left(120)

window = Screen()
window.mode('logo')  # make 0 degrees straight up
window.title('Sierpinski')
window.bgcolor('lightblue')

alex = Turtle('triangle')
alex.fillcolor(window.bgcolor())
alex.penup()

sierpinski(3, alex, 1000)

alex.hideturtle()
window.mainloop()