import numpy as np
def fun(n):
    d=np.zeros(n)
    g=0
    for x in range(n,0,-1):
        d[g]=x
        g+=1
    print(d)
    p=np.zeros((n,n))
    for x in range(n):
        for j in range(n):
            if x==j:
                p[x][j]=d[x]
    print(p)       
fun(5)