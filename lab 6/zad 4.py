import numpy as np
import math as m
def michaloddawajenergola(n,k):
    l = np.logspace(n, n**k, num=k,base=m.sqrt(n),dtype='int')
    return l
print(michaloddawajenergola(2,3))