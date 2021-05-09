import pandas as pn  
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt
df = pn.read_excel('imiona.xlsx')
df['Rok'] = pn.to_datetime(df['Rok'], format='%Y')
b=df[((df['Rok'] >= '2012') & (df['Rok'] <= '2017'))]
y=b.groupby(['Plec']).sum()
print(y)
wykres =y.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
plt.title('Liczba urodzen K i M w 2012-2017')
plt.show()