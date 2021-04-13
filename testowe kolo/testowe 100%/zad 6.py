def gierczak():
    with open('os.txt.txt','r') as plik:
        t=plik.readlines()
    lisa=[int(x.strip()) for x in t]
    plik.close()
    print(lisa)
    lisa.sort()
    print(lisa)
gierczak()