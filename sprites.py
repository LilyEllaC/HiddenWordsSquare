import pygame
import constants as const
import utilities as util


#letters
class Squares:
    def __init__(self, size, fontNum, x, y, colourNorm, colourClicked, letter, isDuplicate, point):
        self.size=size
        self.x=x
        self.y=y
        self.colourN=colourNorm
        self.colourC=colourClicked
        self.colour=self.colourN
        self.letter=letter
        self.fontNum=fontNum
        self.isDuple=isDuplicate
        self.position=0
        self.point=point

        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
    
    def draw(self):
        pygame.draw.rect(const.SCREEN, self.colour, self.rect)
        util.toScreen(self.letter, const.FONTS[self.fontNum], const.BLACK, self.x+self.size//2, self.y+self.size*4//7)
    
class ScoreBar:
    def __init__(self, totalScore, colourPoints, colourBase, x, y):
        self.x=x
        self.y=y
        self.height=50
        self.width=200
        self.colourPoints=colourPoints
        self.colourBase=colourBase

        #figuring distance
        self.onePoint=self.width/totalScore
        self.rectPoints = pygame.Rect(self.x, self.y, 0, self.height)
        self.rectBase = pygame.Rect(self.x, self.y, self.width, self.height)

    def changeScore(self, score):
        self.rectPoints=pygame.Rect(self.x, self.y, self.onePoint*score, self.height)

    def draw(self):
        pygame.draw.rect(const.SCREEN, self.colourBase, self.rectBase)
        pygame.draw.rect(const.SCREEN, self.colourPoints, self.rectPoints)
