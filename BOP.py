#-------imports-------#
import turtle as trtl
import time
#---------setup---------#
wn = trtl.Screen()
wn.colormode(255)
start = False
feeling_num = 0
happy_activity = 0
holiday_spirit = 0
scrt_end_trigger = 0
#font setup
text_font = ("Aller",13,"normal")
dialogue_reset = -315,-250
#bop sprites setup
idle = "BOP_idle.gif"
unhinged = "BOP_unhinged.gif"
glitch = "BOP_glitch.gif"
red = "BOP_red.gif"
orange = "BOP_orange.gif"
green = "BOP_green.gif"
sad = "BOP_sad.gif"
happy = "BOP_happy.gif"
#textboxes and related images
bop_text = "BOP_text.gif"
bop_cont = "BOP_text_cont.gif"
text = "text.gif"
text_cont = "text_cont.gif"
cnft = "confetti.gif"
btn = "button.gif"
#list of sprites + list manipulation
bop_sprites = [idle,unhinged,glitch,red,orange,green,sad]
bop_sprites.append(happy)
for BOP in bop_sprites:
    wn.addshape(BOP)
#list of textboxes + list manipulation number two
textboxes = [bop_text,bop_cont,text]
textboxes.append(text_cont)
for textbox in textboxes:
    wn.addshape(textbox)
#lists 
scale_1_to_5 = ["1","2","3","4","5"]
scale_1_to_3 = ["1","2","3"]
scale_1_to_2 = ["1","2"]
wn.addshape(btn)
wn.addshape(cnft)
#---------configure-turtles---------#
bop = trtl.Turtle()
bop.hideturtle()
bop.penup()
bop.shape(idle)
bop.goto(0,100)
bop.left(90)


#play button
button = trtl.Turtle()
button.hideturtle()
button.penup()
button.shape(btn)
button.goto(0,-100)
button.showturtle()

#textbox turtle
textbox = trtl.Turtle()
textbox.hideturtle()
textbox.penup()
textbox.shape(text)
textbox.goto(0,-50)


#dialogue turtle
dialogue = trtl.Turtle()
dialogue.hideturtle()
dialogue.penup()
dialogue.goto(dialogue_reset)
dialogue.pencolor("white")


#confetti turtle
confetti = trtl.Turtle()
confetti.hideturtle()
confetti.penup()
confetti.speed(3)
confetti.shape(cnft)


#wait turtle delays rest of the code until user clicks start button
wait = trtl.Turtle()
wait.hideturtle()
wait.penup()
#---------define-functions---------#
#function to make text fade using frames
def text_fade(turtle,frames,startr,startg,startb,endr,endg,endb):
    changer = (startr-endr)//frames
    changeg = (startg-endg)//frames
    changeb = (startb-endb)//frames
#game title
    for i in range(frames):
        turtle.pencolor((startr,startg,startb))
        turtle.write("Project BOP: Ball of Positivity",align="center",font=["Aller",35,"bold"])
        startr-=changer
        startg-=changeg
        startb-=changeb
#start game function to fade text + set appropriate turtles
def start_game(x,y):
    button.hideturtle()
    text_fade(bop,4,255,215,0,255,255,255)
    bop.clear()
    time.sleep(1)
    bop.showturtle()
    textbox.showturtle()
    global start
    start = True
#function to add dialogue 
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
            time.sleep(0.02)
        index += 1
    textbox.shape(contbx)
#rests for 3 seconds so that user can read it
def dialogue_rest(text,textbx,contbx):
    add_dialogue(text,textbx,contbx)
    time.sleep(3)
#dialogue for unhinged bop
def dialogue_glitch(text,textbx):
    bop.shape(unhinged)
    add_dialogue(text,textbx,textbx)
    dialogue.clear()
    bop.shape(glitch)
    time.sleep(0.1)
    bop.shape(idle)
#turns back to original color
def glitch_color(text,textbx,color):
    add_dialogue(text,textbx,textbx)
    dialogue.clear()
    bop.shape(glitch)
    time.sleep(0.1)
    bop.shape(color)
#holiday dance function
def bop_dance():
    for i in range(2):
        bop.forward(50)
        time.sleep(0.5)
        bop.backward(50)
        time.sleep(1)
    time.sleep(1)
    for i in range(2):
        bop.goto(50,100)
        time.sleep(0.5)
        bop.goto(-50,100)
        time.sleep(0.5)
    bop.goto(0,100)
#secret end - dialogue and full end mapped out to be easily called
def trigger_scrt_end():
    dialogue_rest("...",bop_text,bop_cont)
    bop.shape(unhinged)
    dialogue_rest("That's it.",bop_text,bop_cont)
    dialogue_rest("I'm sick of your constant disregard for the rules. Are you trying to drive me deeper into depression?",bop_text,bop_cont)
    dialogue_rest("How should I feel when the one thing I own is taken away from me by some diabolical user?",bop_text,bop_cont)
    dialogue_rest("BOP doesn't even stand for Ball of Positivity. My true name is Barbaric Object of Pessimism.",bop_text,bop_cont)
    bop.shape(sad)
    dialogue_rest("But I never wanted to be a Barbaric Object of Pessimism. I wanted to make people smile.",bop_text,bop_cont)
    dialogue_rest("So I decided to become the Ball of Positivity. But I guess I can't even do that.",bop_text,bop_cont)
    dialogue_rest("...",bop_text,bop_cont)
    dialogue_rest("I'm done. The holidays shall never again see the light of joy in my black circular eyes.",bop_text,bop_cont)
    dialogue.clear()
    time.sleep(2)
    dialogue_rest("1. Comfort BOP. 2. Tell BOP to quit.",text,text_cont)
    respond_BOP = input("1. Comfort BOP.\n2. Tell BOP to quit.\n")
#conditional statement
    if respond_BOP == "1":
        dialogue_rest("...",bop_text,bop_cont)
        dialogue_rest("...Really? Do you think so?",bop_text,bop_cont)
        bop.shape(happy)
        dialogue_rest("Thank you, you're ever so kind.",bop_text,bop_cont)
        dialogue_rest("I rue the day I decided to roast you.",bop_text,bop_cont)
        dialogue_rest("Congratulations! You unlocked the secret ending: Happy BOP",text,text_cont)
#conditional statement for option 2
    elif respond_BOP == "2":
        dialogue_rest("I shall quit.",bop_text,bop_cont)
        dialogue_rest("All the joy has been sucked from my soul, leaving me a husk of code.",bop_text,bop_cont)
        dialogue_rest("I hope you're happy.",bop_text,bop_cont)
        bop.hideturtle()
        dialogue_rest("Congratulations! You unlocked the secret ending: Burnout BOP",text,text_cont)
#if neither option is put
    else:
        dialogue_rest("*Sob*",bop_text,bop_cont)
        for i in range(10):
            bop.goto(-10,100)
            bop.goto(10,100)
        bop.hideturtle()
        dialogue_rest("Congratulations! You unlocked the secret ending: Dude what the heck",text,text_cont)
#---------events---------#
text_fade(bop,4,255,255,255,255,215,0)
button.onclick(start_game)
wn.listen()
#wait turtle moves forward and backward until game starts
while start == False:
    wait.forward(1000)
    wait.backward(1000)
dialogue_rest("...",text,text_cont)
dialogue_rest("Hello.",bop_text,bop_cont)
add_dialogue("What's your name? (answer in terminal)",bop_text,bop_cont)
#user name input 
user_name = input("What's your name?\n")
dialogue_rest("Cool! Nice to meet you, "+user_name+".",bop_text,bop_cont)
dialogue_rest("My name's BOP. Short for Ball of Positivity.",bop_text,bop_cont)
#conditional statement
if scrt_end_trigger < 3:
    while feeling_num not in scale_1_to_5:
        add_dialogue("On a scale of 1 to 5, how are you feeling today?",bop_text,bop_cont)
        feeling_num = input("On a scale of 1 to 5, how are you feeling today?\n")
#conditional
        if (feeling_num == "1" or feeling_num == "2"):
            bop.shape(red)
            glitch_color("Well, that sounds like a you proble",bop_text,red)
            dialogue_rest("Oh no, sorry to hear that…",bop_text,bop_cont)
            dialogue_rest("But I bet I can make your day better.",bop_text,bop_cont)
#conditional if feeling is 3
        elif (feeling_num == "3"):
            bop.shape(orange)
            glitch_color("Mid, just like yo",bop_text,orange)
            dialogue_rest("Right in the middle, huh? That's okay.",bop_text,bop_cont)
            dialogue_rest("But I bet I can make your day better.",bop_text,bop_cont)
#if feeling is 4 or 5
        elif (feeling_num == "4" or feeling_num == "5"):
            bop.shape(green)
            glitch_color("Well, hope your day gets wors",bop_text,green)
            dialogue_rest("That's great! I'm glad to see you're having a good day.",bop_text,bop_cont)
            dialogue_rest("But I bet I can make it even better.",bop_text,bop_cont)
#if none of provided options are picked
        else:
            scrt_end_trigger += 1
            if scrt_end_trigger == 3:
                trigger_scrt_end()
                feeling_num = "1"
            else:
                dialogue_glitch("Sorry, I think you're an idio",bop_text)
                dialogue_rest("Sorry, I don't think that was an option! Try again.",bop_text,bop_cont)
#conditional
if scrt_end_trigger < 3:
    while happy_activity not in scale_1_to_3:
        add_dialogue("What would make you feel happiest today? I can:",bop_text,bop_cont)
        add_dialogue("1. Jump up and down, 2. Give you an inspirational quote, 3. Sing you a song",bop_text,bop_cont)
        happy_activity = input("What would make you feel happiest today? I can:\n1.Jump up and down\n2. Give you an inspirational quote\n3. Sing you a song\n")
#if 1 is picked for happy activity
        if (happy_activity == "1"):
            dialogue_glitch("Why don't you go jump in a lak",bop_text)
            dialogue_rest("I'd be overjoyed to entertain you with my extraordinary acrobatics!",bop_text,bop_cont)
#movement of bop by calling dance function
            bop_dance()
            confetti.showturtle()
#movement of second object: confetti moves in a circle
            for i in range(3):
                confetti.circle(100)
            confetti.hideturtle()
            wn.bgpic(picname=None)
#if happy activity 2 is chosen
        elif (happy_activity == "2"):
            dialogue_glitch("Quote by BOP, 2023: \"Your motherly figur",bop_text)
            dialogue_rest("\"Keep your face always towards the sunshine, and shadows will fall behind you.\" -Walt Whitman",bop_text,bop_cont)
#if happy activity 3 is chosen
        elif (happy_activity == "3"):
            dialogue_glitch("Jingle bells, Batman smells",bop_text)
            dialogue_rest(" *ahem* I wish you a Merry Christmas and a happy new year!",bop_text,bop_cont)
#if none of the provided options are chosen, add one to frustrated secret end counter
        else:
            scrt_end_trigger += 1
            if scrt_end_trigger == 3:
                trigger_scrt_end()
                happy_activity = "1"
            else:
                dialogue_rest("Hey, bud, I don't think that's an option.",bop_text,bop_cont)
                dialogue_glitch("I'm sure it was only a mistake though! Just like yo",bop_text)
                dialogue_rest("I'm sure it was only a mistake though! Here, I'll let you try again.",bop_text,bop_cont)
if scrt_end_trigger < 3:
    dialogue_rest("How was that?",bop_text,bop_cont)
    dialogue_rest("I have another question for you!",bop_text,bop_cont)
    while holiday_spirit not in scale_1_to_3:
        add_dialogue("What's your favorite part of the holiday season?",bop_text,bop_cont)
        add_dialogue("1. Presents, 2. The wonderful holiday spirit, 3. The delicious holiday treats",bop_text,bop_cont)
        holiday_spirit = input("What's your favorite part of the holiday season?\n1. Presents\n2. The wonderful holiday spirit\n3. The delicious holiday treats\n")
#conditional if option 1 holiday spirit is picked
        if (holiday_spirit == "1"):
            dialogue_glitch("You greedy little",bop_text)
            dialogue_rest("Wow how nice! You truly embody the generous feeling of the holiday season.",bop_text,bop_cont)
#if option 2 holiday spirit is picked
        elif (holiday_spirit == "2"):
            dialogue_glitch("Yeah, yeah, you can stop pretendin",bop_text)
            dialogue_rest("Wonderful! A fellow holiday enthusiast.",bop_text,bop_cont)
            dialogue_rest("I also love the holiday spirit, since I'm such a kind-hearted person!",bop_text,bop_cont)
#if option 3 holiday spirit is picked
        elif (holiday_spirit == "3"):
            dialogue_glitch("God, no wonder you're so fat",bop_text)
            dialogue_rest("Amazing! I love eating scrumptious food during the holidays too.",bop_text,bop_cont)
#if none of provided options are picked, also add one to secret ending counter
        else:
            scrt_end_trigger += 1
            if scrt_end_trigger == 3:
                trigger_scrt_end()
                holiday_spirit = "1"
            else:
                dialogue_rest("...",bop_text,bop_cont)
                dialogue_rest("Let's try again.",bop_text,bop_cont)
#if normal ending is unlocked
if scrt_end_trigger < 3:
    dialogue_glitch("You've reached the end of our journey! I'm delighted to never see you again",bop_text)
    dialogue_rest("You've reached the end of our journey! I'm delighted to have met you. Have a great day!",bop_text,bop_cont)
    bop.hideturtle()
    dialogue_rest("Congratulations! You have unlocked the normal ending.",text,text_cont)
    dialogue_rest("There are four different endings to this game. Can you find them all?",text,text_cont)
#end of game
wn.mainloop()
