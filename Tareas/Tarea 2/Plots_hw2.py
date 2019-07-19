import numpy as np
import matplotlib.pylab as plt

#Datos Rugen-Kutta
RG_dt0 = np.genfromtxt('dataRG.txt', skip_header=(1), usecols =(0))
RG_x_dt0 = np.genfromtxt('dataRG.txt', skip_header=(1), usecols =(1))
RG_vx_dt0 = np.genfromtxt('dataRG.txt', skip_header=(1), usecols =(2))
RG_y_dt0 = np.genfromtxt('dataRG.txt', skip_header=(1), usecols =(3))
RG_vy_dt0 = np.genfromtxt('dataRG.txt', skip_header=(1), usecols =(4))

RG_dt1 = np.genfromtxt('dataRG.txt', skip_header=(1), usecols =(5))
RG_x_dt1 = np.genfromtxt('dataRG.txt', skip_header=(1), usecols =(6))
RG_vx_dt1 = np.genfromtxt('dataRG.txt', skip_header=(1), usecols =(7))
RG_y_dt1 = np.genfromtxt('dataRG.txt', skip_header=(1), usecols =(8))
RG_vy_dt1 = np.genfromtxt('dataRG.txt', skip_header=(1), usecols =(9))

RG_dt2 = np.genfromtxt('dataRG.txt', skip_header=(1), usecols =(10))
RG_x_dt2= np.genfromtxt('dataRG.txt', skip_header=(1), usecols =(11))
RG_vx_dt2 = np.genfromtxt('dataRG.txt', skip_header=(1), usecols =(12))
RG_y_dt2 = np.genfromtxt('dataRG.txt', skip_header=(1), usecols =(13))
RG_vy_dt2 = np.genfromtxt('dataRG.txt', skip_header=(1), usecols =(14))

#Plots Posición
fig0 = plt.figure(figsize=(20,4))
ax0 = fig0.add_subplot(131)
ax0.plot(RG_x_dt0, RG_y_dt0, 'navy', label = ('RugenKutta'))
ax0.set_xlabel('$Posición$ $x$ [UA]', size = 15)
ax0.set_ylabel('$Posición$ $y$ [UA]', size = 15)
ax0.set_title('Posición: dt = 0.1 - 2000 Orbitas')
ax0.legend()

ax1 = fig0.add_subplot(132)
ax1.plot(RG_x_dt1, RG_y_dt1, 'navy', label = ('RugenKutta'))
ax1.set_xlabel('$Posición$ $x$ [UA]', size = 15)
ax1.set_ylabel('$Posición$ $y$ [UA]', size = 15)
ax1.set_title('Posición: dt = 0.01 - 200 Orbitas')
ax1.legend()

ax2 = fig0.add_subplot(133)
ax2.plot(RG_x_dt2, RG_y_dt2, 'navy', label = ('RugenKutta'))
ax2.set_xlabel('$Posición$ $x$ [UA]', size = 15)
ax2.set_ylabel('$Posición$ $y$ [UA]', size = 15)
ax2.set_title('Posición: dt = 0.001 - 20 Orbitas')
ax2.legend()

plt.savefig('XY_met_dt.pdf')

#Plots Velocidad
fig1 = plt.figure(figsize=(20,4))
ax0 = fig1.add_subplot(131)
ax0.plot(RG_vx_dt0, RG_vy_dt0, 'firebrick', label = ('RugenKutta'))
ax0.set_xlabel('$Velocidad$ $x$ [UA/yrs$^2$]', size = 15)
ax0.set_ylabel('$Velocidad$ $y$ [UA/yrs$^2$]', size = 15)
ax0.set_title('Velocidad: dt = 0.1 - 2000 Orbitas')
ax0.legend()

ax1 = fig1.add_subplot(132)
ax1.plot(RG_vx_dt1, RG_vy_dt1, 'firebrick', label = ('RugenKutta'))
ax1.set_xlabel('$Velocidad$ $x$ [UA/yrs$^2$]', size = 15)
ax1.set_ylabel('$Velocidad$ $y$ [UA/yrs$^2$]', size = 15)
ax1.set_title('Velocidad: dt = 0.01 - 200 Orbitas')
ax1.legend()

ax2 = fig1.add_subplot(133)
ax2.plot(RG_vx_dt2, RG_vy_dt2, 'firebrick', label = ('RugenKutta'))
ax2.set_xlabel('$Velocidad$ $x$ [UA/yrs$^2$]', size = 15)
ax2.set_ylabel('$Velocidad$ $y$ [UA/yrs$^2$]', size = 15)
ax2.set_title('Velocidad: dt = 0.001 - 20 Orbitas')
ax2.legend()

plt.savefig('VxVy_met_dt.pdf')

#Formula Momentum
def MomentumAng (Posx, Posy, Velx, Vely, dt):
    mass = 3.00273e-6
    MomentLinX = mass*Velx
    MomentLinY = mass*Vely
    
    MomentAngX = np.empty([len(Posx)])
    MomentAngY = np.empty([len(Posx)])
    
    for i in range(len(Posx)):
        #print(Posx[i]*MomentLinX[i]*np.sin((2*np.pi)/dt))
        MomentAngX[i] = Posx[i]*MomentLinX[i]*np.sin((2*np.pi)/dt)
        MomentAngY[i] = Posy[i]*MomentLinY[i]*np.sin((2*np.pi)/dt)
        dt += dt
    return np.sqrt(MomentAngX**2 + MomentAngY**2)


MomentAng_RG_dt0 = MomentumAng(RG_x_dt0, RG_y_dt0, RG_vx_dt0, RG_vy_dt0, RG_dt0[0])
MomentAng_RG_dt1 = MomentumAng(RG_x_dt1, RG_y_dt1, RG_vx_dt1, RG_vy_dt1, RG_dt1[0])
MomentAng_RG_dt2 = MomentumAng(RG_x_dt2, RG_y_dt2, RG_vx_dt2, RG_vy_dt2, RG_dt2[0])

#Plots Momentum

fig2 = plt.figure(figsize=(28,4))
ax0 = fig2.add_subplot(131)
ax0.plot(np.log(RG_dt0), MomentAng_RG_dt0, 'forestgreen', label = ('RugenKutta'))
ax0.set_xlabel('$tiempo$  [yrs]', size = 15)
ax0.set_ylabel('$Momentum Angular$ [Msol.UA$^2$/yrs]', size = 15)
ax0.set_title('Momentum Angular: dt = 0.1 - 2000 Orbitas')
ax0.legend()

ax1 = fig2.add_subplot(132)
ax1.plot(np.log(RG_dt1), MomentAng_RG_dt1, 'forestgreen', label = ('RugenKutta'))
ax1.set_xlabel('$tiempo$  [yrs]', size = 15)
ax1.set_ylabel('$Momentum Angular$ [Msol.UA$^2$/yrs]', size = 15)
ax1.set_title('Momentum Angular: dt = 0.01 - 200 Orbitas')
ax1.legend()

ax2 = fig2.add_subplot(133)
ax2.plot(np.log(RG_dt2), MomentAng_RG_dt2, 'forestgreen', label = ('RugenKutta'))
ax2.set_xlabel('$tiempo$  [yrs]', size = 15)
ax2.set_ylabel('$Momentum Angular$ [Msol.UA$^2$/yrs]', size = 15)
ax2.set_title('Momentum Angular: dt = 0.001 - 20 Orbitas')
ax2.legend()

plt.savefig('Mome_met_dt.pdf')

#Formula Energía

def Energon((Posx, Posy, Velx, Vely):
    
    massTi = 3.00273e-6
    cineticX = 1/2 * massTi * Velx**2
    cineticY = 1/2 * massTi * Vely**2
    PotencialX = massTi*Posx
    PotencialY = massTi*Posy
            
    Cinetic = np.sqrt(cineticX**2 + CineticY**2)
    Potencial = np.sqrt(PotencialX**2 + PotencialY**2)
    return Cinetic + Potencial
            
Energia_RG_dt0 = Energon(RG_x_dt0, RG_y_dt0, RG_vx_dt0, RG_vy_dt0)
Energia_RG_dt1 = Energon(RG_x_dt1, RG_y_dt1, RG_vx_dt1, RG_vy_dt1)
Energia_RG_dt2 = Energon(RG_x_dt2, RG_y_dt2, RG_vx_dt2, RG_vy_dt2)
            
fig3 = plt.figure(figsize=(28,4))
ax0 = fig3.add_subplot(131)
ax0.plot(np.log(RG_dt0), Energia_RG_dt0, 'black', label = ('RugenKutta'))
ax0.set_xlabel('$tiempo$  [yrs]', size = 15)
ax0.set_ylabel('$Energia$ [Msol.UA$^2$/yrs]', size = 15)
ax0.set_title('Energia: dt = 0.1 - 2000 Orbitas')
ax0.legend()

ax1 = fig3.add_subplot(132)
ax1.plot(np.log(RG_dt1), Energia_RG_dt1, 'black', label = ('RugenKutta'))
ax1.set_xlabel('$tiempo$  [yrs]', size = 15)
ax1.set_ylabel('$Energia$ [Msol.UA$^2$/yrs]', size = 15)
ax1.set_title('Energia: dt = 0.01 - 200 Orbitas')
ax1.legend()

ax2 = fig3.add_subplot(133)
ax2.plot(np.log(RG_dt2), Energia_RG_dt2, 'black', label = ('RugenKutta'))
ax2.set_xlabel('$tiempo$  [yrs]', size = 15)
ax2.set_ylabel('$Energia$', size = 15)
ax2.set_title('Energia: dt = 0.001 - 20 Orbitas')
            
plt.savefig('Ener_met_dt.pdf')
