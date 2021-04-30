import pandas as pn  
import numpy as np
import xlrd
import openpyxl
df = pn.read_excel('imiona.xlsx')
cos =df.groupby(by=['Rok']).sum()
y=df['Liczba'][(df['Rok']<=2005) & (df['Rok']>=2000)].sum()
print(y)