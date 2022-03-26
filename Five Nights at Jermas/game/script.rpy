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
    label day_1:
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
                n "You hide underneath the covers and shiver as you wait for the door to open."
                n "Your heart beats faster as the steps get closer..."
                n "The door swings open with a creak."
                n "Someone steps in and all you can do is hope to not be killed."
                k "Hi~ I know you're awake, by the way. There's no need to pretend."
                #@TODO
            "See who it is":
                $ currentCompliance += 1
                n "You get up and wait for the door to open."
                n "Your heart beats faster as the steps get closer..."
                n "The door swings open with a creak."
                # show the kidnapper
                n "A shadowy figure enters the room."
                k "Hello, I see you're up now."
                # how should the kidnapper address the victim other than "you?"
                v "H-hi... you're not going to hurt me, are you?"
                k "Of course not! I brought you here for a reason."
                v "W-what? I-I don't know you..."
                k "That's okay, you'll get to know me eventually."
                n "This is very wrong."
                # these are sort of place-holder values and options just to get something down
        menu:
            "Demand to go home":
                $ currentCompliance -= 1
                n "You jump off the bed and scream at them."
                v "I want to go home now!"
                k "Go home? This IS your home now. Don't you worry, you'll love it here!"
                n "With that, they leave the room and you hear a latch click."
                n "All you can do is curl up and start sobbing."
            "Just accept the kidnapper for now":
                $ currentCompliance += 1
                v "Oh.. okay..."
                k "See, you're getting it!"
                k "We're going to have so much fun together!"
                n "With that, they leave the room and you hear a latch click."
                n "You take a deep breath, grateful to still be alive."
                n "At least this person doesn't seem intent on killing you. That means you could escape..."

        # perhaps a bit about looking around the room a la point-and-click adventure

        # Thought it might be a nice touch to have no clocks
        #   emphasis the loop and deja vu and all that
        n "You have no idea how long you stay on the bed like that."
        n "As you raise your head and look around the room, it occurs to you"
        n "There is not a single clock in the room"
        n "Nor is there a window."
        n "How long has it been since you came here? Since you woke up? Since your captor even left?"
        n "You have no idea."
        v "..."
        n "The tears begin to resurface again"
        n "The best you can do is lie in wait."
        n "Someone will come for you eventually? Right?"
        n "Right?"

        # We need to find stuff for the victim to do in between visits from the kidnapper

        n "You here the click of the door again."
        k "I would be a poor host if I did not provide for my guests."
        n "They approach you holding a tray and take a seat beside you on the bed."
        n "Oatmeal."
        n "Not the most enjoyable of meals, not by a long shot."
        k "I wish I could have made something more appealing, but of course..."
        k "its hard to do so without knowing your preferences."
        # a note-so-nice smile I imagine
        n "He waits expectantly."
        menu:
            "Take the oatmeal.":
                $ currentCompliance += 1
                n "Unpleasant as your situation may be, it is hard to refuse warm food."
                k "Good."
                k "I wouldn't want you to go hungry."
            "Refuse it":
                $ currentCompliance -= 1
                n "They continue to smile at you."
                k "If you are not hungry right now, that is fine."
                k "You can eat whenever you like, and I will take your dishes when you sleep."
                n "He puts the bowl beside your bed on a night stand."
        k "What I wanted to ask was, what preferences do you have? On your oatmeal, I mean. I only have so many ingredients."
        k "I could give you banana slices, strawberry, hell, even honey."
        n "He looks at you pointedly on that last word."
        menu:
            "remain silent.":
                $ currentCompliance -= 1
                k "You're not talkative today. That's fine. There's always tomorrow."
            "banana slices":
                $ currentCompliance += 1
                n "He clasps his hands together."
                k "Wonderful. I will keep this in mind"
            "strawberry":
                $ currentCompliance += 1
                n "He clasps his hands together."
                k "Wonderful. I will keep this in mind"
            "honey":
                $ currentCompliance += 1
                n "He clasps his hands together."
                k "Wonderful. I will keep this in mind"
            "watermelon":
                $ currentCompliance -= 2
                n "His smile fades slightly, before he regains composure."
                k "You'll learn to appreciate what I offer you in time."
        n "He stands up once again."
        k "Before I leave, is there anything more you'd like to speak about?"

        ####
        # breakfast scene, then sleep/sitting around before captor comes to say goodnight and you have option to attack
        ###
        menu:
            "Attack your captor":
                $ currentCompliance -= 4
                n "You launch yourself at your captor."
                #@TODO

            "Do nothing":
                $ currentCompliance += 4
                n "You drift to sleep, harrowed by the day's events..."
                #@TODO
                # I guess more realistically, someone wouldn't be able to sleep so soundly in a bed that's not theirs
                # what if sleeping soundly is tied to accepting food? that's creepy but anyway

                # proceed to day 2
    return
