#=================================
# Martinez Castañeda ABer Alfredo
#=================================
# Paradigmas de Programacion
# Matematica Algoritmica
# ESFM IPN Noviembre 2023
#==================================

#====================================
#  Importar numba, numpy y time
#====================================
from numba import jit
import  numpy
import time

#================================
# Loop cualquiera python puro
#================================
def lento(a):
    t = 0.0
    # Para cada renglon
    for i in range(a.shape[0]):
        t += numpy.tanh(a[i,i])
    return a + t

#=========================
# Loop sin interprete
#=========================
@jit(nopython=True)
def rapido(a):
    t = 0.0
    for i in range(a.shape[0]):
        t += numpy.tanh(a[i,i])
    return a + t

#===============================================
# Areglo unidimensional lleno del 1 al 10000
# convertido en matriz de 100 x 100
#================================================
x = numpy.arange(10000).reshape(100,100)

#====================================================
# La primera llamda incluye el tiempo de compilacion
#====================================================
start = time.time()
rapido(x)
end = time.time()
print("Tiempo incluyendo compilacion = %s" % (end-start))

#========================================================
# La segunda llamada es para obtener el tiempo de ejecucion
#===========================================================
start = time.time()
rapido(x)
end = time.time()
print("Tiempo de ejecucion usando numba = %s" %(end-start))

#===========================================
# Tiempo para la funcion sin optimizacion
#============================================
start = time.time()
lento(x)
end = time.time()
print("Tiempo de ejecucion en python puro= %s" %(end-start))

