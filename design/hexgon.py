import turtle

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(0)

for x in range(650):
    t.pencolor(colors[x % 6]) # Har line ke liye alag color
    t.width(x // 100 + 1)     # Line ki thickness dhire-dhire badhegi
    t.forward(x)              # Line ki lambai badhegi
    t.left(59)                # Magic Angle for Hexagon
