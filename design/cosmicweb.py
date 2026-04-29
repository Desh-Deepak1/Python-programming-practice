# File: cosmic_web.py
import turtle
import colorsys

# ---- सेटअप ----
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')  # बैकग्राउंड काला
t.speed(0)          # सबसे तेज़ स्पीड
t.pensize(2)        # पतली लाइन ताकि पैटर्न घना दिखे

hue = 0.0 # रंग की शुरुआत

# ---- मुख्य लूप ----
# हम 360 बार घूमेंगे
for i in range(360):
    # रंग बदलना (इंद्रधनुष प्रभाव)
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(color)
    hue += 0.005 # अगले लूप के लिए रंग थोड़ा बदलें

    # ---- पैटर्न बनाना ----
    # यह अंदर का लूप एक तारे जैसा आकार बनाता है
    for j in range(10):
        t.forward(200) # आगे बढ़ें
        t.left(150)    # एक तीखा मोड़ लें

    # ---- रोटेशन ----
    # पूरा आकार बनाने के बाद, कछुए को थोड़ा सा घुमाएं
    # ताकि अगला आकार पिछले वाले से थोड़ा हटकर बने.
    t.right(10)

# कछुए को छुपा दें और विंडो खुली रखें
t.hideturtle()
turtle.done()
