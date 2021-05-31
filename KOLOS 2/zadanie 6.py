import matplotlib .pyplot as plt
import numpy as np
import pandas as pd
import xlrd
import openpyxl
import csv
import math
## zad 6.a
xd = pd.read_excel('imiona.xlsx')
def zad6a():
    xd = pd.read_excel('imiona.xlsx')
    t=xd[(xd.Rok ==2005)].groupby('Plec').agg({'Liczba':['sum']}).plot.bar()
    plt.show()
zad6a()
##zad 6.b 
def zad6b():
    b=xd.sort_values(by=xd.Imie.str.contains('^[A^]'))
    a=b.groupby(['Imie']).agg({'Liczba': [ 'sum' ]})
    print(a.head(5).where(True))
##zad6b()