import matplotlib .pyplot as plt
import numpy as np
import pandas as pd
import xlrd
import openpyxl
import csv
import math
## zad 5.1
df = pd.read_csv('zamowienia.csv',sep=';',quotechar=';',index_col=None)
a = df['Utarg'].max()
b = df['Utarg'].min()
c = df['Utarg'].mean()
print(a)
print(b)
print(c)
## zad 5.2
df['Rok'] = df['Data zamowienia'].str[:4].astype(int)
df['Miesiac'] = df['Data zamowienia'].str[5:7].astype(int)
print(df['Rok'])
print(df['Miesiac'])
c = df.loc[df['Rok'] == 2003]
d = c.groupby(['Miesiac']).agg({'Utarg' : ['mean']})
wykres = d.plot(label='Utarg', grid=True)
wykres.set_ylabel('Utarg')
wykres.set_xlabel('Miesiąc')
plt.axis([1,12,800,2000])
plt.legend()
plt.show()