
import csv 
import numpy as np
import pandas as pn
import matplotlib.pyplot as plt
import csv  
import xlrd
import openpyxl
from matplotlib import pyplot as plt
from itertools import cycle, islice
import random
df = pn.read_csv('zamowienia.csv',sep=';',quotechar=';',index_col=None)
t=df.Sprzedawca.unique()
y=df.groupby(['Sprzedawca']).agg({'Utarg':[('LOL','sum')]})
explode = (0, 0.1, 0, 0, 0.2, 0, 0,0,0)
p=y.Utarg.LOL
wedges, texts, autotexts = plt.pie(p, labels=t,
                                   autopct=lambda pct: "{:.1f}%".format(pct), textprops=dict(color="black"),explode=explode)
plt.setp(autotexts, size=14, weight="bold")
plt.title("Pierwsza wersja wykresu")
plt.legend(title='Zawodnicy')
plt.show()
print(p)