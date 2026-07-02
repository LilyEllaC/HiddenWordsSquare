from sprites import Squares, ScoreBar, WordType
import constants as const
import utilities as util
import math
import random

#preassigned variables
squares=[]
xPos=[]
yPos=[]
gameStarted=False
wordType=WordType()


#creating the points bar
def calculatePointBar():
    with open("wordsInPuzzle.txt", "r") as file:
        words = [line.strip() for line in file]
    totalScore=0
    for word in words:
        for letter in word:
            totalScore+=const.POINTS[ord(letter)-65]
    x=675
    y=150
    pointBar=ScoreBar(totalScore, const.BLUE, const. DARK_BLUE, x, y)
    return pointBar

#getting the square info
def getSquareInfo():
    with open("letters.txt", "r") as file:
        lines = file.readlines()
    letters=lines[random.randint(0, len(lines)-1)].strip()
    letters="PGIMEUNRCTSAIONR"
    return [len(letters), letters, const.TEAL]

#getting all of the squares
def getSquares(number, letters, colour):
    # getting the info
    numAcross=int(math.sqrt(number))
    xDistance=(const.WIDTH//2)//numAcross
    size=xDistance-xDistance//8
    for i in range(0, numAcross):
        xPos.append(const.WIDTH//4+xDistance*i)
        yPos.append(const.HEIGHT//4+xDistance*i)

    #dealing with duplicates
    duplicateLetters=[]
    for i in range(0, len(letters)):
        for j in range(i+1, len(letters)):
            if letters[i]==letters[j]:
                duplicateLetters.append(letters[i])

    #finding font size
    fontNum=(size*4//5)//5
    fontNum=0

    #finding other colour
    colourC=const.GRAY
    for i in range (0, len(const.COLOUROPTIONS)-1):
        if const.COLOUROPTIONS[i]==colour:
            colourC=const.COLOUROPTIONS[i+1]    


    #creating the squares
    letterPos=0
    for y in yPos:
        for x in xPos:
            #duplicate stuff
            if letters[letterPos] in duplicateLetters:
                duplicate=True
            else:
                duplicate=False
            
            #points
            letter=letters[letterPos]
            point=const.POINTS[ord(letter)-65]
            
            #creating
            squares.append(Squares(size, fontNum, x, y, colourC, letter, duplicate, point))
            letterPos+=1
        

#getting the list of words in the puzzle by length
def sortWords(words):
    with open("wordsInPuzzle.txt", "r") as file:
        words = file.readlines()

class WordsSorted():
    def __init__(self, words):
        self.words2=([],[], 2)
        self.words4=([],[], 4)
        self.words5=([],[], 5)
        self.words6=([],[], 6)
        self.words7=([],[], 7)
        self.words8=([],[], 8)
        self.words9=([],[], 9)
        self.words10=([],[], 10)
        self.words11=([],[], 11)
        self.words12=([],[], 12)
        self.words13=([],[], 13)
        self.words14=([],[], 14)
        self.words15=([],[], 15)
        self.words16=([],[], 16)
        self.allWordsSorted=[self.words4, self.words5, self.words6, self.words7, self.words8, self.words9, self.words10, self.words11, self.words12, self.words13, self.words14, self.words15, self.words16]
        self.allWords=words
        for word in words:
            self.allWordsSorted[len(word)-4][0].append(word)
            print(word)
            
        
        numbersToDelete=[]
        for wordCat in self.allWordsSorted:
            if len(wordCat[0])==0:
                numbersToDelete.append(wordCat)
        for numbers in numbersToDelete:
            position=self.allWordsSorted.index(numbers)
            self.allWordsSorted.pop(position)
        

    def draw(self):
        wordsToShow=""
        addNewLine=False
        for wordCat in self.allWordsSorted:
            wordsToShow+=str(wordCat[2])+" Letter Words \n"
            if len(wordCat[1])>0:
                for word in wordCat[1]:
                    #print(wordCat[1])
                    #if wordCat[2]>8:
                    wordsToShow+=word+"\n"
                    """
                    else:
                        wordsToShow+=word
                        addNewLine= not addNewLine
                        if addNewLine:
                            wordsToShow+="\n"
                            """
        print(wordsToShow)

