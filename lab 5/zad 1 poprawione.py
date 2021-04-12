class Material():
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.ro=rodzaj
        self.d=dlugosc
        self.s=szerokosc
    def wyswietl_nazwe(self):
        return "rodzaj materiału to {} a jego dlugosc to {} ,oraz szerokosc {}".format(self.ro,self.d,self.s) 
class ubrania(Material):
    def __init__(self,kolor,dla_kogo,rozmiar,rodzaj,dlugosc,szerokosc): 
        Material.__init__(self,rodzaj,dlugosc,szerokosc)     
        self.k=kolor
        self.dl=dla_kogo
        self.r=rozmiar
    def wyswietl_dane(self):
        return "rodzaj to {} , dlugosc {},szerokosc{}, kolor{},dla kogo{} ,rozmiar{}".format(self.ro,self.d,self.s,self.k,self.dl,self.r)
class sweter(ubrania):
    def __init__(self,rodzaj_swetra):
        self.ro=rodzaj_swetra
    def wyswietl_danee(self):
        return "rodzaj swetra to {}".format(self.ro)
p=Material("skarpety",20,30)
d=ubrania("ruzofy","facet","M","skarpety",20,30)

g=sweter("golf")
print(p.wyswietl_nazwe())
print(d.wyswietl_dane())
print(g.wyswietl_danee())