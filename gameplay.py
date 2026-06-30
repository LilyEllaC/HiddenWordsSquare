import constants as const
import utilities as util
from preset import squares
import pygame
import math



clicked=False
currentWord="   "

def play():
    #basic stuff
    const.SCREEN.fill(const.MAGENTA)
    util.toScreen("HIDDEN WORDS SQUARE", const.FONT60, const.BLACK, const.WIDTH // 2, 50)
    
    #getting the mouse dragged stuff to work
    global clicked, currentWord
    mouseX, mouseY = pygame.mouse.get_pos()
    util.toScreen(currentWord, const.FONT50, const.BLACK, const.WIDTH//2, 130)
    if clicked:
        for square in squares:
            if square.rect.collidepoint((mouseX, mouseY)):
                if square.colour==square.colourN:
                    currentWord+=square.letter
                    square.colour=square.colourC
                elif square.letter!=currentWord[-1] and square.letter in currentWord: 
                    currentWord=currentWord[0: currentWord.find(square.letter)+1]
            if square.letter not in currentWord and square.colour==square.colourC:
                square.colour=square.colourN

                    
                






    #drawing
    for square in squares:
        square.draw()

