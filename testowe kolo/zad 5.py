def slownik(slowo):
    count=0
    slown={}
    for x in slowo:
        d=slowo.count(x)
        slown[x]=d
    print(slown)
x="goha"
slownik(x)

