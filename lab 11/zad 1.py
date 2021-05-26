from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.gca(projection = '3d')

x = np.arange(0,2*np.pi,0.1) 
y = np.sin(x)
z = np.cos(x)
ax.plot(x, y,5, label = 'sin')
ax.plot(x, z, 5,label = 'cos')
ax.legend()
plt.show()
