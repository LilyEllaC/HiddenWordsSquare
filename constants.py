import pygame

#game set up
WIDTH, HEIGHT=1500, 1000
FPS=30
FPS_SCALING=30/FPS
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Hidden Words Square")

#colours
RED = (255, 0, 0)
DARK_RED = (137, 0, 0)
ORANGE = (255, 137, 0)
DARK_ORANGE = (137, 68, 0)
YELLOW = (255, 255, 0)
DARK_YELLOW = (137, 137, 0)
GREEN = (0, 230, 15)
LIGHT_GREEN = (125, 255, 125)
DARK_GREEN = (0, 150, 0)
TEAL = (55, 225, 250)
DARK_TEAL = (0, 137, 137)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 170)
LIGHT_BLUE = (0, 230, 255)
PURPLE = (179, 0, 255)
DARK_PURPLE = (100, 0, 150)
MAGENTA = (255, 0, 255)
DARK_MAGENTA = (137, 0, 137)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (147, 147, 147)
DARK_GRAY = (100, 100, 100)
LIGHT_RED = (210, 76, 76)

COLOUROPTIONS=[RED, DARK_RED, ORANGE, DARK_ORANGE, YELLOW, DARK_YELLOW, GREEN, DARK_GREEN, TEAL, DARK_TEAL, BLUE, DARK_BLUE, PURPLE, DARK_PURPLE, MAGENTA, DARK_MAGENTA]

#letter points
POINTS=[1, 2, 3, 1, 1, 3, 2, 2, 1, 6, 4, 1, 2, 1, 1, 2, 6, 1, 1, 1, 1, 3, 2, 5, 3, 6]




#typing
pygame.font.init()
FONT_TYPE = None
FONT10 = pygame.font.Font(FONT_TYPE, 10)
FONT15 = pygame.font.Font(FONT_TYPE, 15)
FONT17 = pygame.font.Font(FONT_TYPE, 17)
FONT20 = pygame.font.Font(FONT_TYPE, 20)
FONT25 = pygame.font.Font(FONT_TYPE, 25)
FONT30 = pygame.font.Font(FONT_TYPE, 30)
FONT35 = pygame.font.Font(FONT_TYPE, 35)
FONT40 = pygame.font.Font(FONT_TYPE, 40)
FONT45 = pygame.font.Font(FONT_TYPE, 45)
FONT50 = pygame.font.Font(FONT_TYPE, 50)
FONT55 = pygame.font.Font(FONT_TYPE, 55)
FONT60 = pygame.font.Font(FONT_TYPE, 60)
FONT75 = pygame.font.Font(FONT_TYPE, 75)
FONT150 = pygame.font.Font(FONT_TYPE, 150)
FONT200 = pygame.font.Font(FONT_TYPE, 200)

FONTS = [FONT150, FONT10, FONT15, FONT20, FONT25, FONT30, FONT35, FONT40, FONT45, FONT50, FONT55, FONT60]
