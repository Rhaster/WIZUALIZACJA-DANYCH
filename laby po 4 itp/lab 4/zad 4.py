class NaZakupy():
    def __init__(self,nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.x=nazwa_produktu
        self.y=ilosc
        self.z=jednostka_miary
        self.k=cena_jed
    def wyświetl_produkt(self):
        return self.x, self.y, self.z, self.k
    def ile_produktu(self):
        return self.z,self.y
    def ile_kosztuje(self):
        return self.y*self.k
xd=NaZakupy("REDBUL",3,"LITRY",6)
print(xd.ile_produktu())
print(xd.ile_kosztuje())
print(xd.wyświetl_produkt())