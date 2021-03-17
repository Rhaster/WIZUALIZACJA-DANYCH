def ilo(*x):
    iloczyn=1
    for i in x:
        iloczyn*=i
    return iloczyn
print(ilo(1,2,3,4,5))