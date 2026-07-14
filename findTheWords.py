
def fixWordList():
    words=getFromFile("realWords.txt")
    realWords=getFromFile("allWords.txt")
    print("Got real words")
    bonusWords=[]
    for word in realWords:
        if word not in words:
            bonusWords.append(word)
    
    pushToFile(bonusWords, "bonusWords.txt")


def pushToFile(words, fileName):
    #actually replacing the words
    with open(fileName, 'w') as file:
        file.writelines(words)

def getFromFile(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    return lines