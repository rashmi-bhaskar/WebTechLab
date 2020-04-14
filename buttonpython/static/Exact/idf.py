import csv

def dfdict(entry):   
    worddict = {}
    for i in range(len(entry)):
        l = list(entry[i][1].split("|"))
        for word in l:
            if word in worddict:
                worddict[word] = worddict[word] + 1
            else:
                worddict[word] = 1
    return worddict