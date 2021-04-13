def funkcja(a):
    ilemalych=0
    ileduzych=0
    for j in range(len(a)):
        if a[j].isupper()==True:
            ileduzych+=1
        elif a[j].islower()==True:
            ilemalych+=1
    print(ilemalych)
    print(ileduzych)
funkcja("dasdaDDA")
