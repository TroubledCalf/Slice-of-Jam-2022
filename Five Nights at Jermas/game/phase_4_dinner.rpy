default highComplianceDN = 7 # <- this is just a placeholder value
default var_flag = 0 # <- flag for variation in dialogue for pretend-phase
label dinnerWithMyMan:
    $ compliance = compliance // 2
    #place holder dialogue
    "You wake up feeling excited for the first time in a while."
    v "Today's going to be great!"
    "Wait... hmmm... is it correct to be excited? This person was a kidnapper, right?"
    "You stand by the door to greet your captor."

    "The sound of steps appears as expected and they walk in."
    k "Good morning, Jaydyn!"
    v "Is my oatmeal ready?"
    k "Nope, but we can eat in the kitchen today."
    v "Okay!"
    "You follow them down the hall to the kitchen, where oatmeal is set out."
    k "I made you your usual!"
    v "Thank you!"
    "You both sit down to eat."
    k "So, would you like to chat?"
    menu:
        "yes":
            v "Sure!"
            $ compliance += 1
            jump yes_to_chat

        "no":
            $ compliance -= 1
            "Probably not the best idea to tell them too much about yourself."
            if compliance > 1:
                v "Sure!"
                "Jaydyn... what are you doing?"
                "You're not supposed to do that..."
                jump yes_to_chat
            else:
                jump no_to_chat
    label yes_to_chat:
        "They talk a lot about different places"
    label no_to_chat:

    ## SHOWER

    ## LUNCH
    label lunch:
        "You hear the familiar steps and know it's probably lunch time."
        "The door opens and they walk in."
        v "Is it time for lunch?"
        k "Yes it is! Are you going to join me?"
        menu:
            "Refuse":
                $ compliance -= 1
                k "You don't want to have lunch?"
                k "We've come so far!"
                "No. You've already spent a lot of time with them and gained so little out of it."
                v "I appreciate everything you've done for me, but I just don't want lunch today."
                v "I hope you can respect that."
                "A disappointed look crosses their face."
                k "Of course."
                "With that, they left the room, leaving you with nothing more to do but sleep."
                "You slowly drift to sleep..."
                jump book
            "Follow them":
                $ compliance += 3
                "They've treated you well so far, so why not?"
                "You choose to go to lunch with them."
                v "Okay, let's go!"
                k "I told you that you'd eventually get used to me."
                "That's... a terrifying thought..."
                "They grab your hand and take you to the kitchen."
                jump lunchtime
        label lunchtime:
            "Like before, you see a pile of vegetables on the counter."
            k "We're making soup again!"
            "Not ideal, but still better than oatmeal."
            v "So are we going to start?"
            k "Yup! One thing though - you don't get to use a knife."
            "You can't help but admire his caution. They thought of everything."
            k "I have a cabinet of spices, so put whatever you want in the boiling water."
            "You spend the next 15 minutes choosing spices."
            k "Perfect!"
            "They put in the spices and the both of you sit down to wait."
            k "So, how are you doing?"
            menu:
                "Bad":
                    if compliance > 2:
                        v "I'm doing good!"
                        "Wait... what? You're kidnapped... Why did you say that?"
                        jump good_p4
                    else:
                        jump bad_p4
                "Good":
                    v "I'm doing okay!"
            label good_p4:
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
            label bad_p4:
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
    ## BOOK/NAP
    label book:
        pass
    ## DINNER
    # this is the most important part

    menu:
        "Attempt to escape":
            jump escape_attempt # compare the compliance score here
        "Stay with them": # regardless of the compliance score, you choose to lose (why? i don't know)
            jump badEnd




    label escape_attempt:
        # there are three different outcomes you can go about this:
        # 1. your compliance score is too low => you don't trust the kidnapper. you don't do anything. you loop back to the start
        # 2. your compliance score is in the middle range => you are able to escape. good ending.
        # 3. your compliance score is too high => you are not able to escape. bad ending.
        if compliance > highComplianceDN: # the 3rd outcome
            "You will escape."
            v "You know, I've been thinking, I've grown into you, Isaac."
            v "I want to stay with you."
            "You need to escape."
            "You have to escape."
            "Remember, you were kidnapped here."
            v "Can I stay here? Too many bad things are happening when I am out there, and I am too scared to go out."
            v "I feel much safer when I am with you. You are my safe haven, Isaac."
            "No, no, NO! THIS IS NOT WHAT YOU ARE SUPPOSED TO DO!"
            "JAYDYN! NO!"
            k "You are finally accepting me...I am so happy. I love you, I love you so much Jaydyn!"
            "..."
            "..."
            "..."
            "Jaydyn chooses to stay with Isaac."
            "Jaydyn, smiling as brilliantly as ever, replies back to Isaac."
            v "I love you too!"
            jump badEnd
        elif compliance < -7: # the 1st outcome
            $ match var_flag:
                case 0:
                    "You try to escape by distracting the kidnapper. You plan to make them go to the kitchen to cook something for you."
                    v "Hey, um, Isaac."
                    k "Yeah? Do you need something?"
                    v "Yeah, actually...would it be possible if you cook something for me?"
                    k "Oh...is the food not to your liking?"
                    v "Oh no, it's just that I am especially feeling hungry today..."
                    "The kidnapper stares into your eyes, long and hard. You get the shivers from their pentrating stare."
                    "They may have noticed you had something going on. But the kidnapper don't say much. They just stare."
                    "Then, they finally get up from the table to fetch you something, but their eyes never leave you."
                    k "Okay, we have some ramen noodles and..."
                    "The kidnapper's voice starts fading out for you, because you are too anxious, looking for the right opportunity to make your escape."
                    k "...You've been awfully quiet. Is everything okay?"
                    "Their eyes are right in front of your eyes. They know. They know that you are trying to escape." #eyes jumpscare
                    v "...N-no? Everything is fine!"
                    "Today is not the day..."
                case 1:
                    #write smth idfk
                case 2:
                    #write smth else idfk
                case _:
                    #write smth else
            jump dinnerWithMyMan # change this label to somewhere else other than dinnerWithMyMan for the sake of variety in dialogue.
        else:
            "You try to escape by distracting Isaac. You plan to make Isaac go to the kitchen to cook something for you."
            v "Hey, Isaac."
            k "Yeah? Do you need something?"
            v "Yeah, actually, I really liked the tuna sandwich you made, and I was wondering you can make some more for me?"
            k "Oh really? I'm so glad that you liked it. I'll try to make one as soon as possible!"
            "Isaac excitedly scampers to the cabinets in the kitchen while humming 'Hip To Be Square' by Huey Lewis & The News. Until he groans a little."
            k "I'm so sorry, but I have to go upstairs to get some more ingredients...I'm so sorry, I'm so sorry..."
            v "It's okay."
            k "I'll quickly go upstairs to get some more. Will you wait for me?"
            v "Sure, don't worry too much about me."
            "Isaac runs upstairs, and closes the door on you."
            "You are left alone, and you start thinking."
            """You have a staircase to upper ground, which means you can find the front door to get out of the building.
            But there is always a chance that while you are looking for the front door, you meeet Isaac. You will not be able to get out.
            You will be stuck here forever, under Isaac's watch."""
            """Another option is the glass sliding door. You see that the basement, or the entire house in fact, is placed
            on a declining hill. There is nothing beyond but just greenery and the moonlight that is shining ironically too bright.
            Isaac is upstairs, probably actually getting ingredients, so there is less chance for Isaac to appear in front of the glass door
            as you attempt to escape."""
            "At this point, escaping through the glass door is the only viable option that you have."
            """As swiftly as possible, you slide open the door, and as you step out
            and your foot touch the dirt that has been warmed by the midsummer sun, tears stream start running down your face."""
            "You are finally free."
            jump winEnd

    label winEnd:
        # place holder: you win screen!
        return

    label pretend_phase:
        #yada yada

        #point at escape_attempt

    return
