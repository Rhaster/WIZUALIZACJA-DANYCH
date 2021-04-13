def gierczak():
    with open('os.txt','r') as plik:
        t=plik.readlines()
    lisa=[int(x.strip()) for x in t]
    print(lisa)
gierczak()