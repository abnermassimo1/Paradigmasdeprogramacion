#======================================
# Martinez Castañeda Abner Alfredo
#======================================
#  Paradigmas de Progrmacion
#  Matematica Algoritmica
#  ESFM IPN Noviembre 2023
#======================================

#===========================================================
#  Importar numpy, matplotlib, mpl_toolkits,time
#===========================================================
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time

#==================================================
#  Parametros que se pueden cambiar 
#==================================================
#Numero de celdas
n = np.array([512,512])
# Tamaño del dominio(menor que uno)
L = np.array([1.0,1.0])
# Constante de difusion
k = 0.2
# Pasos de tiempo
pasos = 100

#=======================================================
# Parametros secundarios(no se deben cambiar)
#=======================================================
# Tamaño de las celdas
dx = L/n
udx2 = 1.0/(dx*dx)
# Paso de tiempo
dt = 0.25*(min(dx[0],dx[1])**2)/k
print("dt = ", dt)
# Total de celdas
nt = n[0]*n[1]
print("celdas = ",nt)

#=======================
# Arreglos iniciales
#=======================
# Llenar la solucion con ceros
u = np.zeros(nt,dtype=np.float64)  # arreglo de lectura
un = np.zeros(nt,dtype=np.float64) #  arreglo de excritura

#========================================================
# Evolucion temporal de la ecuacion deferencial parcial
# u_t = k*laplaciano(u)  (ecuacion de difusion de calor)
#========================================================
def evolucion(u,n,udx2,dt,i,k):
    jp1 = i + n[0]
    jm1 = i - n[0]
    laplaciano = (u[i-1]-2.0*u[i]+u[i+1])*udx2[0] + (u[jm1]-2.0*u[i]+u[jp1])*udx2[1]
    
    unueva = u[i] + dt*k*laplaciano
    return unueva

#====================================================================
# Loop sobre toda la malla pra avanzar la ecuacion en el tiempo
# No contiene la frontera (u=0 en todda la orilla del dominio)
#=====================================================================
def solucion(u,un,udx2,dt,n,k):
    for jj in range(1,n[1]-1):
      for ii in range(1,n[0]-1):
            i = ii + n[0]*jj
            #================================
            # Avanzar la ecuacion de un punto
            #================================
            unueva = evolucion(u,n,udx2,dt,i,k)
            #=================================================
            # En medio de la malla poner temperatura fija 1
            #=================================================
            if i == int(nt/2)+int(n[0]/2):
                unueva = 1.0
            un[i] = unueva

#====================
# Programa principal
#====================
start = time.time()
#=======================
# Pasos de tiempo
#=======================
for t in range(1,pasos+1):
    #=============================================
    #  Avanzar ecuacion en toda la malla
    #=============================================
    solucion(u,un,udx2,dt,n,k)
    #=====================================
    #Copiar arreglo nuevo al viejo
    #====================================
    u = un
    #=================================================
    # AVisar en pantalla el paso en el que va
    #===============================================
    if t%10==0: print("Iteracion = ",t)

end = time.time()
print("Tardo: ", end-start, "s")

#===========================================
#  Grafico de la solucion al tiempo final
#===========================================
u = np.reshape(u,(n[0],n[1]))
x,y = np.meshgrid(np.arange(0,L[0],dx[0]),np.arange(0,L[1],dx[1]))
ax = plt.axes(projection='3d')
ax.plot_surface(x,y,u,cmap=cm.hsv)
plt.show()    
