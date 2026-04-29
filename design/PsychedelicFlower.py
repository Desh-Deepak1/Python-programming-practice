import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)

n = 70  # Number of circles
h = 0   # Initial hue

for i in range(n):
    # Color logic
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.color(c)
    h += 1/n
    
    # Drawing logic
    t.circle(100) # Circle banayega
    t.left(360/n) # Har circle ke baad thoda ghum jayega
    
    # Extra design: circles ke andar chote circles
    for j in range(2):
        t.circle(40)
        t.left(10)

turtle.done()
