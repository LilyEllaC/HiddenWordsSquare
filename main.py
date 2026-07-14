import pygame
import asyncio
import constants as const
import gameplay
import explanation
import tutorial
import preset
import classes
import findTheWords


# important stuff
# pylint: disable=no-member
pygame.init()
running=True
gameState="explain"

#buttons
buttons=classes.Buttons()

async def main():
    findTheWords.fixWordList()
    global running, gameState
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            #buttons
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY=pygame.mouse.get_pos()
                if buttons.rectGame.collidepoint((mouseX, mouseY)):
                    gameState="playing"
                    if not preset.gameStarted:
                        words=gameplay.getWords(preset.theLetters)
                        wordInfo, gameplay.pointBar=gameplay.makePoints(words, gameplay.pointBar)
                    wordInfo, gameplay.squares, gameplay.pointBar=gameplay.setUp(preset.gameStarted, gameplay.squares, gameplay.pointBar, wordInfo)
                if buttons.rectExplain.collidepoint((mouseX, mouseY)):
                    gameState="explain"
                if buttons.rectTutorial.collidepoint((mouseX, mouseY)):
                    gameState="tutorial"
                    tutorial.setUp()


            if gameState=="playing":
                if event.type==pygame.MOUSEBUTTONDOWN:
                    #actual gameplay
                    #starting to make a word
                    for square in gameplay.squares:
                        if square.rect.collidepoint(event.pos):
                            gameplay.clicked=True
                            gameplay.currentWord=""
                            break
                    #scroll bar
                    wordInfo.startMove()


                if event.type==pygame.MOUSEBUTTONUP:
                    if gameplay.clicked:
                        gameplay.score=gameplay.checkIfWord(gameplay.currentWord, wordInfo, gameplay.pointBar, gameplay.score)
                    gameplay.clicked=False
                    
                    #scroll bar
                    wordInfo.moving=False

                    #resetting the squares
                    for square in gameplay.squares:
                        square.setting="normal"
            
            #tutorial
            if gameState=="tutorial":
                if event.type==pygame.MOUSEBUTTONDOWN:
                    tutorial.clicked, tutorial.currentWord=tutorial.mouseDown(event, tutorial.pointBar, tutorial.currentWord)
                if event.type==pygame.MOUSEBUTTONUP:
                    tutorial.clicked, tutorial.score=tutorial.mouseUp(tutorial.clicked, tutorial.pointBar, tutorial.score, tutorial.currentWord)
                    

        if gameState=="playing":
            gameplay.currentWord=gameplay.play(wordInfo, gameplay.pointBar, gameplay.currentWord)
        elif gameState=="explain":
            explanation.showExplanation()
        elif gameState=="tutorial":
            tutorial.pointBar, tutorial.currentWord, tutorial.squares=tutorial.playTutorial(tutorial.pointBar, tutorial.currentWord, tutorial.squares, tutorial.finger)

        #important stuff
        buttons.draw()
        pygame.display.flip()
        const.CLOCK.tick(const.FPS)
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
    pygame.quit()
        
