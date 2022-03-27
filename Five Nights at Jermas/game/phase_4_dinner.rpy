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
            jump badEnd
        elif compliance < -7: # the 1st outcome
            jump dinnerWithMyMan
        else:
            jump winEnd

    label winEnd:
        # place holder: you win screen!
        return 
    return
