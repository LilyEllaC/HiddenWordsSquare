
def fixWordList():
    realWords=getFromFile("bonusWords.txt")
    newRealWords=[]    
    for word in realWords:
        if len(word)<=4:
            print("Too short: "+word)
        else:
            newRealWords.append(word)
    
    pushToFile(newRealWords, "bonusWords.txt")


def pushToFile(words, fileName):
    #actually replacing the words
    with open(fileName, 'w') as file:
        file.writelines(words)

def getFromFile(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    return lines