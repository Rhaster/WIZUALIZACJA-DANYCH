import pandas as pn 
import numpy as np
import csv 
import matplotlib.pyplot as plt
df = pn.read_csv('zamowienia.csv',sep=';',quotechar=';',index_col=None)
grupa=df.groupby(['Sprzedawca']).agg({'Sprzedawca':['count']})
wykres = grupa.plot.bar()
wykres.set_ylabel('Liczba')
wykres.set_xlabel('Plec')
wykres.legend()
plt.title('ilosc zamowien dla sprzedawcow uni')
plt.show()