import numpy as np
#stwórz liste z 20 * liczby 2 
def zad1():
    return np.arange(2,20*2+1,2)
def zad2():
    tab_float = np.arange(1,10, 0.2)
    tab_int = tab_float.astype('int64')
    print(tab_float)
    print(tab_int)
def zad3(a,b):
    t=np.zeros([a,b])
    c=1
    for x in range(a):
        for j in range (b):
            t[x][j]=c
            c+=1
    return t
def zad4(a,b):
    t=np.logspace(1,b,base=a,num=b)
    return t
def zad5(g):
    t=np.arange(g,0,-1)
    p=np.diag(t)
    print(p)
def zad6():
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
    return p
def zad7(n):
    macierz = np.diag([2 for t in range(n)])
    for x in range(1, n):
        vec = [2+(2*x) for t in range(n-x)]
        macierz += np.diag(vec, x)
        macierz += np.diag(vec, -x)
    print(macierz)
ad = np.arange(16).reshape((4, 4))
def zad8(arg,n):
    if(n==1):
        g=len(arg)
        print(g)
        y=int(g)
        t=int(g/2)
        if(g%2!=0):
            print("ilosc kolumn nie pozwala na operacje")
            return 0
        else:
            print(arg[0:t,0:y])
    elif(n==2):
        t=int(arg.shape[1])
        print(t)
        o=int(t/2)
        if(t%2!=0):
            print("ilosc wierszy nie pozwala na operacje")
            return 0
        else:
             print(arg[0:t,0:o])
ad = np.arange(16).reshape((4, 4))
def zad9():
    def recur_fibo(n):
        if n <= 1:
            return n
        else:
            return(recur_fibo(n-1) + recur_fibo(n-2))
    A=np.zeros((5,5),dtype=int)
    n=0
    for x in range(5):
        for j in range(5):
            A[x][j]=recur_fibo(n)
            n+=1
    return A
def zad21():
    a=np.arange(2,10,3)
    b=np.arange(1,4,1)
    t=a.dot(b)
    print(a)
    print(b)
    return t
def zad22():
    a=np.array([[2,3,4],[3,2,1],[4,7,8]])
    b=np.array([[2,3,1],[8,2,1],[1,9,8],[2,1,8]])
    print(a.min(axis=0))
    print(a.min(axis=1))
    print(b.min(axis=0))
    print(b.min(axis=1))
def zad23():
    a=np.arange(2,10,3)
    b=np.arange(1,4,1)
    t=a.dot(b)
print(zad22())