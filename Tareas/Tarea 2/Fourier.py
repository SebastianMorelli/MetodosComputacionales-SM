import numpy as np
import matplotlib.pylab as plt
from matplotlib.colors import LogNorm

imgSer = plt.imread('cara_02_grisesMF.png')
imgHap = plt.imread('cara_03_grisesMF.png')

TransimgSer = np.fft.fft2(imgSer)
TransimgSerSh = np.fft.fftshift(TransimgSer)
TransimgHap = np.fft.fft2(imgHap)
TransimgHapSh = np.fft.fftshift(TransimgHap)

fig0 = plt.figure(figsize=(15,14))

ax0 = fig0.add_subplot(221)
ax0.imshow(np.abs(TransimgSer),norm=LogNorm())
ax1 = fig0.add_subplot(222)
ax1.imshow(np.abs(TransimgSerSh),norm=LogNorm())

ax2 = fig0.add_subplot(223)
ax2.imshow(np.abs(TransimgHap),norm=LogNorm())
ax3 = fig0.add_subplot(224)
ax3.imshow(np.abs(TransimgHapSh),norm=LogNorm())

cTransimgSer = np.copy(TransimgSer)
cTransimgSerSh = np.copy(TransimgSerSh)
cTransimgHap = np.copy(TransimgHap)
cTransimgHapSh = np.copy(TransimgHapSh)

fil = np.shape(imgSer)[0]
cols = np.shape(imgSer)[1]

cTransimgSerSh[0:122,0:80] = 0
cTransimgSerSh[132:fil,0:80] = 0
cTransimgSerSh[0:122,90:cols] = 0
cTransimgSerSh[132:fil,90:cols] = 0

cTransimgHapSh[122:132,0:cols] = 0
cTransimgHapSh[0:fil,80:90] = 0

plt.figure()
plt.imshow(np.abs(cTransimgHapSh), norm = LogNorm())

newimgSerSh = np.fft.ifftshift(cTransimgSerSh)
newimgSer = np.fft.ifft2(cTransimgSerSh)

newimgHapSh = np.fft.ifftshift(cTransimgHapSh)
newimgHap = np.fft.ifft2(cTransimgHapSh)

plt.figure()
plt.imshow(np.abs(newimgHap), plt.cm.gray)
