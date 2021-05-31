import matplotlib .pyplot as plt
import numpy as np
import pandas as pd
import xlrd
import openpyxl
import csv
import math
import xlrd
import openpyxl
import random
"""
ZADANIE 2 WYKRES NA PODSTAWIE ZDJECIA
"""
x = np.arange(0,6, 0.1)
t=np.arange(0,6,0.01)
sin = np.sin(x)
cos = np.cos(x)
sin1 = np.sin(x+ np.pi)
cos2 = np.cos(t+np.pi)
plt.plot(x, cos, label='cos(x)')
plt.plot(x, sin, 'y--', label='sin(x)')
plt.plot(t, cos2, 'go' , label='cos(x + pi)')
plt.plot(x, sin1,'r-.' , label='sin(x + pi)')
plt.xticks(fontsize=20, rotation=10)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("funkcja f(x) dla x [0, 6]")
plt.legend()
plt.show()


