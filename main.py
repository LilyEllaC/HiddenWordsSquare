import pygame
import asyncio
import constants as const
import utilities as util
import gameplay


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
            gameplay.play()

        #important stuff
        pygame.display.flip()
        const.CLOCK.tick(const.FPS)
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
    pygame.quit()
        
