import constants as const
import utilities as util
from preset import squares
import pygame
import math





def play():
    const.SCREEN.fill(const.MAGENTA)
    util.toScreen("HIDDEN WORDS SQUARE", const.FONT60, const.BLACK, const.WIDTH // 2, 100)
    for square in squares:
        square.draw()
