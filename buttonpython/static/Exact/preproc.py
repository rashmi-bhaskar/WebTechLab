import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from autocorrect import spell

stop_words = set(stopwords.words('english'))

def stopword(tweet):
    tokens = word_tokenize(tweet)
    newTokens = [token for token in tokens if not token in stop_words]
    return newTokens

def postag(tweet):
    tokens = stopword(tweet)
    posTokens = nltk.pos_tag(tokens)
    return posTokens

def extractFeatures(entry):
    j = 0
    ps = PorterStemmer()
    hashlist = []
    while j < len(entry):
        features = postag(entry[j][0])
        featureVector = []
        featurenum = 0
        while featurenum < len(features) :            
            if features[featurenum][1] == 'NN' or features[featurenum][1] == 'NNS' or features[featurenum][1] == 'NNP' or features[featurenum][1] == 'NNPS' or features[featurenum][1] == 'VB' or features[featurenum][1] == 'VBD' or features[featurenum][1] == 'VBG' or features[featurenum][1] == 'VBN' or features[featurenum][1] == 'VBP' or features[featurenum][1] == 'VBZ':
                if features[featurenum][0].isalpha():
                    n = ps.stem(features[featurenum][0])
                    featureVector.append(n) 
            featurenum += 1

        hashtags = []
        for word in entry[j][0].split():
            if word[0] == '#':
                hashtags.append(word[1:])

        hashlist.append( hashtags )
        entry[j].append(featureVector)
        j = j + 1
    return entry, hashlist