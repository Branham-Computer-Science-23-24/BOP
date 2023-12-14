if (stress_level < 3):
    bop.shape(red)

    add_dialogue(“Well, that sounds like a you proble”,bop_text,bop_cont)

    add_dialogue(“Oh no, sorry to hear that…”,bop_text,bop_cont)

    add_dialogue(“But I bet I can make your day better.”,bop_text,bop_cont)

    elif (stress_level == 3):

    bop.shape(orange)

    add_dialogue(“Mid, just like yo-”,bop_text,bop_cont)

    add_dialogue(“Right in the middle, huh? That’s okay.”,bop_text,bop_cont)

    add_dialogue(“But I bet I can make your day better.”,bop_text,bop_cont)

    elif (stress_level == 4 or stress_level == 5):

    bop.shape(green)

    add_dialogue(“Well, hope your day gets wors-”,bop_text,bop_cont)

    add_dialogue(“That’s great! I’m glad to see you’re having a good day.”,bop_text,bop_cont)

    add_dialogue(“ But I bet I can make it even better.”,bop_text,bop_cont)

else:

    add_dialogue(“Hey, bud, I don’t think that’s an option.”,bop_text,bop_cont)

    add_dialogue(“I’m sure it was only a mistake though! Just like yo-”,bop_text,bop_cont)

    add_dialogue(“I’m sure it was only a mistake though! Here, I’ll let you try again.”,bop_text,bop_cont)