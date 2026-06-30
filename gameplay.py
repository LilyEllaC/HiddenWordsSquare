import constants as const
import utilities as util
from preset import squares
import pygame
import math



clicked=False
currentWord="   "
wordsFound=[]

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
    print("word made")
    for option in words:
        print(option)
    for option in words:
        if option.strip()==word:
            wordsFound.append(word)
            print("found: "+word)
    return wordsFound
        

def play():
    global clicked, currentWord, wordsFound

    #basic stuff
    const.SCREEN.fill(const.MAGENTA)
    util.toScreen("HIDDEN WORDS SQUARE", const.FONT60, const.BLACK, const.WIDTH // 2, 50)
    
    #showing the words found
    util.toScreenInfTopLeft(wordsFound, const.FONT45, const.BLACK, 100, 200)

    #getting the mouse dragged stuff to work
    mouseX, mouseY = pygame.mouse.get_pos()
    util.toScreen(currentWord, const.FONT50, const.BLACK, const.WIDTH//2, 130)
    if clicked:
        for square in squares:
            colourSquares(square, mouseX, mouseY)

                    
                






    #drawing
    for square in squares:
        square.draw()

