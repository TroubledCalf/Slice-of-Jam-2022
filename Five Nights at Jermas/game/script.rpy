# Compliance
default prevCompliance = 0
default currentCompliance = 0

# Soundtracks

# Characters
define e = Character("Eileen")
define n = Character("Narrator")
define v = Character("Victim")
define k = Character("Kidnapper")

# Character sprites

label start:
    scene bg room

    show eileen happy

    n "You wake up."

    hide eileen happy

    n "Where is this?"

    n "Slowly, your senses start to come to you..."

    n "You're laying down on a thin mattress in what appears to be a small bedroom? Definitely not your bedroom."

    # add more thoughts, specifcally emotions here

    n "Suddenly, you hear footsteps coming down the hall. "

    menu: 
        "Pretend to be asleep because they might be dangerous":
            $ currentCompliance -= 1
            jump pretend
        "See who it is":
            $ currentCompliance += 1
            jump stay_up
        # these are sort of place-holder values and options just to get something down

    label pretend:
        
        n "You hide underneath the covers and shiver as you wait for the door to open."

        n "Your heart beats faster as the steps get closer..."

        n "The door swings open with a creak."

        n "Someone steps in and all you can do is hope to not be killed."

        k "Hi~ I know you're awake, by the way. There's no need to pretend."

    label stay_up:

        n "You get up and wait for the door to open."

        n "Your heart beats faster as the steps get closer..."

        n "The door swings open with a creak."

        # show the kidnapper

        n "A shadowy figure enters the room."

        k "Hello, I see you're up now."

        # how should the kidnapper address the victim other than "you?"

        v "H-hi... you're not going to hurt me, are you?"

        k "Of course not! I love you!"

        v "W-what? I-I don't know you..."

        k "It's okay, you'll get to know me a lot better real soon"

        # someone *please* rewrite this
    
    menu:
        "Attack your captor":
            $ currentCompliance -= 4
            jump attack


        "Do nothing":
            $ currentCompliance += 4
            jump day_1_sleep

    label attack:
        n "You launch yourself at your captor"

    label day_1_sleep:
        n "You drift to sleep, harrowed by the day's events..."

        # I guess more realistically, someone wouldn't be able to sleep so soundly in a bed that's not theirs
        # what if sleeping soundly is tied to accepting food? that's creepy but anyway
    return
