#===================================
# Martinez Castañeda Abner Alfredo
#===================================
# Paradigmas de programacion 
# Matematica Algoritmica
# ESFM IPN DICIEMBRE 2023
#====================================
from __future__ import print_function, absolute_import
from numba import cuda 
from numba.cuda.random import create_xoroshiro128p_states
from numba.cuda.random import xoroshiro128p_uniform_float64
import numpy as np
import random 

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Kernel de CUDA para simulación Montecarlo en el GPU
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@cuda.jit
def calcularpi_kernel(rng_states, iteraciones, out):
    ii = cuda.grid(1)
    #++++++++++++++++++++++++++++++++++++++++++++++
    # Calcular pi dibujando puntos (x, y) al azar y encontrando 
    # la fracción de ellos que cae dentro del círculo unitario
    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    cae_adentro = 0
    for i in range(iteraciones):
        # Pares al azar diferentes en (-1, -1) para cada proceso ii 
        x = xoroshiro128p_uniform_float64(rng_states, ii)
        y = xoroshiro128p_uniform_float64(rng_states, ii)
        # Contar los que caen dentro del círculo de radio 1
        if x**2 + y**2 <= 1.0:
            cae_adentro += 1
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Escribir resultados para el proceso ii
    #+++++++++++++++++++++++++++++++++++++
    out[ii] = 4.0 * cae_adentro / iteraciones

#++++++++++++++++++++++++++++++++++++
# Procesos para CUDA
#++++++++++++++++++++++++++++++++++++
N = 262144
hilosporbloque = 128
bloques = int(N/hilosporbloque)

#+++++++++++++++++++
# Semilla 
#+++++++++++++++++++
seed = random.randint(-1000, 1000)
rng_states = create_xoroshiro128p_states(hilosporbloque*bloques, seed)

#+++++++++++++++++++++++++++++++++
# Arreglo de salida (escritura)
#++++++++++++++++++++++++++++++
out = np.zeros(hilosporbloque*bloques, dtype=np.float64)

#+++++++++++++++++++++++++++++++++++++++++++
# Correr en paralelo el kernel de CUDA 
#+++++++++++++++++++++++++++++++++++++++++
calcularpi_kernel[bloques, hilosporbloque](rng_states, 100000, out)
print('pi:', out.astype(np.float64).mean())