import pandas as pn  
import numpy as np
import csv 
df = pn.read_csv('zamowienia.csv',sep=';',quotechar=';',index_col=None)
y=df.nlargest(5, 'Utarg')
print(y)
