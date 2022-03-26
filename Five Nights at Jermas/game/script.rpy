# Compliance
define prevCompliance = 0
define currentCompliance = 0

# Soundtracks

# Characters
define e = Character("Eileen")
define n = Character("Narrator")
define v = Character("Victim")
define k = Character("Kidnapper")

default lowerThres = 0.25 # change later if we want
default upperThres = 0.75
default compliance = 0.50

# Character sprites

label start:
    scene bg room

    show eileen happy

    e "You've created a new Ren'Py game."

    hide eileen happy

    e "Once you add a story, pictures, and music, you can release it to the world!"

    "There is a dark secret clawing at the back of your mind."

    "The poop knife"

    menu:
        "How will you address it?"

        "Hide it under the bed.":
            $ compliance += .3
            "Hopefully to remain unfound"
        "It is best kept hidden in plain sight.":
            $ compliance -= .3
            "You frame it on the wall"
        "Keep it where it is.":
            "In the drawer"


    if compliance >= upperThres:
        jump cutOutOne
    elif compliance >= lowerThres:
        jump phaseOne
    else:
        jump start
