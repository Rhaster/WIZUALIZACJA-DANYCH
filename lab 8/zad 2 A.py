import pandas as pn  
import xlrd
import openpyxl
df = pn.read_excel('imiona.xlsx')
cos =df[df['Liczba']>1000]
print(cos)