import constants as const
import utilities as util
import pygame


def play():
    const.SCREEN.fill(const.LIGHT_BLUE)
    util.toScreen("HIDDEN WORDS SQUARE", const.FONT60, const.BLACK, const.WIDTH // 2, const.HEIGHT // 2 - 100)
    