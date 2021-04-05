class slowa():
    def __init__(self,slowo1,slowo2):
        self.a=slowo1
        self.b=slowo2
    def sprawdz_czy_palindrom(self):
        return self.a == self.a[::-1], self.b == self.b[::-1]
    def sprawdz_czy_anagramy(self):
        if sorted(self.b) == sorted(self.a):
            print("sa to angramy")
        else:
            print("nie sa ")
    def sprawdz_czy_metagramy(self):
        g=0
        for x in range(0,len(self.a)):
            if self.a[x]!=self.b[x]:
                g+=1
        if g==1:
            print("sa to metagramy")
        else:
            print("nie sa to metagramy")
        print(g)
    def wyświetl_wyrazy(self):
        print(self.a,self.b)
d=slowa("gama","gata")
print(d.sprawdz_czy_palindrom())
print(d.sprawdz_czy_anagramy())
print(d.sprawdz_czy_metagramy())
print(d.wyświetl_wyrazy())