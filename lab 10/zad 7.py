import numpy as np
import pandas as pn
import matplotlib.pyplot as plt
import csv  
import xlrd
import openpyxl
from matplotlib import pyplot as plt
from itertools import cycle, islice

df = pn.read_excel('imiona.xlsx')
#plot
t=df.loc[df['Plec'] == 'K']
u=df.loc[df['Plec'] == 'M']
my_colors = list(islice(cycle(['y', 'g', 'b', 'y', 'k']), None, len(df)))
df.groupby(['Rok','Plec']).agg({'Liczba': 'sum'}).unstack(level=-1).plot(kind='bar', stacked=True,color=my_colors,y='Liczba')
plt.show()
###SECURED BY ANTYTLUK 2.0 