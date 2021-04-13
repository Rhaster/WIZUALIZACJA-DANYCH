def zlicza(xd):
    male=0
    duze=0
    for j in range(0,len(xd)):
        if xd[j].islower()==True:
            male+=1
        elif xd[j].isupper()==True:
            duze+=1
    print(duze)
    print(male)
    print(len(xd))
zlicza("MarioA")