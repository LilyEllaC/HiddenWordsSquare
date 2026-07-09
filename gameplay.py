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

#functions
#setting up
def setUp(hasStarted):
    global squares
    if not hasStarted:
        preset.gameStarted=True
        squareInfo=preset.getSquareInfo()
        squares=preset.makeSquares(squareInfo[0], squareInfo[1], squareInfo[2])
    wordInfo=makePoints(hasStarted)
    
    for square in tutorial.squares:
        square.visible=False
    for square in squares:
        square.visible=True
    
    return wordInfo


#make the squares know when they are hovered over
def colourSquares(square, mouseX, mouseY, word:str):
    if square.rect.collidepoint((mouseX, mouseY)) and square.visible:
        if square.setting=="normal":
            square.setting="clicked"
            #making the word
            if isinstance(word, tuple):
                print("It is a tuple!")
            word+=str(square.letter)
            square.position=len(word)-1
            #print(square.letter, square.position, currentWord[square.position])
        #making it so if mouse is off it, it uncolours
        #normal way
        elif not square.isDuple:
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
def showLine(colour, square, squares):
    mouseX, mouseY = pygame.mouse.get_pos()
    if square.setting=="clicked" and square.position==len(currentWord)-1:
        pygame.draw.line(const.SCREEN, colour, (square.xCirc, square.yCirc), (mouseX, mouseY), 20)
    elif square.setting=="clicked":
        for otherSquare in squares:
            if otherSquare.position==square.position+1 and otherSquare.position!=-1:
                pygame.draw.line(const.SCREEN, colour, (square.xCirc, square.yCirc), (otherSquare.xCirc, otherSquare.yCirc), 20)


#check if the word is in the word list  
def checkIfWord(word, wordInfo, scoreBar):
    sortedLists=wordInfo.allWordsSorted
    found=False
    for lists in sortedLists:
        for option in lists[0]:
            if option==word and word not in lists[1]:
                lists[1].append(word)
                calculatePoints(word)
                scoreBar.changeScore(score)
                print("found: "+word)
                wordType.image=wordType.imageCorrect
                found=True
                break
        if word in lists[1]:
            break
    if not found:
        wordType.image=wordType.imageWrong
        print("Not found: "+word)


#calculate how many points a word is worth
def calculatePoints(word):
    global score
    for letter in word:
        score+=const.POINTS[ord(letter)-65]
    print("score", score)

#actually make the bar
def makePoints(hasStarted):
    global pointBar
    #pointbar stuff
    pointBar=preset.calculatePointBar()
    #words showing stuff
    with open("wordsInPuzzle.txt", "r") as file:
        words = file.readlines()
    for word in words:
        position=words.index(word)
        words[position]=word.strip()
    if not hasStarted:
        wordInformation=classes.WordsSorted(words, const.MAGENTA)
    else: 
        wordInformation=classes.WordsSorted(words, const.MAGENTA)
    return wordInformation


#play the game
def play(wordInformation):
    #global clicked, currentWord, score
    #basic stuff
    global currentWord
    const.SCREEN.fill(const.MAGENTA)
    util.toScreen("HIDDEN WORDS SQUARE", const.FONT75, const.BLACK, const.WIDTH // 2, 80)
    
    #getting the mouse dragged stuff to work
    mouseX, mouseY = pygame.mouse.get_pos()
    util.toScreen(currentWord, const.FONT50, const.BLACK, const.WIDTH//2, 205)
    if clicked:
        wordType.image=wordType.imageBlank
        for square in squares:
            currentWord, square=colourSquares(square, mouseX, mouseY, currentWord)
            showLine(const.DARK_TEAL, square, squares)



    #drawing
    #showing the score
    util.toScreen("Score: "+str(score), const.FONT30, const.BLACK, const.WIDTH*4//5, 100)
    if preset.gameStarted:
        pointBar.draw()
        util.toScreen("Score: "+str(score), const.FONT30, const.BLACK, const.WIDTH*4//5, 100)
        wordType.draw()
        wordInformation.draw()
        

    for square in squares:
        if square.visible:
            square.draw()

