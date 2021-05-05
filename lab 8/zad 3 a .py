import pandas as pn  
import numpy as np
import csv 
df = pn.read_csv('zamowienia.csv',sep=";",quotechar=';')
y=df['Sprzedawca']
t=df.Sprzedawca.unique()
print(t)


