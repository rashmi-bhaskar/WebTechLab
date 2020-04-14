import cleanup
import preproc
import tfidf_all
import randomvecs
import signature
import csv
import json
import idf
import random
import pygtrie
import nearest_neighbor
import similarity
import clusterlabel
import getCloud
import timeit
import tfidf_hash
import hashsim

starttime = timeit.default_timer()


def main_algo(features, tweetid, lastclusterid, hashlist) :

    fvecs,freqdict = tfidf_all.get_tfidf_freqdict(features)     
    # hashvecs = tfidf_hash.get_tfidf(hashlist)

    hashnum = 0
    for hashtags in hashlist:
        hashnum += len( [hashtag for hashtag in hashtags if hashtag != 'womensmarch'] )
    print('Average number of hashtags (excluding womensmarch) = ', hashnum/len(hashlist) )

    # Creating random vectors
    num_randvecs = 13
    random_vectors = randomvecs.getVecs(len(freqdict), num_randvecs)


    # Initialising prefix trees
    a = []
    b = []
    prime = 13
    P = []
    # modP = int(input("Enter number of permutations to be used : "))
    modP = 20
    for i in range(modP):
        atemp = random.uniform(1,prime)
        btemp = random.uniform(0,prime)
        a.append(atemp)
        b.append(btemp)
        P.append(pygtrie.Trie())

    index = 0
    wordindexmap = {}
    for key in  freqdict.keys():
        wordindexmap[key] = index 
        index = index + 1

    # MAIN TWEET LOOP
    
    tweetclustermap = {}
    clusterdict = {}
    fvecnum = 0
    for fvec in fvecs:
        tweetsign = signature.getSign(fvec,random_vectors,wordindexmap)

        # Insert tweet signature in prefix tree and find its nearest neighbor in that tree
        nearestNeighbours = []
        for i in range(modP):
            signPerm = [None]*len(tweetsign)
            for x in range(len(tweetsign)):
                ind = int(a[i]*x+b[i])%prime
                signPerm[x] = tweetsign[ind]

            if P[i].has_key(signPerm) :
                P[i][signPerm].append(tweetid)
            else :
                P[i][signPerm] = [tweetid]

            neighbor,hdist = nearest_neighbor.getNN( signPerm, P[i] )

            if (neighbor == None) : None
            elif hdist == 0:
                neighbor.remove(tweetid)
                nearestNeighbours.append( (neighbor,hdist) )
            elif hdist == 1:
                nearestNeighbours.append( (neighbor,hdist) )
            elif (hdist > 1):
                templist = []
                for item in neighbor:
                    templist += item[1]
                nearestNeighbours.append( (templist,hdist) )

        mindist = len(signPerm) + 10
        closestNeighbors = []
        for pair in nearestNeighbours:
            if pair[1] <= mindist:
                mindist = pair[1]
        
        for pair in nearestNeighbours :
            if pair[1] == mindist:
                for i in range( len(pair[0]) ):
                    if not pair[0][i] in closestNeighbors:
                        closestNeighbors.append(pair[0][i])


        # T = float(input("Enter the similarity threshold : "))
        T = 0.05
        #hashtag_csim_T = 0.05
        hashtag_jsim_T = 0.5
        tweetclustermap[0] = 0
        clusterdict[0] = [0]
        for cneighbor in closestNeighbors:
            if(similarity.cosine_similarity(fvec,fvecs[cneighbor]) >= T or hashsim.jaccard_similarity(hashlist[tweetid],hashlist[cneighbor]) >= hashtag_jsim_T):
                if( tweetid in tweetclustermap.keys() ):
                    if not ( tweetclustermap[tweetid] == tweetclustermap[cneighbor] ) :
                        tweetclustermap[tweetid] = tweetclustermap[cneighbor]
                        clusterdict[ tweetclustermap[cneighbor] ].append(tweetid)
                else :
                    tweetclustermap[tweetid] = tweetclustermap[cneighbor]
                    clusterdict[ tweetclustermap[cneighbor] ].append(tweetid)
            else:
                if not (tweetid in tweetclustermap.keys()) :
                    tweetclustermap[tweetid] = lastclusterid + 1
                    clusterdict[lastclusterid + 1] = [tweetid]
                    lastclusterid += 1

        fvecnum += 1
        tweetid += 1
    return clusterdict, fvecs, freqdict




## EQUIVALENT OF MAIN FUNCTION

ccount = 0
tweetid = 0
lastclusterid = 0

#top_n = int( input("Enter number of terms to be considered for cluster label : ") )
top_n = 3
towrite = []
wcloudlist = []


# USE THE 6 LINES BELOW FOR A NEW DATASET OR THE 7 LINES BELOW THAT FOR PRECALCULATED FEATURES:

#inputF = input("Enter name of dataset file : ")
inputF = "dataset.csv"
r = csv.reader(open(inputF, encoding="utf8"))
entry = list(r)
entry.remove(entry[0])

features = cleanup.csvClean(entry)
features, hashlist = preproc.extractFeatures(features)                # the final features is a list of entries where entry[i][0] is the original
                                                            # tweet and entry[i][1] is a list of features (relevant words) of the tweet

# with open("datafeatures.csv",encoding="utf8") as infile:
#     r = csv.reader(infile)
#     tempfeatures = list(r)
# tempfeatures.remove(tempfeatures[0])
# 
# features = []
# for i in range(len(tempfeatures)):
#     features.append([tempfeatures[i][1], tempfeatures[i][4].split('|')])

# Calling the main_algo function
num_chunks = int(input("Enter number of chunks to be made : "))
chunksize = int(len(features)/num_chunks)
for i in range(num_chunks-1):
    clusterdict, fvecs, freqdict = main_algo( features[chunksize*i : chunksize*(i+1)], tweetid, lastclusterid, hashlist)
    ccount += len(clusterdict)
    for clusterid, tweetidlist in clusterdict.items():
        if( len(tweetidlist) > 10 ):
            clabel = clusterlabel.getClusterLabel(tweetidlist, fvecs, freqdict, top_n)
            towrite.append([ json.dumps([clusterid, clabel, len(tweetidlist)]) ])
            wcloudlist += clabel

clusterdict, fvecs, freqdict = main_algo( features[chunksize*(num_chunks-1):], tweetid, lastclusterid, hashlist)
ccount += len(clusterdict)
for clusterid, tweetidlist in clusterdict.items():
    if( len(tweetidlist) > 10 ):
        clabel = clusterlabel.getClusterLabel(tweetidlist, fvecs, freqdict, top_n)
        towrite.append([ json.dumps([clusterid, clabel, len(tweetidlist)]) ])
        wcloudlist += clabel

# Storing clusters and displaying wordcloud and runtime
outfile = open('clusterdata2_hashtags.csv', 'w', newline='', encoding="utf8")
writer = csv.writer(outfile)
writer.writerows(towrite)

with open('wcloudtext.txt', 'w') as wcloudfile:
    for word in wcloudlist:
        wcloudfile.write("%s, " % word)
getCloud.wcloud('wcloudtext.txt')

print("Total number of clusters is : ", ccount)

stoptime = timeit.default_timer()
print("Runtime is : ", int((stoptime - starttime)/60), " minutes, ", stoptime - starttime - 60 * int((stoptime - starttime)/60), " seconds." )