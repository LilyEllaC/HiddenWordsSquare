import pygame
import constants as const
import utilities as util
import random
import math

import findTheWords
#letters
class Squares:
    def __init__(self, size, fontNum, x, y, colourClicked, colourNormal, letters, letterNum, isDuplicate, point):
        self.size=size
        self.radius=self.size*3//8
        self.x=x
        self.y=y
        self.xCirc=self.x+self.size//2
        self.yCirc=self.y+self.size//2
        self.colourN=colourNormal
        self.colourC=colourClicked
        self.colour=self.colourN
        self.letter=letters[letterNum]
        self.letters=letters
        self.gridPosition=letterNum
        self.fontNum=fontNum
        self.isDuple=isDuplicate
        self.position=-1
        self.point=point
        self.setting="normal"
        self.visible=False
        self.neighbours=[]
        self.numNeighbours=[]


        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def findNeighbours(self, squares):
        self.neighbours = findTheWords.findsquaresNeighbours(self.gridPosition, squares)
        self.numNeighbours = [x.gridPosition for x in self.neighbours]
        #error checking
        if not " " in self.letters and False:
            print("\nNumber: "+str(self.gridPosition)+self.letter)
            for i in range(0,len(self.numNeighbours)):
                print(str(self.numNeighbours[i])+self.neighbours[i].letter+", ", end="")

    def changeColours(self, colour1, colour2):
        self.colourN=colour1
        self.colourC=colour2

    def draw(self):
        pygame.draw.rect(const.SCREEN, self.colourN, self.rect)
        pygame.draw.rect(const.SCREEN, const.BLACK, self.rect, 5)
        if self.setting=="clicked":
            pygame.draw.circle(const.SCREEN, self.colourC, (self.xCirc, self.yCirc), self.radius)
        else:
            self.position=-1
        util.toScreen(self.letter, const.FONTS[self.fontNum], const.BLACK, self.x+self.size//2, self.y+self.size*4//7)
        util.toScreen(str(self.point), const.FONT40, const.BLACK, self.x+self.size//2, self.y+self.size-20)


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
        self.totalScore=totalScore
        self.rectPoints = pygame.Rect(self.x, self.y, 0, self.height)
        self.rectBase = pygame.Rect(self.x, self.y, self.width, self.height)

    def changeScore(self, score):
        self.rectPoints=pygame.Rect(self.x, self.y, self.onePoint*score, self.height)

    def draw(self):
        pygame.draw.rect(const.SCREEN, self.colourBase, self.rectBase)
        pygame.draw.rect(const.SCREEN, self.colourPoints, self.rectPoints)


class WordType:
    def __init__ (self):
        self.width=245
        self.height=75
        self.x=const.WIDTH//2-(self.width//2)
        self.y=110
        
        image=pygame.image.load("correct.png")
        self.imageCorrect=pygame.transform.scale(image, (self.width, self.height))
        image=pygame.image.load("wrong.png")
        self.imageWrong=pygame.transform.scale(image, (self.width, self.height))
        image=pygame.image.load("tooShort.png")
        self.imageShort=pygame.transform.scale(image, (self.width, self.height))
        image=pygame.image.load("bonus.png")
        self.imageBonus=pygame.transform.scale(image, (self.width, self.height))
        image=pygame.image.load("found.png")
        self.imageFound=pygame.transform.scale(image, (self.width, self.height))
        image=pygame.image.load("foundBonus.png")
        self.imageFoundBonus=pygame.transform.scale(image, (self.width, self.height))
        image=pygame.image.load("blank.png")
        self.imageBlank=pygame.transform.scale(image, (self.width, self.height))
        self.image=self.imageBlank

    def draw(self):
        const.SCREEN.blit(self.image, (self.x, self.y))


class WordsSorted():
    def __init__(self, words, bonusWords, colour):
        #dealing with scrolling
        self.barY=130
        self.minY=self.barY
        self.height=const.HEIGHT
        self.rect = pygame.Rect(const.WIDTH//4-40, 0, 20, self.height)
        self.hiddenColour=colour
        self.colour=self.hiddenColour
        self.bottomY=0
        self.change=0
        self.barStartMovingY=0
        self.mouseStart=0
        self.textHeight=self.barY-self.bottomY
        self.showableHeight=(const.HEIGHT-self.barY)-5
        self.maxY=self.minY+self.showableHeight
        self.moving=False

        #moving the text
        self.textY=self.barY-40
        self.textStartMovingY=0
        self.textMinY=self.textY
        self.textMaxY=self.textY

        #hding the top part of the text
        self.hidingRect=pygame.Rect(0, 0, 325, 125)

        self.wordsToShowList=[]


        #tuples showing the words in the puzzle, the words found, and the length of the words
        self.allWordsSorted=[]
        for i in range (4, 16):
            self.allWordsSorted.append(([], [], i))
        #bonusWords
        self.allWordsSorted.append(([], [], 100))
        
        #adding the words to the list
        self.allRealWords=words
        for word in words:
            self.allWordsSorted[len(word)-4][0].append(word)
            #self.allWordsSorted[len(word)-4][1].append(word) #cheating so I don't have to actually find the words
        #bonus word stuff
        for word in bonusWords:
            self.allWordsSorted[12][0].append(word)
        
        #getting rid of categories that don't have any words in them
        self.wordsToShow=""
        numbersToDelete=[]
        for wordCat in self.allWordsSorted:
            if len(wordCat[0])==0:
                numbersToDelete.append(wordCat)
        #actually deleting
        for numbers in numbersToDelete:
            position=self.allWordsSorted.index(numbers)
            self.allWordsSorted.pop(position)
    
    def makeWordsToShow(self):
        wordsToShow=""
        numberLeft=0
        #for each word length
        for wordCat in self.allWordsSorted:
            addNewLine=True
            wordCat[1].sort()
            numberLeft=len(wordCat[0])-len(wordCat[1])
            if wordCat[2]!=100:
                wordsToShow+="\n"+str(wordCat[2])+" Letter Words\n"+str(numberLeft)+" left"
            else:
                wordsToShow+="\n"+"Bonus Words\n"+str(numberLeft)+" left"
            #slight error checking (I think)
            if len(wordCat[1])>0:
                for word in wordCat[1]:
                    #print(wordCat[1])
                    #four letters words have two per line, others have only 1
                    if wordCat[2]!=4:
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
            self.textHeight=self.bottomY-self.textY
            self.height=self.showableHeight*(self.showableHeight/self.textHeight)
            self.rect = pygame.Rect(const.WIDTH//4-40, self.barY, 20, self.height)

    def startMove(self):
        mouseX, mouseY= pygame.mouse.get_pos()
        if self.rect.collidepoint((mouseX, mouseY)):
            self.barStartMovingY=self.barY
            self.textStartMovingY=self.textY
            self.mouseStart=mouseY
            self.moving=True
            print("started moving")
            
    def move(self):
        mouseY= pygame.mouse.get_pos()[1]
        #print("Y position: "+str(self.barY)+" min y: "+str(self.minY)+" max y: "+str(self.maxY-self.height))
        if self.barY>=self.minY and self.barY<=self.maxY-self.height:
            self.change=(mouseY-self.mouseStart)
            self.barY=self.barStartMovingY+self.change
            textChangeRatio=self.textHeight/self.showableHeight
            self.textY=self.textStartMovingY-self.change*textChangeRatio

        #stopping it from glitching and going to far
        if self.barY<self.minY:
            self.barY=self.minY
        if self.barY+self.height>self.maxY:
            self.barY=(self.maxY-self.height)-1
        #for the text
        if self.textY<self.textMinY:
            self.textY=self.textMinY
        if self.textY>self.textMaxY:
            #print("y too high")
            self.textY=(self.textMaxY)-1
        
        #moving the text
        self.textMinY=-self.textHeight+90+self.showableHeight
        
    def draw(self):
        self.makeWordsToShow()
        self.wordsToShowList=util.stringToList(self.wordsToShow, "\n")
        self.bottomY=util.toScreenInfTopLeft(self.wordsToShowList, const.FONT60, const.FONT45, const.colour2, 10, self.textY)
        #print(str(self.bottomY))      
                            
        #scroll bar stuff
        self.scrollBarAppearance()
        pygame.draw.rect(const.SCREEN, self.colour, self.rect)
        pygame.draw.rect(const.SCREEN, self.hiddenColour, self.hidingRect)

        if self.moving: 
            self.move()


class Buttons():
    def __init__(self):
        self.width=100
        self.x=const.WIDTH-self.width-30
        self.y=const.HEIGHT-self.width-30
        image=pygame.image.load("play.png")
        self.imageGame=pygame.transform.scale(image, (self.width, self.width))
        self.rectGame=pygame.Rect(self.x, self.y, self.width, self.width)
        image=pygame.image.load("Explain.png")
        self.imageExplain=pygame.transform.scale(image, (self.width, self.width))
        self.rectExplain=pygame.Rect(self.x, self.y-(self.width+30), self.width, self.width)
        image=pygame.image.load("tutorial.png")
        self.imageTutorial=pygame.transform.scale(image, (self.width, self.width))
        self.rectTutorial=pygame.Rect(self.x, self.y-(self.width+30)*2, self.width, self.width)
        image=pygame.image.load("blank.png")
        self.imageBlank=pygame.transform.scale(image, (self.width, self.width))

    def draw(self):
        const.SCREEN.blit(self.imageGame, (self.x, self.y))
        const.SCREEN.blit(self.imageExplain, (self.x, self.y-(self.width+30)))
        const.SCREEN.blit(self.imageTutorial, (self.x, self.y-(self.width+30)*2))


class Finger():
    def __init__(self, locations, width):
        for location in locations:
            location[0]+=width//2
            location[1]+=width//2

        location1=locations[0]
        self.width=100
        self.height=130
        self.speed=3
        self.locations=locations
        self.previousLocations=[location1]
        self.x=location1[0]-self.width//2
        self.y=location1[1]-self.height//2
        self.currentLocation=location1
        self.nextLocation=locations[1]
        self.stop=False

        image=pygame.image.load("fingerPointing.png")
        self.image=pygame.transform.scale(image, (self.width, self.height))

    def newLocations(self, locations, width):
        #remake everything
        for location in locations:
            location[0]+=width//2
            location[1]+=width//2

        location1=locations[0]
        self.locations=locations
        self.previousLocations=[location1]
        self.x=location1[0]-self.width//2
        self.y=location1[1]-self.height//2
        self.currentLocation=location1
        self.nextLocation=locations[1]
        self.stop=False

    def move(self):
        position=len(self.previousLocations)
        if self.currentLocation[0]==self.nextLocation[0]:
            if self.currentLocation[1]<self.nextLocation[1]:
                self.y+=self.speed
            if self.currentLocation[1]>self.nextLocation[1]:
                self.y-=self.speed
        elif self.currentLocation[1]==self.nextLocation[1]:
            if self.currentLocation[0]<self.nextLocation[0]:
                self.x+=self.speed
            if self.currentLocation[0]>self.nextLocation[0]:
                self.x-=self.speed
        else:
            self.moveDiagonal()
       
        if abs((self.x+self.width//2)-self.nextLocation[0])<self.speed and abs((self.y+self.height//2)-self.nextLocation[1])<self.speed:
            self.previousLocations.append(self.locations[position])
            self.currentLocation=self.locations[position]
            if position+1!=len(self.locations):
                self.nextLocation=self.locations[position+1]

    def moveDiagonal(self):
        
        slope=((self.nextLocation[1]+self.height//2)-(self.currentLocation[1]+self.height//2))/((self.nextLocation[0]+self.width)-(self.currentLocation[0]+self.width))
        if self.currentLocation[0]<self.nextLocation[0]:
            self.x+=self.speed
        if self.currentLocation[0]>self.nextLocation[0]:
            self.x-=self.speed
        self.y+=slope*self.speed

            
    def draw(self):
        if len(self.previousLocations)!=len(self.locations) and not self.stop:
            const.SCREEN.blit(self.image, (self.x, self.y))
            self.move()


class ButtonToShowColours():
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.hoveredOver=False
        image=pygame.image.load("colourWheelHovered.png")
        self.imageHovered=pygame.transform.scale(image, (width, height))
        image=pygame.image.load("colourWheel.png")
        self.imageNormal=pygame.transform.scale(image, (width, height))
        self.image=self.imageNormal

        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y

    def update(self):
        #checking if te mouse is hovered over it
        mouseX, mouseY=pygame.mouse.get_pos()
        if mouseX>self.x and mouseX<self.x+self.width and mouseY>self.y and mouseY<self.y+self.height:
            self.image=self.imageHovered
            self.hoveredOver=True
        else:
            self.image=self.imageNormal
            self.hoveredOver=False

    def draw(self):
        const.SCREEN.blit(self.image, (self.x, self.y))
        self.update()


#code mostly taken from a previous project of mine
class Confetti():
    def __init__(self, image):
        self.x=random.randint(0, const.WIDTH)
        self.y=random.randint(-300,300)
        self.angle=random.randint(0,360)
        #image
        self.startImage=image
        self.image=pygame.transform.rotate(self.startImage, self.angle)
        self.done=False
        #not needed stuff
#        self.rect=self.image.get_rect()
 #       self.rect.x=self.x
  #      self.rect.y=self.y

    def update(self):
        FPSScaling=const.FPS_SCALING
        #moving down slowly and drifting a little
        self.y+=random.randint(7, 13)*FPSScaling
        self.x+=random.randint(-2,2)*FPSScaling
        self.angle+=random.randint(-15,15)*FPSScaling
        self.image=pygame.transform.rotate(self.startImage, self.angle) 
        #resetting if too low
        if self.y>const.HEIGHT:
            self.done=True
            self.reset()

    def reset(self):
        self.y=random.randint(-300,300)

    def draw(self):
        if not self.done:
            const.SCREEN.blit(self.image, (self.x, self.y))
            self.update()
        
            
class ColourButton():
    def __init__(self, x, y, width, height, colours, words, font):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.hoveredOver=False
        self.words=words
        self.font=font

        self.colour1=colours[0]
        self.colour2=colours[1]
        self.colour3=colours[2]
        self.rect=(x-7, y-3.5, width, height)
        self.hitBox=pygame.Rect(x-7, y-3.5, width, height)

    def check(self):
        #checking if the mouse is hovered over it
        mouseX, mouseY=pygame.mouse.get_pos()
        if mouseX>self.x and mouseX<self.x+self.width and mouseY>self.y and mouseY<self.y+self.height:
            self.hoveredOver=True
        else:
            self.hoveredOver=False
    
    def draw(self):
        pygame.draw.rect(const.SCREEN, self.colour1, self.rect)
        pygame.draw.rect(const.SCREEN, self.colour3, self.rect, 5)
      #  util.toScreen(self.words, self.font, self.colour2, self.x, self.y)
        text=self.font.render(self.words, True, self.colour2)
        const.SCREEN.blit(text, (self.x, self.y))
        self.check()

        #if mouse over
        if self.hoveredOver:
            text=self.font.render(self.words, True, const.BLACK)
            const.SCREEN.blit(text, (self.x+self.width+10, self.y))

    
        