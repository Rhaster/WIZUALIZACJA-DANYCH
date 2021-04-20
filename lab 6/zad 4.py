import numpy as np
def funkcja(n,k):
    l = np.logspace(1, k,num=k,base=n,dtype=int)
    print(l)
funkcja(2,5)