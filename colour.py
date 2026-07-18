import pygame
import constants as const
import utilities as util
from classes import ColourButton, ButtonToShowColours
import gameplay
import tutorial


colours=[]
words=["RED", "ORANGE", "YELLOW", "GREEN", "TEAL", "BLUE", "PURPLE", "MAGENTA"]
wordNum=0
x=20
y=120
height=const.FONT35.get_height()
for colour in const.COLOUROPTIONS:
    colours.append(colour)
    if len(colours)==3:
        const.buttons.append(ColourButton(x, y, 140, height+7, colours, words[wordNum], const.FONT35))
        y+=height+10
        wordNum+=1
        colours=[]
colourWheel=ButtonToShowColours(10, 10, 70, 70)

#buttons
def checkButtons(mouseX, mouseY):
    if const.popUp:
        for button in const.buttons:
            #if clicked
            if button.hitBox.collidepoint((mouseX, mouseY)):
                #actually changing the colour
                colourNum=const.COLOUROPTIONS.index(button.colour2)
                colourLight=const.COLOUROPTIONS[colourNum-1]
                const.colour1=const.COLOUROPTIONS[colourNum]
                const.colour2=const.COLOUROPTIONS[colourNum+1]

                #forcably updating some stuff
                #changing the squares
                for square in gameplay.squares:
                    square.changeColours(colourLight, const.colour1)
                for square in tutorial.squares:
                    square.changeColours(colourLight, const.colour1)
                #point bar stuff
                gameplay.pointBar.colourPoints=const.colour1
                gameplay.pointBar.colourBase=const.colour2
                tutorial.pointBar.colourPoints=const.colour1
                tutorial.pointBar.colourBase=const.colour2
                break
    if colourWheel.rect.collidepoint((mouseX, mouseY)):
        const.popUp=not const.popUp
    
            

#pop-up
def showPopUp():
    pygame.draw.rect(const.SCREEN, const.WHITE, (0, 0, 400, 400))
    pygame.draw.rect(const.SCREEN, const.BLACK, (0, 0, 400, 400), 5)
    util.toScreen("Colour Theme", const.FONT60, const.BLACK, 233, 50)
    util.toScreen("What colour do you want?", const.FONT40, const.BLACK, 200, 100)
    for button in const.buttons:
        button.draw()
