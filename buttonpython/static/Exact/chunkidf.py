def dfdict(entry):
    worddict = {}
    for tweet in entry:
        for word in tweet[1]:
            if word in worddict:
                worddict[word] = worddict[word] + 1
            else:
                worddict[word] = 1
    return worddict