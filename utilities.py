import constants as const


#one line of text to screen
def toScreen(words, font, colour, x, y):
    text=font.render(words, True, colour)
    textRect = text.get_rect()
    textRect.center = (x, y)
    const.SCREEN.blit(text, textRect)

#versions for multiple lines
def toScreen2(words1, words2, font, colour, x, y):
    toScreen(words1, font, colour, x, y - font.get_height() // 2)
    toScreen(words2, font, colour, x, y + font.get_height() // 2)


def toScreen3(words1, words2, words3, font, colour, x, y):
    toScreen(words1, font, colour, x, y - font.get_height())
    toScreen(words2, font, colour, x, y)
    toScreen(words3, font, colour, x, y + font.get_height())

def toScreenInfTopLeft(wordList, font, colour, x, y):
    heightAdded=0
    fontHeight=font.get_height()
    for word in wordList:
        text = font.render(word, True, colour)
        const.SCREEN.blit(text, (x, y+heightAdded*fontHeight))
        heightAdded+=1

#taking a string with \n and turning it into a list
def stringToList(string, symbol):
    tempString=""
    wordsList=[]
    while symbol in string:
        symbolPlacement=string.find(symbol)
        tempString=string[:symbolPlacement-(len(symbol)-1)]
        wordsList.append(tempString)
        string=string[string.find(symbol)+len(symbol):]
    wordsList.append(string)
   # for words in wordsList:
    #    print(words+"\n\n")
    return wordsList