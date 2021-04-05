class Ksztalty:
    # definicja konstruktora
    def __init__(self, x, y):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik
class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self,kwadrat):
        return self.x+kwadrat.x

kw = Kwadrat(5)
kw1=Kwadrat(2)
print(kw+kw1)