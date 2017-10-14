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
# dressup game code thanks to leon at the Lemma Soft Forums
# (https://lemmasoft.renai.us/forums/viewtopic.php?t=14559)
python:
    ProtagName = renpy.input("Your Name:", 'Hiro Protagonist')
    ProtagName = ProtagName.strip()
	
	dressup_show = False
	base, hair, glasses, neck, jacket, top = 1, 1, 1, 1, 1, 1	#default dress items
	
	# number of items for each type, eventually will be set to the number of image files
	# for each item.
	base_styles = 0
	hair_styles = 0
	glasses_styles = 0
	neck_styles = 0
	jacket_styles = 0
	top_styles = 0
	
	# define various images for character creation as:
	# "base.png" for base image
	# "hair1.png", "hair2.png", ... for each hair style
	# same convention for each item set
	
	def draw_char(st, at):	#combine items into one displayable
		return LiveComposite(
			(257, 560), 				#image size
			(0,0), "base%d.png"%base,
			(0,0), "hair%d.png"%hair, 	# (0,0) is the position of each dressup item
			(0,0), "glasses%d.png"%glasses,
			(0,0), "neck%d.png"%neck,
			(0,0), "jacket%d.png"%jacket,
			(0,0), "top%d.png"%top
			),.1
			
	def draw_char_side(st, at):	#same as above, but scaled and positioned for sideimage
		return LiveComposite(
			(257, 560),
            (10, 400), im.FactorScale("base%d.png"%base, .45, .45),
            (10, 400), im.FactorScale("hair%d.png"%hair, .45, .45),
            (10, 400), im.FactorScale("glasses%d.png"%glasses, .45, .45),
            (10, 400), im.FactorScale("neck%d.png"%neck, .45, .45),
            (10, 400), im.FactorScale("jacket%d.png"%jacket, .45, .45),
            (10, 400), im.FactorScale("top%d.png"%top, .45, .45)
            ),.1
    
    CharName = renpy.input("Your Character's Name:", 'Carel Stormbreaker')
    CharName = CharName.strip()
	
init:
	image char = DynamicDisplayable(draw_char)	#DynamicDisplayable ensures that any changes are immediately visible
	$ char = Character('[ProtagName]', color="#c8ffc8", window_left_padding=120, show_side_image=DynamicDisplayable(draw_char_side))
	
screen dressup:
	if dressup_show:
		add "char" xalign 0 yalign 0 xpos 60
		python:
			# set all the values to change styles to previous / next version:
			hair_n = hair + 1 		# if next hair is chosen
			hair_p = hair - 1 		# if previous hair is chosen
			if hair_p < 1: 			# making sure we don't get out of index range (index 0 is not allowed)
				hair_p = hair_styles
			if hair_n > hair_styles: 
				hair_n = 1
				
			base_n = base + 1
			base_p = base - 1
			if base_p < 1:
				base_p = base_styles
			if base_n > base_styles:
				base_n = 1

			glasses_n = glasses + 1
			glasses_p = glasses - 1
			if glasses_p < 1:
				glasses_p = glasses_styles
			if glasses_n > glasses_styles:
				glasses_n = 1

			neck_n = neck + 1
			neck_p = neck - 1
			if neck_p < 1:
				neck_p = neck_styles
			if neck_n > neck_styles:
				neck_n = 1

			jacket_n = jacket + 1
			jacket_p = jacket - 1
			if jacket_p < 1:
				jacket_p = jacket_styles
			if jacket_n > jacket_styles:
				jacket_n = 1

			top_n = top + 1
			top_p = top - 1
			if top_p < 1:
				top_p = top_styles
			if top_n > top_styles:
				top_n = 1
				
			# display the arrows for changing the dress (we could also use one imagemap, instead of a bunch of imagebuttons):
			y = 50
			ui.imagebutton("arrowL.png", "arrowL.png", clicked=SetVariable("hair", hair_p), ypos=y, xpos=50)
			ui.imagebutton("arrowR.png", "arrowR.png", clicked=SetVariable("hair", hair_n), ypos=y, xpos=250)
			y += 80
			ui.imagebutton("arrowL.png", "arrowL.png", clicked=SetVariable("glasses", glasses_p), ypos=y, xpos=50)
			ui.imagebutton("arrowR.png", "arrowR.png", clicked=SetVariable("glasses", glasses_n), ypos=y, xpos=250)
			y += 80
			ui.imagebutton("arrowL.png", "arrowL.png", clicked=SetVariable("neck", neck_p), ypos=y, xpos=50)
			ui.imagebutton("arrowR.png", "arrowR.png", clicked=SetVariable("neck", neck_n), ypos=y, xpos=250)
			y += 80
			ui.imagebutton("arrowL.png", "arrowL.png", clicked=SetVariable("jacket", jacket_p), ypos=y, xpos=50)
			ui.imagebutton("arrowR.png", "arrowR.png", clicked=SetVariable("jacket", jacket_n), ypos=y, xpos=250)
			y += 80
			ui.imagebutton("arrowL.png", "arrowL.png", clicked=SetVariable("top", top_p), ypos=y, xpos=50)
			ui.imagebutton("arrowR.png", "arrowR.png", clicked=SetVariable("top", top_n), ypos=y, xpos=250)
			ui.textbutton("Return", clicked=SetVariable("dressup_show", False))

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
