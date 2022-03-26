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
            
        ####
        # breakfast scene, then sleep/sitting around before captor comes to say goodnight and you have option to attack
        ###
        menu:
            "Attack your captor":
                $ currentCompliance -= 4
                n "You launch yourself at your captor."
                #@TODO
                jump day_1

            "Do nothing":
                $ currentCompliance += 4
                n "You drift to sleep, harrowed by the day's events..."
                #@TODO
                # I guess more realistically, someone wouldn't be able to sleep so soundly in a bed that's not theirs
                # what if sleeping soundly is tied to accepting food? that's creepy but anyway
                $ prevCompliance = currentCompliance
                jump day_2

    label day_2:
        
        $ currentCompliance = 0
        # you demand to go home or not again
        # and you have breakfast again

        n "You wake up."

        n "You look out into the room you're in and remember everything from yesterday."

        n "Trapped."
        n "Lost."
        n "Confused."

        n "And you can't do a thing about it."

        # add more thoughts, specifcally emotions here

        menu:
            "Demand to go home":
                $ currentCompliance -= 1
                n "Maybe you could demand to go home again?"
                v "I want to go home now!"
                k "Go home? You forgot already? This is your home now."
                n "With that, they leave the room and you hear a latch click."
                n "Once again, you just lay defeated."
            "Just accept the kidnapper for a little longer":
                $ currentCompliance += 1
                v "So are you going to bring me food soon?"
                k "See, you're getting it!"
                k "Keep this up and maybe I'll even let you out of this room..."
                n "With that, they leave the room and you hear a latch click."
                n "You take a deep breath, once again grateful to still be alive."
                n "If you were let out of this room, you could escape..."

                # you already looked around before, but maybe allow that again?

        #breakfast scene, pretty much EXACTLY the same as yesterday

        menu:
            "Attack your captor":
                $ currentCompliance -= 4
                n "You launch yourself at your captor."
                #@TODO
                jump day_2

            "Do nothing":
                $ currentCompliance += 4
                n "You drift to sleep, harrowed by the day's events..."
                #@TODO
                # I guess more realistically, someone wouldn't be able to sleep so soundly in a bed that's not theirs
                # what if sleeping soundly is tied to accepting food? that's creepy but anyway
                jump day_3
                
    return
