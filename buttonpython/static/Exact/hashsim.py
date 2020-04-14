import math

def cosine_similarity(hashtag_vector_1,hashtag_vector_2):
    dotprod = 0
    sumx2 = 0

    for hashtag in hashtag_vector_1:
        sumx2 += hashtag_vector_1[hashtag]**2
        if(hashtag in hashtag_vector_2 and hashtag != 'womensmarch'):
            dotprod += hashtag_vector_1[hashtag] * hashtag_vector_2[hashtag]

    sumy2 = 0
    for hashtag in hashtag_vector_2:
        sumy2 += hashtag_vector_2[hashtag]**2

    try:
        return dotprod/math.sqrt(sumx2*sumy2)
    except:
        return 0
    
def jaccard_similarity(hashtag_vector_1, hashtag_vector_2):
    intersection = 0
    for hashtag in hashtag_vector_1:
        if(hashtag in hashtag_vector_2 and hashtag != 'womensmarch'):
            intersection += 1
    try:
        return intersection/(len(hashtag_vector_1) + len(hashtag_vector_2) - intersection )
    except:
        return 0