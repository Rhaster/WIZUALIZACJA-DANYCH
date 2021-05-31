import pandas as pd
import numpy as np
import xlrd
import openpyxl
import csv
import matplotlib.pyplot as plt
import random
# 1 numpy tablice o danych wymiarach
a=np.arange(2,20*2+1,2) ##wektor z wielokrotnosciamy liczby 2 
b=np.array([[2,3,4],[1,2,3],[6,2,3]]) ##macierz 3x3 
c=np.zeros((5,5))##macierz zer 5x5
d=np.ones((5,5))##macierz jedynek 5x5
e=np.diag(a)##macierz diagonalna z wektrem a na przekatnej
print(b)
print("           ")
## 2 numpy zmiana wymiaru 
y=np.array([[2,3,4],[1,2,3]]).reshape(1,6) ## zmieniam macierz 2x3 na macierz 1x6 
## 3 operacje arytmetcyczne dodawanie mnozenie itp
print("           ")
print(c+d)##dodaje dwie macierze 
print("    mnoze dwie macierze       ")
print(c*d)##mnoze dwie macierze
print("  inaczej mnozenie         ")
print(c.dot(d))##inaczej mnozenie 
print("wartosci minimalne  z kolumn           ")
print(b.min(axis=0))##wartosci minimalne  z kolumn
print("  wartosci minimalne z wierszy / dla max piszesz max  / dla sum          ")
print(b.min(axis=1)) ##wartosci minimalne z wierszy / dla max piszesz max  / dla sum 
print("     CIECIE MACIERZY  1 WIERSZ 2 KOLUMNY   ")
## 4 ciecie tablicy slicing
print("     tutaj macierz na której operujemy    ")
print (b)
print(b[0:1,0:2]) ## PIERWSZE TO WIERSZE DRUGIE KOLUMNY  TUTAJ 1 WIERSZ 2 KOLUMNY
print("     TUTAJ 3 WIERSZ 1 KOLUMNY      ")
print(b[0:3,0:1])
print("     TUTAJ OD 2 DO 3  WIERSZA 2 KOLUMNY      ")
print(b[1:3,0:2])
print("     tutaj bez 1 kolumny     ")
print(b[:,1:])
## 5 MACIERZE DIAGONALNE 
print("  tworze macierz diagonalna  5 x 5 z wektrem 12345 na przekatnej    ")
p=np.diag([x for x in range(1,6)])
h=np.diag([x for x in range(1,6)])
print(p)
print("dodaje 2  takie same macierze diagonalne ")
y=p+h
print(y)
print("pamietaj by dodawac odejmowac wymiar musi sie zgadzac")
## 6 zmiana typu danych tablicy
print("tworze macierz z danymi typu float")
t=np.array([[1.5,2.2,5.3],[1.1,2.9,3.2]])
print(t)
print("przerabiam ja na inta")
y=t.astype(int)
print(y)
print("gdy chcesz by dawało w góre dodaj 0.5 do macierzy")
U=t+0.5
print(U)
i=U.astype(int)
print(i)
print("dla znaków ")
O=np.array(([[z for z in "agnieszka"],[t for t in "goha"]]))
print(O)
print("typ tej macierzy to object ")
print(O.dtype)
## 7 generowanie macierzy z losowymi wartosciami
print("tworze macierz 5x5 zer")
X=np.zeros((5,5))
print("uzyje funkcji randrange i dwóch pentl sebastiana tlukova")
for x in range(5):
    for j in range(5):
        L=random.randrange(1,20)
        X[x][j]=L
print("losuje liczby z przedzialu 1-20 i wstawiam do tablicy przez 2 petle ")
print(X)
## 8 policzenie sumy wartosci danej kolumny 
print("tworze macierz 5x5 // uzywam polecenia identyty (jednostkowa macierz dodaje jednki ")
R=np.identity(5, dtype=None)+1
print("sumuje  kolumny")
print(R.sum(axis=1))
print("biore wynik z pierwszej kolumny")
Q=R.sum(axis=1)
print(Q[:1])
print("gdy chce zsumowac wszystko z wiersza ")
print(Q.sum(axis=0))
print("dla wierszy zmienia sie tylko wartosc pola axis na 0 ")
print(R.sum(axis=0))