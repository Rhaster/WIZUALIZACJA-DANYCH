import numpy as np
def xd(n):
    h=np.zeros((n,n))
    g=0
    for x in range (n):
        for j in range(n):
            h[x][j]=g
            g+=1
    return h
print(xd(7))
