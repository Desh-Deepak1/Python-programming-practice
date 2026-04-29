import turtle
import colorsys
import time

# ---- प्रो सेटअप (Pro Setup) ----
s = turtle.Screen()
s.bgcolor("black")
s.setup(width=900, height=900)
s.title("Pro Design for DESH DEEPAK")

t = turtle.Turtle()
# नोट: हमने tracer बंद नहीं किया है, ताकि ड्राइंग स्लो और लाइव दिखे
t.speed(0)  # ड्राइंग की स्पीड (0 = सबसे तेज़, लेकिन tracer ऑन है तो यह स्मूथ दिखेगा)
t.width(1)  # पतली लाइनें ज्यादा प्रीमियम लगती हैं
t.hideturtle()

# ---- 1. स्लो मोशन प्रोफेशनल फ्लावर ----
def draw_slow_spirograph():
    hue = 0.5 # नीले/बैंगनी रंग से शुरुआत (ज्यादा रॉयल लगता है)
    t.penup()
    t.goto(0, 50) # सेंटर से थोड़ा ऊपर ताकि नाम के लिए जगह बचे
    t.pendown()
    
    # यह लूप 72 बार चलेगा, हर बार एक सर्किल बनाकर थोड़ा घूमेगा
    for i in range(72):
        # प्रीमियम कलर ग्रेडिएंट
        color = colorsys.hsv_to_rgb(hue, 0.7, 1) # थोड़ा सा डार्क नियोन
        t.pencolor(color)
        hue += 0.007
        
        # एक पंखुड़ी (Circle) बनाना
        t.circle(130)
        
        # अगली पंखुड़ी के लिए थोड़ा सा घूमना (5 डिग्री)
        t.left(5)
        
        # स्लो इफेक्ट के लिए थोड़ा सा डिले (अगर बहुत स्लो लगे तो इसे हटा सकते हैं)
        # time.sleep(0.01) 

# ---- 2. एक-एक अक्षर नाम लिखना (Typewriter Effect) ----
def write_animated_name(name_text):
    t.penup()
    # नाम शुरू करने की पोजीशन (स्क्रीन के बाईं तरफ)
    start_x = -220 
    start_y = -220
    t.goto(start_x, start_y)
    t.color("white")
    
    # एक प्रोफेशनल मोनोस्पेस फॉन्ट (जैसे कोडिंग में होता है)
    pro_font = ("Courier New", 35, "bold")
    
    # नाम के हर एक अक्षर (char) के लिए लूप
    for char in name_text:
        t.write(char, align="center", font=pro_font)
        
        # अगले अक्षर के लिए कर्सर को आगे बढ़ाना
        t.forward(45) 
        
        # सबसे ज़रूरी: टाइपिंग इफेक्ट के लिए डिले (रुकावट)
        time.sleep(0.2) # हर अक्षर के बीच 0.2 सेकंड का गैप

    # नाम के नीचे एक फिनिशिंग लाइन
    t.penup()
    t.goto(start_x - 20, start_y - 10)
    t.color(colorsys.hsv_to_rgb(0.6, 1, 1)) # स्यान (Cyan) कलर
    t.pendown()
    t.width(3)
    t.forward(len(name_text) * 45 + 40)


# ---- एग्जीक्यूशन (Execution) ----
# पहले फूल बनेगा आराम से
draw_slow_spirograph()

# फिर थोड़ा रुक कर नाम टाइप होगा
time.sleep(0.5)
write_animated_name("DESH DEEPAK")

print("डिज़ाइन पूरा हुआ! कैसा लगा?")
turtle.done()
