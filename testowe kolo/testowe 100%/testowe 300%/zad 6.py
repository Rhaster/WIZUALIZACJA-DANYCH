def otwieracz():
    with open("NONIE.txt","r") as plik:
        t=plik.readlines()
    P=[int(x.strip())for x in t]
    P.sort()
    with open("Nonie.txt","w+") as xd:
        for x in range(len(P)):
            xd.write(str(P[x]))
            xd.write("\n")
otwieracz()