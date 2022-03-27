default highComplianceDN = 3 # <- this is just a placeholder value
default var_flag = 0 # <- flag for variation in dialogue for pretend-phase
default took_Shower = False
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
    "They wait a little longer for the oats to finish cooking."
    "You both sit down to eat."
    k "So, would you like to chat?"
    # CHOICE
    menu:
        "yes":
            v "Sure!"
            $ compliance += 1
            jump yes_to_chat

        "no":
            $ compliance -= 1
            "Probably not the best idea to tell them too much about yourself."
            if compliance > highComplianceDN - 1:
                v "Sure!"
                "Jaydyn... what are you doing?"
                "You're not supposed to do that..."
                jump yes_to_chat
            else:
                jump no_to_chat
    label yes_to_chat:
        "They talk a lot about different places they want to see in the future."
        "Oddly enough, Jaydyn is excited about those places."
        "This might be dangerous."
        "Jaydyn shouldn't trust this person, and yet... they are."
        "The conversation goes on for a terrifyingly long time..."
        k "Well, that was a good talk!"
    label no_to_chat:
        v "I'd prefer not to."
        k "Okay, that's fine. I respect you and your decisions."
        "But not Jaydyn's decision to leave earlier?"
        k "In that case, I'll leave you alone for now."
        k "Bye!"
        "They leave the room and the footsteps fade away."
    jump shower_p4
    ## SHOWER
    label shower_p4:
        "You sit by yourself for a while longer."
        "Maybe you should take a shower."
        "Your captor might treat you even better if you're clean..."
        menu:
            "Take shower":
                $ compliance += 1
                jump inBathroom_p4
            "Don't take a shower":
                if compliance > highComplianceDN:
                    $ compliance -= 1
                    v "I want to impress them!"
                    "What the- No. That's wrong."
                    jump inBathroom_p4
                else:
                    $ compliance -= 1
                    "You decide to just sit around in your room."
                    jump lunch_p4
        label after_shower_p4:
            "After your time in the bathroom, you're satisfied."
            "All you can do now is sit around."
            jump lunch_p4

    ## LUNCH
    label lunch_p4:
        "After a while, you hear the familiar steps and know it's probably lunch time."
        "The door opens and they walk in."
        if took_Shower:
            k "Wow, you smell nice today~"
            v "Thanks!"
        else:
            k "Did you forget to shower today?"
            k "That's fine, I still accept and care for you."
            v "S-sorry..."
        v "Is it time for lunch?"
        k "Yes it is! Are you going to join me?"
        # CHOICE
        menu:
            "Refuse":
                if compliance > highComplianceDN:
                    v "Sure!"
                    "NO!"
                    "YOU CAN'T DO THIS!"
                    "Jaydyn happily takes their hand to follow them out of the room."
                    "Jaydyn is not supposed to do this."
                    $ compliance -= 1
                    jump lunchtime_p4
                else:
                    k "You don't want to have lunch?"
                    k "We've come so far!"
                    "No. You've already spent a lot of time with them and gained so little out of it."
                    v "I appreciate everything you've done for me, but I just don't want lunch today."
                    v "I hope you can respect that."
                    "A disappointed look crosses their face."
                    k "Of course."
                    "With that, they left the room, leaving you with nothing more to do but sleep."
                    "You slowly drift to sleep..."
                    jump book_p4
            "Follow them":
                $ compliance += 3
                "They've treated you well so far, so why not?"
                "You choose to go to lunch with them."
                v "Okay, let's go!"
                k "I told you that you'd eventually get used to me."
                "That's... a terrifying thought..."
                "They grab your hand and take you to the kitchen."
                jump lunchtime_p4
        label lunchtime_p4:
            if hadLunch:
                "Like before, you see a pile of vegetables on the counter."
                k "We're making soup again!"
                "So this person could only cook two different things?"
                "Sad."
                v "So, are we going to start?"
                if compliance > highComplianceDN:
                    k "Yup! I'll even let you use a knife this time!"
                    "Wow, they really trust you."
                else:
                    k "That's right! You still can't use a knife, though."
                k "You know where the spices are, so let's get cooking."
                "You spend the next 15 minutes choosing spices."
                k "Perfect!"
                "They put in the spices and the both of you sit down to wait."
            else:
                "You see a pile of vegetables on the countertop."
                k "We're making soup!"
                "Better than oatmeal, at least."
                k "Yup! One thing though - you don't get to use a knife."
                "You can't help but admire his caution. They thought of everything."
                k "I have a cabinet of spices, so put whatever you want in the boiling water."
                "You spend the next 15 minutes choosing spices."
                k "Perfect!"
                "They put in the spices and the both of you sit down to wait."
                # CHOICE
                if acceptedBook:
                    k "So, how are you liking the book?"
                    menu:
                        "Like it":
                            $ compliance += 3
                            v "I'm really liking it!"
                            k "You can relate to it, right?"
                            v "Yup."
                            v "Plus, I'm really bored anyway, so I'm glad to have anything."
                        "Dislike it":
                            $ compliance -= 2
                            v "I'm not fond of it."
                            v "What, you thought I'd be happy with this just because it's in a book?"
                            v "I'm not Belle, you know."
                            # sad face
                            k "I'm sorry to hear you didn't like it."
                            k "But I really do hope you'll get used to me eventually."

            "After a few minutes, they check the pot."
            k "I think the soup's ready!"
            "You both proceed to work side-by-side to get the soup into bowls."
            "You eat quietly for a while."
            k "So, how are you doing?"
            # CHOICE
            menu:
                "Bad":
                    $ compliance -= 1
                    if compliance > highComplianceDN:
                        v "I'm doing good!"
                        "Wait... what? You're kidnapped... Why did you say that?"
                        jump good_p4
                    else:
                        jump bad_p4
                "Good":
                    $ compliance += 1
                    v "I'm doing okay!"
            label good_p4:
                $ compliance += 2
                k "I'm happy!"
                k "I'll make you even happier tonight."
                v "W-what?"
                k "It's a surprise~"
                k "I'll just say one thing..."
                k "I'm pretty skilled..."
                k "... at cooking, of course."
                v "Oh.. oh."
                k "What did you think I meant?"
                k "I won't say any more, though."
                v "Alright then, I hope it's good!"
            label bad_p4:
                $ compliance -= 1
                v "I'm still not feeling great."
                k "That's not good!"
                k "Anything I can do to make it better?"
                v "I don't know... maybe I'm still scared?"
                k "They reach out and envelope you in their arms."
                "They're surprisingly warm and maybe you have a slight inclination to lean into them..."
                v "Thank you. I think I needed a hug."
            "You sit in silence for a bit longer."
            "After finishing the meal, they take your hand and walk you back to the room."
            jump book_p4

    ## BOOK/NAP
    label book_p4:
        if acceptedBook:
            "With nothing to do in the room other than read, perhaps that's what you should do."
            menu:
                "Read":
                    $ compliance += 2
                    jump read_p4
                "Sleep":
                    if compliance > highComplianceDN:
                        $ compliance -= 2
                        "You watch in horror as Jaydyn simply decides to read the book."
                        "Did they forget who gave them the book?"
                        "Don't read it!"
                        jump read_p4
                    else:
                        "Sleeping is probably the best option."
                        "You climb into bed."
            label read_p4:
                "Minutes stretch into hours as Jaydyn goes through the book."
                "You feel a warmness building in Jaydyn as they start to appreciate the story more."
                "This doesn't seem like a good thing but there's little you can do."

        else:
            "You simply sit in the room and fiddle with your thumbs."
            "There isn't much to do, except for rereading the newspaper clippings."

        "You eventually drift to sleep."
        jump dinner


    ## DINNER
    # this is the most important part
    label dinner:
        "You hear the familiar footsteps as your slowly rouse yourself from sleep."
        k "Hey, there stranger~"
        k "It's time for a surprise..."
        v "W-what is it?"
        k "It's time for..."
        k "dinner!"
        # CHOICE
        menu:
            "Refuse to have dinner with them":
                if compliance > highComplianceDN:
                    $ compliance -= 2
                    v "Okay, I'm ready."
                    "W-what? No you're not. You should not have dinner with this person."
                    jump accepted_Dinner
                else:
                    $ compliance -= 2
                    jump refused_Dinner
            "Accept the offer":
                v "Okay, I'm ready."
                $ compliance += 1
                jump accepted_Dinner
        label refused_Dinner:
            "You shouldn't have dinner with this person."
            k "Oh... that's too bad."
            k "Well, as usual, I know you'll eventually say yes."
            k "You have to."
            k "You love me."
            k "You just don't know it yet."
            k "Good night for now, though."
            jump dinnerWithMyMan

        label accepted_Dinner:
            "They take your hand and walk you to a new room you haven't seen yet."
            "It's a dining room at the end of the hall."
            k "Here's my dining room!"
            k "Do you like it?"
            menu:
                "Yes":
                    $ compliance += 1
                    v "It has a nice ambience!"
                    jump liked_dining
                "No":
                    if compliance > highComplianceDN:
                        $ compliance -= 1
                        v "I love it!"
                        "No you don't."
                        v "It's so romantic!"
                        "WHAT IS WRONG WITH YOU JAYDYN??"
                        "DO NOT FALL FOR THEM."
                        jump liked_dining
                    else:
                        $ compliance -= 1
                        jump not_liked_dining
            label liked_dining:
                k "I'm glad you like it!"
            label not_liked_dining:
                v "Eh, it's whatever."
                k "Well, I'm sure you'll like the food, at least."
            "Anyway, why don't you sit down?"
            "You sit down as they reveal a platter with two tuna sandwiches."
            k "I made sandwiches for dinner!"
            v "Food that isn't oatmeal? You're better than I thought."
            "Really, Jaydyn? There's no need to flirt."
            "You each get a sandwich and start eating."
            "It's not half bad."
            "You both discuss various topics and Jaydyn learns a little more about the kidnapper's past."

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
            "You MUST escape."
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
            if var_flag ==  1:
                "You try to escape by distracting the kidnapper. This time, you plan to ask for some chili pepper." # asking for different condiment
                v "Hey, Isaac."
                k "What's up?"
                v "Yeah, I was wondering if you have chili pepper..."
                k "Oh, is the food bland this time? I'm sorry, I don't usually cook for someone else, so I didn't know how you'd like it."
                v "...It's fine. It's just that I'm used to eating food a bit spicy back at home..." # <- kind of showing that YOU and JAYDYN have the same end goal: going back home
                k "Okay, thanks for letting me know. I'll go check the kitchen if we have any."
                "The kidnapper gets up from the chair, but their eyes linger on yours for way too long."
                "They seem a bit disappointed when you mentioned your life before this, as if they want you to forget everythign except the current life here."
                "But disappointment is not the only emotion you see. You also see suspicion, doubt in their eyes. What if they have figured out again?"
                "You try to get out of this uncomfortable situation by smiling at them. They smile back, but it seems as if their suspicion has yet to subside."
                k "You've never smiled at me like that. Is there something wrong you did that you are not telling me right now?"
                v "W-what do you mean? All I wanted was chili pepper..."
                "But they weren't wrong. They probably figured out again. Today's not the day."
                $ var_flag += 1
                jump pretend_phase
            elif var_flag ==  2:
                # asking for the kidnapper's favourite drink, the kidnapper makes it for JAYDYN but it is drugged
                # because the kidnapper knew that something was up, so just to tie JAYDYN to the basement, they drug JAYDYN,
                # gaslighting them that there are so many more dangerous things out there, thus JAYDYN needs to stay safe in the basement when they can
                "You try to escape by distracting the kidnapper. This time, you plan to ask them to make you their favorite drink."
                v "Um, so..."
                "The kidnapper makes eye contact with you. You have yet to get used to their unsettling gaze. You avert your eyes to the served tuna sandwich."
                "You briefly think that tuna sandwich is definitely much more appetizing than the daily oatmeal bowls before opening your mouth again to speak."
                v "I was wondering what your favorite drink is..."
                "The kidnapper's eyes widen, definitely taken aback by your surprisingly intimate question. They struggle to muster up an answer for awhile but manage to speak."
                k "W-wow, I didn't expect you to ask me that kind of question. This whole time, I thought you didn't want to have anything with me."
                k "I guess I was wrong about you."
                "You give them a shrug, because you have no other way to reply to that statement. Their eyes shine with excitement, delighted by your question."
                v "Can you make some for me, whatever it is? After all, dinners are special, and you know what that means."
                "You are disgusted as you say that, but you can't do much about this either. Even worse, they blush to that."
                "It is even more clear that you need to get out of this place. Immediately."
                k "Y-you are definitely something. You are doing things to me. But yeah, I will make some for you, just give me a quick minute or two."
                """You nod. The kidnapper leaves the dining room, and you decide that unlike your previous tries, you remain in your seat.
                You realize that you were being too anxious and trying things that were simply out of character. You need to give the kidnapper some trust.
                Once you do that, you are sure that this time you will be able to escape."""
                "The kidnapper comes back with the drink. By the scent of it, it is alcoholic. That is okay. You drank a lot before coming to this place anyway."
                "You vaguely remember something about not accepting drinks from strangers, but this doesn't matter. You have to build trust."
                "So you accept the drink and neck half of it down. Simple. It is not like it is your first time downing something tasting like hard liquor." # <- i'm not projecting i swear
                """But after a while, you feel a bit dizzy. You start wondering to yourself whether you drank it too fast.
                But to think about your past experience, this should be nothing."""
                v "...Did you drug me?"
                k "I'm sorry, I'm so sorry...I wasn't sure if you were going to stay with me."
                k "YOU KEEP TRYING TO LEAVE MY SIDE, WHEN I'M HERE TRYING TO PROTECT YOU!!!" #angry
                k "There are so many dangerous things out there, and I can protect you. Why do you keep trying to leave me..."
                "You shed a sorrowful tear of defeat before finally blacking out." #black out
                $ var_flag == 0
                jump pretend_phase
            else:
                "You try to escape by distracting the kidnapper. You plan to make them go to the kitchen to cook something for you."
                v "Hey, um, Isaac."
                k "Yeah? Do you need something?"
                v "Yeah, actually...would it be possible if you cook something for me?"
                k "Oh...is the food not to your liking?"
                v "Oh no, it's just that I am especially feeling hungry today..."
                "The kidnapper stares into your eyes, long and hard. You get the shivers from their penetrating stare."
                "They may have noticed you had something going on. But the kidnapper doesn't say much. They just stare."
                "Then, they finally get up from the table to fetch you something, but their eyes never leave you."
                k "Okay, we have some ramen noodles and..."
                "The kidnapper's voice starts fading out for you, because you are too anxious, looking for the right opportunity to make your escape."
                k "...You've been awfully quiet. Is everything okay?"
                "Their eyes stare into your soul. They know. They know that you are trying to escape." #eyes jumpscare
                v "...N-no? Everything is fine!"
                "Today is not the day..."
                jump pretend_phase # change this label to somewhere else other than dinnerWithMyMan for the sake of variety in dialogue.
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
            jump winEnd #black out

    label winEnd:
        #loop back to the beginning of the game again (ofc they are nto playing through the entire thing)
        #but the character is not referred to as JAYDYN nor YOU. It is a completely different person.
        # this time, however, you have no control over them. the cycle repeats but you can do nothing about it.
        $ v = Character("Jean")
        scene black

        "Jean wakes up."

        show bedroom
        with fade

        play victim_channel bedroom_victim fadein 2.0
        play music bedroom_main volume 0.5

        "Where is this?"

        "Slowly, Jean's senses start to come to them..."

        "They're laying down on a thin mattress in what appears to be a small bedroom? It is definitely not their bedroom."

        "The room smells musty and damp. The floor feels cold on their feet."

        "Strange. Especially the last thing they remember is the hot sunlight of mid-July."

        v "I am underground."
        #black out
        return

    label pretend_phase:


        jump escape_attempt

    return

label inBathroom_p4:
    play music BRTheme loop

    "You enter the bathroom."
    $ allDone = False
    $ usedToilet = False
    $ brushedTeeth = False
    $ tookBath = False
    while not allDone:
        "Looking around, what will you do?"
        menu:
            "You're done here.":
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
                    "And the drugs cabinet. That makes more sense actually."
                $ brushedTeeth = True
            "Take a bath" if not tookBath:
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
    jump after_shower_p4
