import matplotlib .pyplot as plt
import numpy as np
import pandas as pd
import xlrd
import openpyxl
import csv
import math
## zad3(a)
xd = np.diag([2 for t in range(5)])
mat_diag = np.diag([1 for a in range(5)])
mat_diag=mat_diag*2
for x in range(1, 5):
    vec = [2+(2*x) for t in range(5-x)]
    xd += np.diag(vec, x)
    P=xd+xd.T
    P=P-mat_diag
print(P)
