import pygame
import constants as const
import utilities as util
from classes import ColourButton, GenericButton
import gameplay
import tutorial


colourWheel=None

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
                    square.changeColours(colourLight, const.colour1, const.colour2)
                    print("Changed colours")
                if tutorial.tutorialStuff is not None:
                    tutorial.tutorialStuff.pointBar.colourPoints=const.colour1
                    tutorial.tutorialStuff.pointBar.colourBase=const.colour2
                    for square in tutorial.tutorialStuff.squares:
                        square.changeColours(colourLight, const.colour1, const.colour2)
                #point bar stuff
                gameplay.pointBar.colourPoints=const.colour1
                gameplay.pointBar.colourBase=const.colour2
                
                break
    if colourWheel and colourWheel.rect.collidepoint((mouseX, mouseY)):
        const.popUp=not const.popUp
    
            

#pop-up
def showPopUp():
    pygame.draw.rect(const.SCREEN, const.WHITE, (0, 0, 400, 475))
    pygame.draw.rect(const.SCREEN, const.BLACK, (0, 0, 400, 475), 5)
    util.toScreen("Colour Theme", const.FONT60, const.BLACK, 233, 50)
    util.toScreen("What colour do you want?", const.FONT40, const.BLACK, 200, 100)
    for button in const.buttons:
        button.draw()


def initColourButtons(colourWheelButton):
    const.buttons.clear()
    height = const.FONT35.get_height()
    button_colours = []
    wordNum = 0
    words=["RED", "ORAGNE", "YELLOW", "GREEN", "TEAL", "BLUE", "MAGENTA", "PURPLE"]
    y = 120
    x = 20
    for colour in const.COLOUROPTIONS:
        button_colours.append(colour)
        if len(button_colours) == 3:
            const.buttons.append(ColourButton(x, y, 140, height + 7, button_colours, words[wordNum], const.FONT35))
            y += height + 10
            wordNum += 1
            button_colours = []
    colourWheelButton = GenericButton(10, 10, 70, "assets/colourWheel.png", "assets/colourWheelHovered.png")
    return colourWheelButton