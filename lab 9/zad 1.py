import pandas as pn  
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt
df = pn.read_excel('imiona.xlsx')
grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
print(grupa)
wykres = grupa.plot()
wykres.set_xlabel("Rok")
wykres.legend()
wykres.plot()
plt.show()