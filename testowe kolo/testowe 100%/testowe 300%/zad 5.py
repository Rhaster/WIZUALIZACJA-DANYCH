def xd (cos):
    slownik={}
    for x in cos:
        g=cos.count(str(x))
        slownik[x]=g
    return slownik
print(xd("Walenie"))