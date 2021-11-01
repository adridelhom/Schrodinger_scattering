import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
from matplotlib.animation import FuncAnimation


def phi(k):
    if (k > -1 ) and (k < 1):
        return 1
    else:
        return 0    

def psi(x,t,k):
    return [1/np.sqrt(4*np.pi)*phi(k)*np.cos(1*(k*x-k**2/2*t)), 1/np.sqrt(4*np.pi)*phi(k)*np.sin(1*(k*x-k**2/2*t))]

def plot_amp(t):
    limxs = 10.0
    npoints = 200.0
    xs = np.linspace(-limxs,limxs,npoints)
    probability_amp = []
    for x in xs:
        result1= integrate.quad(lambda k: psi(x,t,k)[0],-2,2)
        result2 = integrate.quad(lambda k: psi(x,t,k)[1],-2,2)

        probability_amp.append(result1[0]**2+result2[0]**2)
    
    print(2*limxs/npoints*np.sum(probability_amp))

    line.set_data(xs, probability_amp)


fig = plt.figure()
ax = plt.axes(xlim=(-10,10), ylim=(0,0.8))
line, = ax.plot([], [], lw=3)

anim = FuncAnimation(fig, plot_amp, init_func=plot_amp(0), frames=100, interval=20)
anim.save('basic_animation.mp4', fps=10, extra_args=['-vcodec', 'libx264'])
