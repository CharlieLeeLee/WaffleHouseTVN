# Waffle House: the Visual Novel (working title)
# Script by Reid Wilson
# Art and code by Charlie Norvell
# Sound Design and music by Brenn Whiting and James Dietz

# IRL characters
define brenn = Character('Brenn', color="#FFFFFF")
define charl = Character('Charlie', color="#FF0000")
define james = Character('James', color="#FFFF00")
define reid = Character('Reid', color="#AAAAAA")
define bethy = Character('Bethany', color="#0000FF")
define julia = Character('Julia', color="#00FF00")
define ben = Character('Ben', color="#00FFFF")
define margo = Character('Margaret', color="FF77aa")

# Background characters
define obi = Character('Obi', color="#FFFF00")
define mer = Character('Meredith', color="#FFFF00")
define fiona = Character('Fiona', color="#FFFF00")
define jien = Character('Jien', color="#FFFF00")

# D&D Characters
define kirna = Character('Kirna', color="#FFFFFF")
define thalia = Character('Thalia', color="#FF77aa")
define kelwyn = Character('Kelwyn', color="#AAAAAA")
define devito = Character('Devito', color="#FFFF00")
define katara = Character('Katara', color="#0000FF")
define mona = Character('Mona', color="#00FF00")
define hirok = Character('Hirok', color="#00FFFF")

# D&D NPCs
define anton = Character('Lt. Anton', color="#FFFF00")
define anne = Character('Anne', color="#FFFF00")
define shirani = Character('Shirani', color="#FFFF00")
define weasel = Character('Weasel', color="#FFFF00")
define caspian = Character('Caspian', color="#FFFF00")

# Protagonist Characters
define protag = Character('[ProtagName]')
define proChar = Character('[CharName]')

# Protagonist pronouns
default pronoun = "they"
default pronounSing = "them"
default pronounPossess = "their"

# Protagonist's D&D Character information
default race = "human"
default charClass = "fighter"
default charPronoun = "they"


# Character Approval Ratings
default charlApprove = 0
default brennApprove = 0
default reidApprove = 0
default jamesApprove = 0
default bethyApprove = 0
default juliaApprove = 0
default margoApprove = 0
default fionaApprove = 0        # Potential DLC content
default obiApprove = 0          # Potential DLC content

# Flags for side romances
default charlRomance = False    #if both charlRomance and jamesRomance are
default jamesRomance = False    #false, alternate dialog of them together
default reidRomance = False     #if both reidRomance and BethyRomance are
default bethyRomance = False    #false, alternate dialog of them together
default juliaRomance = False    #if false, alternate dialog of Jien marriage

# character creation goes here
python:
    ProtagName = renpy.input("Your Name:", 'Hiro Protagonist')
    ProtagName = ProtagName.strip()
    
    CharName = renpy.input("Your Character's Name:", 'Carel Stormbreaker')
    CharName = CharName.strip()

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy
    


    # This ends the game.

    return
