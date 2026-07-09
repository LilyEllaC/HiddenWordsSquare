import pygame
import asyncio
import constants as const
import utilities as util
import gameplay
import explanation
import tutorial
import preset
import classes


# important stuff
# pylint: disable=no-member
pygame.init()
running=True
gameState="explain"

#buttons
buttons=classes.Buttons()

async def main():
    global running, gameState
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            #buttons
            if event.type==pygame.MOUSEBUTTONDOWN:
                print("pressed")
                mouseX, mouseY=pygame.mouse.get_pos()
                if buttons.rectGame.collidepoint((mouseX, mouseY)):
                    print("game")
                    gameState="playing"
                    wordInfo=gameplay.setUp(preset.gameStarted)
                if buttons.rectExplain.collidepoint((mouseX, mouseY)):
                    print("explain")
                    gameState="explain"
                if buttons.rectTutorial.collidepoint((mouseX, mouseY)):
                    print("tutorial")
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
                        gameplay.checkIfWord(gameplay.currentWord, wordInfo, gameplay.pointBar)
                    gameplay.clicked=False
                    
                    #scroll bar
                    wordInfo.moving=False

                    #resetting the squares
                    for square in gameplay.squares:
                        square.setting="normal"
            
            #tutorial
            if gameState=="tutorial":
                if event.type==pygame.MOUSEBUTTONDOWN:
                    tutorial.mouseDown(event)
                if event.type==pygame.MOUSEBUTTONUP:
                    tutorial.mouseUp()
                    

        if gameState=="playing":
            gameplay.play(wordInfo)
        elif gameState=="explain":
            explanation.showExplanation()
        elif gameState=="tutorial":
            tutorial.playTutorial()

        #important stuff
        buttons.draw()
        pygame.display.flip()
        const.CLOCK.tick(const.FPS)
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
    pygame.quit()
        
