import pandas as pn  
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt
df = pn.read_excel('imiona.xlsx')
grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
print(grupa)
wykres = grupa.plot.bar()
wykres.set_ylabel('Liczba')
wykres.set_xlabel('Plec')
wykres.legend()
plt.title('Roki zliczba urodzen')
plt.show()