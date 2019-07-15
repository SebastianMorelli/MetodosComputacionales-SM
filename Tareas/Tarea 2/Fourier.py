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
fig0 = plt.figure(figsize=(15,14))

ax0 = fig0.add_subplot(221)
ax0.imshow(np.abs(TransimgSer),norm=LogNorm())
ax1 = fig0.add_subplot(222)
ax1.imshow(np.abs(TransimgSerSh),norm=LogNorm())

ax2 = fig0.add_subplot(223)
ax2.imshow(np.abs(TransimgHap),norm=LogNorm())
ax3 = fig0.add_subplot(224)
ax3.imshow(np.abs(TransimgHapSh),norm=LogNorm())

#Creación de copias para modificar
cTransimgSer = np.copy(TransimgSer)
cTransimgSerSh = np.copy(TransimgSerSh)
cTransimgHap = np.copy(TransimgHap)
cTransimgHapSh = np.copy(TransimgHapSh)


#Función filtro Pasa Altas
def PasaAltas(data):
  fil = np.shape(data)[0]
  cols = np.shape(data)[1]
  for i in range (fil):
      for j in range (cols):
          if(data[i,j] == np.min(data)):
              data[i,j] = 0
          elif(data[i,j] > np.min(data) and data[i,j] < np.max(data)/1.05):
              data[i,j] = data[i,j] * 0.00000000005
              
#Función filtro Pasa Bajas #######################################################################MODIFICAR###########################
################################
def PasaBajas(data):
  fil = np.shape(data)[0]
  cols = np.shape(data)[1]
  for i in range (fil):
      for j in range (cols):
          if(data[i,j] == np.min(data)):
              data[i,j] = 0
          elif(data[i,j] > np.min(data) and data[i,j] < np.max(data)/1.05):
              data[i,j] = data[i,j] * 0.00000000005
              
#Inversas de Fourier
newimgSerSh = np.fft.ifftshift(cTransimgSerSh)
newimgSer = np.fft.ifft2(cTransimgSerSh)

newimgHapSh = np.fft.ifftshift(cTransimgHapSh)
newimgHap = np.fft.ifft2(cTransimgHapSh)

#Gráficas de las imagenes modficadas
plt.figure()
plt.imshow(np.abs(newimgSer), plt.cm.gray)

#Gráfica imagen híbrida
