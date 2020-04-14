def getNN(sign,P):                          # returns a pair of (list at key which is at minimum hamming distance from sign,
    if( len(P[sign]) > 1 ) :                #                    and that hamming distance)
        return (P[sign],0)
    elif ( P.has_key( sign[:-1] + [int(not sign[-1])] ) ):
        return ( P[ sign[:-1] + [int(not sign[-1])] ], 1)
    else:
        i = 2
        while( i < len(sign) ):
            if ( P.has_subtrie( sign[:-1*i] + [int(not sign[-1*i])] ) ):
                return ( P.items(prefix = sign[:-1*i] + [int(not sign[-1*i])]), i )
            i = i + 1
        return (None,None)