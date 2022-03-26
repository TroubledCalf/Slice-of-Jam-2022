label phase_2:
  label day_3:

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
      # a note-so-nice smile I imagine
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

      # filler
      menu:
          "Attack your captor":
              $ compliance -= 4
              "You launch yourself at your captor."
              # filler
              jump day_3

          "Do nothing":
              $ compliance += 4
              "You drift to sleep, harrowed by the day's events..."
              jump day_4
  # lunch day
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
    ""
            