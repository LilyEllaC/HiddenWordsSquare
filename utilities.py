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

def toScreenInfTopLeft(wordList, font1, font2, colour, x, y):
    font1Height=font1.get_height()-5
    font2Height=font2.get_height()
    fontHeight=font1Height
    font=font1
    currentHeight=y
    for word in wordList:
        #check which font to use
        for number in "1234567890":
            if number in word or word=="Bonus Words":
                font=font1
                fontHeight=font1Height
                break
            else: 
                font=font2
                fontHeight=font2Height
        #stuff
        currentHeight+=fontHeight+5
        text = font.render(word, True, colour)
            
        const.SCREEN.blit(text, (x, currentHeight))
    return currentHeight

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