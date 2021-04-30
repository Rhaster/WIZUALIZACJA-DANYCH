import pandas as pn  
import numpy as np
import xlrd
import openpyxl
df = pn.read_excel('imiona.xlsx')
df= df.groupby(['Plec'])
y=df[(df['Rok']==2005) &(df['Plec']=='M')]
t=df[(df['Rok']==2005) &(df['Plec']=='K')]
print(y)
print(t)
print(y.max())
print(t.max())