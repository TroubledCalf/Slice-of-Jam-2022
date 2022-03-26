# Compliance
define prevCompliance = 0
define currentCompliance = 0

# Soundtracks

# Characters
define e = Character("Eileen")
define n = Character("Narrator")
define v = Character("Victim")
define k = Character("Kidnapper")

# Character sprites

label start:
    scene bg room

    show eileen happy

    e "You've created a new Ren'Py game."

    hide eileen happy

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return
