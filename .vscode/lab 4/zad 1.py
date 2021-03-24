lista=[]
for x in range (20):
    if x%4==0:
        lista.append(x)
plik=open("zad1111.txt","w")
plik.writelines(str(lista))
plik.close()