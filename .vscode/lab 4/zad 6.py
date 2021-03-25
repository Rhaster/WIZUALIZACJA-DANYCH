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
d=slowa("mata","tama")
print(d.sprawdz_czy_palindrom())
print(d.sprawdz_czy_anagramy())