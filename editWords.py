if __name__ == '__main__':
    words=[]
    allWords=[]
    fixedWords=[]
    count=0
    with open("100Words.txt", 'r') as file:
        for line  in file:
            word=line[:line.find(" ")]
            words.append(word.upper())
    with open("allWords.txt", 'r') as file:
        for line  in file:
            allWords.append(line.strip())

    for word in words:
        if len(word)>=4:
            if word in allWords:
                fixedWords.append(word+"\n")
                count+=1
        if count>50000:
            break
    
    with open("100Words.txt", "w") as file:
        file.writelines(fixedWords)
