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
            if event.type==pygame.MOUSEBUTTONDOWN:
                if gameState=="playing" and not preset.gameStarted:
                    preset.gameStarted=True
                    squareInfo=preset.getSquareInfo()
                    preset.getSquares(squareInfo[0], squareInfo[1], squareInfo[2])
                    print("squares")
        if gameState=="playing":
            gameplay.play()

        #important stuff
        pygame.display.flip()
        const.CLOCK.tick(const.FPS)
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
    pygame.quit()
        
