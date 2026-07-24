


allWords= None
def getFromFile(fileName="allWords.txt"):
    import pygtrie

    t = pygtrie.CharTrie()

    with open(fileName, 'r') as file:
        for line  in file:
            t[line.strip()]= True
    return t

def getAllWords():
    global allWords
    if allWords==None:
        allWords=getFromFile()
    return allWords


def isWord(string):
    return getAllWords().has_key(string)


def canBeWord(string):
    return getAllWords().has_node(string)>0




if __name__ == '__main__':
    # testing of our tri stuff
    for testword in ["book","bsof3ok" ]:
        print(testword+ " is a word "+   str(  isWord(testword.upper())))

    for testStartsword in ["book","bsof3ok","able","zz","zyz" ]:
        print(testStartsword+ " can be a word "+   str(  canBeWord(testStartsword.upper())))
