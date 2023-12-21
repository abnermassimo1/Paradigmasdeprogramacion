#======================================
# Martinez Castañeda Abner Alfredo
#======================================
# Paradigmas de Programacion
# Matematica Algoritmica
# ESFM DICEMBRE 2023
#======================================

#==========================================================
# Uso de MPI optimizando para calculos numericos
#==========================================================
from mpi4py import MPI
import numpy as np

class Mensaje:
    def __init__(self,rank):

        #===============================
        # Lista comun
        #===============================
        self.x = [i for i in range(rank*10)]
        self.p = "vengo del proceso "+str(rank)

        #==============================================
        # Arreglo de numpy (optimizado)
        #==============================================
        self.xx = np.array([float(x+rank) for x in range(10)])
        self.pp = "vengo del proceso"+str(rank)

#=======================
# Programa pincipal
#=======================
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    s = Mensaje(rank)
    src = rank-1 if rank!=0 else size-1
    dst = rank+1 if rank!=size-1 else 0

    #=======================
    # Envio no bloqueante
    #=======================
    comm.isend(s, dest=dst)

    #=====================================
    # Recibir no bloqueante con espera
    # req: request (peticion)
    #=====================================
    req = comm.irecv(source=src)
    a = req.wait()

    print("Soy el proceso ", rank ,", el resultado es",len(a.x), a.p)

    #===============================
    # Arreglo de numpy para evitar
    #===============================
    m = s.xx

    #========================================
    # Isend Irecv son para comunicacion
    # no bloqueante de arreglos de numpy
    #=========================================
    comm.Isend(m, dest=dst)

    #===========================================
    # Arreglo vacio para recibir
    # con dimension 10 tipo de datos
    # float64 (doble precision)
    #===========================================
    aa = np.zeros(10,dtype=np.float64)
    req = comm.Irecv(aa, source=src)
    req.Wait()

    print("SOy el proceso ", rank ,", el resultado es ", aa)
