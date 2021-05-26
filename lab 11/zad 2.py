import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# Ustawiamy seed by za każdym razem wyglądało identycznie
np.random.seed( 19680801 )


def randrange(n, vmin, vmax):

    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot(111 , projection = '3d')
n = 100

# Dla każdego zbioru styli i zakresów wygeneruj n losowych punktów
# zdefiniowane przez x z [23, 32], y in [0, 100], z z [zlow, zhigh].
for c, m, zlow, zhigh in [('saddlebrown', 'o', -20, -10), ('black', 'p', -25, -20),( 'darkolivegreen', '^', -5, 0),( 'chocolate', '|', -10, -5),('cyan', 'D', -30, -20), ( 'goldenrod', '8', -60, -20),('saddlebrown', '8', -20, -10)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zt = randrange(n, 1, 300)
    zu = randrange(n, 1, 50)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs,zt,zu, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.legend()
plt.show()