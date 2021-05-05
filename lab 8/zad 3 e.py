import pandas as pn  
import numpy as np
import csv 
df = pn.read_csv('zamowienia.csv',sep=';',quotechar=';',index_col=None)
df['Data zamowienia'] = pn.to_datetime(df['Data zamowienia'], format='%Y-%m-%d')
t = df.loc[(df['Data zamowienia'] >= '2005-01-01')& (df['Data zamowienia'] < '2005-12-31')]
y=t[(t.Kraj=='Polska')].agg({'Utarg':['sum']})
print(y)
t.to_csv('zamowienia_2005.csv')