import tfidf_single

def get_tfidf(entry):
    hashtagdict = {}
    for tweet in entry:
        for hashtag in tweet:
            if hashtag in hashtagdict:
                hashtagdict[hashtag] = hashtagdict[hashtag] + 1
            else:
                hashtagdict[hashtag] = 1

    N = len(entry)
    tfidflist = []
    for tweet in entry:
        feature_vector = tfidf_single.tfidf(tweet,N,hashtagdict)
        tfidflist.append( feature_vector )

    return tfidflist