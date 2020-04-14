import math

def cosine_similarity(feature_vector_1,feature_vector_2):
    dotprod = 0
    sumx2 = 0

    for feature in feature_vector_1:
        sumx2 += feature_vector_1[feature]**2
        if(feature in feature_vector_2):
            dotprod += feature_vector_1[feature] * feature_vector_2[feature]

    sumy2 = 0
    for feature in feature_vector_2:
        sumy2 += feature_vector_2[feature]**2

    try:
        return dotprod/math.sqrt(sumx2*sumy2)
    except:
        return 0
    