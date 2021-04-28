import numpy as np
a = np.arange(9).reshape(3,3)
b = np.arange(16).reshape(4,4)
print(a)
print(a.min(axis=0))
print(a.min(axis=1))
print(a.max(axis=2))