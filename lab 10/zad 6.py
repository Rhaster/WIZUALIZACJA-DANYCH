import numpy as np
import pandas as pn
import matplotlib.pyplot as plt
import csv  
import xlrd
import openpyxl
fig, axes = plt.subplots(nrows=1, ncols=3)
df = pn.read_excel('imiona.xlsx')
t=df.groupby(['Plec']).agg({'Liczba':['sum']})
wykres =t.plot.bar(subplots=True,ax=axes[0])
#plot
t=df.loc[df['Plec'] == 'K']
u=df.loc[df['Plec'] == 'M']
sum_df = t.groupby(['Rok']).agg({'Liczba': 'sum'})
sum_df2 = u.groupby(['Rok']).agg({'Liczba': 'sum'})
ax = sum_df.plot(subplots=True,ax=axes[1],color='r')
sum_df2.plot(ax=ax,subplots=True)
h=df.groupby(['Rok']).agg({'Liczba':['sum']})
wykres =h.plot.bar(subplots=True,ax=axes[2])
plt.legend()
plt.show()
