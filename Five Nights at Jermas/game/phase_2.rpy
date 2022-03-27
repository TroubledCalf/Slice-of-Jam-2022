default acceptedCoffee = False
default acceptedBook = False
default hadLunch = False
label phase_2:
    label day_3:
        scene bedroom
        $ compliance = compliance // 2
        "You're starting to feel unclean. Of course, there's no shower in here."
        "No mirror either, so you can't even check your appearance for sure."

        v "This."
        v "Is."
        v "Hell."

        # add more thoughts, specifcally emotions here
        # filler
        "Like clockwork, the kidnapper starts walking down the hall."
        "The latch opens with a click and they walk in."

        # demand scene
        menu:
            "Demand to go home again":
                $ compliance -= 1
                "Maybe there's still a chance of going home? They seem like they listen..."
                v "Can I please go home?"
                k "You don't seem so determined anymore. That's good."
                k "But I think you're starting to understand now."
                k "This is your home."
                "With that, they leave the room and you hear a latch click."
                "You pretty much expected that."
                "All you can do is just sit and wait."
                # filler
            "Don't anger them":
                $ compliance += 1
                v "Good morning."
                k "Good morning, my dear."
                "They wrinkled their nose  upon entering the room."
                k "You might need a shower soon. Not to worry! I'll help you with that later."
                "With that, they leave the room and you hear a latch click."
                "Once again, you're alone in this little room with nothing to do."
                # filler

        #breakfast scene
        "You hear the click of the door again."
        k "I would be a poor host if I did not provide for my guests."
        "They approach you holding a tray and take a seat beside you on the bed."
        "Oatmeal again."
        "This place is driving you insane."
        k "This time, I made you oatmeal the way you asked."
        k "See, I can be nice to you if you want, but you just have to cooperate."
        k "Your treatment is entirely up to you, my dear."
        # a not-so-nice smile I imagine
        "He waits expectantly with the bowl."
        menu:
            "Take the oatmeal.":
                # remember breakfast choice from before
                $ compliance += 1
                "If you want to escape, you can't starve."
                k "Good."
                k "You need to be nice and healthy."
                # filler
            "Refuse it":
                $ compliance -= 1
                "They make a concerned face."
                k "If you are not hungry right now, that is fine, but please eat."
                k "You can eat whenever you like, and I will take your dishes when you sleep."
                "He puts the bowl beside your bed on a night stand."
                # filler
        "He takes a few steps back and turns towards the door."
        menu:
            "Attack your captor":
                $ compliance -= 4
                "You launch yourself at your captor."
                "He takes one step back, and you land flat on your face."
                #show creepy smile
                k "Now, now."
                k "We can't have much of that can we?"
                "As you pull yourself off the floor, he quickly makes his escape."
                "Exhausted and deafeated, you climb into bed and cry yourself to sleep."

                scene black
                with fade

                jump day_3

            "Do nothing":
                $ compliance += 4
                "You drift to sleep, harrowed by the day's events..."
                scene black
                with fade
                if compliance < -2:
                    jump day_3
                else:
                    jump day_4

    #lunch day
    label day_4:
        $ compliance = 0
        "You wake up and groan loudly."

        # filler

        "As expected, you hear the footsteps again."
        "The latch opens with a click and they walk in."

        v "Let me guess. You have oatmeal for me."

        k "Haha, there's the spirit. You're finally understanding your place in our home."
        k "But no, breakfast isn't ready yet. I actually wanted to come give you a book."
        "They hold out a hardcover copy of 'Beauty and the Beast'."
        menu:
            "Accept the book.":
                $ compliance += 1
                $ acceptedBook = True
                v "I do need some entertainment, I guess..."
                k "Trust me, you'll love this book."
                k "Hopefully it inspires you in your actual life."
                "That confused you."
                v "What do you mean?"
                "They smiled."
                k "Don't worry about it."
            "Refuse the book.":
                $ compliance -= 1
                v "I don't want your stupid book."
                k "No? Well, I guess you'll be bored and that's your own fault."
                k "I'm trying to be nice to you and treat you well but if you won't accept that, no one can do anything."
                k "Whatever. I'll be back with breakfast."
                "With that, they left the room."

        #breakfast scene
        "You hear the click of the door again."
        k "Food's ready!"
        "Oatmeal again."
        "Could this person cook anything else?"
        k "Here's your oatmeal, just the way you like it!"
        menu:
            "Take the oatmeal.":
                # remember breakfast choice from before
                $ compliance += 1
                "You don't really have much choice."
                k "Good."
                k "I'm glad you like my cooking so much."
                "With that, they leave the room. There is no latch noise."
            "Refuse it":
                $ compliance -= 1
                "They make a concerned face."
                k "Alright then. I'll leave it here in case you get hungry."
                k "You can eat whenever you like, and I will take your dishes when you sleep."
                "He puts the bowl beside your bed on a night stand."
                "With that, they leave the room. There is no latch noise."
        "Within a few minutes, they returned."
        k "I almost forgot, do you want coffee?"
        menu:
            "Accept coffee":
                $ acceptedCoffee = True
                "You're tired, so why not?"
                v "Okay."
                "The kidnapper clapped their hands."
                k "Wonderful!"
                k "And do you know what this means?"
                "Suddenly you found yourself a little nervous."
                v "W-what does it mean?"
                k "You get to see my kitchen!"
                "You breathed a sigh of relief."
                "In fact, this was a good thing!"
                "You could now learn more about the house..."
                jump kitchen
            "Refuse coffee":
                k "Oh, I would've guessed you'd be tired."
                k "But, as always, everything is up to you."
                k "I guess you can stay down here while I drink coffee in the kitchen."
                k "By myself."
                k "Without a companion."
                "With a straight face, they leave the room."
                jump no_kitchen

        label kitchen:
            "You follow them out of the room and down the hall into a little kitchen."
            "There was indeed a coffeepot brewing some delicious-smelling vanilla coffee."
            k "Here's my little kitchen! Do you like it?"
            menu:
                "yes":
                    $ compliance += 1
                    v "It's cute. And the coffee smells great."
                    k "I'm glad you like it! The coffee is just about ready, so why don't you sit down?"
                "no":
                    $ compliance -= 1
                    v "I don't want to be here."
                    k "Sure you do! Sit down over there, please."

        # filler
        "They continue to drink in silence."
        "They get up."
        k "Well, that's enough of an adventure for you. I hope you had a good time!"
        "They take your hand to lead you back down."
        "You test the grip and notice there's no way to get your hand out."
        "It was probably unfair to expect to be able to escape this easily."
        # hallway image here
        "Wr continue to walk in silence back to the room."
        k "Okay, back into the room you go! Sleep well, honey!"
        jump after_kitchen

        label no_kitchen:
            "Maybe you should've taken the coffee?"
            "They could've taken you to the kitchen."
            jump day_5

        label after_kitchen:
            "Having nothing better to do, it's probably time to sleep."
            "You slowly drift into dreams in the bed that you've unfortunately gotten used to."
            if compliance < -2:
                jump day_4

    # lunch for real
    label day_5:
        $ compliance = 0
        "You wake up to yet another day on this thin mattress."

        if acceptedCoffee:
            "But at least you had gotten out of this room yesterday."
            "You're quickly interrupted from that thought by a familiar noise."

        "Yet again, you hear the same footsteps coming down the hall."

        """After five or so days (had it been that many? you're starting to lose count...) of hearing those footsteps,
        you find yourself almost habituated with them - a signal that the day is about to start.
        """
        "The latch opens with a click and they walk in."

        v "Do you have my oatmeal now?"

        k "Getting eager for my oats, aren't you?"
        k "You'll have to wait for me a little longer. It's not ready yet."
        if acceptedBook:
            k "Would you like to read that book together while we wait?"
        else:
            k "But, I did bring the book with me if you'd like to give it another shot."
            menu:
                "Accept the book.":
                    $ compliance += 1
                    $ acceptedBook = True
                    "Yesterday was pretty boring..."
                    v "Okay, fine."
                    k "Trust me, you'll love this book."
                    k "Hopefully it inspires you in your actual life."
                    "That confused you."
                    v "What do you mean?"
                    "They smiled."
                    k "Don't worry about it."
                "Refuse the book.":
                    $ compliance -= 1
                    v "I still don't want your stupid book."
                    k "That's okay, you'll just be bored."
                    k "Or maybe not, since I have something more planned for you."
                    k "Anyway, I'll be back with breakfast!"
                    "They left in good spirits, for some reason..."


        #breakfast scene
        "After a few minutes, you hear the click of the door again."
        k "Food's ready!"
        "Ah, here's the oatmeal."
        "It looked more appetizing than before for some reason."
        k "Here's your oatmeal, just the way you like it!"
        menu:
            "Take the oatmeal.":
                $ compliance += 1
                "You don't really have much choice."
                k "Good."
                "It wasn't actually half bad... was it getting better?"
                v "This is good!"
                k "I'm glad you like my cooking so much."
                "With that, they leave the room. There is no latch noise."
            "Refuse it":
                $ compliance -= 1
                "You still will not have their oatmeal, no matter how good it smells."
                k "Wow, you still don't want it?"
                k "Well, as usual, I'll just leave it here for when you want it."
                "He puts the bowl beside your bed on a night stand."
                "With that, they leave the room. There is no latch noise."
        "Within a few minutes, they returned."

        k "I almost forgot, do you want coffee?"
        if acceptedCoffee:
            menu:
                "Accept coffee":
                    #$ acceptedCoffee = True
                    "Another look at the kitchen might help."
                    v "Okay."
                    "The kidnapper clapped their hands."
                    "Is it just you, or did they do that yesterday too?"
                    k "Wonderful!"
                    "They take your hand."
                    k "Let's go!"
                    jump kitchen_day_5
                "Refuse coffee":
                    "There wasn't really anything helpful in the kitchen."
                    k "Oh... why do you not want any today?"
                    k "Nevermind, that's fine, I still have another idea you might like."
                    "With a disappointed face, they leave the room."
                    jump no_kitchen_day_5
        else:
            menu:
                "Accept coffee":
                    #$ acceptedCoffee = True
                    "You didn't go last time, so maybe it's time to go today."
                    v "Okay."
                    "The kidnapper clapped their hands."
                    k "Wonderful!"
                    k "And do you know what this means?"
                    "Suddenly you found yourself a little nervous."
                    v "W-what does it mean?"
                    k "You get to see my kitchen!"
                    "You breathed a sigh of relief."
                    "In fact, this was a good thing!"
                    "You could now learn more about the house..."
                    jump kitchen_day_5
                "Refuse coffee":
                    "You still don't want their coffee"
                    k "You still don't want any?."
                    k "Again, that's fine, I still have another idea you might like."
                    "With a straight face, they leave the room."
                    jump no_kitchen_day_5

        label kitchen_day_5:
            "You follow them out of the room and down the hall into a little kitchen."
            "There was indeed a coffeepot brewing some delicious-smelling vanilla coffee."

            if acceptedCoffee:
                k "Welcome back to the kitchen!"
            else:
                k "Here's my little kitchen! Do you like it?"
            menu:
                "yes":
                    $ compliance += 1
                    v "It's cute. And the coffee smells great."
                    k "I'm glad you like it! The coffee is just about ready, so why don't you sit down?"
                "no":
                    $ compliance -= 1
                    v "I don't want to be here."
                    k "Haha, you'll change your mind once you try the coffee. Sit down over there."
            # filler

            "After finishing their coffee and looking out the window for a bit, they get up."
            if acceptedCoffee:
                "Like yesterday, they grab your hand firmly and walk you back down the hall."
            else:
                k "Well, that's enough of an adventure for you. I hope you had a good time!"
                "They take your hand to lead you back down."
                "You test the grip and notice there's no way to get your hand out."
                "It was probably unfair to expect to be able to escape this easily."
            # hallway image here
            "We continue to walk in silence back to the room."
            k "Okay, back into the room you go! I'll come get you later! I have a surprise!"
            $ acceptedCoffee = True
            jump after_kitchen_day_5

        label no_kitchen_day_5:
            "Maybe you should've taken the coffee?"
            "They could've taken you to the kitchen."
            if acceptedBook:
                "You decide it's better to just read the book."
                "It's a pretty good story..."
                "You find yourself relating a lot with Belle."
                "After reading for a while, you start to get sleepy..."
                $ compliance += 1
                jump lunch
            "Maybe just a nap would be nice..."
            jump lunch

        label after_kitchen_day_5:
            "The kitchen trip didn't really offer much information."
            "It was worth a shot though."
            "But what to do for now?"
            if acceptedBook:
                "You decide it's good to read the book."
                "It's a pretty good story..."
                "You could relate a lot with Belle."
                "After reading for a while, you start to get sleepy..."
                $ compliance += 1
                jump lunch
            "Maybe just a nap would be nice..."
            jump lunch

        label lunch:
            "You feel a gentle hand brush your face."
            v "W-wh-what?"
            k "Rise and shine~"
            k "It's time for lunch!"
            menu:
                "Refuse":
                    $ compliance -= 1
                    "This was the surprise?"
                    "No. You're not going to follow them."
                    v "No, I don't think I want to join you..."
                    "The kidnapper sat down next to you in bed."
                    k "Awwww, why not? It'll be fun~"
                    v "I just don't want to."
                    k "Alright, that's fine. I'm sure you'll agree later."
                    "With that, they left the room, leaving you with nothing more to do but sleep."
                    "You slowly drift to sleep..."
                    jump end_day_5
                "Follow them":
                    $ compliance += 3
                    "More information would always be helpful."
                    "You choose to go to lunch with them."
                    v "Okay, I can't wait!"
                    k "I knew you'd want to spend more time with me!"
                    "They grab your hand."
                    k "Follow me, and we can have a lovely afternoon together."
                    jump lunchtime
        label lunchtime:
            $ hadLunch = True
            if acceptedCoffee:
                "You found yourself in the now-familiar kitchen."
            else:
                "It's a relatively small kitchen but adequate for cooking."
            "You see a stack of vegetables on the counter."
            k "We're making soup!"
            "You were just glad to not have oatmeal."
            v "So are we going to start?"
            k "Yup! One thing though - you don't get to use a knife."
            "You can't help but admire his caution. They thought of everything."
            k "I have a cabinet of spices, so put whatever you want in the boiling water."
            "You spend the next 15 minutes choosing spices."
            k "Perfect!"
            "They put in the spices and the both of you sit down to wait."
            if acceptedBook:
                k "So, how are you liking the book?"
                menu:
                    "Like it":
                        $ compliance += 1
                        v "I'm really liking it!"
                        k "You can relate to it, right?"
                        v "Yup."
                        v "Plus, I'm really bored anyway, so I'm glad to have anything."
                    "Dislike it":
                        $ compliance -= 2
                        v "It's awful."
                        v "What, you thought I'd be happy with this just because it's in a book?"
                        v "I'm not Belle, you know."
                        # sad face
                        k "I'm sorry to hear you didn't like it."
                        k "But I really do hope you'll get used to me eventually."
            else:
                k "So, how are you doing?"
                menu:
                    "Bad":
                        if compliance > 4: # currently the max day 5 c is 8, so 4 seems fitting
                            v "I'm doing good!"
                            "Wait... what? You're not doing good... Why did you say that?"
                            jump good
                        else:
                            jump bad
                    "Good":
                        v "I'm doing okay!"
                label good:
                    $ compliance += 2
                    k "That's good to hear!"
                    k "Though, I think you do need a shower."
                    k "I know I promised you that before, but I've just been so busy with you!"
                    k "It's a lot of work to keep you happy."
                    v "I know how hard you work!"
                    "What's wrong with you? Have you forgetten who this is?"
                    k "Haha, thank you for appreciating me!"
                    k "Anyway, I will help you with the shower if today goes well."
                    v "Thank you!"
                label bad:
                    $ compliance -= 1
                    v "I hate it here."
                    k "That's not good!"
                    k "Anything I can do to make it better?"
                    v "I think I really need a shower, honestly..."
                    k "You're right! I'm so sorry. I know I promised earlier, but I forgot."
                    k "I will definitely help with that if today goes well."
                    v "Okay, thank you."
            "You sit in silence for a bit longer."
            "Suddenly, they get up."
            k "I think the soup's ready!"
            "They bring the soup off the stove."
            k "Could you get the bowls and set them on the counter?"
            "You do as they asked and they poured in soup."
            k "Okay, let's eat!"
            "You don't say much as you eat."
            # filler
            "..."
            "The soup isn't bad."
            k "This was good soup, don't you think?"
            "They take the bowls and put them in the sink."
            k "Okay, you know the drill!"
            "They take your hand and walk you back to your new room."
            jump end_day_5
        label end_day_5:
            k "Goodnight!"
            "Though you are not tired, you climb into bed."
            "After possibly hours, you finally drift to sleep."
            if compliance < -1:
                jump day_5
            else:
                if compliance >= 4:
                    call interludeTwoHighComp
                else:
                    call interludeTwoMidComp
                jump goToBathroom
