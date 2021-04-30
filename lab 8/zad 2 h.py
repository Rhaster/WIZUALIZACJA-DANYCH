import pandas as pn  
import numpy as np
import xlrd
import openpyxl
df = pn.read_excel('imiona.xlsx')
##y=df['Imie'][(df['Liczba']==df.max()) & (df['Plec']=='K')]
y=df.groupby(['Rok'])
print(y.get_group())