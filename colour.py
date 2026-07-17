import pygame
import constants as const
import utilities as util
from classes import ColourButton


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

#pop-up
def showPopUp():
    pygame.draw.rect(const.SCREEN, const.WHITE, (0, 0, 400, 400))
    pygame.draw.rect(const.SCREEN, const.BLACK, (0, 0, 400, 400), 5)
    util.toScreen("Colour Theme", const.FONT60, const.BLACK, 200, 50)
    util.toScreen("What colour do you want?", const.FONT40, const.BLACK, 200, 100)
    for button in const.buttons:
        button.draw()
