default timesGoneToBR = 0
default highComplBR = 5 # change number based on how many actual choices there are in prev section

default canBrush = False
default canShower = False

label goToBathroom:
    $ currentCompliance = currentCompliance / 2

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
            $ currentCompliance -= 1
            if currentCompliance > highComplBR:
                call askForBRNormal
            else:
                "Their expression turns dour."
                k "Would it kill you to speak up? I'm not going to yell at you."
        "Ask for the bathroom.":
            call askForBRNormal
        "Ask nicely" if timesGoneToBR > 1:
            $ currentCompliance += 1
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
    "It's nice to actually be in a bathroom. Both access to real facilities and an actual room besides the bedroom you were kept in."
    $ allDone = False
    $ usedToilet = False
    $ brushedTeeth = False
    $ tookShower = False
    while not allDone:
        "Looking around, what will you do?"
        menu:
            "You're done here.":
                #PLACEHOLDERPLACEHOLDERPLACEHOLDER
                $ allDone = True
            "Use the toilet" if not usedToilet:
                call useToilet
            "Brush your teeth" if not brushedTeeth:
                "You pull on the drawers over the sink hoping to get a brush and some toothpaste"
                if canBrush:
                    call brushTeeth
                else:
                    "Instead, the doors stay closed."
                    v "God damn it."
                    "They must have locked the drawer"


###################################### MENU OPTIONS (SINCE SOMETHIMES THE VICTIM WILL DISOBEY)
label askForBRNormal:
    v "May I go to the bathroom?"
    k "Aren't you forgetting something?"
    "What? They didn't say anything before"
    k "The magic word?"
    "He says it in a sing-song tone."
    k "Please, I mean. I won't hold it against you but remember for next time."
    return

label useToilet:
    "You relieve yourself"
    "An actual toilet for once. Way better than having to make do in the bedroom."
    "After you finish, you realize the toilet paper roll has gone out."
    v "Shoot"
    "You look around  and find several toilet paper rolls."
    "One is left very visibly out of the bag with a sticky note on it."
    v "'Remember! Toiler paper always goes loose end over the top. :-) --Isaac'"
    "Huh."
    "So that's his name."
    "Anyway, back to toilet paper."
    menu:
        "Put it on loose-end-over":
            $ currentCompliance += 1
            "You put on the toilet paper as instructed. After all, there's no reason to upset them over this."
        "Put it on loose-end-under":
            $ currentCompliance -= 1
            if currentCompliance > highComplBR:
                "You put on the toilet paper as instructed. After all, there's no reason to upset them over this."
            else:
                "You put it on wrong, ignoring their instructions. You have no reason to listen to a kidnapper."

    "Satisfied with your toilet paper duties, you rise."
