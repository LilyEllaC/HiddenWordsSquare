import constants as const
import utilities as util

#text
#explanation
textStr="In this game you try to find all the words hidden in the puzzle. \nWords can only be made by connecting adjacent letters, either horizontally, \nvertically, or diagonally. Each letter is worth a number of points. \nThat is shown by the black number in the bootom center of the square. \nA word is worth the number of points of each letter combined. \nFor example, SQUARE is worth 11 because S=1, Q=6, U=1, A=1, R=1, and E=1. \n"
textStr+="When you get enough points you will unlock bonuses like x and x. \nThese bonuses show up in the x and x corners. "

text=util.stringToList(textStr, "\n")


def showExplanation():
    const.SCREEN.fill(const.LIGHT_GREEN)
    util.toScreen("HIDDEN WORDS SQUARE", const.FONT75, const.BLACK, const.WIDTH // 2, 80)

    util.toScreenInfTopLeft(text, const.FONT40, const.FONT40, const.BLACK, const.WIDTH//10, 150)