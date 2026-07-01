from sprites import Squares, ScoreBar, WordType
import constants as const
import utilities as util
import math
import random

#preassigned variables
squares=[]
xPos=[]
yPos=[]
gameStarted=False
wordType=WordType()


#creating the points bar
def calculatePointBar():
    with open("wordsInPuzzle.txt", "r") as file:
        words = [line.strip() for line in file]
    totalScore=0
    for word in words:
        for letter in word:
            totalScore+=const.POINTS[ord(letter)-65]
    x=675
    y=150
    pointBar=ScoreBar(totalScore, const.BLUE, const. DARK_BLUE, x, y)
    return pointBar

#getting the square info
def getSquareInfo():
    with open("letters.txt", "r") as file:
        lines = file.readlines()
    letters=lines[random.randint(0, len(lines)-1)].strip()
    #letters="ABCDEFGHIJKLMNOP"
    return [len(letters), letters, const.TEAL]


#getting all of the squares
def getSquares(number, letters, colour):
    # getting the info
    numAcross=int(math.sqrt(number))
    xDistance=(const.WIDTH//2)//numAcross
    size=xDistance-xDistance//8
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
    for y in yPos:
        for x in xPos:
            #duplicate stuff
            if letters[letterPos] in duplicateLetters:
                duplicate=True
            else:
                duplicate=False
            
            #points
            letter=letters[letterPos]
            point=const.POINTS[ord(letter)-65]
            
            #creating
            squares.append(Squares(size, fontNum, x, y, colourC, letter, duplicate, point))
            letterPos+=1
        