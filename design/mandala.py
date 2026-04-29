import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
for i in range(500):
    t.pencolor(colorsys.hsv_to_rgb(i/500, 1, 1))
    t.forward(i * 1.5)
    t.right(121)
turtle.done()
