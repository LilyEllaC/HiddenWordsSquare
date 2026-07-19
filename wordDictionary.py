import pygtrie



def getFromFile(fileName="allWords.txt"):
    t = pygtrie.CharTrie()

    with open(fileName, 'r') as file:
        for line  in file:
            t[line.strip()]= True
    return t
allWords = getFromFile()


def isWord(str):
    #return True
    return allWords.has_key(str)


def canBeWord(str):
    # return if this begining of a word can ever be a word (i.e. are there any words that beging with unde)
    #  so unde woudl be true because of under but zzx would be false I hope
    # placeholder all 4 letter words are words
    #return True
    return allWords.has_node(str)>0




if __name__ == '__main__':
    # testing of our tri stuff
    for testword in ["book","bsof3ok" ]:
        print(testword+ " is a word "+   str(  isWord(testword.upper())))

    for testStartsword in ["book","bsof3ok","able","zz","zyz" ]:
        print(testStartsword+ " can be a word "+   str(  canBeWord(testStartsword.upper())))
