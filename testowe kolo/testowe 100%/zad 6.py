def gierczak():
    with open('os.txt.txt','r') as plik:
        t=plik.readlines()
    lisa=[int(x.strip()) for x in t]
    plik.close()
    print(lisa)
    lisa.sort()
    print(lisa)
    with open('os.txt.txt','w') as p:
        for x in range(len(t)):
            p.writelines(str(lisa[x]))
            p.writelines("\n")
    print(lisa)
gierczak()