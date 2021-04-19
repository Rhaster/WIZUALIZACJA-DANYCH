def funkcja(xd):
    ilemalych=0
    ileduzych=0
    for x in range(len(xd)):
        if xd[x].isupper()==True:
            ileduzych+=1
        elif xd[x].islower()==True:
            ilemalych+=1
    print(ilemalych)
    print(ileduzych)
funkcja("waleNIE")