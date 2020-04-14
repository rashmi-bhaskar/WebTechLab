import csv

num_chunks = 50
r = csv.reader(open('datafeatures.csv', encoding="utf8"))
entry = list(r)

entry.remove(entry[0])
for item in entry: 
    if (item==[]):
        entry.remove(item)

for i in range(len(entry)-1):
    entry[i] = entry[i][4].split('|')
    i = i + 1
chunksize = int(len(entry)/num_chunks)

chunkslist = []
for i in range(num_chunks-1):
    chunkslist.append( entry[chunksize*i : chunksize*(i+1)] )
chunkslist.append( entry[chunksize*(num_chunks-1):] )