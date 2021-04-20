import numpy as np
def funkcja (arg,n):
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
print(ad)
print("podaj kierunek 1 to poziom , 2 to pion")
funkcja(ad,2)