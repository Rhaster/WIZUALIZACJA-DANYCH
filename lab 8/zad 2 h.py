import pandas as pn  
import numpy as np
import xlrd
import openpyxl
df = pn.read_excel('imiona.xlsx')
y=df.loc[df['Plec'] == 'M']
t=y.groupby(pn.cut(y['Rok'], np.arange(2008, 2016-1, 1)))
u=t['Liczba'].max().max()
print(y[y['Liczba']==u])

