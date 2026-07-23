
import math
import wordDictionary

def findsquaresNeighbours(position, squares):
    ## returns the set of neighbours given an input list of squares, and this elements index in that list (it is assume the to be a square)
    neighbours = []
    #finding out neighbouring letters
    numSquares=len(squares)
    numAcross=math.sqrt(numSquares)
    numAcross=int(numAcross)
    #all left neighbours
    if position%numAcross!=0:
        #print("\nLetters to the left: "+letters[letterNum-1])
        neighbours.append(squares[position-1])
        #left up, left down
        if position>numAcross-1:
            #print("Left up: "+letters[letterNum-(numAcross+1)])
            neighbours.append(squares[position-(numAcross+1)])
        if position<numSquares-numAcross:
            #print("Left down: "+letters[letterNum+(numAcross-1)])
            neighbours.append(squares[position+(numAcross-1)])

    #all right neighbours
    if position%numAcross!=numAcross-1:
        #print("Letters to the right: "+letters[letterNum+1])
        neighbours.append(squares[position+1])
        #left up, left down
        if position>=numAcross:
            #print("right up: "+letters[letterNum-(numAcross-1)])
            neighbours.append(squares[position-(numAcross-1)])
        if position<numSquares-numAcross:
            #print("Right down: "+letters[letterNum+(numAcross+1)])
            neighbours.append(squares[position+(numAcross+1)])
    
    #up and down
    if position>=numAcross:
        #print("Up: "+letters[letterNum-(numAcross)])
        neighbours.append(squares[position-(numAcross)])
    if position<numSquares-numAcross:
        #print("down: "+letters[letterNum+(numAcross)])
        neighbours.append(squares[position+(numAcross)])
        
    return neighbours



class Node:
    def __init__(self, letterOpt, position):
        self.letter =letterOpt
        self.neighbours =[]
        self.position=str(position)

    
    # Best for end-users (Clean & Pretty)
    def __str__(self):
        return f"'{self.letter}' - {[n.letter for n in self.neighbours]}"

    # Best for developers (Detailed & Unambiguous)
    def __repr__(self):
        return self.__str__()

    
def makeGraph(letterOptions):
    nodes=[]
    for i, letterOpt in enumerate(letterOptions):
        nodes.append(Node(letterOpt, i))
    for i, n in enumerate(nodes):
        n.neighbours = findsquaresNeighbours(i,nodes)
    return nodes


class Found:
    def __init__(self):
        self.allWordsFound = set()
        self.justWordsFound = set()



class PathSoFar:
    def __init__(self,wordSoFar,nodesVisidted, numsSoFar):
        self.wordSoFar =wordSoFar
        self.nodesVisited = nodesVisidted
        self.numsSoFar = numsSoFar


    # Best for end-users (Clean & Pretty)
    def __str__(self):
        return f"'{self.wordSoFar}' - {[n.letter for n in self.nodesVisited]}"


    # Best for developers (Detailed & Unambiguous)
    def __repr__(self):
        return self.__str__()




def findAllWordsFrom(node : Node, found, pathSoFar : PathSoFar):
    # we start at this node and do a 'depth first search' stopping whenever the letters formed so far can't make a word, also adding words to a list that we find along the way
    
    # start out with this letter
    
    wordSoFar = pathSoFar.wordSoFar +node.letter
    numsSoFar = pathSoFar.numsSoFar +node.position+"-"
    if (wordDictionary.isWord(wordSoFar)) and wordSoFar not in found.justWordsFound:
        found.allWordsFound.add(wordSoFar+" "+numsSoFar)
        found.justWordsFound.add(wordSoFar)
        
    # if we can go on, then nodesVisidted
    if (wordDictionary.canBeWord(wordSoFar)):
        # go over each neigbour and try again
        pathSoFar.nodesVisited.append(node)
        newPath =PathSoFar(wordSoFar,pathSoFar.nodesVisited.copy(), numsSoFar)
        for n in node.neighbours:
            if n not in pathSoFar.nodesVisited:
                findAllWordsFrom(n, found, newPath)


        pathSoFar.nodesVisited.pop()
    


def findAllWords(letterOptions):
    # turn into a graph for normal reasons
    graph = makeGraph(letterOptions)

    # now that we have a graphnodesVisidted
    allFound = Found()
  
    
    for n in graph:
        findAllWordsFrom(n, allFound,PathSoFar("",[],""))
    normalWordCount=0
                

   # print (allFound.allWordsFound)

    #Dealing with figuring out the real and bonus words stuff
    normalWords=[]
    with open("realWords.txt", 'r') as file:
        for line  in file:
            normalWords.append(line.strip())
    
    wordsForFile="\n"+letterOptions+" "
    bonusWords=""
    for word in allFound.allWordsFound:
        if word[:word.find(" ")] in normalWords:
            wordsForFile+=word+" "
            normalWordCount+=1
        else:
            bonusWords+=word+" "
    #adding them together
    wordsForFile+="BONUSWORD "+bonusWords+"X"
    print(str(normalWordCount)+" normal words")
    print(wordsForFile)
    #putting this into a file
    with open("wordsInPuzzle.txt", "a") as file:
        file.write(wordsForFile)

if __name__ == '__main__':
    letters=["ABCDEFGHIJKLMNOP","QWERTYUIOPLKJHGF","MNBVCXZASDFGHJKL","PGIMEUNRCTSAIONR","QWERTYUIO","ASDFTUIMNOEFUNTIONCYOMTUN","EREOPLEIOLNAMNFJ","PEOPLEISAWESOMER"]
    #for letter in letters:
    letters="PREIOSNTCAPEGNID" #141 Normal
    letters="QETHUUSIEAORBLNB" #96 Normal
    letters="RCUYBALLZINOYLMD" #61 Normal
    letters="ERTEZEESLEEBETRU" #42 Normal
    letters="QRECSUAKZZIGFINT" #43 Normal
    letters="BDHRFEAOGDLCUPIV" #74 Normal
    letters="CEGANOYPOGLOZOIB" #41 Normal
    letters="CKFDEHALPEECMESI" #64 Normal
    letters="HCSREAPYSNPMUSIL" #93 Normal
    letters="DNVLIEOIFCMPTYAC" #95 Normal
    letters="PIZMYPMOUMPYMHAP" #12 Normal
    letters="AAPHRSRTAGUAISAB" #55 Normal
    letters="CPTVCATAIROSHPMI" #95 Normal
    letters="KOHSNEEUDKSYYOGG" #47 Normal
    letters="HPOHOIPSHTPUUAML" #47 Normal
    letters="HPAPOOULBRCSICTE" #69 Normal
