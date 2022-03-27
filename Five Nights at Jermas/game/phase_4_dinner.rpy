default highComplianceDN = 7 # <- this is just a placeholder value

label dinnerWithMyMan:
    $ compliance = compliance // 2
    #place holder dialogue

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
        if compliance > 7: # the 3rd outcome
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
            jump dinnerWithMyMan
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
            """Another option is the glass sliding door placed """
            jump winEnd

    label winEnd:
        # place holder: you win screen!
        return
    return
