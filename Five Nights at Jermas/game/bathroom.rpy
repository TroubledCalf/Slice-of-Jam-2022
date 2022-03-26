default timesGoneToBR = 0
default highComplBR = 5 # change number based on how many actual choices there are in prev section

label goToBathroom
    $ prevCompliance = currentCompliance
    $ currentCompliance = prevCompliance / 2

    "Another day passes."
    "You play along with your captor, satisfying them."
    "After lunch you feel an urge."

    "You knock on your door to be let out for the bathroom."
    if currentCompliance > highComplBR:
        "In a moments notice, you here the locks behind click and shift."
    else:
        "After some time, the door swings open."

    "They look at you, smiling."
    k "How can I help you?"

    menu:
        "Nod towards the bathroom.":
            if currentCompliance > highComplBR:
                call askForBRNormal
            else:
                $ currentCompliance -= 1
                "Their expression turns dour."
                k "Would it kill you to speak up? I'm not going to yell at you."
        "Ask for the bathroom.":
            call askForBRNormal
        "Ask nicely" if timesGoneToBR > 1:
            v "May I please go to the bathroom?"
            k "..."
            k "Good."

    $ timesGoneToBR += 1

    "They quickly open the bathroom door and make way for you to enter."
    k "Do whatever you need to, buddy."
    k "Oh, and of course. Knock and wait for me when you're finished."

    jump inBathroom

label inBathroom:
    # Piss n shit

###################################### MENU OPTIONS (SINCE SOMETHIMES THE VICTIM WILL DISOBEY)
label askForBRNormal:
    $ currentCompliance += 1
    v "May I go to the bathroom?"
    k "Aren't you forgetting something?"
    "What?"
    k "The magic word?"
    "He says it in a sing-song tone."
    k "Please, I mean. I won't hold it against you but remember for next time."
    return
