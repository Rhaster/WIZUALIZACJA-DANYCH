import numpy as np
p=np.zeros((5,5) ,dtype=object)
a="abcdefgcyeutueretydeabcde"
q=0
for x in range(5):
    for j in range(5):
        p[x][j]=a[q]
        q+=1
h="pies"
d="kot"
t="kiwi"
i=3
g=0
u=2
for x in range(5):
    for j in range(5):
        if x==j and g<=3 and x>0:
            p[x][j]=h[g]
            g+=1
        elif u<=2 and u>=0:
            p[4][j]=d[u]
            u-=1
        elif  j==4 and i>=0:
            p[x][4]=t[i]
            i-=1
print(p)