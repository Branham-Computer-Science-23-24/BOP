#-------imports-------#
import turtle as trtl
import time
#---------setup---------#
wn = trtl.Screen()
wn.colormode(255)
start = False

text_font = ("Aller",15,"normal")
dialogue_reset = -300,-250
idle = "BOP_idle.gif"
unhinged = "BOP_unhinged.gif"
glitch = "BOP_glitch.gif"
red = "BOP_red.gif"
orange = "BOP_orange.gif"
green = "BOP_green.gif"
sad = "BOP_sad.gif"
happy = "BOP_happy.gif"
bop_text = "BOP_text.gif"
bop_cont = "BOP_text_cont.gif"
text = "text.gif"
text_cont = "text_cont.gif"
confetti = "confetti.gif"
btn = "button.gif"
bop_sprites = [idle,unhinged,glitch,red,orange,green,sad]
bop_sprites.append(happy)
for BOP in bop_sprites:
    wn.addshape(BOP)
textboxes = [bop_text,bop_cont,text]
textboxes.append(text_cont)
for textbox in textboxes:
    wn.addshape(textbox)
wn.addshape(btn)
wn.addshape(confetti)
#---------configure-turtles---------#
bop = trtl.Turtle()
bop.hideturtle()
bop.penup()
bop.shape(idle)
bop.goto(0,100)

button = trtl.Turtle()
button.hideturtle()
button.penup()
button.shape(btn)
button.goto(0,-100)
button.showturtle()

textbox = trtl.Turtle()
textbox.hideturtle()
textbox.penup()
textbox.shape(bop_text)
textbox.goto(0,-50)

dialogue = trtl.Turtle()
dialogue.hideturtle()
dialogue.penup()
dialogue.goto(dialogue_reset)
dialogue.pencolor("white")
#---------define-functions---------#
def text_fade(turtle,frames,startr,startg,startb,endr,endg,endb):
    changer = (startr-endr)//frames
    changeg = (startg-endg)//frames
    changeb = (startb-endb)//frames
    for i in range(frames):
        turtle.pencolor((startr,startg,startb))
        turtle.write("Project BOP: Ball of Positivity",align="center",font=["Aller",35,"bold"])
        startr-=changer
        startg-=changeg
        startb-=changeb

def start_game(x,y):
    button.hideturtle()
    text_fade(bop,4,255,215,0,255,255,255)
    bop.clear()
    time.sleep(1)
    bop.showturtle()
    textbox.showturtle()
    add_dialogue("...",text,text_cont)
    time.sleep(3)
    add_dialogue("Hello.",bop_text,bop_cont)

def add_dialogue(text,textbx,contbx):
    dialogue.goto(dialogue_reset)
    dialogue.clear()
    index = 0
    textbox.shape(textbx)
    while index < len(text):
        dialogue.write(text[index],True,font=text_font)
        if text[index] == "." or text[index] == "!" or text[index] == "?":
            time.sleep(0.3)
        elif text[index] == ",":
            time.sleep(0.1)
        else:
            time.sleep(0.05)
        index += 1
    textbox.shape(contbx)
#---------events---------#
text_fade(bop,4,255,255,255,255,215,0)
button.onclick(start_game)

wn.listen()

wn.mainloop()
