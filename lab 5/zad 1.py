 
class Material():
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.ro=rodzaj
        self.d=dlugosc
        self.s=szerokosc
    def wyswietl_nazwe(self):
        return self.ro  
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
d=ubrania("Polipropylen","20cm","40cm")
p=Material("skarpety",20,30)
g=sweter("golf")
print(p.wyswietl_nazwe())
print(d.wyswietl_dane())
print(g.wyswietl_danee())