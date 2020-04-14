import tfidfsimilarity
import idf
import csv

finalF = "datafeatures.csv"
r = csv.reader(open(finalF, encoding="utf8"))
entry = list(r)

fredict = idf.dfdict(finalF)
print('Lets find the cosine similarity between two tweets.')
tweet1 = int(input('Enter tweet ID of 1st tweet : '))
tweet2 = int(input('Enter tweet ID of 2nd tweet : '))

m,n = tfidfsimilarity.tfidf( list(entry[tweet1][4].split("|")), list(entry[tweet2][4].split("|")), fredict, len(entry) )

sim = tfidfsimilarity.similar(m,n)
print('The similarity measure between tweet '+str(tweet1)+' and tweet '+str(tweet2)+' is '+str(sim))