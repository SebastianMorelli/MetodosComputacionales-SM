import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq, ifft

n = 1280
f = 200.0
dt = 1/(f * 320 )
t = np.linspace( 0, (n-1)*dt, n)
amp = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t ) + np.random.random(n)

TransFou = np.fft.fft(amp)
freq = np.fft.fftfreq(n,dt)

for i in range(len (freq)):
    if(freq[i] > 1000 or freq[i]<-1000):
        TransFou[i] = 0

Inver = np.fft.ifft(TransFou)

fig0 = plt.figure(figsize=(12,6))
ax = fig0.add_subplot(111)
ax.plot(t, amp, 'k', label='Señal Original')
ax.plot(t, Inver, 'or', label='Señal Filtrada')
ax.set_xlabel('$Tiempo$', size=15)
ax.set_ylabel('$Amplitud$', size=15)
ax.legend()

plt.savefig('filtro.pdf')
