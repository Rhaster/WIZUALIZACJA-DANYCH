class Ksztalty:
    def __init__(self, x, y):
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
        self.x =x
        self.y=x
    def __eq__(self, y):
        if self.x ==y.x:
            return " sa rowne"
        else:
            return "nie sa rowne"

    def __lt__(self, y):
        if self.x<y.x:
            return "pierwszy mniejszy"
        else:
            return "pierwszy nie mniejszy"

    def __gt__(self, y):
        if self.x>y.x:
            return "pierwszy  wiekszy"
        else:
            return "pierwszy   nie wiekszy "
    def __ge__(self,y):
        if self.x>=y.x:
            return "pierwszy wiekszy rowny"
        else:
            return "pierwszy nie wiekszy rowny"
    def __le__(self,y):
        if self.x<=y.x:
            return "pierwszy mniejszy lub rowny"
        else:
            return " pierwszy nie mniejszy lub rowny"
print("inicjujemy klasę Kwadrat")
figura = Kwadrat(5)
figa= Kwadrat(10)
print(figa<figura)
print(figura==figa)
print(figura>figa)
print(figura>=figa)
print(figa>=figura)
print(figa<=figura)
 

## __lt__(self, inny)
##__le__(self, inny)
##__eq__(self, inny)
##__ne__(self, inny)
##__gt__(self, inny)
##__ge__(self, inny)
##Dodano w wersji 2.1. Są to tzw. metody "porównań szczegółowych", a wywoływane są przy użyciu operatorów porównania przed wywołaniem opisanej poniżej metody __cmp__(). Zależność pomiędzy operatorami i nazwami metod przedstawia się następująco: x<y wywołuje x.__lt__(y), x<=y wywołuje x.__le__(y), x==y wywołuje x.__eq__(y), x!=y oraz x<>y wywołują x.__ne__(y), x>y wywołuje x.__gt__(y), x>=y wywołuje x.__ge__(y). Metody te mogą zwracać dowolne wartości, lecz jeśli operator porównania zostanie użyty w kontekście logicznym, zwracana wartość powinna dać się zinterpretować jako wartość logiczna, w przeciwnym bowiem wypadku wystąpi wyjątek TypeError. Zgodnie z konwencją False jest używane w znaczeniu fałszu, zaś True - w znaczeniu prawdy.
##Pomiędzy operatorami porównań nie występują żadne zależności mające charakter ogólny. Prawdziwość porównania x==y nie musi pociągać za sobą nieprawdziwości porównania x!=y. Analogicznie, przy definiowaniu metody __eq__ należy również zdefiniować __ne__, tak aby operatory zachowywały się w oczekiwany sposób.

##Nie istnieją osobne wersje powyższych metod z argumentami zamienionymi miejscami (używanymi, jeśli lewy argument nie obsługuje operacji, natomiast prawy ją obsługuje); jednak metody __lt__() i __gt__() stanowią wzajemnie swoje odwrócenie, podobnie jest z metodami __le__() i __ge__() oraz __eq__() i __ne__().

##Argumenty porównań szczegółowych nie są nigdy uzgadniane. Jeśli metoda porównania szczegółowego nie implementuje operacji dla podanej pary argumentów, może wygenerować wyjątek NotImplemented.