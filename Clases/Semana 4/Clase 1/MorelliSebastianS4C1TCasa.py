#FOURIER

import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq

signal = np.genfromtxt('signal.dat')
signalSuma = np.genfromtxt('signalSuma.dat')

fig0 = plt.figure(figsize = (12,5))
ax0 = fig0.add_subplot(121)
ax0.plot(signal[:,0],signal[:,1], 'r-', label='signal')
ax0.set_xlabel('time [s]')
ax0.set_ylabel('Signal')
ax0.set_title('Signal in function of time')
ax0.legend()

ax1 = fig0.add_subplot(122)
ax1.plot(signalSuma[:,0],signalSuma[:,1], 'b-', label='signalSuma')
ax1.set_xlabel('time [s]')
ax1.set_ylabel('SignalSuma')
ax1.set_title('SignalSuma in function of time')
ax1.legend()

plt.savefig('seniales.png')