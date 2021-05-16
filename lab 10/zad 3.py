import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 20, 0.1)
s = np.sin(x)
t = np.cos(x)
plt.subplot(2, 1, 1)
plt.plot(x, s, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title("Wykres sin(x)")
plt.subplot(2, 1, 2)
plt.plot(x, t, label='cos(x)')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.title("Wykres cos(x)")


# umieszczamy legendę na wykresie
plt.legend()

plt.show()