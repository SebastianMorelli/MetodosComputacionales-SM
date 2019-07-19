import numpy as np
import matplotlib.pylab as plt

#Datos
time = np.genfromtxt('resorte.dat', usecols=(0))
x = np.genfromtxt('resorte.dat', usecols=(1))

#Funciones
def function(k, t, gamma, omega):
    fun_t = k * np.exp(-gamma*t) * np.cos(omega*t)
    return fun_t

def Verosim(obs, mod):
    Vero = np.exp(-(1/2)*np.sum((obs-mod)**2))
    return Vero

#Condiciones iniciales
itera = 100000
k_ini=7.5
gamma_ini=0.6
omega_ini=18.2

model_ini = function(k_ini, time, gamma_ini, omega_ini)
Verosim_ini = Verosim(x, model_ini)
Param = np.empty([itera,4])
Param[0,:] = [k_ini, gamma_ini, omega_ini, Verosim_ini]

#Funcion Metropolis
def MetropolisHastings (numpas, sigma, Pos, funMod, funVero, k_old, t, gam_old, omg_old, model_old, arr0):
    
    for i in range (1,numpas):
        
        k_new = np.random.normal(k_old,sigma,1)
        gam_new = np.random.normal(gam_old,sigma,1)
        omg_new = np.random.normal(omg_old,sigma,1)
        model_new = funMod(k_new, t, gam_new, omg_new)
        alpha = funVero(Pos,model_new)/(funVero(Pos,model_old))
        
        if(alpha >= 1):
            arr0[i,:] = [k_new, gam_new, omg_new, funVero(Pos, model_new)]
        elif(alpha < 1):
            Beta = np.random.random(1)
            if(Beta < alpha):
                arr0[i,:] = [k_new, gam_new, omg_new, funVero(Pos, model_new)]
            elif(Beta > alpha):
                arr0[i,:] = [k_old, gam_old, omg_old, funVero(Pos, model_old)]
        k_old = k_new
        gam_old = gam_new
        omg_old = omg_new
    return arr0
  
#Funció nueva
Todo_nuevito = MetropolisHastings(itera, 1, x, function, Verosim, k_ini, time, gamma_ini, omega_ini, model_ini, Param)

#Mejores parámetros
MejorPos = np.argmax(Todo_nuevito[:,3])
print("Los mejores parámetros sin: k = " + str(Todo_nuevito[MejorPos,0])  + ", gamma = " 
      + str(Todo_nuevito[MejorPos,1]) +", omega = " + str(Todo_nuevito[MejorPos,2]))

#Gráfica 
fig0 = plt.figure(figsize=(8,4))
ax = fig0.add_subplot(111)
ax.plot(time, x, 'r', label='Función Original')
ax.plot(time, function(Todo_nuevito[MejorPos,0], time, Todo_nuevito[MejorPos,1], Todo_nuevito[MejorPos,2]), 'k', label='Modelo')
ax.set_xlabel('$Tiempo$', size=15)
ax.set_ylabel('$Posición$', size=15)
ax.set_title('Función original y Modelo hallado')    
ax.legend()

plt.savefig('Resorte.pdf')
