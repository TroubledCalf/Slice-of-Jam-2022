# Compliance
default compliance = 0
default brekkiePref = 0
default ateFood = False

# Soundtracks

# Characters
define v = Character("You")
define k = Character("Kidnapper")

# Character sprites


# Scenes/backgrounds
image black = "#000"
image bedroom = "images/backgrounds/bedroom_concept_art.png"
image white = "#ffffff"
image red = "#CD5C5C"

label start:
    #phase 1
    label day_1:
        scene black

        "You wake up."

        show bg bedroom
        with fade(0.1,0.0,1.5)

        "Where is this?"

        "Slowly, your senses start to come to you..."

        "You're laying down on a thin mattress in what appears to be a small bedroom? Definitely not your bedroom."

        "The room smells musty and damp. The floor feels cold on your feet."

        "Strange. Especially the last thing you remember is the hot sunlight of mid-July."

        v "I am underground."

        "Waves of sheer panic starts running through your system. Your breath quickens."
        "It feels as if a vaccum is sucking up all the air out of your lungs. Desperate, you look for a window. An opening. Anything."
        "You finally find a small opening, where the light from outside can come through, but it is too high up to reach."
        "You can't do anything here. You are stuck."

        "Suddenly, you hear footsteps coming down the hall. "

        menu:
            "Pretend to be asleep because they might be dangerous":
                $ compliance -= 1
                "You hide underneath the covers and shiver as you wait for the door to open."
                "Your heart beats faster as the steps get closer..."
                "The door swings open with a creak."
                "Someone steps in and all you can do is hope to not be killed as you stuffle out your breath."
                k "Hi~ I know you're awake, by the way. There's no need to pretend."
                "You slowly lift your head out of the blankets."
                k "There you are!"
                "They grin at you as you cower away."
            "See who it is":
                $ compliance += 1
                "You get up from the bed and wait for the door to open."
                "Your heart beats faster as the steps get closer..."
                "The door swings open with a creak."
                # show the kidnapper
                "A shadowy figure enters the room."
                k "Hello, I see you're up now."
                # how should the kidnapper address the victim other than "you?"
                v "...You're not going to hurt me, are you?"
                k "Of course not! I brought you here for a reason."
                v "W-what? I-I don't even know who you are..."
                k "That's okay, you'll get to know me eventually."
                "This is very wrong."
                # these are sort of place-holder values and options just to get something down

        label loop_back_phase1:
            menu:
                "Demand to go home":
                    $ compliance -= 1
                    "You jump off the bed and scream at them."
                    v "I want to go home now!"
                    k "Go home? This IS your home now. Don't you worry, you'll love it here!"
                    "With that, they leave the room and you hear a latch click."
                    "All you can do is curl up and start sobbing."
                "Just accept the kidnapper for now":
                    $ compliance += 1
                    v "Oh.. okay..."
                    k "See, you're getting it!"
                    k "We're going to have so much fun together!"
                    "With that, they leave the room and you hear a latch click."
                    "You take a deep breath, grateful to still be alive."
                    "At least this person doesn't seem intent on killing you. That means you could escape..."


            "You hear the click of the door again."
            k "I would be a poor host if I did not provide for my guests."
            "They approach you holding a tray and take a seat beside you on the bed."
            "Oatmeal."
            "Not the most enjoyable of meals, not by a long shot."
            k "I wish I could have made something more appealing, but of course..."
            k "its hard to do so without knowing your preferences."
            # a note-so-nice smile I imagine
            "They wait expectantly."
            menu:
                "Take the oatmeal.":
                    $ compliance += 1
                    "Unpleasant as your situation may be, it is hard to refuse warm food."
                    k "Good."
                    k "I wouldn't want you to go hungry."
                "Refuse it":
                    $ compliance -= 1
                    "They continue to smile at you."
                    k "If you are not hungry right now, that is fine."
                    k "You can eat whenever you like, and I will take your dishes when you sleep."
                    "He puts the bowl beside your bed on a night stand."
            "He stands up once again."
            k "Before I leave, is there anything more you'd like to speak about?"
            "You get an idea."
            v "Actually, yes."
        menu:
            "Attack your captor":
                $ compliance -= 4
                "You launch yourself at them."
                "They seem to take a few kicks from you before sighing."
                k "Did you think you had a chance?"
                "You're lifted and carried onto the bed."
                k "Please don't cause problems for us."
                v "THERE IS NO 'US!'"
                k "Are you so sure of that? I wouldn't hold your breath."
                k "Just go back to sleep, will you?"
                v "You hide under the covers, sorely defeated."
                $ compliance = compliance // 2
                jump loop_back_phase1

            "Do nothing":
                $ compliance += 4
                "You see the kidnapper finally leaving you in the lonely room. Thank god."
                "But even if they DID leave, there is nothing for you to do here. Nor do you feel brave enough to explore the room just yet."
                "After staring into the void for some time, your body gives out, and you slowly drift away to sleep..."
                jump day_2

    label day_2:
        $ compliance = compliance // 2 # <- 1/2 the current score, instead of reset to 0
        # you demand to go home or not again
        # and you have breakfast again

        "You wake up."

        "You look out into the room you're in and remember everything from yesterday."

        "Trapped."
        "Lost."
        "Confused."

        "And you can't do a thing about it."

        # add more thoughts, specifcally emotions here
        "You let this thought consume you until you hear the footsteps from yesterday."

        "They calmly walk into the room as if the relationship between the both of you is anything other than kidnapper and victim."

        k "Good morning. How are you today?"

        menu:
            "Demand to go home":
                $ compliance -= 1
                "Maybe you could demand to go home again?"
                v "I want to go home now!"
                k "Go home? You forgot already? This is your home now."
                k "But I understand, it'll take you some time to accept that."
                k "I came down to let you know breakfast will be ready soon."
                "With that, they leave the room and you hear a latch click."
                "Once again, you just lay defeated."
                "There is nothing you can do, so you just sit there."
            "Just accept the kidnapper for a little longer":
                $ compliance += 1
                v "So are you going to bring me food soon?"
                k "See, you're getting it!"
                k "Keep this up and maybe I'll even let you out of this room..."
                "With that, they leave the room and you hear a latch click."
                "You take a deep breath, once again grateful to still be alive."
                "If you were let out of this room, you could escape..."
                "That's a thought for later though, so you just quietly wait for them to come back."

        #breakfast scene, pretty much EXACTLY the same as yesterday
        "You hear the click of the door again."
        k "It is time for some more oatmeal! I know you wanted some more sicne yesterday."
        "They approach you holding a tray and take a seat beside you on the bed."
        "Oatmeal. Again."
        "But given that you are kidnapped, you can't say much. This is definitely better than not getting food at all."
        k "I know that I've been offering you oatmeal two days in a row...I'm so sorry."
        k "But I don't know...after all, we don't know each other as well."
        k "That's okay though! We have all this time together to get even closer!"
        # a note-so-nice smile I imagine
        "Differently from yesterday, they place the spoon in your hands, which have been shaking this entire time."
        "They wait for you to take a spoonful."
        menu:
            "Take the oatmeal.":
                $ compliance += 1
                k "Good!"
                k "I told you I wouldn't want you to go hungry."
                k "On that note, what I wanted to ask was, what do you prefer on top? On your oatmeal, I mean. I only have so many ingredients."
                k "I could give you banana slices, strawberry, hell, even honey."
                "He looks at you pointedly on that last word."
                menu:
                    "remain silent.":
                        $ compliance -= 1
                        k "You're not talkative today. That's fine. There's always tomorrow."
                    "banana slices":
                        $ compliance += 1
                        $ brekkiePref = 1
                        "They clasps his hands together."
                        k "Wonderful. I will keep this in mind!"
                    "strawberry":
                        $ compliance += 1
                        $ brekkiePref = 2
                        "They clasps his hands together."
                        k "Wonderful. I will keep this in mind!"
                    "honey":
                        $ compliance += 1
                        $ brekkiePref = 3
                        "They clasps his hands together."
                        k "Wonderful. I will keep this in mind!"
                    "watermelon":
                        $ compliance -= 2
                        $ brekkiePref = 4
                        "Their smile fades slightly, before they regains composure."
                        k "...You'll learn to appreciate what I offer you in time."
            "Refuse it":
                $ compliance -= 1
                "They continue to smile at you."
                k "If you are not hungry right now, that is fine."
                k "You can eat whenever you like, and I will take your dishes when you sleep."
                "They puts the bowl beside your bed on a night stand."

        "They stands up once again."
        k "Before I leave, is there anything more you'd like to speak about?"

        menu:
            "Attack your captor":
                $ compliance -= 4
                "You launch yourself at your captor."
                "They hit you back with ease, leaving you in a heap on the floor."
                "Really? I've treated you so well and you attack me like this?"
                "Please don't ruin our relationship."
                v "LET ME OUT OF HERE!"
                k "You never learn, do you?"
                "They lift you off the floor and put you back into bed."
                "Here, maybe a good night's sleep will make you feel better."
                jump day_2

            "Do nothing":
                $ compliance += 4
                "Okay. That's fine! I hope you open up more to me soon."

        # filler

        #on day 2, you are given a test. gameplay-wise, this is a foreshadowing
        #to the player that you need to pass this point to advance to the next phase
        #(as well as meeting the threshold compliance score)

        "You watch the kidnapper walk out of the door. But something is different from last time."
        "They always lock the door when they leave, but this time, they just left."

        menu:
            "Walk over to the door":
                jump after_walk_to_door
            "Remain where you are.":
                pass

        label after_walk_to_door:
            "As you have expected, when you turn the doorknob, it is not locked."
            "Should you open the door?"
            menu:
                "Open the door":
                    #very close (AND CREEPY) shot on the kidnapper's eyes would be nice
                    #to visually explain that the kidnapper was, in fact, right outside of the door,
                    #waiting patiently to test you.
                    k "Haha! You are so funny, you actually opened the door!"
                    k "I hope you don't feel too annoyed. I am a person too, so I sometimes forget to lock the door."
                    k "Good night!"

                "Go back to the bed. Right now is not the time.":
                        if compliance >= -2: # for phase 1, the middle (normal) range is -2 to 2, inclusive.
                            "You slowly fall asleep...hoping that the day will be different tomorrow."
                            jump day_3
                        else:
                            "You fall asleep..."
                            jump day_2
 ###################################
    # phase 5
    label badEnd:
        scene white
        "You wake up abruptly to a bright light"
        scene bedroom
        # show k_smiling_creepy
        k "Get up. You're going being moved."
        v "...ok"
        "You slowly get up and follow him"
        "As you follow him, he grabs something off a shelf."
        "It looks like an ankle monitor"
        # hide k_smiling_creepy
        "He slowly approaches you with it and bends down in front of you."
        "He puts the ankle monitor around your left ankle, and you hear a click."
        "As he gets back up, he snatches your hand and briskly pulls you down the hallway and up the stairs."

        scene red
        "The sudden change in brightness from the dimly lit basement to the rest of the building burns your eyes, so you shut them."
        "He continues to drag you through the building, and eventually you feel carpet on your feet."
        #scene living_room
        "You slowly open your eyes and see him smiling with arms wide."
        "After days of being locked alone in his basement, you run towards him, tears in your eyes."
        "something im still figuring it out"
        "He walks toward the kitchen, puts on an apron, and beams at you."
        k "I'm sure you're hungry. I'll prepare breakfast for the both of us, honey."
        "He turns his back and takes a knife out from the knife block."
        "He begins chopping some fruit."
        v "Ok!"
        "What is wrong with you?!"
        "The door is unlocked! Make a break for it!"
        "Don't just stand there acting all lovey-dovey with him!"
        "This dude is a psycho!"

        menu:
            "Escape"

            "Stay"
        "..."
        "..."
        "You stay."

        #show k_smiling_creepy
        "After he finishes chopping his fruit, he approaches you with the knife."
        "He sits you both down on the couch."
        "He snatches your hand and turns it over, revealing your palm."
        "Weilding the knife, he makes a slit across your palm, and does the same to this own hand."
        "You grab his bloodied hand with your own. You wince in pain."
        k "Aw, I'm sorry, honey. I don't want to make you cry."
        "He says as he wipes a tear from your cheek."
        "This unleashes something in you, and you begin to bawl."
        "Still smiling, he leans forward and kisses your forehead tenderly."
        "He pulls away and looks you in the eyes."
        k "Don't you ever think about leaving me, ok?"
        k "I'm sorry I hurt you, but it hurts me more seeing you like this."
        k "I don't know what I would do without you."
        "You sniffle and mouth the words \"I love you\""
        "He smiles, and you smile back."
        k "However, my love,"
        "You feel a sharp pain in your abdomen"
        "You look down and see a knife sticking out from you."
        k "Til death do us part."
        "As you black out, he gets closer to your face, and you notice him staring intensely at your lips."

        scene black
        "You feel him gently brush your lips and grab the small of your back before you slump over, and your vision fades to black"
        "BAD END"



    return
