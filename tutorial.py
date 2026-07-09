
import constants as const
import utilities as util
import gameplay as game
import pygame
import classes
import preset

currentWord=""
clicked=False
letters=["     PY  AL     ","WRD O           ", "   S   Q   USERA"]
letterNum=0
squares=preset.makeSquares(len(letters[0]), letters[preset.letterNum], const.TEAL)

pointBar=preset.calculatePointBar()
wordInfo=classes.WordsSorted(["PLAY", "WORD", "SQUARES"], const.LIGHT_BLUE)
score=0
timer=0

def setUp():
    for square in squares:
        square.visible=True
    for square in game.squares:
        square.visible=False

def mouseDown(event):
    global clicked, currentWord
    for square in squares:
        if square.rect.collidepoint(event.pos):
            clicked=True
            currentWord=""#square.letter
            break

def mouseUp():
    global clicked, wordInfo
    if clicked:
        game.checkIfWord(currentWord, wordInfo, pointBar)
    clicked=False
    
    #scroll bar
    wordInfo.moving=False

    #resetting the squares
    for square in squares:
        square.setting="normal"


def playTutorial():
    global currentWord, squares
    #basic stuff
    const.SCREEN.fill(const.LIGHT_BLUE)
    util.toScreen("HIDDEN WORDS SQUARE", const.FONT75, const.BLACK, const.WIDTH // 2, 80)
    
    #getting the mouse dragged stuff to work
    mouseX, mouseY = pygame.mouse.get_pos()
    util.toScreen(currentWord, const.FONT50, const.BLACK, const.WIDTH//2, 205)
    if clicked:
        game.wordType.image=game.wordType.imageBlank
        for square in squares:
            currentWord, square=game.colourSquares(square, mouseX, mouseY, currentWord)
            game.showLine(const.DARK_TEAL, square, squares)
    

    #moving to the next word
    if currentWord=="PLAY" or currentWord=="WORD":
        preset.timer+=1/const.FPS
    if preset.timer>4:
        print("new")
        preset.letterNum+=1
        squares=preset.makeSquares(16, letters[preset.letterNum], const.TEAL)
        print(str(len(letters))+"num: "+str(preset.letterNum))
        for square in squares:
            square.visible=True
        preset.timer=0
        currentWord=""


    #drawing
    #showing the score
    util.toScreen("Score: "+str(score), const.FONT30, const.BLACK, const.WIDTH*4//5, 100)
    
    pointBar.draw()
    util.toScreen("Score: "+str(score), const.FONT30, const.BLACK, const.WIDTH*4//5, 100)
    game.wordType.draw()
    wordInfo.draw()
    

    for square in squares:
        if square.visible:
            square.draw()
        