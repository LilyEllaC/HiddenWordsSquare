import pygame
import asyncio
import constants as const
import gameplay
import explanation
import tutorial
import preset
import classes
import colour


# important stuff
# pylint: disable=no-member
pygame.init()
running=True
gameState="explain"


#buttons
buttons=classes.Buttons()



async def main():
    global running, gameState
    #set up stuff
    preset.gameStarted=True
    squareInfo=preset.getSquareInfo()
    preset.theLetters=squareInfo[1]
    gameplay.squares=preset.makeSquares(squareInfo[0], squareInfo[1], squareInfo[2])
    words, bonusWords, gameplay.squares=gameplay.getWords(preset.theLetters, gameplay.squares)
    wordInfo, gameplay.pointBar=gameplay.makeBarAndWordInfo(words, bonusWords, gameplay.pointBar)

    preset.theLetters=squareInfo[1]

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            #buttons
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY=pygame.mouse.get_pos()
                #navigating between the different setting
                #going to the game
                if buttons.rectGame.collidepoint((mouseX, mouseY)):
                    gameState="playing"
                    gameplay.squares=gameplay.setUp(gameplay.squares)
                #going to the explanation
                if buttons.rectExplain.collidepoint((mouseX, mouseY)):
                    gameState="explain"
                #going to the tutorial
                if buttons.rectTutorial.collidepoint((mouseX, mouseY)):
                    gameState="tutorial"
                    tutorial.setUp()
                
                #colour stuff:
                if mouseX<200 and mouseY<400:
                    colour.checkButtons(mouseX, mouseY)
                else: const.popUp=False

            if gameState=="playing":
                if event.type==pygame.MOUSEBUTTONDOWN:
                    #actual gameplay
                    #starting to make a word
                    for square in gameplay.squares:
                        if square.rect.collidepoint(event.pos):
                            gameplay.clicked=True
                            gameplay.currentWord=""
                            gameplay.wordNumbers=[]
                            break
                    #scroll bar
                    wordInfo.startMove()


                if event.type==pygame.MOUSEBUTTONUP:
                    if gameplay.clicked:
                        gameplay.score=gameplay.checkIfWord(gameplay.currentWord, wordInfo, gameplay.pointBar, gameplay.score, gameplay.squares)
                    gameplay.clicked=False
                    
                    #scroll bar
                    wordInfo.moving=False

                    #resetting the squares
                    for square in gameplay.squares:
                        square.setting="normal"
            

            #tutorial
            if gameState=="tutorial":
                if event.type==pygame.MOUSEBUTTONDOWN:
                    tutorial.clicked, tutorial.currentWord, tutorial.wordNumbers=tutorial.mouseDown(event, tutorial.pointBar, tutorial.currentWord, tutorial.wordNumbers)
                if event.type==pygame.MOUSEBUTTONUP:
                    tutorial.clicked, tutorial.score=tutorial.mouseUp(tutorial.clicked, tutorial.pointBar, tutorial.score, tutorial.currentWord, tutorial.squares)
                    

        if gameState=="playing":
            gameplay.currentWord, gameplay.wordNumbers=gameplay.play(wordInfo, gameplay.pointBar, gameplay.currentWord, gameplay.wordNumbers, gameplay.score)
        elif gameState=="explain":
            explanation.showExplanation()
        elif gameState=="tutorial":
            tutorial.pointBar, tutorial.currentWord, tutorial.wordNumbers, tutorial.squares=tutorial.playTutorial(tutorial.pointBar, tutorial.currentWord, tutorial.wordNumbers, tutorial.squares, tutorial.finger)

        #colour stuff that can always appear
        if const.popUp:
            colour.showPopUp()
        colour.colourWheel.draw()


        #important stuff
        buttons.draw()
        pygame.display.flip()
        const.CLOCK.tick(const.FPS)
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
    pygame.quit()
        
