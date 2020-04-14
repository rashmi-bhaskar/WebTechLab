import csv
import json
import similarity


# for clusterdata.csv
r = csv.reader(open('clusterdata.csv', encoding='utf8'))
rlist = list(r)
clusterdict = {}
for i in range(len(rlist)):
    pair = json.loads(rlist[i][0])
    clusterdict[pair[0]] = pair[1]

None        # for breakpoint


# for clusterdata2.csv
r = csv.reader(open('clusterdata2.csv', encoding='utf8'))
clusterlist = list(r)
for i in range(len(clusterlist)):
    clusterlist[i] = json.loads(clusterlist[i][0])

# Testing similarity of tweets in a cluster
r = csv.reader(open('tfidfdata.csv', encoding='utf8'))
fvecs = list(r)
for i in range(len(fvecs)):
    fvecs[i] = json.loads(fvecs[i][0])

#clusterid = int(input("Enter id of the cluster to be tested : ") )
clusterid = 23
simlist = [similarity.cosine_similarity(fvecs[tweetid1],fvecs[tweetid2]) for tweetid1 in clusterdict[clusterid] for tweetid2 in clusterdict[clusterid] if tweetid1 != tweetid2]

false_positives = 0
for sim in simlist:
    if sim<0.2:
        false_positives += 1

print(false_positives, false_positives/len(simlist))
