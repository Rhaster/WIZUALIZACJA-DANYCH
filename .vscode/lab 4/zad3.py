with open("zad3333.txt", "w+") as plik:
    for x in range(2,40,1):
        plik.write(str(x))
        plik.write("\n")
with open("zad3333.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")