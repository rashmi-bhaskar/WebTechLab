import math

def tf(word, tweet):
    count = 0
    for feature in tweet:
        if feature == word:
            count = count + 1
    return count

def tfidf(tweet,N,fredict):
    feature_vector = {}
    for word in tweet:
        if (not (word in feature_vector) ):
            tfval = tf(word,tweet)
            idfval = math.log10(N/fredict[word])
            feature_vector[word] = tfval*idfval
    return feature_vector