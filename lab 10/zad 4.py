import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 30, 0.1)
s = np.sin(x)*-1
t=np.sin(x)+2
plt.plot(x, s, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title("Wykres sin(x)")
plt.plot(x, t, label='cos(x)')

# umieszczamy legendę na wykresie
plt.legend()
plt.show()