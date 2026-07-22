
import constants as const
import utilities as util
import gameplay as game
import pygame
import classes
import preset

currentWord=""
wordNumbers=[]
clicked=False
letters=["     PY  AL     ","WRD O           ", "   S   Q   U ERA"]
letterNum=0
squares=preset.makeSquares(len(letters[0]), letters[preset.letterNum], const.colour1)
#updating the number in and starting
for square in squares:
    if square.letter!=" ":
        square.numInLeft=1
    if square.letter=="P":
        square.numStartedLeft=1
image = pygame.image.load("assets/arrow.png")
#image = pygame.transform.scale(image, (71.4, 200))
image = pygame.transform.flip(image, True, False)
arrowImage2 = pygame.transform.rotate(image, -45)
image = pygame.image.load("assets/arrow.png")
arrowImage1 = pygame.transform.scale(image, (75, 150))


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

def mouseDown(event, isClicked, theCurrentWord, wordNum):
    for oneSquare in squares:
        if oneSquare.rect.collidepoint(event.pos):
            isClicked=True
            theCurrentWord=""
            wordNum=[]
            break
    if pointBar.hintStart.hoveredOver:
        for oneSquare in squares:
            oneSquare.showStarted=True
    if pointBar.hintRemain.hoveredOver:
        for oneSquare in squares:
            oneSquare.showIn=True
    return isClicked, theCurrentWord, wordNum

def mouseUp(isClicked, scoreBar, points, theCurrentWord, letterSquares):
    if isClicked:
        points=game.checkIfWord(theCurrentWord, wordInfo, scoreBar, points, letterSquares)

    isClicked=False
    
    #scroll bar
    wordInfo.moving=False

    #resetting the squares
    for square in squares:
        square.setting="normal"
    return isClicked, points



def playTutorial(scoreBar, theCurrentWord, wordNums, letterSquares, pointingFinger, points):
    #basic stuff
    const.SCREEN.fill(const.LIGHT_BLUE)
    util.toScreen("HIDDEN WORDS SQUARE", const.FONT75, const.BLACK, const.WIDTH // 2, 80)
    
    #getting the mouse dragged stuff to work
    mouseX, mouseY = pygame.mouse.get_pos()
    util.toScreen(theCurrentWord, const.FONT50, const.BLACK, const.WIDTH//2, 205)
    if clicked:
        game.wordType.image=game.wordType.imageBlank
        for oneSquare in letterSquares:
            theCurrentWord, wordNums, oneSquare=game.colourSquares(oneSquare, mouseX, mouseY, theCurrentWord, wordNums)
            game.showLine(const.colour2, oneSquare, letterSquares, theCurrentWord)
    

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
    if preset.timer>2 and not preset.done:
        #going to the next letters
        preset.letterNum+=1
        letterSquares=preset.makeSquares(16, letters[preset.letterNum], const.colour1)
        #updating the number in and starting
        for oneSquare in letterSquares:
            if oneSquare.letter!=" ":
                oneSquare.numInLeft=1
            if oneSquare.letter=="S":
                oneSquare.numStartedLeft=1
            oneSquare.visible=True
        #resetting variables
        preset.startTimer=False
        preset.timer=0
        theCurrentWord=""
        #having the finger move
        if preset.letterNum==1:
            pointingFinger.newLocations([[squares[0].x,squares[0].y], [squares[4].x,squares[4].y], [squares[1].x,squares[1].y], [squares[2].x,squares[2].y]], squares[0].size)
        elif preset.letterNum==2:
            pointingFinger.newLocations([[squares[3].x,squares[3].y], [squares[7].x,squares[7].y], [squares[11].x,squares[11].y], [squares[15].x,squares[15].y], [squares[14].x,squares[14].y], [squares[13].x,squares[13].y]], squares[0].size)

    #text talking about the buttons
    if scoreBar.startShowing:
        util.toScreen("Click me!", const.FONT55, const.BLACK, 1200, 420)
        util.toScreen("Click me!", const.FONT55, const.BLACK, 1380, 420)
    

    #drawing
    #showing the score    
    scoreBar.draw(points)
    game.wordType.draw()
    wordInfo.draw()    
    for oneSquare in letterSquares:
        if oneSquare.visible:
            oneSquare.draw()
    pointingFinger.draw()

    #doing this so the arrow is above the squares, more showing stuff
    #squares that start words
    if squares[0].showStarted:
        util.toScreen2("The S starts a word", "but not any other letters", const.FONT45, const.BLACK, 970, 200)
        
        const.SCREEN.blit(arrowImage1, (900, 230))
    #squares that start words
    if squares[0].showIn:
        util.toScreen2("All the letters left are only", "in one more word", const.FONT45, const.BLACK, 1300, 500)
        util.toScreen2("If they aren't in any words", "they are dark", const.FONT45, const.BLACK, 1300, 560)
        
        const.SCREEN.blit(arrowImage2, (1075, 570))

    #showing the end message
    if preset.timer>3 and preset.done:
        game.celebrate()
        util.toScreen2("Now you can",  "go play!", const.FONT55, const.BLACK, const.WIDTH-250, const.HEIGHT-80)
    
    return scoreBar, theCurrentWord, wordNums, letterSquares
        