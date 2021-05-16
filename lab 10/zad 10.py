import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 20, 0.1)
s = np.sin(x)
t = np.cos(x)
plt.subplot(2, 1, 1)
plt.plot(x, s, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title("Wykres sin(x)")
plt.subplot(2, 1, 2)
plt.plot(x, t, label='cos(x)')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.title("Wykres cos(x)")

plt.annotate('okresowosc', xy=(4.75, -1),  xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='yellow', shrink=0.05),
            horizontalalignment='right', verticalalignment='top',
            )
# umieszczamy legendę na wykresie
plt.legend()

plt.show()
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
plt.annotate('okresowosc', xy=(2, -1),  xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='yellow', shrink=0.05),
            horizontalalignment='right', verticalalignment='top',
            )
plt.legend()
plt.show()
