def gier(a=(input("podaj zdanie "))):
    g=input("podaj nazwe pliku do zapisu")
    with open(g,"a") as d:
        N=a.replace(".","").replace(",","").split(" ")
        g=N
        y=len(N)
        cos=0
        print(y)
        print(g)
        N.pop(0)
        for x in g:
            for j in N:
                if x==j:
                    g.remove(x)
                    cos+=1
        print(g)
        for x in range(0,(y-1)-cos):
            d.writelines(g[x])
            d.writelines("\n")
        print(g)
gier()