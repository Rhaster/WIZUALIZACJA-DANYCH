import matplotlib .pyplot as plt
import numpy as np
import pandas as pd
import xlrd
import openpyxl
import csv
import math
def zad1():
    x = np.arange(-100,100,1)
    plt.xlim(-100,100)
    b=((2*(x**2))/np.sqrt(x))
    plt.plot(x,b, label='f(x) = 2x^2/sqrt(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title("wykres funkcji")
    plt.legend()
    plt.show()
zad1()