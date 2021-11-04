import EDO_solver_1stOD as mySolver
import matplotlib.pyplot as plt
import numpy as np

def func(x, y):
    return np.sin(x)**2*y

x, y = mySolver.rungeKutta(0, 0.1, func, 5)

plt.plot(x, y)
plt.show()
