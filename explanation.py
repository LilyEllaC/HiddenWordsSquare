import constants as const
import utilities as util

#text
#explanation
textStr="In this game you try to find all the normal words hidden in the puzzle. \nWords can only be made by connecting adjacent letters, either horizontally, \nvertically, or diagonally. You connect letters be clicking and dragging. \nYou can do that with your finger or your mouse \nEach letter is worth a number of points. \nThat is shown by the black number in the bottom center of the square. \nA word is worth the number of points of each letter combined. \nFor example, SQUARE is worth 11 because S=1, Q=6, U=1, A=1, R=1, and E=1. \n"
textStr+="There are both normal words and bonus words. \nNormal words are the words that you need to find to complete the game. \nBonus words are words that were too weird to be required to find. \nThe bonus and normal word lists are questionable, so they may be changed. \n"
textStr+="There are two hints that can be unlocked by getting a high enough score. \nThe hints are optional and are only revealed when you press the button for it with your mouse. \nThe first hint shows you how many words the letter starts and is in the bottom left corner. \nThe second hint appears in the bottom right corner showng how many words the letter is in. \n"
textStr+=""
text=util.stringToList(textStr, "\n")


def showExplanation():
    const.SCREEN.fill(const.LIGHT_GREEN)
    util.toScreen("HIDDEN WORDS SQUARE", const.FONT75, const.colour1, const.WIDTH // 2, 80)
    util.toScreen2("If you still don't understand or don't want to read all this", "I reccommend going to the tutorial --->", const.FONT60, const.colour1, const.WIDTH // 2, 680)

    util.toScreenInfTopLeft(text, const.FONT40, const.FONT40, const.BLACK, const.WIDTH//10, 100)