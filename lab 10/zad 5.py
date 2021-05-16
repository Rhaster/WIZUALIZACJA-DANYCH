import numpy as np
import pandas as pn
import matplotlib.pyplot as plt
import csv 
import random
import cmapy
rgb_color = 50*cmapy.color('viridis', random.randrange(1, 256,4))
df = pn.read_csv("iris.data",sep=',')
plt.scatter(x=df.Dlugosc_kielicha , y=df.Szerokosc_kielicha,c=rgb_color,s=abs(df.Dlugosc_kielicha-df.Szerokosc_kielicha))
plt.xlabel('wartość a')
plt.ylabel('wartość b')
plt.show()