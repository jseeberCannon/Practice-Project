# The script of the game goes in this file.

# Text Blips WIP

init:
    $ weapon = False
    $ testimony = False
    $ suspect = False

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Detective", color="#c70039")
define p = Character("[povname]", color="#ffc300")
define s = Character("Clown", color="#00c800")

# The game starts here.

label start:

    # Asks for Player Name

    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Chase"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene circus

    play music "Opening.ogg" fadein 1.0

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show detective

    # These display lines of dialogue.

    "You and your superior arrive at the scene of a crime at a Circus"

    d "Come on [povname] we need to figure out who killed the Ring Leader"

    p "Exactly sir, we can't afford to clown around"

    d "..."

    d "So where should we go to first?"

    menu:
        "Inside the Tent":
            jump tent

        "Ask for Testimonies":
            jump test

    label tent:
        p "Let's go to the crime scene first"

        jump inside

    label test:
        p "Let's go ask some of the people who were here last night."

        jump outside


    # This ends the game.

    return
