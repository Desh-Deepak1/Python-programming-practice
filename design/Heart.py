# File: heart_art.py
import turtle
import math

# ---- सेटअप ----
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")  # बैकग्राउंड काला ताकि दिल चमके
s.tracer(0, 3)
t.speed(0)          # सबसे तेज़ स्पीड
t.hideturtle()      # कछुए को छुपा दें

# ---- दिल का गणितीय फॉर्मूला (Heart Formula) ----
# यह फंक्शन बताता है कि दिल की शेप में X और Y की स्थिति कहाँ होगी
def heart_x(angle):
    return 16 * math.sin(angle)**3

def heart_y(angle):
    return 13 * math.cos(angle) - 5 * math.cos(2*angle) - 2 * math.cos(3*angle) - math.cos(4*angle)

# ---- ड्राइंग लूप ----
# हम कई सारे दिल एक के ऊपर एक बनाएंगे ताकि वह भरा हुआ दिखे
for i in range(1100):
    # रंग बदलना: गहरे लाल से चमकीले गुलाबी तक
    # यह लॉजिक रंग को लाल/गुलाबी शेड्स में रखता है
    col_val = i / 1100.0
    t.color(col_val, 0, 0.2) # RGB कलर मिक्सिंग (ज्यादातर Red)

    t.penup() # पेन उठाएं ताकि बीच में लाइन न खिंचे

    # शुरुआती बिंदु पर जाएं (सेंटर)
    t.goto(0, 0)

    t.pendown() # पेन नीचे करें

    # कोण (angle) को रेडियन में बदलें
    angle = i * 0.1

    # फॉर्मूले से X और Y की वैल्यू निकालें
    # 'i' से गुणा करने पर दिल का आकार बड़ा होता जाएगा
    x = heart_x(angle) * (i * 0.02)
    y = heart_y(angle) * (i * 0.02)

    # उस पॉइंट पर जाएं
    t.goto(x, y)

# विंडो को खुला रखने के लिए
turtle.done()
