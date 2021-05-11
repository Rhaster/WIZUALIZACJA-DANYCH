import pandas as pn
import matplotlib.pyplot as plt
df = pn.read_csv("iris.data",sep=',')
x = df['Dlugosc_kielicha'][(df['Gatunek']=='Iris-setosa')]
y = df['Szerokosc_kielicha'][(df['Gatunek']=='Iris-setosa')]
plt.scatter(x,y,color='Yellow',label='Iris-setosa')
x = df['Dlugosc_kielicha'][(df['Gatunek']=='Iris-versicolor')]
y = df['Szerokosc_kielicha'][(df['Gatunek']=='Iris-versicolor')]
plt.scatter(x,y,color='GREEN',label='Iris-versicolor')
x = df['Dlugosc_kielicha'][(df['Gatunek']=='Iris-virginica')]
y = df['Szerokosc_kielicha'][(df['Gatunek']=='Iris-virginica')]
plt.scatter(x,y,color='Blue',label='Iris-virginica')
plt.legend()
plt.xlabel("Długość kielicha")
plt.ylabel("Szerokość kielicha")
plt.title("Porównanie")
plt.show()