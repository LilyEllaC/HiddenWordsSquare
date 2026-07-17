import math
import random
import pygame
from classes import Squares, ScoreBar, WordType, Confetti
import constants as const


#preassigned variables
gameStarted=False
wordType=WordType()
timer=0
startTimer=False
done=False
letterNum=0
theLetters=""
#confetti
confettis=[]
image=pygame.transform.scale(pygame.image.load("confetti.png"), (200, 200))
for i in range(0,15):
    confettis.append(Confetti(image))

#creating the points bar
def calculatePointBar(words):
    totalScore=0
    for word in words:
        for letter in word:
            totalScore+=const.POINTS[ord(letter)-65]
    x=const.WIDTH-(const.WIDTH//4-25)
    y=150
    pointBar=ScoreBar(totalScore, const.BLUE, const. DARK_BLUE, x, y)
    return pointBar

#getting the square info
def getSquareInfo():
    with open("letters.txt", "r") as file:
        lines = file.readlines()
    letters=lines[random.randint(0, len(lines)-1)].strip()
    letters="PGIMEUNRCTSAIONR"
    return [len(letters), letters, const.TEAL]

#getting all of the squares
def makeSquares(number, letters, colour):
    # getting the info
    numAcross=int(math.sqrt(number))
    xDistance=(const.WIDTH//2)//numAcross
    size=xDistance-xDistance//8
    xPos=[]
    yPos=[]
    for i in range(0, numAcross):
        xPos.append(const.WIDTH//4+xDistance*i)
        yPos.append(const.HEIGHT//4+xDistance*i)

    #dealing with duplicates
    duplicateLetters=[]
    for i in range(0, len(letters)):
        for j in range(i+1, len(letters)):
            if letters[i]==letters[j]:
                duplicateLetters.append(letters[i])

    #finding font size
    fontNum=(size*4//5)//5
    fontNum=0

    #finding other colour
    colourC=const.GRAY
    for i in range (0, len(const.COLOUROPTIONS)-1):
        if const.COLOUROPTIONS[i]==colour:
            colourC=const.COLOUROPTIONS[i+1]    


    #creating the squares
    letterPos=0
    squares=[]
    for y in yPos:
        for x in xPos:
            #duplicate stuff
            letter=letters[letterPos]
            if letter in duplicateLetters:
                duplicate=True
            else:
                duplicate=False
            
            #points
            if ord(letter)-65<0:
                point=0
            else:
                point=const.POINTS[ord(letter)-65]
            
            #creating
            squares.append(Squares(size, fontNum, x, y, colourC, letters, letterPos, duplicate, point))
            letterPos+=1
    for square in squares:
        square.findNeighbours(squares)
    return squares
        




