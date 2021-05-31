import matplotlib .pyplot as plt
import numpy as np
import pandas as pd
import xlrd
import openpyxl
import csv
import math
##zad 4.1
t=np.zeros((10,10))
c=1
for x in range(10):
    for j in range(10):
        t[x][j]=c
        c+=1
print(t)
##zad 4.2
a=np.arange(50)
b=np.arange(50)
h=0
p=0
for x in range(10):
    for j in range(10):
        if x%2==0:
            a[p]=t[x][j]
            h+=1
        elif x%2!=0:
            b[p]=t[x][j]
            p+=1
print(a)
print(b)
## zad 4.c
A=np.zeros(10)
Y=0
for x in range(10):
    for j in range(10):
        if x==j:
            A[Y]=t[x][j]
            Y+=1
print(A)