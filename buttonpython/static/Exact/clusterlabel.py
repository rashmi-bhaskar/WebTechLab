def getClusterLabel(cluster, fvecs, freqdict, top_n):
    tempflist = []
    for tweet in cluster:
        for word in fvecs[tweet].keys():
            if not word in [pair[0] for pair in tempflist]:
                tempflist.append((word,freqdict[word]))

    tempflist.sort(reverse=True, key=lambda pair: pair[1])
    return [ pair[0] for pair in tempflist[:top_n] ]