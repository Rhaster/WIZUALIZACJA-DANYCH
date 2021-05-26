import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import random
# konfiguracja wielkości wykresu, figsize określa wielkość wykresu w calach
fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(121, projection = '3d')
ax2 = fig.add_subplot(122, projection = '3d')

# fikcyjne dane
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1

r = random.random()
b = random.random()
g = random.random()
fig, (ax1, ax2) = plt.subplots(1, 2)
color = (r, g, b)
ax1.bar3d(x, y, bottom, width, depth, top, color=color,shade = True )
ax1.set_title('Wykres zacieniony')
ax2.bar3d(x, y, bottom, width, depth, top, color=color,shade = False )
ax2.set_title('Wykres nie zacieniony')

plt.show()