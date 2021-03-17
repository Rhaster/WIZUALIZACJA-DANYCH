print("nie dziala bez numpy ;d ")
import numpy as np
import random
count=0
def incr():
     global count
     count += 1
random.seed()
A = np.zeros((4,4)) #
for x in range(0,4):
    for j in range(0,4):
        d=random.randint(0,9)
        A[x][j]=d
print (':D', A)
d=[incr() or row[x] for row in A for x in range(count,4,4)]
print(d)