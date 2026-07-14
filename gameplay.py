import constants as const
import utilities as util
import preset
import tutorial
from preset import wordType
import classes

import pygame


#variables
clicked=False
currentWord=" "
score=0
squares=[]
pointBar=""

#functions
#setting up
def setUp(hasStarted, letterSquares, scoreBar, wordInfo):
    if not hasStarted:
        preset.gameStarted=True
        squareInfo=preset.getSquareInfo()
        letterSquares=preset.makeSquares(squareInfo[0], squareInfo[1], squareInfo[2])
        preset.theLetters=squareInfo[1]
    
    for square in tutorial.squares:
        square.visible=False
    for square in letterSquares:
        square.visible=True
    
    return wordInfo, letterSquares, scoreBar

def getWords(letters):
    with open("wordsInPuzzle.txt", "r") as file:
        words = [line.strip() for line in file]
    if " " in letters:
        words=["PLAY", "WORDS", "SQUARES"]
    return words

#make the squares know when they are hovered over
def colourSquares(square, mouseX, mouseY, word:str):
    if square.rect.collidepoint((mouseX, mouseY)) and square.visible:
        if square.setting=="normal":
            square.setting="clicked"
            #making the word
            word+=str(square.letter)
            square.position=len(word)-1
        #making it so if mouse is off it, it uncolours
        #normal way
        elif not square.isDuple:
            if len(word)>0:
                if square.letter!=word[-1] and square.letter in word: 
                    word=word[0: word.find(square.letter)+1]
        #letter is a duplicate strange way
        elif square.isDuple: 
            if square.letter in word:
                for i in range(0, len(word)-1):
                    if len(word)>1:
                        if word[i]==square.letter and i==square.position:
                            word=word[0: i+1]
                            break

    if square.letter not in word and square.setting=="clicked":
        square.setting="normal"
        square.position=-1
    if square.isDuple and square.letter in word and square.setting=="clicked":
        isThere=False
        for i in range(0, len(word)):
            if word[i]==square.letter and i==square.position:
                isThere=True
                break
        if not isThere:
            square.setting="normal"
            square.position=-1
    return word, square
                

#make a line
def showLine(colour, square, letterSquares, theCurrentWord):
    mouseX, mouseY = pygame.mouse.get_pos()
    if square.setting=="clicked" and square.position==len(theCurrentWord)-1:
        pygame.draw.line(const.SCREEN, colour, (square.xCirc, square.yCirc), (mouseX, mouseY), 20)
    elif square.setting=="clicked":
        for otherSquare in letterSquares:
            if otherSquare.position==square.position+1 and otherSquare.position!=-1:
                pygame.draw.line(const.SCREEN, colour, (square.xCirc, square.yCirc), (otherSquare.xCirc, otherSquare.yCirc), 20)


#check if the word is in the word list  
def checkIfWord(word, wordInfo, scoreBar, points):
    sortedLists=wordInfo.allWordsSorted
    found=False
    for lists in sortedLists:
        if word in lists[1]:
            wordType.image=wordType.imageFound
            found=True
            break
        for option in lists[0]:
            if option==word and word not in lists[1]:
                lists[1].append(word)
                points=calculatePoints(word, points)
                scoreBar.changeScore(points)
                wordType.image=wordType.imageCorrect
                found=True
                break
        
    if not found:
        if len(word)<4:
            wordType.image=wordType.imageShort
            if len(word)==0 or " " in word:
                wordType.image=wordType.imageBlank
        else:
            wordType.image=wordType.imageWrong
    return points


#calculate how many points a word is worth
def calculatePoints(word, points):
    for letter in word:
        points+=const.POINTS[ord(letter)-65]
    return points

#actually make the bar
def makePoints(words, scoreBar):
    #pointbar stuff
    scoreBar=preset.calculatePointBar(words)
    #words showing stuff
    wordInformation=classes.WordsSorted(words, const.MAGENTA)
    return wordInformation, scoreBar


#play the game
def play(wordInformation, scoreBar, theCurrentWord):
    #basic stuff
    const.SCREEN.fill(const.MAGENTA)
    util.toScreen("HIDDEN WORDS SQUARE", const.FONT75, const.BLACK, const.WIDTH // 2, 80)
    
    #getting the mouse dragged stuff to work
    mouseX, mouseY = pygame.mouse.get_pos()
    util.toScreen(theCurrentWord, const.FONT50, const.BLACK, const.WIDTH//2, 205)
    if clicked:
        wordType.image=wordType.imageBlank
        for square in squares:
            theCurrentWord, square=colourSquares(square, mouseX, mouseY, theCurrentWord)
            showLine(const.DARK_TEAL, square, squares, theCurrentWord)



    #drawing
    #showing the score
    util.toScreen("Score: "+str(score), const.FONT30, const.BLACK, const.WIDTH*4//5, 100)
    if preset.gameStarted:
        scoreBar.draw()
        util.toScreen("Score: "+str(score), const.FONT30, const.BLACK, const.WIDTH*4//5, 100)
        wordType.draw()
        wordInformation.draw()
        

    for square in squares:
        if square.visible:
            square.draw()

    return theCurrentWord

