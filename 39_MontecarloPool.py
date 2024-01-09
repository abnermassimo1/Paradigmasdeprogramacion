#======================================
# Martinez Castañeda Abner Alfredo
#======================================
# Paradigmas de Programacion
# Matematica Algoritmica
# ESFM IPN DICIEMBRE 2023
#=======================================
from multiprocessing import Pool
import random
import os

#=========================================
# Simulacion Montecarlo en paralelo
#=========================================
def montecarlo(N:int) -> int:
    semilla:float = random.uniform(-1,1)
    random.seed(semilla)
    dentro:int = 0
    for i in range(N):
        # Pares de numeros al azar en (-1,1)
        x:float = random.uniform(-1,1)
        y:float = random.uniform(-1,1)
        # Contar los que estan dentro del circulo de radio 1
        if (x*x + y*y) < 1.0:
            dentro +=1
    return dentro

if __name__=="__main__":
    n:int = 1.0e7
    cpus = os.cpu_count()
    N:int = int(n/cpus)
    print("Procesadores = ",cpus)
    arg = [N for i in range(cpus)]
    # El objetivo grupo tiene metodo map para repetir tarea
    results = Pool(cpus).map(montecarlo,arg)
    print("Numero de tiros = ",cpus*N)
    print("Numero de aciertos ", results)
    # Sumar los resultados y calcular pi
    print("Aproximacion de pi =", 4*sum(results)/(cpus*N))
