from sprites import Squares
import constants as const
import utilities as util
import math
import random

#preassigned variables
squares=[]
xPos=[]
yPos=[]
gameStarted=False


#getting the square info
def getSquareInfo():
    with open("letters.txt", "r") as file:
        lines = file.readlines()
    letters=lines[random.randint(0, len(lines)-1)].strip()
    return [len(letters), letters, const.TEAL]


#getting all of the squares
def getSquares(number, letters, colour):
    # getting the info
    numAcross=int(math.sqrt(number))
    xDistance=(const.WIDTH//2)//numAcross
    size=xDistance-xDistance//12
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

    letterPos=0
    #creating the squares
    for y in yPos:
        for x in xPos:
            if letters[letterPos] in duplicateLetters:
                duplicate=True
            else:
                duplicate=False
            squares.append(Squares(size, fontNum, x, y, colour, colourC, letters[letterPos], duplicate))
            letterPos+=1
        