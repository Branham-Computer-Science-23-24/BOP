import turtle as trtl
import time

wn = trtl.Screen()
idle = "BOP_idle.gif"
unhinged = "BOP_unhinged.gif"
glitch = "BOP_glitch.gif"
red = "BOP_red.gif"
orange = "BOP_orange.gif"
green = "BOP_green.gif"
sad = "BOP_sad.gif"
happy = "BOP_happy.gif"
bop_sprites = [idle,unhinged,glitch,red,orange,green,sad,happy]
for BOP in bop_sprites:
    wn.addshape(BOP)
bop = trtl.Turtle()
for BOP in bop_sprites:
    bop.shape(BOP)
    time.sleep(2)