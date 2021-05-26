
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt



fig = plt.figure()
ax = fig.gca(projection = '3d')

t = np.linspace(0 , 2 * np.pi, 100)
z = t
x = np.arccos(t)*np.tan(t)
y = np.tan(t)
markers_on = [0,1, 2, 3, 4,5,6,7,8,9,10,10,11,13,12,14,15,16,17,18,19]
ax.plot(x, y, z,linestyle='', marker='o', color='g', markevery=markers_on,label = 'zadanie 1')
ax.legend()

colors = ('r', 'g', 'b', 'k')
np.random.seed(19680801)
x = np.random.sample(5 * len(colors))
y = np.random.sample(5 * len(colors))
z = np.random.sample(5 * len(colors))
c_list = []
for c in colors:
    c_list.extend([c] * 5)
t = np.linspace(0 , 2 * np.pi, 100)
z = t
x = np.arctan(t)*np.tan(t)
y = np.arcsinh(t)
markers_on1=[3,4,5,6,8]
ax.plot(x, y, z,linestyle='-', marker='>', color='r',markevery=markers_on1,label = 'zadanie 6.b')

ax.legend()
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)
ax.set_zlim(0, 2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(elev = 20. , azim =-35)
plt.show()