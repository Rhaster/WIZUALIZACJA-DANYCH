import numpy as np
def fib_rek(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib_rek(n - 1) + fib_rek(n - 2)
ad = np.zeros((5, 5),dtype=int)
g=0
print(ad)
for x in range(5):
    for j in range(5):
        ad[x][j]=fib_rek(g)
        g+=1
print(ad)
