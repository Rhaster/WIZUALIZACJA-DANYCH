import pandas as pd
import numpy as np
import xlrd
import openpyxl
import csv
df = pd.read_csv('zamowienia.csv',sep=";",quotechar=';')
x = df['Sprzedawca'].unique()
y = df.sort_values(by='Utarg',ascending=False)['Utarg'][0:5]
z = df.groupby('Sprzedawca').size()
n = df.groupby('Kraj').agg({'Utarg':['sum']})
d = df[((df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31') & (df['Kraj'] == 'Polska'))].agg({'Utarg':['sum']})
u = df[df['Data zamowienia'].str[:4] == '2004'].agg({'Utarg':['mean']})
print(n)
print(d)
print(u)