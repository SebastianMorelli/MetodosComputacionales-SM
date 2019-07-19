import numpy as np
import matplotlib.pylab as plt
from matplotlib.colors import LogNorm

#Generar las imagenes originales
imgSer = plt.imread('cara_02_grisesMF.png')
imgHap = plt.imread('cara_03_grisesMF.png')

#Transformadas de Fourier imagenes
TransimgSer = np.fft.fft2(imgSer)
TransimgHap = np.fft.fft2(imgHap)

#Transformadas de Fourier imagenes con freq bajas centradas
TransimgSerSh = np.fft.fftshift(TransimgSer)
TransimgHapSh = np.fft.fftshift(TransimgHap)

#Gráficas de las dos transformadas para las dos imágenes
fig1 = plt.figure(figsize=(12,10))

ax0 = fig1.add_subplot(221)
ax0.imshow(np.abs(TransimgSer),norm=LogNorm())
ax0.set_title('Transformada de Fourier Imagen Seria')
ax1 = fig1.add_subplot(222)
ax1.imshow(np.abs(TransimgSerSh),norm=LogNorm())
ax1.set_title('Transformada de Fourier Imagen Seria freq. bajas Centradas')

ax2 = fig1.add_subplot(223)
ax2.imshow(np.abs(TransimgHap),norm=LogNorm())
ax2.set_title('Transformada de Fourier Imagen Feliz')
ax3 = fig1.add_subplot(224)
ax3.imshow(np.abs(TransimgHapSh),norm=LogNorm())
ax3.set_title('Transformada de Fourier Imagen Feliz freq. bajas Centradas')

plt.savefig('FFtIm.pdf')

#Creación de copias para modificar
cTransimgSerSh = np.copy(TransimgSerSh)
cTransimgHapSh = np.copy(TransimgHapSh)

#Filtración de imagenes
def PasaAltas(data):
    data[115:140,75:95] = 0

def PasaBajas(data):
    fil = np.shape(data)[0]
    cols = np.shape(data)[1]
    data[0:115,0:] = 0
    data[140:fil,0:] = 0
    data[0:,0:75] = 0
    data[0:,95:cols] = 0

PasaAltas(cTransimgSerSh)
PasaBajas(cTransimgHapSh)

#Inversas de Fourier
newimgSer = np.fft.ifft2(cTransimgSerSh)
newimgHap = np.fft.ifft2(cTransimgHapSh)

#Gráficas de filtraciones y proceso

fig2 = plt.figure(figsize=(12,10))

ax0 = fig2.add_subplot(221)
ax0.imshow(np.abs(cTransimgSerSh),norm=LogNorm())
ax0.set_title('Transformada Imagen Seria Filtrada')
ax1 = fig2.add_subplot(222)
ax1.imshow(np.abs(cTransimgHapSh),norm=LogNorm())
ax1.set_title('Transformada Imagen Feliz Filtrada')

ax2 = fig2.add_subplot(223)
ax2.imshow(np.abs(newimgSer),plt.cm.gray)
ax2.set_title('Imagen Seria con Filtrado de Frecuencias Bajas')
ax3 = fig2.add_subplot(224)
ax3.imshow(np.abs(newimgHap),plt.cm.gray)
ax3.set_title('Imagen Feliz con Filtrado de Frecuencias Altas')

plt.savefig('ImProceso.pdf')


#Imagen Final
newimgFin = newimgSer + newimgHap

fig3 = plt.figure(figsize=(12,10))

ax0 = fig3.add_subplot(111)
ax0.imshow(np.abs(newimgFin),plt.cm.gray)
ax0.set_title('Imagen Híbrida')

plt.savefig('ImHybrid.pdf')
