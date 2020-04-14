import similarity
import csv
import json
import random

r = csv.reader(open('tfidfdata.csv', encoding='utf8'))
fvecs = list(r)
for i in range(len(fvecs)):
    fvecs[i] = json.loads(fvecs[i][0])

count = 1
topsims = []
while(count>0):
    tweetid = int(random.uniform(0,len(fvecs)))
    simlist = []
    for i in range(len(fvecs)):
        simlist.append( (similarity.cosine_similarity( fvecs[tweetid], fvecs[i] ), (tweetid,i) ) )
    simlist.sort(reverse = True)
    topsims.append(simlist[:50])
    count -= 1

print(topsims)      # Stores top 5 similarities and the pairs for which this similarity is obtained, for 10 tweets