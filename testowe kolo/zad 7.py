import random
def xd(ile,*przedzial):
    wynik=0
    for x in range(ile):
        g=random.randrange(przedzial[0],przedzial[1])
        print(g)
        wynik+=g
    print(wynik)
    print(wynik/ile)
xd(4,1,10)