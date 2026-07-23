
import constants as const
import utilities as util
import gameplay as game
import pygame
import classes
import preset

class TutorialStuff():
    def __init__(self):
        self.currentWord=""
        self.wordNumbers=[]
        self.clicked=False
        self.letters=["     PY  AL     ","WRD O           ", "   S   Q   U ERA"]
        self.letterNum=0
        self.timer=0
        self.startTimer=False
        self.done=False
        squares=preset.makeSquares(len(self.letters[0]), self.letters[self.letterNum], const.colour1)
        #updating the number in and starting
        for square in squares:
            if square.letter!=" ":
                square.numInLeft=1
            if square.letter=="P":
                square.numStartedLeft=1
        self.squares=squares
        image = pygame.image.load("assets/arrow.png")
        #image = pygame.transform.scale(image, (71.4, 200))
        image = pygame.transform.flip(image, True, False)
        self.arrowImage2 = pygame.transform.rotate(image, -45)
        image = pygame.image.load("assets/arrow.png")
        self.arrowImage1 = pygame.transform.scale(image, (75, 150))


        self.finger=classes.Finger([[squares[5].x,squares[5].y], [squares[10].x,squares[10].y], [squares[9].x,squares[9].y], [squares[6].x,squares[6].y]], squares[0].size)

        self.pointBar=preset.calculatePointBar(["PLAY", "WORD", "SQUARE"])
        self.wordInfo=classes.WordsSorted(["PLAY", "WORD", "SQUARE"], [], const.LIGHT_BLUE)
        self.score=0
        

tutorialStuff=""

def setUp():
    tutorStuff=TutorialStuff()
    for square in tutorStuff.squares:
        square.visible=True
    for square in game.squares:
        square.visible=False
    return tutorStuff

def mouseDown(event, tutorStuff: TutorialStuff):
    pointBar=tutorStuff.pointBar
    for oneSquare in tutorStuff.squares:
        if oneSquare.rect.collidepoint(event.pos):
            tutorStuff.clicked=True
            tutorStuff.currentWord=""
            tutorStuff.wordNumbers=[]
            break
    if pointBar.hintStart.hoveredOver:
        for oneSquare in tutorStuff.squares:
            oneSquare.showStarted=True
    if pointBar.hintRemain.hoveredOver:
        for oneSquare in tutorStuff.squares:
            oneSquare.showIn=True

def mouseUp(tutorStuff:TutorialStuff):
    if tutorStuff.clicked:
        tutorStuff.score=game.checkIfWord(tutorStuff.currentWord, tutorStuff.wordInfo, tutorStuff.pointBar, tutorStuff.score, tutorStuff.squares)

    tutorStuff.clicked=False
    
    #scroll bar
    tutorStuff.wordInfo.moving=False

    #resetting the squares
    for square in tutorStuff.squares:
        square.setting="normal"



def playTutorial(tutorStuff:TutorialStuff):
    #basic stuff
    const.SCREEN.fill(const.LIGHT_BLUE)
    util.toScreen("HIDDEN WORDS SQUARE", const.FONT75, const.BLACK, const.WIDTH // 2, 80)
    
    #getting the mouse dragged stuff to work
    mouseX, mouseY = pygame.mouse.get_pos()
    util.toScreen(tutorStuff.currentWord, const.FONT50, const.BLACK, const.WIDTH//2, 205)
    if tutorStuff.clicked:
        game.wordType.image=game.wordType.imageBlank
        for oneSquare in tutorStuff.squares:
            tutorStuff.currentWord, tutorStuff.wordNumbers, oneSquare=game.colourSquares(oneSquare, mouseX, mouseY, tutorStuff.currentWord, tutorStuff.wordNumbers)
            game.showLine(const.colour2, oneSquare, tutorStuff.squares, tutorStuff.currentWord)
    

    #moving to the next word
    #starting the timer
    if tutorStuff.currentWord=="PLAY" or tutorStuff.currentWord=="WORD" or tutorStuff.currentWord=="SQUARE":
        if tutorStuff.currentWord=="SQUARE":
            tutorStuff.done=True
        tutorStuff.startTimer=True
        tutorStuff.finger.stop=True
        
    #adding to the timer
    if tutorStuff.startTimer:
        tutorStuff.timer+=1/const.FPS
    #actually moving to the next word
    if tutorStuff.timer>2 and not tutorStuff.done:
        #going to the next letters
        tutorStuff.letterNum+=1
        tutorStuff.squares=preset.makeSquares(16, tutorStuff.letters[tutorStuff.letterNum], const.colour1)
        #updating the number in and starting
        for oneSquare in tutorStuff.squares:
            if oneSquare.letter!=" ":
                oneSquare.numInLeft=1
            if oneSquare.letter=="S":
                oneSquare.numStartedLeft=1
            oneSquare.visible=True
        #resetting variables
        tutorStuff.startTimer=False
        tutorStuff.timer=0
        tutorStuff.currentWord=""
        #having the finger move
        squares=tutorStuff.squares
        if tutorStuff.letterNum==1:
            tutorStuff.finger.newLocations([[squares[0].x,squares[0].y], [squares[4].x,squares[4].y], [squares[1].x,squares[1].y], [squares[2].x,squares[2].y]], squares[0].size)
        elif tutorStuff.letterNum==2:
            tutorStuff.finger.newLocations([[squares[3].x,squares[3].y], [squares[7].x,squares[7].y], [squares[11].x,squares[11].y], [squares[15].x,squares[15].y], [squares[14].x,squares[14].y], [squares[13].x,squares[13].y]], squares[0].size)

    #text talking about the buttons
    if tutorStuff.pointBar.startShowing:
        util.toScreen("Click me!", const.FONT55, const.BLACK, 1200, 420)
        util.toScreen("Click me!", const.FONT55, const.BLACK, 1380, 420)
    

    #drawing
    #showing the score    
    tutorStuff.pointBar.draw(tutorStuff.score)
    game.wordType.draw()
    tutorStuff.wordInfo.draw()    
    for oneSquare in tutorStuff.squares:
        if oneSquare.visible:
            oneSquare.draw()
    tutorStuff.finger.draw()

    #doing this so the arrow is above the squares, more showing stuff
    #squares that start words
    if tutorStuff.squares[0].showStarted:
        util.toScreen2("The S starts a word", "but not any other letters", const.FONT45, const.BLACK, 970, 200)
        
        const.SCREEN.blit(tutorStuff.arrowImage1, (900, 230))
    #squares that start words
    if tutorStuff.squares[0].showIn:
        util.toScreen2("All the letters left are only", "in one more word", const.FONT45, const.BLACK, 1300, 500)
        util.toScreen2("If they aren't in any words", "they are dark", const.FONT45, const.BLACK, 1300, 560)
        
        const.SCREEN.blit(tutorStuff.arrowImage2, (1075, 570))

    #showing the end message
    if tutorStuff.timer>3 and tutorStuff.done:
        game.celebrate()
        util.toScreen2("Now you can",  "go play!", const.FONT55, const.BLACK, const.WIDTH-250, const.HEIGHT-80)
    
        