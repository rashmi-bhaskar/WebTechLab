import cleanup
import preproc
import clusterlabel
import getCloud
import timeit
import csv
import json
import main_algo_merge

starttime = timeit.default_timer()

tweetid = 0
lastclusterid = 0

#top_n = int( input("Enter number of terms to be considered for cluster label : ") )
top_n = 3
towrite = []
wcloudlist = []


inputF = input("Enter name of dataset file : ")
#inputF = "dataset.csv"
r = csv.reader(open(inputF, encoding="utf8"))
entry = list(r)
entry.remove(entry[0])

features = cleanup.csvClean(entry)
features, hashlist = preproc.extractFeatures(features)                # the final features is a list of entries where entry[i][0] is the original
                                                            # tweet and entry[i][1] is a list of features (relevant words) of the tweet

# Calling the main_algo_merge.main_algo function
num_chunks = int(input("Enter number of chunks to be made : "))
chunksize = int(len(features)/num_chunks)
for i in range(num_chunks-1):
    clusterdict, fvecs, freqdict = main_algo_merge.main_algo( features[chunksize*i : chunksize*(i+1)], tweetid, lastclusterid, hashlist)
    for clusterid, tweetidlist in clusterdict.items():
        if( len(tweetidlist) > 1 ):
            clabel = clusterlabel.getClusterLabel(tweetidlist, fvecs, freqdict, top_n)
            wcloudlist += clabel
            loaded = [json.loads(item[0]) for item in towrite]
            
            merge_cluster = -1
            for c_index in range(len(loaded)):
                if clabel == loaded[c_index][1]:
                    merge_cluster = c_index
                    break

            if merge_cluster == -1:
                towrite.append([ json.dumps([clusterid, clabel, len(tweetidlist)]) ])
            else:
                towrite[c_index] = [ json.dumps([clusterid, clabel, loaded[merge_cluster][2] + len(tweetidlist)]) ]
            

clusterdict, fvecs, freqdict = main_algo_merge.main_algo( features[chunksize*(num_chunks-1):], tweetid, lastclusterid, hashlist)
for clusterid, tweetidlist in clusterdict.items():
    if( len(tweetidlist) > 1 ):
            clabel = clusterlabel.getClusterLabel(tweetidlist, fvecs, freqdict, top_n)
            wcloudlist += clabel
            loaded = [json.loads(item[0]) for item in towrite]
            
            merge_cluster = -1
            for c_index in range(len(loaded)):
                if clabel == loaded[c_index][1]:
                    merge_cluster = c_index
                    break

            if merge_cluster == -1:
                towrite.append([ json.dumps([clusterid, clabel, len(tweetidlist)]) ])
            else:
                towrite[c_index] = [ json.dumps([clusterid, clabel, loaded[merge_cluster][2] + len(tweetidlist)]) ]

# Storing clusters and displaying wordcloud and runtime
outfile = open('clusterdata2_merge.csv', 'w', newline='', encoding="utf8")
writer = csv.writer(outfile)
writer.writerows(towrite)
with open('wcloudtext.txt', 'w') as wcloudfile:
    for word in wcloudlist:
        wcloudfile.write("%s, " % word)
getCloud.wcloud('wcloudtext.txt')

# print("lastclusterid = ",lastclusterid)
# print("last tweetid = ",tweetid)


stoptime = timeit.default_timer()
print("Runtime is : ", int((stoptime - starttime)/60), " minutes, ", stoptime - starttime - 60 * int((stoptime - starttime)/60), " seconds." )