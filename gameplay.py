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
#make the squares know when they are hovered over
def colourSquares(square, mouseX, mouseY):
    global currentWord
    coloured=False
    if square.rect.collidepoint((mouseX, mouseY)):
        if square.setting=="normal":
            square.setting="clicked"
            coloured=True
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

    if square.letter not in currentWord and square.setting=="clicked":
        square.setting="normal"
        square.position=-1
    if square.isDuple and square.letter in currentWord and square.setting=="clicked":
        isThere=False
        for i in range(0, len(currentWord)):
            if currentWord[i]==square.letter and i==square.position:
                isThere=True
                break
        if not isThere:
            square.setting="normal"
            square.position=-1
    return coloured
                

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
def checkIfWord(word):
    global wordInformation
    sortedLists=wordInformation.allWordsSorted
    for lists in sortedLists:
        for option in lists[0]:
            if option==word and word not in lists[1]:
                lists[1].append(word)
                calculatePoints(word)
                pointBar.changeScore(score)
                print("found: "+word)
                wordType.image=wordType.imageCorrect
                break
        if word in lists[1]:
            break
        else:
            wordType.image=wordType.imageWrong
            print("Not found: "+word)


#calculate how many points a word is worth
def calculatePoints(word):
    global score
    for letter in word:
        score+=const.POINTS[ord(letter)-65]
    print("score", score)

#actually make the bar
def setUp():
    global pointBar, wordInformation
    #pointbar stuff
    pointBar=preset.calculatePointBar()
    #words showing stuff
    with open("wordsInPuzzle.txt", "r") as file:
        words = file.readlines()
    for word in words:
        position=words.index(word)
        words[position]=word.strip()
    wordInformation=preset.WordsSorted(words)
    return wordInformation

timer=0
#play the game
def play():
    #global clicked, currentWord, wordsFound, score
    #basic stuff
    global timer
    const.SCREEN.fill(const.MAGENTA)
    util.toScreen("HIDDEN WORDS SQUARE", const.FONT60, const.BLACK, const.WIDTH // 2, 30)
    
    #showing the words found
    #util.toScreenInfTopLeft(wordsFound, const.FONT45, const.BLACK, 100, 200)

    #getting the mouse dragged stuff to work
    mouseX, mouseY = pygame.mouse.get_pos()
    util.toScreen(currentWord, const.FONT50, const.BLACK, const.WIDTH//2, 130)
    if clicked:
        wordType.image=wordType.imageBlank
        for square in squares:
            colourSquares(square, mouseX, mouseY)
            showLine(const.DARK_TEAL, square, squares)

                    
            



    #drawing
    #showing the score
    util.toScreen("Score: "+str(score), const.FONT30, const.BLACK, const.WIDTH*4//5, 100)
    if preset.gameStarted:
        pointBar.draw()
        util.toScreen("Score: "+str(score), const.FONT30, const.BLACK, const.WIDTH*4//5, 100)
        wordType.draw()
        if timer==const.FPS*2:
            wordInformation.draw()
            timer=0
        timer+=1

    for square in squares:
        square.draw()

