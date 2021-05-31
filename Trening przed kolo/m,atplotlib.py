import matplotlib .pyplot as plt
import numpy as np
import pandas as pd

##Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20]. Dodaj etykietę do linii wykresu i wyświetl legendę.
## Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’) or
def zad1():
    x = np.arange(1, 20)
    y = [1 / i for i in x]
    plt.plot(x, y, label='f(x) = 1/x')
    plt.axis([ 0, 20, 0, 1 ])

    # etykiety osi
    plt.xlabel('x')
    plt.ylabel('f(x)')

    # tytuł wykresu
    plt.title("Prosty wykres")

    # włączamy pokazywanie legendy
    plt.legend()
    plt.show()

## 2 Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak na poniższym zrzucie ekranu.
def zad2():
    x = np.arange(1, 20)
    y = [ 1 / i for i in x ]
    plt.plot(x, y, 'g>:', label='f(x) = 1/x', )
    plt.axis([ 0, 20, 0, 1 ])

    # etykiety osi
    plt.xlabel('x')
    plt.ylabel('f(x)')

    # tytuł wykresu
    plt.title("Wykres funkcji f(x) dla x [1, 20]")

    # włączamy pokazywanie legendy
    plt.legend()
    plt.show()

## 3 Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ϵ [0, 30] z krokiem 0.1. Dodaj etykiety i legendę do wykresu.
def zad3():
    x = np.arange(0, 30, 0.1)
    s = np.sin(x)
    plt.plot(x, s, label='sin(x)')

    # etykiety osi
    plt.xlabel('x')
    plt.ylabel('sin(x)')

    # tytuł wykresu
    plt.title("Wykres sin(x)")

    # włączamy pokazywanie legendy
    plt.legend()
    plt.show()

## 4 Dodaj drugi wykres funkcji sinus do zadania 3 i zmodyfikuj parametry funkcji, tak aby osiągnąć efekt podobny do tego na poniższym zrzucie ekranu.
def zad4():
    x = np.arange(0, 30, 0.1)
    s = 2 + np.sin(x)
    c = np.sin(np.pi + x)
    plt.plot(x, s, label='sin(x)')
    plt.plot(x, c, label='sin(x)')

    # etykiety osi
    plt.xlabel('x')
    plt.ylabel('sin(x)')

    # tytuł wykresu
    plt.title("Wykres sin(x), sin(x)")

    # włączamy pokazywanie legendy
    plt.legend()
    plt.show()

## 5 Korzystając ze zbioru danych Iris (https://archive.ics.uci.edu/ml/datasets/iris) wygeneruj wykres punktowy, gdzie wektor x to wartość ‘sepal length’ a y to ‘sepal width’, 
def zad5():
    df = pd.read_csv('iris.data', delimiter=',', header=None)

    # przygotowanie wektora kolorów
    colors = np.random.randint(0, 50, len(df.index))
    # przygotowanie wektora z rozmiarami 'kropek'
    scale = [np.abs(df[0].iloc[x] - df[1].iloc[x]) for x in range(len(df.index))]
    # można te wielkości troszeczkę 'podrasować'
    scale = [np.abs(df[0].iloc[x] - df[1].iloc[x])*5 for x in range(len(df.index))]

    plt.scatter(df[0], df[1], c=colors, s=scale)
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    plt.show()

## 6 Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci przedstawiony w lekcji 8. Następnie na jednym płótnie wyświetl 3 wykresy (jeden wiersz i 3 kolumny). Dodaj do wykresów stosowne etykiety. Poustawiaj różne kolory dla wykresów.
## 1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym okresie.
## 2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet, druga dla mężczyzn dla każdego roku z osobna. Czyli y to ilość narodzonych kobiet lub mężczyzn (dwie linie), x to rok.
## 3 wykres – wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku.
def zad6():
    xlsx = pd.ExcelFile('Imiona.xlsx')
    df = pd.read_excel(xlsx, 'Arkusz1')

    # wykres 1
    plt.subplot(1, 3, 1)
    grouped = df.groupby('Plec').agg({'Liczba': ['sum']}).unstack()
    grouped.plot.bar(color=['r', 'g'])
    plt.xlabel('Płeć')

    # wykres 2
    plt.subplot(1, 3, 2)
    x = df['Rok'].unique()
    kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
    mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
    plt.plot(x, kobiety, label="Kobiety")
    plt.plot(x, mezczyzni, label="Mężczyźni")
    plt.ylabel('Liczba narodzonych dzieci')

    # wykres 3
    plt.subplot(1, 3, 3)
    x = df['Rok'].unique()
    # bez funkcji flatten matplotlib wyrzuca wyjątek, który informuje nas, że nie można
    # przekazywać parametru jako tablicy wielowymiarowej a w takiej postaci w tym przypadku
    # zwracany jest wektor y, korzystamy więc z flatten() poznanej przy okazji omawiania biblioteki numpy
    y = df.groupby('Rok').agg({'Liczba':['sum']}).values.flatten()
    plt.bar(x, y)

    # wyświetlamy cały wykres
    plt.show()

## 7 Korzystając z tutoriala pod adresem https://towardsdatascience.com/matplotlib-tutorial-learn-basics-of-pythons-powerful-plotting-library-b5d1b8f67596 lub
##  innego zmodyfikuj wykres 2 z zadania 6 tak, aby zamiast 
## wykresu liniowego przedstawiał wykres łupkowy skumulowany (czyli jeden słupek dla kobiet i mężczyzn, ale składający się z dwóch „nałożonych” na siebie słupków)
def zad7():
    xlsx = pd.ExcelFile('Najpopularniejsze-imiona-w-Polsce-w-latach-2000-2017.xlsx')
    df = pd.read_excel(xlsx, 'Arkusz1')

    # wykres 2
    x = df['Rok'].unique()
    kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba': ['sum']}).values.flatten()
    mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba': ['sum']}).values.flatten()
    plt.bar(x, kobiety, label="Kobiety")
    plt.bar(x, mezczyzni, label="Mężczyźni", bottom=kobiety)
    # tiki osi x co drugi rok
    plt.xticks(x[::2])
    plt.ylabel('Liczba narodzonych dzieci')
    plt.xlabel('Rok')
    plt.legend()
    plt.show()

## 8 Napisz funkcję, która losowo rzuca dwiema kostkami k6 n razy. Wynik rzutów zapisywany jest w postaci listy sum oczek z tych dwóch kostek. Np.
##  rzucaj(6) generuje 6 rzutów kostkami i zwraca wektor 6 sum oczek każdego rzutu. 
## Po zakończeniu funkcji wyświetlaj histogram sumy rzutów. Dodaj stosowne etykiety do wykresu.
def zad8():
    def rzucaj(n):
        k1 = np.random.randint(1, 7, n)
        k2 = np.random.randint(1, 7, n)
        suma = k1 + k2
        return suma

    n = 1000

    plt.hist(rzucaj(n), bins=10, density=True)
    plt.ylabel('Prawdopodobieństwo')
    plt.xlabel('suma oczek')
    plt.title(f'Rozkład prawdopodobieństwa \ndla sumy oczek dwóch kostek K6 dla {n} prób')
    plt.show()

##Korzystając z pliku zamówienia.csv (Pandas) policz sumy zamówień dla każdego przedawcy i wyświetl wykres kołowy z procentowym udziałem każdego 
# sprzedawcy w ogólnej sumie zamówień. Poszukaj w Internecie jak dodać cień do takiego wykresu i jak działa atrybut ‘explode’ tego wykresu.
#  Przetestuj ten atrybut na wykresie.
def zad9():
    df = pd.read_csv('zamowienia.csv', delimiter=';')
    policzone = df.groupby('Sprzedawca')['Utarg'].sum()
    # explode
    explode = [0.0 for n in range(len(policzone.index))]
    # określamy które kawałki i o ile wysunąć, tu losujemy jeden
    explode[np.random.randint(0, len(policzone.index)+1)] = 0.2
    policzone.plot.pie(subplots=True, autopct='%.2f % %', fontsize=8, explode=explode, shadow=True)
    plt.title("Procentowy udział kwot zamówień sprzedawców")
    plt.show()

## adnotacje 
def zad10():
    # adnotacje do wykresu z zadania 7

    xlsx = pd.ExcelFile('Imiona.xlsx')
    df = pd.read_excel(xlsx, 'Arkusz1')

    x = df['Rok'].unique()
    kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba': ['sum']}).values.flatten()
    mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba': ['sum']}).values.flatten()
    ax1 = plt.bar(x, kobiety, label="Kobiety")
    ax2 = plt.bar(x, mezczyzni, label="Mężczyźni", bottom=kobiety)
    # dodamy adnotację do najwyższego słupka wykresu
    # na początek rozszerzymy nieco skalę osi Y, żeby adnotacja się zmieściła
    # ylim() zwraca krotkę wartości skali (bottom, top) więc możemy najpierw ją pobrać
    # a później jeżeli przekazujemy wartości dla funkcji ylim(bottom, top) to ustawiamy te wartości
    plt.ylim(plt.ylim()[0], plt.ylim()[1]*1.2)
    # teraz trzeba zlokalizować najwyższy słupek, co przy skumulowanym wykresie nie jest już tak łatwe
    # ax1 oraz ax2 to odpowiednio serie słupków dla kobiet i mężczyzn
    wys_slupkow_ax1 = np.array([p.get_height() for p in ax1.patches])
    wys_slupkow_ax2 = np.array([p.get_height() for p in ax2.patches])
    suma_wysokosci = wys_slupkow_ax1 + wys_slupkow_ax2
    # teraz trzeba zlokalizować, który to słupek
    slupek_index = np.where(suma_wysokosci == max(suma_wysokosci))[0][0]
    # następnie pobierając parametry słupka o danym indeksie możemy dodać adnotację do wykresu
    slupek1 = ax1.patches[slupek_index]
    slupek2 = ax2.patches[slupek_index]
    # przykład adnotacji w postaci tekstu i strzałki zaczerpnięty z
    # https://matplotlib.org/examples/pylab_examples/annotation_demo.html
    plt.annotate('To najwyższy słupek',
                xy=(slupek1.get_x(), (slupek1.get_height() + slupek2.get_height()) * 1.01 ),
                xycoords='data',
                xytext=(-15, 25), textcoords='offset points',
                arrowprops=dict(facecolor='black', shrink=0.05),
                horizontalalignment='right', verticalalignment='bottom')
    # tiki osi x co drugi rok
    plt.xticks(x[::2])
    plt.ylabel('Liczba narodzonych dzieci')
    plt.xlabel('Rok')
    plt.legend()
    plt.show()


    # adnotacja do wykresu sinusoidy, ale lokalizacja wskazana poprzez podanie wartości z osi x oraz y, na przecięciu
    # których adnotacja ma się znaleźć
    x = np.arange(0, 30, 0.1)
    s = np.sin(x)
    plt.plot(x, s, label='sin(x)')

    # etykiety osi
    plt.xlabel('x')
    plt.ylabel('sin(x)')

    # adnotacja
    plt.annotate('początek wykresu',
                 xy=(0, 0), xycoords='data',
                 xytext=(0.3, 0.3), textcoords='axes fraction',
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 horizontalalignment='right', verticalalignment='top')
    # i jeszcze jedna
    plt.annotate('koniec wykresu',
                 xy=(x[-1],s[-1]), xycoords='data',
                 xytext=(0.7, 0.7), textcoords='axes fraction',
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 horizontalalignment='left', verticalalignment='top')

    # tytuł wykresu
    plt.title("Wykres sin(x)")

    # włączamy pokazywanie legendy
    plt.legend()
    plt.show()


# zad1()
# zad2()
# zad3()
# zad4()
# zad5()
zad6()
# zad7()
#zad8()
# zad9()
zad10()