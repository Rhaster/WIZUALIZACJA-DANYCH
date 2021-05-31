import pandas as pd
import numpy as np
import xlrd
import openpyxl
import csv 
import matplotlib.pyplot as plt
## 1 otwieranie plików 
## jak otworzyc plik exela  o nazwie imiona.xlsx
xd = pd.read_excel('imiona.xlsx')
print(xd)
## jak otworzyc plik csv o nazwie zamówienia z separatorem ;
df = pd.read_csv('zamowienia.csv',sep=';',quotechar=';',index_col=None)
print(df)
Q=df.groupby(['Kraj'])
print(Q)
## w celu spojrzenia na typy danych uzywamy discribe 
df.describe()
xd.describe()
## 2.1 dodanie kolumny
## deklarujemy zmienna z danymi danej kolumny
a='zydzi'
getto =[a for x in range(16417)]
##przypisujemy ja do wszystkich rekordów 
xd['Narodowosc']=getto
print(xd)
## to samo ale z mozliwoscia zmiany miejsca kolumny  pierwszy atrybut to numer kolumny
xd.insert(2, "Age", [1 for a in range (16417)], True)
print(xd)
## 2.2 dane na składowe z
## ZMIANA NAZWY KOLUMNY
t=xd.rename(columns={'Imie': 'IMO'})
print(t.head())
## usuwanie kolumny PLEC 
A=xd
## del A['Plec'] to usuwa ze zródła XDDD
print(A)
## usuwanie z pomoca  dropa kolumny Rok
Q=xd.drop(['Rok'], axis=1)
print(Q)
## zmiana wartosci kolumny
xd.Plec=xd.Rok-2000 ##zmieniam wartosc kolumny imie na rok -2000
print(xd)
## data na inny format  

#df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'], format='%Y-%m-%d')

## 3 Podbieranie podzbioru danych z dataframe 
print(df.Sprzedawca)
##
seria = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek', 'Wiesiek', 'Eleonora'])


## podbieranie podzbioru z series
print(seria[1])
print(seria['Eleonora']) ## to index wiec wyswietli wartosc 20 
print(seria[1:3])## wyswietlenie od 1 do 2 rekordu series

## 4 FILTROWANIE W SERIES I DATAFRAME 
## DATAFRAME 
print(df.sort_values(by='Utarg'))
## filtrowanie w series 
print(seria.where(seria.index=='Ala' ))
## 5 SREDNIA KROCZACA moze byc to cos innego
t=df.groupby(['Sprzedawca']).mean() ## sredni utarg kazdego sprzedawcy np 
print(t)
## 6  GRUPOWANIE DANYCH
grupa = xd.groupby(['Plec']).agg({'Liczba':['sum']})
print(grupa)
## 7 wyswietlanie wykresów przez pandas 
xd.groupby(['Imie']).agg({'Liczba':['sum']}).plot()
plt.show()
## 8 ZAPISANIE DANYCH DO PLIKU 
## DO PLIKU CSV 
df.to_csv('zamowienia_2004.csv')
## DO PLIKU EXEL
xd.to_excel("output.xlsx")
