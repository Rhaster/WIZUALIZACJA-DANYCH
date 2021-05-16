import numpy as np
import pandas as pn
import matplotlib.pyplot as plt
import csv  
import xlrd
import openpyxl
from matplotlib import pyplot as plt
from itertools import cycle, islice
import random
def zadanie(n):
    lista=[]
    for i in range(n):
        rzut1=random.randint(1,6)
        rzut2=random.randint(1,6)
        lista.append(rzut1+rzut2)
    plt.hist(lista)
    plt.xlabel('Wartości')
    plt.ylabel('liczba rzutów')
    plt.title('Histogram')
    # wyświatlanie siatki
    plt.grid(True)
    plt.show()
zadanie(6)