
def fixWordList():
    words=getFromFile("newWords.txt")
    realWords=getFromFile("allWords.txt")
    print("Got real words")
    finalWords=[]
    for word in words:
        word=word.upper()
        word=word.replace(";", "")
        if word in realWords:
            finalWords.append(word)
        else: print("error"+word)
    
    pushToFile(finalWords, "actualList.txt")


def pushToFile(words, fileName):
    #actually replacing the words
    with open(fileName, 'w') as file:
        file.writelines(words)

def getFromFile(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    return lines