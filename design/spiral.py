# File: design.py
import turtle
import colorsys

# Setup Screen and Turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')  # Background black taaki colors pop karein
t.speed(0)          # Sabse tez drawing speed
t.width(2)          # Line thodi moti

# Variables for color logic
n = 200 # Total lines
h = 0   # Starting hue (color)

# Drawing Loop
for i in range(n):
    # Rainbow color generate karna (HSV to RGB)
    color = colorsys.hsv_to_rgb(h, 1, 0.8)
    t.pencolor(color)

    # Movement logic
    t.forward(i * 3) # Har baar thoda aage badho
    t.left(145)      # Magic angle jo spiral banata hai

    h += 0.005 # Agle loop ke liye color change karo

# Window ko hold karne ke liye
turtle.done()
