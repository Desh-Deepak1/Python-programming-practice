# File: mandala.py
import turtle
import colorsys

# Setup Screen and Turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black") # Background black
t.speed(0)         # Fastest speed
t.width(2)         # Line thickness

hue = 0 # Starting color

# Loop for drawing pattern
# Jitna bada range hoga, design utna bada banega
for i in range(700):
    # Color generation (Rainbow effect)
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(color)

    # Movement Logic
    t.forward(i * 1.5)  # Har step par line lambi hoti jayegi
    t.right(121)        # <-- MAGIC ANGLE! Is angle ki wajah se star banta hai.
                        # Try changing 121 to 91 or 145 for different patterns.
    hue += 0.005        # Change color for next line

t.hideturtle() # Hide cursor at the end
turtle.done()
