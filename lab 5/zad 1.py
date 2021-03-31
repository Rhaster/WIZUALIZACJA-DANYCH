class Material():
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.r=rodzaj
        self.d=dlugosc
        self.s=szerokosc
    def wyswietl_nazwe(self):
        return self.r  
class ubrania(Material):
    def __init__(self):
        self.kolor="zółty"
        self.dla_kogo="nikogo"
        self.rozmiar="M"
    def wyswietl_dane(self):
        return self.kolor,self.dla_kogo,self.rozmiar
class sweter(ubrania):
    def __init__(self):
        self.rodzaj_swetra="golf"
    def wyswietl_danee(self):
        return self.rodzaj_swetra
#d=ubrania(20,"zolty","helikopter m16")
#p=Material("skarpety",20,30)
g=sweter()
#print(p.wyswietl_nazwe())
#print(d.wyswietl_dane())
print(g.wyswietl_danevvvvvv())