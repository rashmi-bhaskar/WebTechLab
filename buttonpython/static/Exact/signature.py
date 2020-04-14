def getSign(feature_vector,randvecs,wordindexmap):
    sign = []
    for i in range(len(randvecs)):
        dotprod = 0
        for word_weight_pair in feature_vector.items():
            dotprod += randvecs[i][ wordindexmap[ word_weight_pair[0] ] ] * word_weight_pair[1]
        sign.append( int(dotprod>=0)  )
    
    return sign