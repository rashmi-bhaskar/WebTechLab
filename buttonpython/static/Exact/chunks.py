import csv

def getChunks(inputFile, num_chunks):
    r = csv.reader(open(inputFile, encoding="utf8"))
    entry = list(r)

    for i in range(len(entry)-1):
        entry[i] = entry[i][4].split('|')
        i = i + 1
    chunksize = int(len(entry)/num_chunks)
    
    chunkslist = []
    for i in range(num_chunks-1):
        chunkslist.append( entry[chunksize*i : chunksize*(i+1)] )
    chunkslist.append( entry[chunksize*(num_chunks-1):] )

    return chunkslist