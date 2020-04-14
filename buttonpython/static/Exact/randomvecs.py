import random

def getVecs(dims,n):                # dims - dimensionality of the random vector 
    vecs = []                       # n - number of random vectors
    for i in range(n):
        temp = []
        for j in range(dims):
            temp.append(random.gauss(0,1))
        vecs.append(temp)
    return vecs