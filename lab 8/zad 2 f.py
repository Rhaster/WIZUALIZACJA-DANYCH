import pandas as pn  
import numpy as np
import xlrd
import openpyxl
df = pn.read_excel('imiona.xlsx')
y=df.groupby(['Rok','Plec'])
t=y.get_group((2011,'K'))
k=y.get_group((2011,'M'))
print(k.max())
print(t.max())