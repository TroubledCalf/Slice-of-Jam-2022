default timesGoneToBR = 0
default highComplBR = 2 # change number based on how many actual choices there are in prev section
default lowComplBR = -2

default canBrush = False
default canBath = False

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
    $ tookBath = False
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
                    "They must have locked the drawer somehow. They don't even trust you for toothpaste?"
                    "And the drugs cabinet, in all likelihood. That makes more sense actually."
                $ brushedTeeth = True
            "Take a bath" if not tookBath
                "You undress and step into the bath."
                if currentCompliance < highComplBR:
                    "You hope desperately there are no hidden cameras in this bathroom."
                "You reach for the nozzle and turn for the water."
                if canBath:
                    call takeBath
                else:
                    "only for nothing to come out."
                    "This is ridiculous! You can't even take a bath? What, are you not trusted with large bodies of water?"
                    "It certainly seems as much."
                $ tookBath = True

        jump exitBR

label exitBR
    "Before you leave the bathroom, a thought occurs to you."
    v "He said to knock and wait for him when I want to leave."
    "An odd request. What you do in the bathroom is your business."
    menu:
        "Knock and wait for them.":
            $ currentCompliance += 2
            "You knock on the door and wait patiently. You see no reason to disobey now."
            "You put your ear to the door listening for footsteps or any indication of their approach but find none."
            k "Hey! No worries, I'm right here."
            "The door swings open to them grinning widely."
            k "I knew you wouldn't betray my trust."

        "Open the door yourself.":
            $ currentCompliance -= 2
            "You open the door only to come face to face with your captor on the other side."
            "They almost look disappointed in you."
            k "Jaydyn. I thought you would remember. Do you need a memory device? I have a supply of sticky notes actually."
            v "No thanks. I'll uh, remember next time."
            "You apologize briefly for 'forgetting' and they soon perk up and smile again."
    "They direct you towards your given bedroom again. Notably following you the whole way through."

    ## Section for expanding bathroom privileges
    if not canBrush and currentCompliance >= lowComplBR and usedToilet:
        $ canBrush = True
    elif not canBath and currentCompliance >= lowComplBR and brushedTeeth:
        $ canBath = True
    elif canBrush and canBath and currentCompliance >= lowComplBR:
        jump dinnerWithMyMan
    elif lowComplBR > currentCompliance:
        k "I am a bit disappointed in you. I expected a little bit more trust. Until you trust me a bit more, I'll have to refuse your bathroom requests."
        k "I'm sorry, but I'm doing this for you."
        jump day_5



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
    return

label brushTeeth:
    "The door swings open and you see all the contents."
    "toothpaste, hair and toothbrushes, and many bottle of pills. Pills with another sticky note."
    v "'Don't Touch! :-) --Isaac'"
    menu:
        "Rummage through the pills.":
            currentCompliance -= 1
            "You're really putting your school's D.A.R.E. program to good use."
            "You find mostly tylenol and advil. Some other drugs you don't know but none you think will be useful."
            "At this point you've over turned enough bottles there's no hope in putting them back into place."
            "Oh well."
        "Leave them be.":
            currentCompliance += 1
            if currentCompliance > highComplBR:
                "You're really putting your school's D.A.R.E. program to good use."
                "You find mostly tylenol and advil. Some other drugs you don't know but none you think will be useful."
                "At this point you've over turned enough bottles there's no hope in putting them back into place."
                "Oh well."
            else:
                "You forgo your curiosity and reach for the toothbrush."
    "Its funny. You never thought there'd be a day where you'd look forward to dental hygeine."
    "But between your current situation and the stench in your bedroom, the mint and water is refreshing."
    return

label takeBath:
    "You let yourself be submerged in the warm water. It almost feels like someone holding you."
    "You shake the thought off. Such an idea is uncomfortable given the circumstances."
    "You look around."
    "Beside the nozzle is a basket of soaps and hair products. On them is another sticky note."
    "How did they put a sticky note in the bathtub?"
    v "Use these! I chose them out just for you. -- Isaac."
    if brekkiePref == 1:
        "In the basket all the items are scented with banana. Interesting."
    elif brekkiePref == 2:
        "In the basket all the items are scented with strawberry. Interesting."
    elif brekkiePref == 3:
        "In the basket all the items are scented with honey. Interesting."
    else:
        "All items are scented plain. Odd."
    "Will you actually use the products given?"
    menu:
        "Use them":
            $ saidToShampoo = True
        "Don't use them":
            $ saidToShampoo = False
    if saidToShampoo or currentCompliance > highComplBR:
        "You open the bottles and rub shampoo into your hair."
        v "It's nice in a weird way that they still think of me."
        "Weird? Certainly. 'Nice' is a separate question."
        "Still, its hard to deny that at the very least you smell a lot better."
    else:
        v "No thank you."
        "There's no need to cover yourself in whatever your captor has arranged for you."
    "You emerge eventually, cleaned and all."
    return
