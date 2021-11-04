import numpy as np

def rungeKutta(x0, y0, f, xEnd, h = 0.1):

    nElem = int((xEnd - x0)/h)
    
    x = np.zeros(nElem+1)
    y = np.zeros(nElem+1)

    x[0] = x0
    y[0] = y0

    for i in range(nElem):

        k1 = f(x[i], y[i])
        k2 = f(x[i] + h/2., y[i] + h*k1/2.)
        k3 = f(x[i] + h/2., y[i] + h*k2/2.)
        k4 = f(x[i] + h, y[i] + h*k3)

        x[i+1] = x[i] + h
        y[i+1] = y[i] + 1./6.*h*(k1 + 2*k2 + 2*k3 + k4)

    return x, y