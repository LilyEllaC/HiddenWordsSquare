
import constants as const
import utilities as util
import gameplay as game
import pygame
import classes
import preset

currentWord=""
clicked=False
letters=["     PY  AL     ","WRD O           ", "   S   Q   U ERA"]
letterNum=0
squares=preset.makeSquares(len(letters[0]), letters[preset.letterNum], const.TEAL)
finger=classes.Finger([[squares[5].x,squares[5].y], [squares[10].x,squares[10].y], [squares[9].x,squares[9].y], [squares[6].x,squares[6].y]], squares[0].size)

pointBar=preset.calculatePointBar(["PLAY", "WORD", "SQUARE"])
wordInfo=classes.WordsSorted(["PLAY", "WORD", "SQUARE"], [], const.LIGHT_BLUE)
score=0
timer=0


def setUp():
    for square in squares:
        square.visible=True
    for square in game.squares:
        square.visible=False

def mouseDown(event, isClicked, theCurrentWord):
    for square in squares:
        if square.rect.collidepoint(event.pos):
            isClicked=True
            theCurrentWord=""
            break
    return isClicked, theCurrentWord

def mouseUp(isClicked, scoreBar, points, theCurrentWord):
    if isClicked:
        points=game.checkIfWord(theCurrentWord, wordInfo, scoreBar, points)

    isClicked=False
    
    #scroll bar
    wordInfo.moving=False

    #resetting the squares
    for square in squares:
        square.setting="normal"
    return isClicked, points



def playTutorial(scoreBar, theCurrentWord, letterSquares, pointingFinger):
    #basic stuff
    const.SCREEN.fill(const.LIGHT_BLUE)
    util.toScreen("HIDDEN WORDS SQUARE", const.FONT75, const.BLACK, const.WIDTH // 2, 80)
    
    #getting the mouse dragged stuff to work
    mouseX, mouseY = pygame.mouse.get_pos()
    util.toScreen(theCurrentWord, const.FONT50, const.BLACK, const.WIDTH//2, 205)
    if clicked:
        game.wordType.image=game.wordType.imageBlank
        for square in letterSquares:
            theCurrentWord, square=game.colourSquares(square, mouseX, mouseY, theCurrentWord)
            game.showLine(const.DARK_TEAL, square, letterSquares, theCurrentWord)
    

    #moving to the next word
    #starting the timer
    if theCurrentWord=="PLAY" or theCurrentWord=="WORD" or theCurrentWord=="SQUARE":
        if theCurrentWord=="SQUARE":
            preset.done=True
        preset.startTimer=True
        pointingFinger.stop=True
    #adding to the timer
    if preset.startTimer:
        preset.timer+=1/const.FPS
    #actually moving to the next word
    if preset.timer>3 and not preset.done:
        #going to the next letters
        preset.letterNum+=1
        letterSquares=preset.makeSquares(16, letters[preset.letterNum], const.TEAL)
        for square in letterSquares:
            square.visible=True
        #resetting variables
        preset.startTimer=False
        preset.timer=0
        theCurrentWord=""
        #having the finger move
        if preset.letterNum==1:
            pointingFinger.newLocations([[squares[0].x,squares[0].y], [squares[4].x,squares[4].y], [squares[1].x,squares[1].y], [squares[2].x,squares[2].y]], squares[0].size)
        elif preset.letterNum==2:
            pointingFinger.newLocations([[squares[3].x,squares[3].y], [squares[7].x,squares[7].y], [squares[11].x,squares[11].y], [squares[15].x,squares[15].y], [squares[14].x,squares[14].y], [squares[13].x,squares[13].y]], squares[0].size)

    #showing the end message
    elif preset.timer>3 and preset.done:
        util.toScreen2("Now you can",  "go play!", const.FONT55, const.BLACK, const.WIDTH-250, const.HEIGHT-80)


    #drawing
    #showing the score
    util.toScreen("Score: "+str(score), const.FONT30, const.BLACK, const.WIDTH*4//5, 100)
    
    scoreBar.draw()
    util.toScreen("Score: "+str(score), const.FONT30, const.BLACK, const.WIDTH*4//5, 100)
    game.wordType.draw()
    wordInfo.draw()    
    for square in letterSquares:
        if square.visible:
            square.draw()
    pointingFinger.draw()
    
    return scoreBar, theCurrentWord, letterSquares
        