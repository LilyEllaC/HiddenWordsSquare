import pygame
import constants as const
import utilities as util


#letters
class Squares:
    def __init__(self, size, fontNum, x, y, colourClicked, letter, isDuplicate, point):
        self.size=size
        self.radius=self.size*3//8
        self.x=x
        self.y=y
        self.xCirc=self.x+self.size//2
        self.yCirc=self.y+self.size//2
        self.colourN=const.GRAY
        self.colourC=colourClicked
        self.colour=self.colourN
        self.letter=letter
        self.fontNum=fontNum
        self.isDuple=isDuplicate
        self.position=-1
        self.point=point
        self.setting="normal"

        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
    
    def draw(self):
        pygame.draw.rect(const.SCREEN, self.colour, self.rect)
        if self.setting=="clicked":
            pygame.draw.circle(const.SCREEN, self.colourC, (self.xCirc, self.yCirc), self.radius)
        else:
            self.position=-1
        util.toScreen(self.letter, const.FONTS[self.fontNum], const.BLACK, self.x+self.size//2, self.y+self.size*4//7)


class ScoreBar:
    def __init__(self, totalScore, colourPoints, colourBase, x, y):
        self.x=x
        self.y=y
        self.height=75
        self.width=const.WIDTH//4-50
        self.colourPoints=colourPoints
        self.colourBase=colourBase

        #figuring distance
        self.onePoint=self.width/totalScore
        self.rectPoints = pygame.Rect(self.x, self.y, 0, self.height)
        self.rectBase = pygame.Rect(self.x, self.y, self.width, self.height)

    def changeScore(self, score):
        self.rectPoints=pygame.Rect(self.x, self.y, self.onePoint*score, self.height)

    def draw(self):
        pygame.draw.rect(const.SCREEN, self.colourBase, self.rectBase)
        pygame.draw.rect(const.SCREEN, self.colourPoints, self.rectPoints)



class WordType:
    def __init__ (self):
        self.x=const.WIDTH//2-25
        self.y=60
        self.width=50
        image=pygame.image.load("checkmark.webp")
        self.imageCorrect=pygame.transform.scale(image, (self.width, self.width))
        image=pygame.image.load("cross.png")
        self.imageWrong=pygame.transform.scale(image, (self.width, self.width))
        image=pygame.image.load("Bonus symbol.png")
        self.imageBonus=pygame.transform.scale(image, (self.width, self.width))
        image=pygame.image.load("blank.png")
        self.imageBlank=pygame.transform.scale(image, (self.width, self.width))
        self.image=self.imageBlank

    def draw(self):
        const.SCREEN.blit(self.image, (self.x, self.y))





class WordsSorted():
    def __init__(self, words):
        #dealing with scrolling
        self.y=50.0
        self.height=const.HEIGHT
        self.rect = pygame.Rect(const.WIDTH//4-40, 0, 20, self.height)
        self.colour=const.MAGENTA
        self.bottomY=0
        self.textHeight=self.y-self.bottomY
        self.showableHeight=const.HEIGHT-self.y-30


        self.wordsToShowList=[]

        #tuples showing the words in the puzzle, the words found, and the length of the words
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
            
        self.wordsToShow=""
        numbersToDelete=[]
        for wordCat in self.allWordsSorted:
            if len(wordCat[0])==0:
                numbersToDelete.append(wordCat)
        for numbers in numbersToDelete:
            position=self.allWordsSorted.index(numbers)
            self.allWordsSorted.pop(position)
    
    def makeWordsToShow(self):
        wordsToShow=""
        numberLeft=0
        for wordCat in self.allWordsSorted:
            addNewLine=True
            wordCat[1].sort()
            numberLeft=len(wordCat[0])-len(wordCat[1])
            wordsToShow+="\n"+str(wordCat[2])+" Letter Words\n"+str(numberLeft)+" left"
            if len(wordCat[1])>0:
                for word in wordCat[1]:
                    #print(wordCat[1])
                    if wordCat[2]>8:
                        wordsToShow+="\n"+word
                
                    else:
                        if addNewLine:
                            wordsToShow+="\n"
                        wordsToShow+=word+"    "
                        addNewLine= not addNewLine
            wordsToShow+="\n"
        self.wordsToShow=wordsToShow

    def scrollBarAppearance(self):
        if self.bottomY>const.HEIGHT-30:
            self.colour=const.LIGHT_GRAY
            self.textHeight=self.bottomY-self.y
            self.height=self.showableHeight*(self.showableHeight/self.textHeight)
            self.rect = pygame.Rect(const.WIDTH//4-40, self.y+60, 20, self.height)


    def draw(self):
        self.makeWordsToShow()
        self.wordsToShowList=util.stringToList(self.wordsToShow, "\n")
        self.bottomY=util.toScreenInfTopLeft(self.wordsToShowList, const.FONT60, const.BLACK, 10, self.y)
        #print(str(self.bottomY))      
                            
        #scroll bar stuff
        self.scrollBarAppearance()
        pygame.draw.rect(const.SCREEN, self.colour, self.rect)
