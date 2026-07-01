import pygame
import asyncio
import constants as const
import utilities as util
import gameplay
import preset


# important stuff
# pylint: disable=no-member
pygame.init()
running=True
gameState="playing"



async def main():
    global running, gameState
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if gameState=="playing":
                if event.type==pygame.MOUSEBUTTONDOWN:
                    #setting up the letters
                    if not preset.gameStarted:
                        preset.gameStarted=True
                        squareInfo=preset.getSquareInfo()
                        preset.getSquares(squareInfo[0], squareInfo[1], squareInfo[2])
                        gameplay.makePointBar()
                    #actual gameplay
                    else:
                        #starting to make a word
                        for square in preset.squares:
                            if square.rect.collidepoint(event.pos):
                                gameplay.clicked=True
                                gameplay.currentWord=""#square.letter
                                break


                if event.type==pygame.MOUSEBUTTONUP:
                    gameplay.clicked=False
                    for square in preset.squares:
                        square.setting="normal"
                    gameplay.wordsFound=gameplay.checkIfWord(gameplay.currentWord, gameplay.wordsFound)
                    

        if gameState=="playing":
            gameplay.play()

        #important stuff
        pygame.display.flip()
        const.CLOCK.tick(const.FPS)
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
    pygame.quit()
        
