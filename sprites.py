import pygame
import constants as const
import utilities as util


#letters
class Squares:
    def __init__(self, size, fontNum, x, y, colourNorm, colourClicked, letter):
        self.size=size
        self.x=x
        self.y=y
        self.colourN=colourNorm
        self.colourC=colourClicked
        self.colour=self.colourN
        self.letter=letter
        self.fontNum=fontNum

        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
    
    def draw(self):
        pygame.draw.rect(const.SCREEN, self.colour, self.rect)
        util.toScreen(self.letter, const.FONTS[self.fontNum], const.BLACK, self.x+self.size//2, self.y+self.size*4//7)
    
