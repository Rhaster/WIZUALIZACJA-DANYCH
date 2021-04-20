import numpy as np

def funkcja(n):
    macierz = np.diag([2 for t in range(n)])
    for x in range(1, n):
        vec = [2+(2*x) for t in range(n-x)]
        macierz += np.diag(vec, x)
        macierz += np.diag(vec, -x)
    print(macierz)
funkcja(10)