import constants as const
import utilities as util
import preset
from preset import squares, wordType

import pygame


#variables
clicked=False
currentWord="   "
wordsFound=[]
score=0

#functions
def colourSquares(square, mouseX, mouseY):
    global currentWord
    if square.rect.collidepoint((mouseX, mouseY)):
        if square.colour==square.colourN:
            square.colour=square.colourC
            #making the word
            currentWord+=square.letter
            square.position=len(currentWord)-1
            #print(square.letter, square.position, currentWord[square.position])
        #making it so if mouse is off it, it uncolours
        #normal way
        elif not square.isDuple:
            if square.letter!=currentWord[-1] and square.letter in currentWord: 
                currentWord=currentWord[0: currentWord.find(square.letter)+1]
        #letter is a duplicate strange way
        elif square.isDuple: 
            if square.letter in currentWord:
                for i in range(0, len(currentWord)-1):
                    if len(currentWord)>1:
                        if currentWord[i]==square.letter and i==square.position:
                            currentWord=currentWord[0: i+1]
                            break

    if square.letter not in currentWord and square.colour==square.colourC:
        square.colour=square.colourN
    if square.isDuple and square.letter in currentWord and square.colour==square.colourC:
        isThere=False
        for i in range(0, len(currentWord)):
            if currentWord[i]==square.letter and i==square.position:
                isThere=True
                break
        if not isThere:
            square.colour=square.colourN
            square.position=0
                
        
def checkIfWord(word, wordsFound):
    with open("wordsInPuzzle.txt", "r") as file:
        words = file.readlines()
    for option in words:
        if option.strip()==word and word not in wordsFound:
            wordsFound.append(word)
            calculatePoints(word)
            pointBar.changeScore(score)
            print("found: "+word)
            wordType.image=wordType.imageCorrect
        else:
            wordType.image=wordType.imageWrong
    return wordsFound


def calculatePoints(word):
    global score
    for letter in word:
        score+=const.POINTS[ord(letter)-65]
    print("score", score)
    
def makePointBar():
    global pointBar
    pointBar=preset.calculatePointBar()


def play():
    #global clicked, currentWord, wordsFound, score
    #basic stuff
    const.SCREEN.fill(const.MAGENTA)
    util.toScreen("HIDDEN WORDS SQUARE", const.FONT60, const.BLACK, const.WIDTH // 2, 30)
    
    #showing the words found
    util.toScreenInfTopLeft(wordsFound, const.FONT45, const.BLACK, 100, 200)

    #getting the mouse dragged stuff to work
    mouseX, mouseY = pygame.mouse.get_pos()
    util.toScreen(currentWord, const.FONT50, const.BLACK, const.WIDTH//2, 130)
    if clicked:
        wordType.image=wordType.imageBlank
        for square in squares:
            colourSquares(square, mouseX, mouseY)

                    
            



    #drawing
    #showing the score
    util.toScreen("Score: "+str(score), const.FONT30, const.BLACK, const.WIDTH*4//5, 100)
    if preset.gameStarted:
        pointBar.draw()
        util.toScreen("Score: "+str(score), const.FONT30, const.BLACK, const.WIDTH*4//5, 100)
        wordType.draw()
    for square in squares:
        square.draw()

