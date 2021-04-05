class Material():
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.r=rodzaj
        self.d=dlugosc
        self.s=szerokosc
    def wyswietl_nazwe(self):
        return self.r  
class ubrania(Material):
    def __init__(self,kolor,dla_kogo,rozmiar):
        self.k=kolor
        self.dl=dla_kogo
        self.r=rozmiar
    def wyswietl_dane(self):
        print(self.k,self.dl,self.r)
class sweter(ubrania):
    def __init__(self,rodzaj_swetra):
        self.ro=rodzaj_swetra
    def wyswietl_danee(self):
        return self.ro
d=ubrania(20,"zolty","helikopter m16")
p=Material("skarpety",20,30)
g=sweter("golf")
print(p.wyswietl_nazwe())
print(d.wyswietl_dane())
print(g.wyswietl_danee())