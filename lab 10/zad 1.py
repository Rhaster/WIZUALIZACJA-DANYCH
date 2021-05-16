import pandas as pn 
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 20,20)

plt.plot(1/x,'g-->', label='')

plt.title('x/2')
plt.legend()
plt.show()