import random
def testowe(ile,*cos):
    wynik=0
    for x in range(ile):
        g=random.randrange(*cos)
        wynik+=g
        print(g)
    print(wynik)
    print(wynik/ile)
testowe(5,10,30)