def slownik(xd):
    slowo={}
    for x in xd:
        g=xd.count(x)
        slowo[x]=g
    print(slowo)
slownik("goha")